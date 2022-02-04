import os
import numpy as np
import scipy.io.wavfile as wav
import argparse

toks = " abcdefghijklmnopqrstuvwxyz'-"

def wav2arr(path):

    list_ = os.listdir(path)
    list_.sort()
    audios = []
    lengths = []
    for file_ in list_:
        fs, audio = wav.read(os.path.join(path, file_))
        assert fs == 16000
        assert audio.dtype == np.int16
        
        audios.append(list(audio))
        lengths.append(len(audio))

    maxlen = max(lengths)
    audios = np.array([x+[0]*(maxlen-len(x)) for x in audios])

    return audios, lengths, maxlen, list_

def text2arr(path):
    list_ = os.listdir(path)

    list_.sort()
    texts = []
    lengths = []
    for file_ in list_:
        with open(os.path.join(path, file_), 'r') as f:
            text = f.read()

        text = [toks.index(x) for x in text] 
        texts.append(text)
        lengths.append(len(text))

    maxlen = max(lengths)
    texts = np.array([x+[0]*(maxlen-len(x)) for x in texts])

    return texts, lengths, maxlen, list_


#transform raw data into numpy array form
def process_data(src_path, dst_path):
    audios, audio_lengths, _, _ = wav2arr(os.path.join(src_path, "audio"))
    texts, text_lengths, _, _ = text2arr(os.path.join(src_path, "text"))

    parts = ["audios", "audio_lengths", "texts", "text_lengths"]
    for part in parts:
        np.save(os.path.join(dst_path, part), eval(part))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=None)
    
    parser.add_argument('--in', dest = "input",
                        type=str,
                        required=False, default= "data/raw")
    parser.add_argument('--out', dest = "output",
                        type=str,
                        required=False, default= "data/cache",
                        help="") 
    args = parser.parse_args()
    if not os.path.exists(args.output):
        os.mkdir(args.output)

    splits = ["train", "dev", "test"]
    for split in splits:
        output_path = os.path.join(args.output, split)
       
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        process_data(os.path.join(args.input, split), output_path)