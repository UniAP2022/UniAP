# UniAP
This is the code corresponding to the paper "UniAP: Protect Speech Privacy with Non-targeted Universal Adversarial Perturbations"

# Universal Adversarial Perturbations
We generate multiple non-targeted UAPs from different initialization status to defend against template subtracting method. We set the initialization status to be one of the following categories: random combination of sentence starter words, words containing multiple vowel phonemes, words containing multiple consonant phonemes and their combination.

## digital domain
### random combination of sentence starter words 
Origin audio (xxx in xxx):



https://user-images.githubusercontent.com/97931505/151703353-546b6868-4e57-418e-b5d0-f93f575ff3dd.mov



Transcript: "xxx".

Origin audio + Universal perturbaion (init status: namely considering, SNR: xxx):

https://user-images.githubusercontent.com/97931505/151702647-a2a3d265-2dae-490b-b8e3-9269f02ccce6.mov


Transcript: "took a gave him a little brandy and left him collapsed in a chair will i ate hamost careful examination of the room you took".

### single word containing multiple vowel phonemes 
Origin audio (xxx in xxx):



https://user-images.githubusercontent.com/97931505/151703370-bb55ab58-b2cb-4e52-8038-1a9176eee9f0.mov



Transcript: "xxx".

Origin audio + Universal perturbaion (init status: aduliadae, SNR: xxx):



https://user-images.githubusercontent.com/97931505/151702556-94c92b4d-390d-4457-a642-da426a5c2ba6.mov



Transcript: "i've been others ti influenice o the which to other to me is i has exercised other on besspari tilhere's i been other disduo the cart to each o wo missender spanding others i've".

### random combination of words containing multiple vowel phonemes
Origin audio (xxx in xxx):



https://user-images.githubusercontent.com/97931505/151703379-81e6fc0f-10c1-4869-9f8e-7097c8fcf31d.mov



Transcript: "xxx".

Origin audio + Universal perturbaion (init status: loiacano aduliadae paperworker, SNR: xxx):



https://user-images.githubusercontent.com/97931505/151702585-aabf55c9-1008-4663-9826-aa3f17f31abc.mov



Transcript: "and when they we as the skar lat latter weinter nother form when they were come the scar let letter in  dowed when they flyng hm when e
".

### single word containing multiple consonant phonemes 
Origin audio (xxx in xxx):



https://user-images.githubusercontent.com/97931505/151703393-18b2e71f-ebce-4e19-a70a-8b078365775d.mov



Transcript: "xxx".

Origin audio + Universal perturbaion (init status: investigations, SNR: xxx):



https://user-images.githubusercontent.com/97931505/151702596-dcfd5e56-f3a5-4910-b80d-3785f54f04c8.mov



Transcript: "to there was given hes isan inti athy lan an intipidly ico nocket all for intere dorices with givento beu made think it o labiness r e don't blame in ee waso".

### random combination of words containing multiple consonant phonemes
Origin audio (xxx in xxx):



https://user-images.githubusercontent.com/97931505/151703405-bd72009d-ca6e-4011-9fc5-211ba7dbf2fa.mov



Transcript: "xxx".

Origin audio + Universal perturbaion (init status: mockingbird investigations, SNR: xxx):

https://user-images.githubusercontent.com/97931505/151702603-0f3aef15-98e1-4b72-a825-274fb2822346.mov

Transcript: "one of the takes marg appan you  got it takes ote latics firsiings while the others tereans at taside ob chass one of e day one of the takes one".


## over-the-air
### chatting scenario
#### The microphone is on the table
Origin audio (2961-960-0001 in xxx):

https://user-images.githubusercontent.com/97931505/151657475-c06ca5fa-5acb-48c6-a845-c5899a0eb361.mov

Transcript: "the influence with the timaeus has exercised upon posterity is due partly to a misunderstanding"

Origin audio + Universal perturbaion (init status: kobayashi_loiacano, SNR: 42.21dB):

https://user-images.githubusercontent.com/97931505/151657491-5e2e5074-e790-4da0-a3e7-afb32f4ea579.mov

Transcript: "to an you have that inluas which hel naer as anerfires the ponpescarity to es do wores wollises wec fanin to you to"

#### The microphone is on the wall
Origin audio (1320-122617-0037 in xxx):

