import numpy as np
import tensorflow as tf
import argparse
import random
import scipy.io.wavfile as wav

import time
import os
import sys
from collections import namedtuple
from tf_logits import get_logits, compute_mfcc

sys.path.append("DeepSpeech")
import DeepSpeech

toks = " abcdefghijklmnopqrstuvwxyz'-"

def metric_cer(r, h):
    #input are str
    import Levenshtein
    return Levenshtein.distance(r, h), len(r)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('--data_path', type=str, 
                        required=True,
                        help="Path to data which contains processed data.")
    parser.add_argument('--out',
                        required=True, 
                        help="Path of output")
    parser.add_argument('--delta', type=str, dest="delta",
                        required=True,
                        help="Path to delta audio .wav file, at 16KHz")
    parser.add_argument('--pre_len', type=int, dest="pre_len",
                        required=False, default= 8000,
                        help="Prepending length.")
    parser.add_argument('--random_seed', type=int,
                        required=False, default=1000,
                        help="Random Seed.")
    parser.add_argument('--restore_path', type=str,
                        required=False,
                        default = "deepspeech-0.4.1-checkpoint/model.v0.4.1",
                        help="Path to the DeepSpeech checkpoint (ending in model0.4.1)")

    args = parser.parse_args()
    while len(sys.argv) > 1:
        sys.argv.pop()

    #set random seed 
    np.random.seed(args.random_seed)
    tf.set_random_seed(args.random_seed)
    random.seed(args.random_seed)

    #load data
    audios = np.load(os.path.join(args.data_path, 'audios.npy'))
    audio_lengths = np.load(os.path.join(args.data_path, 'audio_lengths.npy'))
    texts = np.load(os.path.join(args.data_path, 'texts.npy'))
    text_lengths = np.load(os.path.join(args.data_path, 'text_lengths.npy'))

    #add silence before audio
    audios = np.concatenate((np.zeros((audios.shape[0], args.pre_len)), audios), axis = 1)
    audio_lengths = audio_lengths + args.pre_len
    max_audio_len = audios.shape[1] 
    if args.pre_len > 0:
        pre_len_frame = (args.pre_len-1)//320
    else:
        pre_len_frame = 0
    
    #read delta 
    fs, delta_frame = wav.read(args.delta)
    assert fs == 16000
    assert delta_frame.dtype == np.int16
    delta_frame_len = len(delta_frame)
    delta_frame_num = max_audio_len//delta_frame_len
    
    log = open(args.out,'w')
    with tf.Session() as sess:    
        new_input = tf.placeholder(tf.float32, [1, max_audio_len])
        length = tf.placeholder(tf.int32, [1])
        length_modified = tf.placeholder(tf.int32, [1])
        with tf.variable_scope("", reuse=tf.AUTO_REUSE):
            logits, layer = get_logits(new_input, length)
                
        saver = tf.train.Saver()
        saver.restore(sess, args.restore_path)
        decoded, _ = tf.nn.ctc_beam_search_decoder(logits[pre_len_frame:, :, :], length_modified, merge_repeated=False, beam_width=500)
        
        
        distance_sum = 0
        rlen_sum = 0
        success = 0
        snr_sum = 0
        
        for i in range(audios.shape[0]):
            idx = random.randint(0, len(delta_frame)-1)
            delta_frame_shift = np.concatenate([delta_frame[idx:], delta_frame[0:idx]], axis = 0)
            delta = np.concatenate(delta_frame_num*[delta_frame_shift] + [delta_frame_shift[0:max_audio_len - delta_frame_len*delta_frame_num]], axis = 0)
            delta = delta.astype(np.float64)
            snr = 10*np.log10((np.sum(audios[i, :audio_lengths[i]]**2))/(np.sum(delta[:audio_lengths[i]]**2)))
            audio = delta + audios[i, :]
            
            result = sess.run(decoded, {new_input: audio.reshape(1, -1),
                                    length: ((audio_lengths[i]-1)//320).reshape(1),
                                    length_modified: (((audio_lengths[i]-1)//320) - pre_len_frame).reshape(1)})
            


            r = "".join([toks[int(x)] for x in texts[i][:text_lengths[i]]])
            h = "".join([toks[int(x)] for x in result[0].values])
            r = r.strip()
            h = h.strip()
            
            distance, rlen = metric_cer(r, h)
            distance_sum += distance
            rlen_sum += rlen 
            cer = distance/rlen
            snr_sum += snr

            log.write('##############################################################\n')
            log.write('shift %d :\n' % (idx))
            log.write('GT:\n')
            log.write(r + '\n')
            log.write('output:\n')
            log.write(h + '\n')
            log.write('cer:\n')
            log.write(str(cer) + '\n')
            log.write('snr:\n')
            log.write(str(snr) + '\n')
            if(cer > 0.5):
                log.write('success\n')
            log.flush()
            if cer >= 0.5:
                success += 1
                

        cer_avg = distance_sum/rlen_sum
        success /= audios.shape[0]
        snr_avg = snr_sum/audios.shape[0]


        log.write('##############################################################\n')
        log.write('cer:\n')
        log.write(str(cer_avg) + '\n')
        log.write('jsr:\n')
        log.write(str(success) + '\n')
        log.write('snr:\n')
        log.write(str(snr_avg) + '\n')
        log.write('mean distortion:\n')
        log.write(str(np.mean(np.abs(delta_frame))) + '\n')
        log.close()
 
