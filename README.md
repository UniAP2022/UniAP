# UniAP
This is the code corresponding to the paper "UniAP: Protect Speech Privacy with Non-targeted Universal Adversarial Perturbations"

# Universal Adversarial Perturbations
We generate multiple non-targeted UAPs from different initialization status to defend against template subtracting method. We set the initialization status to be one of the following categories: random combination of sentence starter words, words containing multiple vowel phonemes, words containing multiple consonant phonemes and their combination.

## digital domain
### random combination of sentence starter words 
Origin audio 19-198-0034 in Librispeech):






https://user-images.githubusercontent.com/97931505/152574075-a27166b7-1052-492a-a302-31c7e3034eeb.mov





Transcript: "there was not one family among their acquaintance who had reared and supported a boy accidentally found at their door not one young man whose origin was unknown her father had no ward and the squire of the parish no children".

Origin audio + Universal perturbaion (init status: especially namely furthermore, SNR: 24.47):






https://user-images.githubusercontent.com/97931505/168715163-c8d7760f-e848-4ec1-b2f0-e92ce8eb9362.mov







Transcript: "uldn't from they would new as not win family among  their acquaintant roh scho had t reared and some ported an they accidentally found at vendorm an they wouldn't from they wouldn't not onrun young than whose arigen was on knoone from they wouldn't from the carfather had now thy ware an they wouldn't from and at the squired of the parish we now children  from they wouldn't".

### single word containing multiple vowel phonemes 
Origin audio (5703-47198-0056 in Librispeech):



https://user-images.githubusercontent.com/97931505/152574625-3e0a07a0-75e1-4cad-940d-7ace8aa7f770.mov





Transcript: "scandalized at the idea of such a precious garment being put on before breakfast that very one juliet assured her undaunted and was arrayed in it in spite of obvious disapproval after breakfast they went out".

Origin audio + Universal perturbaion (init status: aduliadae, SNR: 22.80):






https://user-images.githubusercontent.com/97931505/168715252-e7e7c0b3-1eb5-4f48-b3ac-cbbefe568c36.mov




Transcript: "the other plank of skindalrose than the oveia round sucaly a recious grment of the onther guonanian  fling of the ro plentoy other plank of the upler in the one on the other to of the other churan her upon in the antod of the other plack of the enewas or rave in a the plican supplid them ith on of the other slus an o the rillng of the other plank of the other catheron lar cloce t tey one aly other".

### random combination of words containing multiple vowel phonemes
Origin audio (7517-100429-0009 in Librispeech):






https://user-images.githubusercontent.com/97931505/152575161-73f8f86c-14f7-4a73-95c5-f9fe21917764.mov




Transcript: "has done the damage the soul yearns for something more startling than that the record of the pond".

Origin audio + Universal perturbaion (init status: kobayashi odonohue, SNR: 25.16):








https://user-images.githubusercontent.com/97931505/168715770-f2368fc9-6921-4659-b004-9e008692eba8.mov








Transcript: "only to post down in the damn ance you only to let you only to assoull yo yeur n his first some thing with you only tours startle in none do hat lik to let you only to let you only tirectrt of the pand ou ol".

### single word containing multiple consonant phonemes 
Origin audio (5049-25947-0080 in Librispeech):





https://user-images.githubusercontent.com/97931505/152575370-ff2df804-1b10-4a48-9ef8-b856c95a7a42.mov





Transcript: "as though we were at target practice and an irish sergeant byrne was assisting him by keeping up a continuous flow of comments and criticisms that showed the keenest enjoyment of the situation".

Origin audio + Universal perturbaion (init status: mockingbird, SNR: 21.12):







https://user-images.githubusercontent.com/97931505/168715798-30b025f6-a780-4381-af6c-2373c0101cab.mov







Transcript: "uld have olo neler of bad par net he raftive have what he manded irish largein what he would hearn would have what he was the sisty we him of by healy wave in continuous flow of omment he would hear ousthat was he would have atshuwed himc enes to ujoyme a would has what yeash  he would have what h".

### random combination of words containing multiple consonant phonemes
Origin audio (3436-172162-0005 in Librispeech):


https://user-images.githubusercontent.com/97931505/152575563-8bc3ac70-6ea9-4821-b74b-ddb14a45f4aa.mov


Transcript: "so upon the morn they took their horses with the queen and rode a maying in woods and meadows as it pleased them in great joy and delight now there was a knight".

Origin audio + Universal perturbaion (init status: investigations rosenboom mockingbird, SNR:  26.42):







https://user-images.githubusercontent.com/97931505/168716044-a95f82f9-a917-48dd-8a3a-40cb50c3b9eb.mov







Transcript: "in they held them in they saw upon the mord thayed took their horsehes wwimenly helmen im help them in they had roawed them an unmanig old the ini oer anc an y meatows as if pleased  them in they helpd them in the in great that yoy and delight help them in they held them in they helpd them in they ano their was u night ti".

### random-chunk UAP
Origin audio (1363-135842-0022 in Librispeech):


https://user-images.githubusercontent.com/97931505/168720913-6a396729-3553-4263-a8cd-166c93d25064.mov

Transcript: "and forgotten to brush his hair it pointed every which way his legs were dark his feet black and his toes white his ears were without any hair at all".

Origin audio + Universal perturbaion (random-chunk, SNR:  30.18):


https://user-images.githubusercontent.com/97931505/168720955-5fb8a794-a975-4399-affb-50750f60c226.mov

Transcript: "the help in for a gut intol the riht he his hair be through tham n the hat the pointed every wich way would have ling with in aflick of the otheas le lags he would dar when think you took his with he would be glad the other thing you tened his cos would mi ly would have what he would have for the morning ame as fears tho here without  any hair at all ther the for the".

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