https://user-images.githubusercontent.com/97931505/151657512-780bf48f-0e56-4699-9a35-c6fac935d370.mov

Transcript: "the delaware dog he said leaning forward and peering through the dim light to catch the expression of the other's features is he afraid"

Origin audio + Universal perturbaion (init status: notwithstanding_moreover_unusually, SNR: 42.11dB):

https://user-images.githubusercontent.com/97931505/151657523-65f4535c-4b04-4025-ab53-b5452d73c888.mov

Transcript: "was more tha was more the deliver ons iv ras le eforwadid en ho the den line e cash e fesion ye e shoers his hit fert was"

#### The mocrophone is on the windowstill
Origin audio (1284-134647-0000 in xxx):

https://user-images.githubusercontent.com/97931505/151657658-fcc3c79b-40f6-4bd8-949f-b50849ad4890.mov

Transcript: "the grateful applause of the clergy has consecrated the memory of a prince who indulged their passions and promoted their interest"

Origin audio + Universal perturbaion (init status: notwithstanding_moreover_unusually, SNR: 42.11dB):

https://user-images.githubusercontent.com/97931505/151657663-7a936445-c904-4fcf-adc2-6020cf9e7846.mov

Transcript: "was mor tham with a rad ole balo that ers was o head on as e aze an medary os creates was lose olst es hatas wit ad e noe ities fo was"

#### chatting while walking
![walking_scenario_mosaic](https://user-images.githubusercontent.com/97931505/151647536-1fce9d39-9ab7-4faf-bed5-78c2ee735ac4.png)

https://user-images.githubusercontent.com/97931505/151294873-daee34eb-b221-400c-ad14-e014b18c0e50.mov

Origin audio (2094-142345-0039 in xxx):

https://user-images.githubusercontent.com/97931505/151660153-a2f991e4-bab0-4c27-8ca5-e735d24a3f2d.mov

Transcript: "i've strong assurance that no evil will happen to you and my uncle and the children from anything i've done"

Origin audio + Universal perturbaion (init status: notwithstanding_moreover_unusually, SNR: 42.71dB):

https://user-images.githubusercontent.com/97931505/151660159-46040e9c-ac2c-40ca-92c6-1ea21c0826bc.mov

Transcript: "was wat e i sar e ser tit olels an ian hee was my hunwold an e soer or mittin the it dot was ore".

### voice call scenario
Origin audio (2094-142345-0039 in xxx):

https://user-images.githubusercontent.com/97931505/151660109-20b7d8da-cc33-47bd-bfdd-6cd45b7b3d18.mov

Transcript: "i've strong assurance that no evil will happen to you and my uncle and the children from anything i've done".

Origin audio + Universal perturbaion (init status: underplayed_conclusions_flextronic, SNR1: 48.21, SNR2: 31.51dB):

https://user-images.githubusercontent.com/97931505/151660115-c083fec5-1e7a-4d00-8c6b-c62f37aa730b.mov

Transcript: "they would with a they would with a ive strong as suran they spetan no egil wit had the te you and my own cold ind the children fermany ley nifeve dones they would". 

# Code Usage

  1. 
  
  2. get deepspeech and checkpoint

    git clone https://github.com/mozilla/DeepSpeech.git
    cd DeepSpeech
    git checkout tags/v0.4.1
    cd ..
    wget https://github.com/mozilla/DeepSpeech/releases/download/v0.4.1/deepspeech-0.4.1-checkpoint.tar.gz
    tar -xzf deepspeech-0.4.1-checkpoint.tar.gz
    
    
  3. docker image setup
    Pull the docker image and start it. 
    
    
    docker pull nvcr.io/nvidia/tensorflow:20.10-tf1-py3
    nvidia-docker run -it --name aae -v <yourdir>:/workspace/aae nvcr.io/nvidia/tensorflow:20.10-tf1-py3
    pip3 install progressbar numpy scipy pandas python_speech_features tables attrdict pyxdg ds-ctcdecoder Levenshtein
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
    The generation procedure shall read train and dev data from <processed_data_dir>, generate perturbation and saves it in <output_dir>/adv.wav
  6. evaluation
    ```
     python evaluation.py --data_path <processed_test_data_dir> --out <report_path> --random_shift
    ```
# Nontice
  Most of the code in this repo is based on https://github.com/carlini/audio_adversarial_examples. 
    
