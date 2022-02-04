# UniAP
This is the code corresponding to the paper "UniAP: Protect Speech Privacy with Non-targeted Universal Adversarial Perturbations"

# Universal Adversarial Perturbations
We generate multiple non-targeted UAPs from different initialization status to defend against template subtracting method. We set the initialization status to be one of the following categories: random combination of sentence starter words, words containing multiple vowel phonemes, words containing multiple consonant phonemes and their combination.

## digital domain
### random combination of sentence starter words 
Origin audio 19-198-0034 in Librispeech):






https://user-images.githubusercontent.com/97931505/152574075-a27166b7-1052-492a-a302-31c7e3034eeb.mov





Transcript: "there was not one family among their acquaintance who had reared and supported a boy accidentally found at their door not one young man whose origin was unknown her father had no ward and the squire of the parish no children".

Origin audio + Universal perturbaion (init status: namely considering, SNR: 24.52):



https://user-images.githubusercontent.com/97931505/152573763-7d5dcb72-e220-4bd0-bbfb-9f8f51a9f0ff.mov


Transcript: "you took a think you took a there was not in wone family anlong there acquaintidos who had reared and supported of boy accidentally found it their door took a think you took a thinke not thing you wan  the on e man who as arigin was unknowhon yo took a think you took our father had no mor took at think you time ot the squire of de parish couldno children you took a thing".

### single word containing multiple vowel phonemes 
Origin audio (5703-47198-0056 in Librispeech):



https://user-images.githubusercontent.com/97931505/152574625-3e0a07a0-75e1-4cad-940d-7ace8aa7f770.mov





Transcript: "scandalized at the idea of such a precious garment being put on before breakfast that very one juliet assured her undaunted and was arrayed in it in spite of obvious disapproval after breakfast they went out".

Origin audio + Universal perturbaion (init status: aduliadae, SNR: 23.08):





https://user-images.githubusercontent.com/97931505/152574510-cbf93ecb-0bd0-4eff-8856-0f91774efe4c.mov





Transcript: "others i've been others iv escered be ros with the ogia an o'm suchor corecious garm a  been in the won in ryfo iy been rit for the hn others i've been benspury in the onemante other ol be other shiven hurt i'm been daing thord been others i've been aml wos or raved the amothers i can sick i om at he onopanyo stos in coter is iv been others i've been other after br e first le ose i dont other".

### random combination of words containing multiple vowel phonemes
Origin audio (7517-100429-0009 in Librispeech):






https://user-images.githubusercontent.com/97931505/152575161-73f8f86c-14f7-4a73-95c5-f9fe21917764.mov




Transcript: "has done the damage the soul yearns for something more startling than that the record of the pond".

Origin audio + Universal perturbaion (init status: loiacano aduliadae paperworker, SNR: 25.18):





https://user-images.githubusercontent.com/97931505/152574965-386865f0-bfbf-4eff-9e5f-fefe39651ddf.mov




Transcript: "ercome when they were compos don me dam age and they were come when they were custol year and was fir some thing when they were commerce startling they on natthey were come when they were come when they were terectord of the pawnd wn they er".

### single word containing multiple consonant phonemes 
Origin audio (5049-25947-0080 in Librispeech):





https://user-images.githubusercontent.com/97931505/152575370-ff2df804-1b10-4a48-9ef8-b856c95a7a42.mov





Transcript: "as though we were at target practice and an irish sergeant byrne was assisting him by keeping up a continuous flow of comments and criticisms that showed the keenest enjoyment of the situation".

Origin audio + Universal perturbaion (init status: investigations, SNR: 22.17):



https://user-images.githubusercontent.com/97931505/152575337-a35857e7-14e6-4d8b-916e-f0373fd1cb41.mov



Transcript: "given to ther was goeloely wer rwas gaat they hard it tracutive was given to pand in irish sorganeven to they were earnd ther was given to lose o the sist am him and ligktlya emng out ther was continuous flow of commens and gritouses anvistther was nat show with he acenisty n joying tive ild thet was didtuation a ther was given o".

### random combination of words containing multiple consonant phonemes
Origin audio (3436-172162-0005 in Librispeech):


https://user-images.githubusercontent.com/97931505/152575563-8bc3ac70-6ea9-4821-b74b-ddb14a45f4aa.mov


Transcript: "so upon the morn they took their horses with the queen and rode a maying in woods and meadows as it pleased them in great joy and delight now there was a knight".

Origin audio + Universal perturbaion (init status: mockingbird investigations, SNR: 26.42):




https://user-images.githubusercontent.com/97931505/152575449-96625f50-5142-4992-80bb-c9bc136fdf1c.mov


Transcript: "the takes one of the takes one of the telopon the more n they hee their horses an he wit on of the team takes one of the ten road hees whene hunmained hakes kin e rood s in td madows as it wlesing on one of the takes one of the ningrat thejoy and delight akes one of the takes one of the takes one of the tew there was un night".


## over-the-air
### chatting scenario
#### The microphone is on the table
Origin audio (2961-960-0001 in Librispeech):

https://user-images.githubusercontent.com/97931505/151657475-c06ca5fa-5acb-48c6-a845-c5899a0eb361.mov

Transcript: "the influence with the timaeus has exercised upon posterity is due partly to a misunderstanding"

Origin audio + Universal perturbaion (init status: kobayashi_loiacano, SNR: 42.21dB):

