# UniAP
This is the code corresponding to the paper "UniAP: Protect Speech Privacy with Non-targeted Universal Adversarial Perturbations"

# Universal Adversarial Perturbations
We generate multiple non-targeted UAPs from different initialization status to defend against template subtracting method. We set the initialization status to be one of the following categories: random combination of sentence starter words, words containing multiple vowel phonemes, words containing multiple consonant phonemes and their combination.

## digital domain
### random combination of sentence starter words 
Origin audio (xxx in xxx):

https://user-images.githubusercontent.com/97931505/149879984-87b26ce0-0b06-479a-88a5-1af5038b119f.mov

Transcript: "xxx".

Origin audio + Universal perturbaion (init status: xxx, SNR: xxx):

https://user-images.githubusercontent.com/97931505/149879984-87b26ce0-0b06-479a-88a5-1af5038b119f.mov

Transcript: "xxx".

### single word containing multiple vowel phonemes 
Origin audio (xxx in xxx):

https://user-images.githubusercontent.com/97931505/149879984-87b26ce0-0b06-479a-88a5-1af5038b119f.mov

Transcript: "xxx".

Origin audio + Universal perturbaion (init status: xxx, SNR: xxx):

https://user-images.githubusercontent.com/97931505/149879984-87b26ce0-0b06-479a-88a5-1af5038b119f.mov

Transcript: "xxx".

### random combination of words containing multiple vowel phonemes
Origin audio (xxx in xxx):

https://user-images.githubusercontent.com/97931505/149879984-87b26ce0-0b06-479a-88a5-1af5038b119f.mov

Transcript: "xxx".

Origin audio + Universal perturbaion (init status: xxx, SNR: xxx):

https://user-images.githubusercontent.com/97931505/149879984-87b26ce0-0b06-479a-88a5-1af5038b119f.mov

Transcript: "xxx".

### single word containing multiple consonant phonemes 
Origin audio (xxx in xxx):

https://user-images.githubusercontent.com/97931505/149879984-87b26ce0-0b06-479a-88a5-1af5038b119f.mov

Transcript: "xxx".

Origin audio + Universal perturbaion (init status: xxx, SNR: xxx):

https://user-images.githubusercontent.com/97931505/149879984-87b26ce0-0b06-479a-88a5-1af5038b119f.mov

Transcript: "xxx".

### random combination of words containing multiple consonant phonemes
Origin audio (xxx in xxx):

https://user-images.githubusercontent.com/97931505/149879984-87b26ce0-0b06-479a-88a5-1af5038b119f.mov

Transcript: "xxx".

Origin audio + Universal perturbaion (init status: xxx, SNR: xxx):

https://user-images.githubusercontent.com/97931505/149879984-87b26ce0-0b06-479a-88a5-1af5038b119f.mov

Transcript: "xxx".


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

# Code
