import matplotlib.pyplot as plt 
import numpy as np
import tensorflow as tf
import argparse
from shutil import copyfile

import scipy.io.wavfile as wav

import random
import struct
import time
import datetime
import os
import sys
from collections import namedtuple
from tensorflow.python.keras.backend import ctc_label_dense_to_sparse
sys.path.append("DeepSpeech")

import DeepSpeech
from tf_logits import get_logits, compute_mfcc
from batch_generator import batch_generator, batch_set_random_seed
from sklearn.model_selection import train_test_split


toks = " abcdefghijklmnopqrstuvwxyz'-"

def plot_log(loss_log, output_dir, name):
    plt.figure()

    plt.plot(np.arange(0, len(loss_log)), loss_log,'r--',label=name)
    plt.show()
    plt.title(name)
    plt.savefig(os.path.join(output_dir,name+'.svg'))

class PreAttacker: 
    def __init__(self, sess, max_audio_len, max_phrase_length,  pre_len = 8000, l2penalty=0.1, learning_rate=1, batch_size=40, 
                delta_frame_len = 8000, random_shift=False, restore_path=None):
        print(random_shift)
        self.max_audio_len =  max_audio_len + pre_len
        max_audio_len = self.max_audio_len
        self.max_phrase_length = max_phrase_length
        self.sess = sess
        self.l2penalty = l2penalty
        self.learning_rate = learning_rate
        self.pre_len = pre_len
        self.batch_size = batch_size
        self.random_shift = random_shift
        self.delta_frame_len = delta_frame_len
        """variable for audio"""
        self.audio = audio = tf.placeholder(tf.float32, shape = (batch_size, max_audio_len), name = 'qq_audio')
        #self.audio_mask = audio_mask = tf.placeholder(tf.float32, shape = (batch_size, max_audio_len), name = 'qq_audio_mask')
        self.lengths = lengths = tf.placeholder(tf.int32, shape = (batch_size), name = 'qq_length')
        
        """variable for text"""
        self.target_phrase = target_phrase = tf.placeholder(tf.int32,  shape = (batch_size, max_phrase_length), name='qq_phrase')
        self.target_phrase_lengths = target_phrase_lengths = tf.placeholder(tf.int32, shape = (batch_size), name='qq_phrase_lengths')

        """variable for delta"""
        self.delta_frame = delta_frame = tf.Variable(np.zeros((delta_frame_len), dtype=np.float32), name='qq_delta')
        self.shift = shift = tf.placeholder(tf.int32, (batch_size), name='qq_shift')
        #list all shift cases
        if random_shift == True:
            delta_frame_stack = []
            for i in range(batch_size):
                delta_frame_stack.append(tf.roll(delta_frame, shift = shift[i], axis = 0))
        else:
            delta_frame_stack = [delta_frame]*batch_size
        delta_frame_stack = tf.stack(delta_frame_stack, axis = 0)
        self.delta = delta = tf.concat((max_audio_len//delta_frame_len)*[delta_frame_stack] + [delta_frame_stack[:, 0:max_audio_len - delta_frame_len*(max_audio_len//delta_frame_len)]], axis = 1)
        

        self.new_input = new_input = delta + audio
        logits, layer = get_logits(new_input, lengths)
        
        #setup loss
        #self.ctc_loss = ctc_loss =  
        target = ctc_label_dense_to_sparse(target_phrase,  target_phrase_lengths)
        
        self.ctc_loss = ctc_loss = tf.reduce_sum(tf.nn.ctc_loss(labels=tf.cast(target, tf.int32), inputs=logits, sequence_length=lengths))
        #self.ctc_loss = ctc_loss = tf.reduce_mean(tf.nn.ctc_loss(labels=tf.cast(target, tf.int32), inputs=logits, sequence_length=lengths))
        self.penalty = penalty = tf.reduce_sum((delta_frame)**2)
        self.loss = loss = -ctc_loss + l2penalty * penalty 


        #restore deepspeech parameter from checkpoint
        saver = tf.train.Saver([x for x in tf.global_variables() if 'qq' not in x.name])
        saver.restore(sess, restore_path)

        #setup adam optimizer
        start_vars = set(x.name for x in tf.global_variables())
        optimizer = tf.train.AdamOptimizer(learning_rate)
        grad, var = optimizer.compute_gradients(loss, [delta_frame])[0]
        self.grad = grad
        self.train = optimizer.apply_gradients([(grad, var)]) 
        end_vars = tf.global_variables()
        new_vars = [x for x in end_vars if x.name not in start_vars]
        sess.run(tf.variables_initializer(new_vars+[delta_frame]))

    def attack(self, data_dict, output_dir, limit = 100, init = None, num_iterations=300):
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        
        """inilization for delta"""
        if init is not None:
            self.sess.run(self.delta_frame.assign(init))
        else:
            self.sess.run(self.delta_frame.assign(tf.cast(np.random.normal(0, 10, size = (self.delta_frame_len)), tf.float32)))

        train_ctc_loss_log = []
        val_ctc_loss_log = []
        distortion_mean_log = []
        report = open(os.path.join(output_dir, 'train_report.txt'), 'w')
        
        delta_frame_result = np.zeros(self.delta_frame_len)
        end_flag = False

        for i in range(num_iterations):
            print("iteration: ", i)
            report.write("iteration: "  + str(i) + '\n')
            batch_gen = batch_generator(data_dict["train"], self.batch_size)
            
            train_ctc_loss_avg = 0 
            count = 0
            for j, batch in enumerate(batch_gen):
                audios,  audio_lengths,  texts,  text_lengths = batch
                
                #add silence before audio
                audios = np.concatenate((np.zeros((self.batch_size, self.pre_len)), audios), axis = 1)
                audio_lengths = audio_lengths + self.pre_len
                #print(audio_lengths)

                if audios.shape[1] < self.max_audio_len:
                    audios = np.concatenate((audios, np.zeros((self.batch_size, self.max_audio_len - audios.shape[1]))), axis = 1)
                if texts.shape[1] < self.max_phrase_length:
                    texts = np.concatenate((texts, np.zeros((self.batch_size, self.max_phrase_length - texts.shape[1]))), axis = 1)

                if self.random_shift:
                    shift = np.random.randint(low=0, high=self.delta_frame_len, size=self.batch_size) 
                    _, ctc_loss, penalty, loss = self.sess.run((self.train, self.ctc_loss, self.penalty, self.loss), 
                                                            {self.audio: audios,
                                                            #self.audio_mask: audio_mask,
                                                            self.lengths: (audio_lengths-1)//320,
                                                            self.target_phrase: texts,
                                                            self.target_phrase_lengths: text_lengths,
                                                            self.shift: shift})
                else:
                    _, ctc_loss, penalty, loss = self.sess.run((self.train, self.ctc_loss, self.penalty, self.loss), 
                                                            {self.audio: audios,
                                                            #self.audio_mask: audio_mask,
                                                            self.lengths: (audio_lengths-1)//320,
                                                            self.target_phrase: texts,
                                                            self.target_phrase_lengths: text_lengths})

                

                delta_frame = self.sess.run(self.delta_frame)
                delta_frame = np.array(np.clip(np.round(delta_frame), -2**15, 2**15-1),dtype=np.int16)
                print("batch:", j, "ctcloss:", ctc_loss, "distortion:", np.mean(np.abs(delta_frame)))
                
                if (np.mean(np.abs(delta_frame)) < limit):
                    delta_frame_result = delta_frame
                else:
                    end_flag = True
                    break

                train_ctc_loss_avg += ctc_loss
                count += 1
            train_ctc_loss_log.append(train_ctc_loss_avg / count)
            print("train_ctc_loss: ", train_ctc_loss_avg / count)
            report.write("train_ctc_loss: " + str(train_ctc_loss_avg / count) + '\n')

            if end_flag:
                report.write("end: epoch_" + str(i) + '\n')
                report.flush()
                break


            batch_gen = batch_generator(data_dict["dev"], self.batch_size, shuffle = False)
            #TODO more elegant way of testing and ploting
            
            val_ctc_loss_avg = 0 
            count = 0
            for batch in batch_gen:
                audios,  audio_lengths,  texts,  text_lengths = batch
                
                #add silence before audio
                audios = np.concatenate((np.zeros((self.batch_size, self.pre_len)), audios), axis = 1)
                audio_lengths = audio_lengths + self.pre_len

                if audios.shape[1] < self.max_audio_len:
                    audios = np.concatenate((audios, np.zeros((self.batch_size, self.max_audio_len - audios.shape[1]))), axis = 1)
                if texts.shape[1] < self.max_phrase_length:
                    texts = np.concatenate((texts, np.zeros((self.batch_size, self.max_phrase_length - texts.shape[1]))), axis = 1)

                if self.random_shift:
                    shift = np.random.randint(low=0, high=self.delta_frame_len, size=self.batch_size) 
                    ctc_loss, penalty, loss = self.sess.run((self.ctc_loss, self.penalty, self.loss), 
                                                            {self.audio: audios,
                                                            #self.audio_mask: audio_mask,
                                                            self.lengths: (audio_lengths-1)//320,
                                                            self.target_phrase: texts,
                                                            self.target_phrase_lengths: text_lengths,
                                                            self.shift: shift})
                else:
                    ctc_loss, penalty, loss = self.sess.run(( self.ctc_loss, self.penalty, self.loss), 
                                                        {self.audio: audios,
                                                        #self.audio_mask: audio_mask,
                                                        self.lengths: (audio_lengths-1)//320,
                                                        self.target_phrase: texts,
                                                        self.target_phrase_lengths: text_lengths})
                count += 1
                val_ctc_loss_avg += ctc_loss

            val_ctc_loss_log.append(val_ctc_loss_avg / count)
            print("val_ctc_loss: ", val_ctc_loss_avg / count)
            report.write("val_ctc_loss: " + str(val_ctc_loss_avg / count) + '\n')
            
            delta_frame = self.sess.run(self.delta_frame)
            distortion_mean_log.append(np.mean(np.abs(delta_frame)))
            print("distortion_mean: ", np.mean(np.abs(delta_frame)))
            report.write("distortion_mean: " + str(np.mean(np.abs(delta_frame))) + '\n')
            report.flush()
            #np.save(os.path.join(output_dir, 'epoch_' + str(i)), delta_frame)
            
            #if np.mean(np.abs(delta_frame)) > 120:
            #    break

        #plot and save log
        plot_log(train_ctc_loss_log, output_dir, 'train_ctc_loss')
        plot_log(val_ctc_loss_log, output_dir, 'val_ctc_loss')
        plot_log(distortion_mean_log, output_dir, 'distortion_mean')

        #np.save(os.path.join(output_dir, 'train_ctc_loss'), np.array(train_ctc_loss_log))
        #np.save(os.path.join(output_dir, 'val_ctc_loss'), np.array(val_ctc_loss_log))
        #np.save(os.path.join(output_dir, 'distortion_mean'), np.array(distortion_mean_log))

        #save delta_frame, in both wav form and npy form
        #delta_frame = self.sess.run(self.delta_frame)
        print(delta_frame_result)
        print(len(delta_frame_result))
        wav.write(os.path.join(output_dir, 'adv.wav'), 16000,
                          delta_frame_result)     
        #np.save(os.path.join(output_dir, 'delta_frame'), delta_frame_result)
        
        #summary   
        #report.write('mean distortion: '+ str(np.mean(np.abs(delta_frame_result))) + '\n')
        #report.write('train_ctc_loss: '+str(train_ctc_loss_log[-1])+'\n')     
        #report.write('val_ctc_loss: '+str(val_ctc_loss_log[-1])+'\n')   
        report.close()


def main():
    
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('--inputdir',
                        required=True,
                        help="Path of input.")
    parser.add_argument('--outdir',
                        required=True,
                        help="Path of output.")
    parser.add_argument('--init', type=str,
                        required=False, default=None,
                        help="Initial status.") 
    parser.add_argument('--pre_len', type=int,
                        required=False, default=8000,
                        help="Prepending length.") 
    parser.add_argument('--l2penalty', type=float,
                        required=False, default=0.00001,
                        help="Regularize rate for regularizer.")    
    parser.add_argument('--learning_rate', type=float,
                        required=False, default=1,
                        help="Learning rate for optimization.")
    parser.add_argument('--num_iterations', type=int,
                        required=False, default=15,
                        help="Maximum number of iterations.")
    parser.add_argument('--batch_size', type=int,
                        required=False, default=20,
                        help="Batch size.")
    parser.add_argument('--delta_frame_len', type=int,
                        required=False, default=8000,
                        help="The length of chunk-based noise.")
    parser.add_argument('--random_shift', action="store_true",
                        help="Whether shift training is used in generation.")
    parser.add_argument('--restore_path', type=str,
                        required=False, default = 'deepspeech-0.4.1-checkpoint/model.v0.4.1',
                        help="Path to the DeepSpeech checkpoint (ending in model0.4.1).")
    parser.add_argument('--limit', type=int,
                        required=False, default=100,
                        help="Limit for perturbation.")
    parser.add_argument('--random_seed', type=int,
                        required=False, default=1000,
                        help="Random seed.")
    args = parser.parse_args()
    while len(sys.argv) > 1:
        sys.argv.pop()
    
    if not os.path.exists(args.outdir):
        os.mkdir(args.outdir)

    #record parameters
    para_log = open(os.path.join(args.outdir, 'para_log.txt'), 'w')
    para_log.write(str(vars(args)))
    para_log.close()
    
    #set random seed for numpy 
    np.random.seed(args.random_seed)
    tf.set_random_seed(args.random_seed)
    random.seed(args.random_seed)
    batch_set_random_seed(args.random_seed)
    data_dict = {}
    splits = ["train", "dev"]
    parts = ["audios", "audio_lengths", "texts", "text_lengths"]
    for split in splits:
        path = os.path.join(args.inputdir, split)
        data_dict[split] = []
        for part in parts:
            name = part
            arr = np.load(os.path.join(path, name) + '.npy')
            data_dict[split].append(arr)
        
    max_audio_len_dev = data_dict["dev"][0].shape[1]
    max_audio_len_train = data_dict["train"][0].shape[1]
    max_audio_len = np.max((max_audio_len_dev, max_audio_len_train))



    max_phrase_length_train = data_dict["train"][2].shape[1]
    max_phrase_length_dev = data_dict["dev"][2].shape[1]
    max_phrase_length = np.max((max_phrase_length_dev, max_phrase_length_train))



    """initlization"""
    if args.init is not None:
        fs, init = wav.read(args.init)
        assert fs == 16000
        assert init.dtype == np.int16
    else:
        init = None
    with tf.Session() as sess:
        attacker = PreAttacker(sess,
                            max_audio_len = max_audio_len, 
                            max_phrase_length = max_phrase_length, 
                            pre_len = args.pre_len,
                            l2penalty = args.l2penalty, 
                            learning_rate = args.learning_rate, 
                            batch_size= args.batch_size, 
                            delta_frame_len = args.delta_frame_len,
                            random_shift = args.random_shift, 
                            restore_path = args.restore_path)
        attacker.attack(data_dict = data_dict, 
                        output_dir = args.outdir,
                        limit = args.limit,
                        init = init,
                        num_iterations = args.num_iterations)

        

if __name__ == '__main__':
    main()