https://user-images.githubusercontent.com/97931505/151657491-5e2e5074-e790-4da0-a3e7-afb32f4ea579.mov

Transcript: "to an you have that inluas which hel naer as anerfires the ponpescarity to es do wores wollises wec fanin to you to"

#### The microphone is on the wall
Origin audio (1320-122617-0037 in Librispeech):

https://user-images.githubusercontent.com/97931505/151657512-780bf48f-0e56-4699-9a35-c6fac935d370.mov

Transcript: "the delaware dog he said leaning forward and peering through the dim light to catch the expression of the other's features is he afraid"

Origin audio + Universal perturbaion (init status: notwithstanding_moreover_unusually, SNR: 42.11dB):

https://user-images.githubusercontent.com/97931505/151657523-65f4535c-4b04-4025-ab53-b5452d73c888.mov

Transcript: "was more tha was more the deliver ons iv ras le eforwadid en ho the den line e cash e fesion ye e shoers his hit fert was"

#### The mocrophone is on the windowstill
Origin audio (1284-134647-0000 in Librispeech):

https://user-images.githubusercontent.com/97931505/151657658-fcc3c79b-40f6-4bd8-949f-b50849ad4890.mov

Transcript: "the grateful applause of the clergy has consecrated the memory of a prince who indulged their passions and promoted their interest"

Origin audio + Universal perturbaion (init status: notwithstanding_moreover_unusually, SNR: 42.11dB):

https://user-images.githubusercontent.com/97931505/151657663-7a936445-c904-4fcf-adc2-6020cf9e7846.mov

Transcript: "was mor tham with a rad ole balo that ers was o head on as e aze an medary os creates was lose olst es hatas wit ad e noe ities fo was"

#### chatting while walking
![walking_scenario_mosaic](https://user-images.githubusercontent.com/97931505/151647536-1fce9d39-9ab7-4faf-bed5-78c2ee735ac4.png)

https://user-images.githubusercontent.com/97931505/151294873-daee34eb-b221-400c-ad14-e014b18c0e50.mov

Origin audio (2094-142345-0039 in Librispeech):

https://user-images.githubusercontent.com/97931505/151660153-a2f991e4-bab0-4c27-8ca5-e735d24a3f2d.mov

Transcript: "i've strong assurance that no evil will happen to you and my uncle and the children from anything i've done"

Origin audio + Universal perturbaion (init status: notwithstanding_moreover_unusually, SNR: 42.71dB):

https://user-images.githubusercontent.com/97931505/151660159-46040e9c-ac2c-40ca-92c6-1ea21c0826bc.mov

Transcript: "was wat e i sar e ser tit olels an ian hee was my hunwold an e soer or mittin the it dot was ore".

### voice call scenario
Origin audio (2094-142345-0039 in Librispeech):

https://user-images.githubusercontent.com/97931505/151660109-20b7d8da-cc33-47bd-bfdd-6cd45b7b3d18.mov

Transcript: "i've strong assurance that no evil will happen to you and my uncle and the children from anything i've done".

Origin audio + Universal perturbaion (init status: underplayed_conclusions_flextronic, SNR1: 48.21, SNR2: 31.51dB):

https://user-images.githubusercontent.com/97931505/151660115-c083fec5-1e7a-4d00-8c6b-c62f37aa730b.mov

Transcript: "they would with a they would with a ive strong as suran they spetan no egil wit had the te you and my own cold ind the children fermany ley nifeve dones they would". 

# Code Usage

1. get the code  
```
git clone https://github.com/UniAP2022/UniAP.git
```
2. get deepspeech and checkpoint

```
cd UniAP/src
git clone https://github.com/mozilla/DeepSpeech.git
cd DeepSpeech
git checkout tags/v0.4.1
cd ..
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.4.1/deepspeech-0.4.1-checkpoint.tar.gz
tar -xzf deepspeech-0.4.1-checkpoint.tar.gz
```

3. docker image setup
Pull the docker image and start it. 

```
docker pull nvcr.io/nvidia/tensorflow:20.10-tf1-py3
nvidia-docker run -it --name aae -v UniAP/src:/workspace/aae nvcr.io/nvidia/tensorflow:20.10-tf1-py3
pip3 install progressbar numpy scipy pandas python_speech_features tables attrdict pyxdg ds-ctcdecoder Levenshtein
```
4. data preparation 
Before generating adversarial perturbation, we should process the data (audios and texts) into a format that matches the input form of generation procedure.
```
cd /workspace/aae
python process_data.py --in <raw_data_dir> --out <processed_data_dir>
```  

The <raw_data_dir> should be originized as three folders, train, dev and test. These folders are futher divided into two folders, namely audio and text, which contains  audio files in wav form with 16 bit depth and 16k sampling rate and their corresponding transcripts. It should be noted audio files and text files need to have the same filename. For more details , we have provided a simple in data/raw. The audio files and text files are selected from Librispeech train-clean-100.
5. generation perturabtion  
```
python attack.py --inputdir <processed_data_dir> --outdir <output_dir> --random_shift  
```

The generation procedure shall read train and dev data from <processed_data_dir>, generate perturbation and save it in <output_dir>/adv.wav  
6. evaluation  
```
python evaluation.py --data_path <processed_data_dir>/test --delta <output_dir>/adv.wav --out <report_path> 
```

The evaluation procedure shall summary the evaluation in the text form with the path of <report_path>.
# Nontice
  Most of the code in this repo is based on https://github.com/carlini/audio_adversarial_examples. 
    
