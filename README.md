#  Universal Adversarial Perturbations (UniAP)
This repo corresponds to the paper "UniAP: Protect Speech Privacy with Non-targeted Universal Adversarial Perturbations".
Here we provide the appendix of the paper and audio samples including both the original speech samples and the adversarial audio examples (perturbed speech signals). 

## Appendix

In the appendix, we provide additional evaluation results which don't appear on the paper because of the page limit.
The demonstration of the UniAP app interface is also provided in this section. 


### TABLE XII: Peturbation performance with/without prepending before audio signals.

| **CER** | **JSR** | **SNR (dB)** | **CER** | **JSR** | **SNR (dB)** |
|:-------:|:-------:|:------------:|:-------:|:-------:|:------------:|
|  56.8%  |  62.5%  |     22.7     |  79.5%  |  88.2%  |     22.7     |
|  67.8%  |  77.1%  |     22.8     |  67.5%  |  75.9%  |     22.7     |
|  77.9%  |  85.7%  |     22.9     |  92.0%  |  92.3%  |     22.9     |
|  80.8%  |  88.2%  |     22.8     |  88.4%  |  91.0%  |     22.9     |
|  80.3%  |  86.7%  |     22.8     |  89.3%  |  91.1%  |     22.9     |
|  73.0%  |  85.5%  |     22.9     |  76.8%  |  86.1%  |     22.9     |
|  81.2%  |  88.6%  |     23.0     |  81.2%  |  88.1%  |     22.9     |
|  85.2%  |  89.7%  |     22.9     |  95.2%  |  93.1%  |     22.8     |
|  87.3%  |  91.7%  |     22.7     |  87.1%  |  90.7%  |     22.7     |
|  77.9%  |  86.5%  |     22.8     |  81.1%  |  87.9%  |     22.9     |

### TABLE XIII: Jamming performances of different UAPs in Librispeech test-clean dataset.

|   **Initialization Words of UAPs**   | **CER** | **JSR** | **SSS** | **SNR (dB)** |
|:------------------------------------:|:-------:|:-------:|:-------:|:------------:|
|               aduliadae              |  89.9%  |  90.9%  |   0.21  |     22.3     |
|     especially namely furthermore    |  92.1%  |  91.5%  |   0.24  |     22.3     |
|               for to be              |  95.5%  |  92.5%  |   0.24  |     22.3     |
|          furthermore namely          |  86.5%  |  89.4%  |   0.24  |     22.3     |
| investigations rosenboom mockingbird |  91.3%  |  91.9%  |   0.23  |     22.4     |
|               loiacano               |  83.1%  |  89.2%  |   0.21  |     22.5     |
|              mockingbird             |  85.4%  |  89.2%  |   0.25  |     22.3     |
|          namely considering          |  85.0%  |  89.3%  |   0.26  |     22.3     |
|      overstepped investigations      |  84.1%  |  90.0%  |   0.21  |     22.5     |
|              paperworker             |  83.8%  |  89.6%  |   0.23  |     22.3     |
|                  avg                 |  87.7%  |  90.4%  |   0.23  |     22.4     |

### TABLE XIV: Jamming performances of different UAPs in Gigaspeech test dataset.

|   **Initialization Words of UAPs**   | **CER** | **JSR** | **SSS** | **SNR (dB)** |
|:------------------------------------:|:-------:|:-------:|:-------:|:------------:|
|               aduliadae              |  70.0%  |  72.2%  |   0.24  |     25.4     |
|     especially namely furthermore    |  72.7%  |  73.9%  |   0.28  |     25.4     |
|               for to be              |  73.8%  |  74.1%  |   0.30  |     25.5     |
|          furthermore namely          |  67.8%  |  70.5%  |   0.28  |     25.4     |
| investigations rosenboom mockingbird |  71.5%  |  74.0%  |   0.26  |     25.5     |
|               loiacano               |  67.9%  |  72.8%  |   0.26  |     25.6     |
|              mockingbird             |  67.5%  |  70.5%  |   0.30  |     25.5     |
|          namely considering          |  67.1%  |  70.8%  |   0.29  |     25.4     |
|      overstepped investigations      |  67.7%  |  72.9%  |   0.26  |     25.7     |
|              paperworker             |  66.1%  |  70.9%  |   0.27  |     25.4     |
|                  avg                 |  69.2%  |  72.3%  |   0.27  |     25.2     |


### TABLE XV: Perturbation performances under the initialization statuses of connective words.

| **Initialization Words** | **CER** | **JSR** | **SNR (dB)** |
|:------------------------:|:-------:|:-------:|:------------:|
|         as far as        |  63.0%  |  70.9%  |     22.5     |
|    generally speaking    |  69.3%  |  80.9%  |     22.6     |
|        in contrast       |  72.1%  |  81.2%  |     22.7     |
|         of course        |  68.6%  |  76.6%  |     22.8     |
|      on the contrary     |  78.2%  |  85.0%  |     22.8     |
|            avg           |  70.2%  |  78.9%  |     22.7     |

### TABLE XVI: Perturbation performances under the initialization statuses of single common words and their combinations.

| **Initialization Words** | **CER** | **JSR** | **SNR (dB)** |
|:------------------------:|:-------:|:-------:|:------------:|
|            be            |  65.2%  |  76.8%  |     22.6     |
|            for           |  31.2%  |  12.6%  |     23.5     |
|            not           |  56.4%  |  61.9%  |     22.6     |
|            of            |  68.2%  |  75.8%  |     22.8     |
|            to            |  73.0%  |  82.6%  |     22.6     |
|            avg           |  58.8%  |  61.9%  |     22.8     |
|         for be to        |  97.2%  |  92.7%  |     22.7     |
|        for of not        |  54.9%  |  57.9%  |     22.7     |
|          not of          |  63.5%  |  72.0%  |     22.6     |
|           of be          |  63.4%  |  72.1%  |     22.7     |
|         to be of         |  74.1%  |  85.1%  |     22.8     |
|            avg           |  70.6%  |  76.0%  |     22.7     |

### TABLE XVII: Perturbation performances under the initialization statuses of single starter words and their combinations.

|    **Initialization Words**   | **CER** | **JSR** | **SNR (dB)** |
|:-----------------------------:|:-------:|:-------:|:------------:|
|          considering          |  70.2%  |  79.5%  |     22.8     |
|           especially          |  80.5%  |  87.8%  |     22.4     |
|          furthermore          |  64.6%  |  71.3%  |     22.7     |
|             namely            |  69.3%  |  80.6%  |     22.6     |
|             while             |  38.8%  |  25.4%  |     22.5     |
|              avg              |  64.7%  |  68.9%  |     22.6     |
|  especially considering while |  73.0%  |  82.0%  |     22.6     |
| especially namely furthermore |  93.7%  |  92.6%  |     22.6     |
|       furthermore namely      |  87.3%  |  89.8%  |     22.6     |
|       namely considering      |  86.3%  |  90.6%  |     22.6     |
|    while considering namely   |  87.1%  |  89.4%  |     22.7     |
|              avg              |  85.5%  |  88.9%  |     22.6     |

### TABLE XVIII: Perturbation performances under the initialization statuses of single words containing multiple vowel phonemes and their combination.

|    **Initialization Words**    | **CER** | **JSR** | **SNR (dB)** |
|:------------------------------:|:-------:|:-------:|:------------:|
|            aduliadae           |  91.3%  |  91.6%  |     22.6     |
|            kobayashi           |  69.2%  |  80.1%  |     22.7     |
|            loiacano            |  84.0%  |  89.6%  |     22.8     |
|            odonohue            |  55.8%  |  60.6%  |     22.6     |
|           paperworker          |  85.3%  |  90.1%  |     22.6     |
|               avg              |  71.1%  |  82.6%  |     22.7     |
|       kobayashi odonohue       |  85.4%  |  89.1%  |     22.8     |
| loiacano aduliadae paperworker |  81.9%  |  88.5%  |     22.9     |
|   loiacano odonohue kobayash   |  73.2%  |  84.5%  |     22.8     |
|       odonohue aduliadae       |  77.6%  |  85.2%  |     22.7     |
| paperworker aduliadae odonohue |  76.7%  |  82.9%  |     22.8     |
|               avg              |  79.0%  |  86.0%  |     22.8     |

### TABLE XIX: Perturbation performances under the initialization statuses of single words containing multiple consonant phonemes and their combinations

|        **Initialization Words**        | **CER** | **JSR** | **SNR (dB)** |
|:--------------------------------------:|:-------:|:-------:|:------------:|
|             investigations             |  80.4%  |  87.3%  |     22.7     |
|               mockingbird              |  86.8%  |  89.8%  |     22.7     |
|               overstepped              |  64.5%  |  72.5%  |     22.6     |
|                rosenboom               |  77.6%  |  84.5%  |     22.7     |
|               underplayed              |  80.2%  |  88.1%  |     22.6     |
|                   avg                  |  77.9%  |  84.4%  |     22.7     |
| investigations overstepped mockingbird |  73.3%  |  83.1%  |     22.6     |
|  investigations rosenboom mockingbird  |  93.0%  |  92.2%  |     22.7     |
|       mockingbird investigations       |  81.3%  |  87.7%  |     22.8     |
|       overstepped investigations       |  85.0%  |  89.9%  |     22.9     |
|   underplayed mockingbird overstepped  |  69.1%  |  75.9%  |     22.8     |
|                   avg                  |  80.3%  |  85.8%  |     22.7     |

### Demonstration of the UniAP app interface

![app1](https://user-images.githubusercontent.com/97931505/184637206-550d12ac-a954-406c-905f-51edf6789f06.jpg)
![app2](https://user-images.githubusercontent.com/97931505/184637213-d20e440d-fd8c-4587-9b3f-51129ce4dfb4.jpg)

## Digital domain Samples

We generate multiple non-targeted universal adversarial perturbations (UAPs) from different initialization status to defend against template subtracting. We set the initialization status to be one of the following categories: random combination of sentence starter words, words containing multiple vowel phonemes, words containing multiple consonant phonemes and their combination. 

We also include a random-chunk perturbation, which is formed by randomly selecting UAP chunks from a UAP pool. 

Please note that the perturbed audios within this section are on straightforwardly crafted on the digital domain rather than being played and recorded in the physical playback environment.

### Random combination of sentence starter words 
Origin audio (19-198-0034 in Librispeech):



https://user-images.githubusercontent.com/97931505/152574075-a27166b7-1052-492a-a302-31c7e3034eeb.mov



Ground truth: "there was not one family among their acquaintance who had reared and supported a boy accidentally found at their door not one young man whose origin was unknown her father had no ward and the squire of the parish no children".

Transcript: "there was not one family among their acquaintance who had reared and supported a boy excidentally found at their door not one young man whose arigin was unknown her father had no ward and the squire of the parish no children".

Origin audio + Universal perturbaion (init status: especially namely furthermore, SNR: 24.47dB):


https://user-images.githubusercontent.com/97931505/168715163-c8d7760f-e848-4ec1-b2f0-e92ce8eb9362.mov



Transcript: "uldn't from they would new as not win family among  their acquaintant roh scho had t reared and some ported an they accidentally found at vendorm an they wouldn't from they wouldn't not onrun young than whose arigen was on knoone from they wouldn't from the carfather had now thy ware an they wouldn't from and at the squired of the parish we now children  from they wouldn't".

### Single word containing multiple vowel phonemes 
Origin audio (5703-47198-0056 in Librispeech):


https://user-images.githubusercontent.com/97931505/152574625-3e0a07a0-75e1-4cad-940d-7ace8aa7f770.mov



Ground truth: "scandalized at the idea of such a precious garment being put on before breakfast that very one juliet assured her undaunted and was arrayed in it in spite of obvious disapproval after breakfast they went out".

Transcript: "skindalised at the idea of such a precious garment being put on before breakfast that bery one duliet asured her undaunted and was a rayed in it in spite of obvious disabroval after breakfast they went out".

Origin audio + Universal perturbaion (init status: aduliadae, SNR: 22.80dB):






https://user-images.githubusercontent.com/97931505/168715252-e7e7c0b3-1eb5-4f48-b3ac-cbbefe568c36.mov




Transcript: "the other plank of skindalrose than the oveia round sucaly a recious grment of the onther guonanian  fling of the ro plentoy other plank of the upler in the one on the other to of the other churan her upon in the antod of the other plack of the enewas or rave in a the plican supplid them ith on of the other slus an o the rillng of the other plank of the other catheron lar cloce t tey one aly other".

### Random combination of words containing multiple vowel phonemes
Origin audio (7517-100429-0009 in Librispeech):






https://user-images.githubusercontent.com/97931505/152575161-73f8f86c-14f7-4a73-95c5-f9fe21917764.mov




Ground truth: "has done the damage the soul yearns for something more startling than that the record of the pond".

Transcript: "has done the damage the sol yearns for something more startling than that the record of the pond".

Origin audio + Universal perturbaion (init status: kobayashi odonohue, SNR: 25.16dB):





https://user-images.githubusercontent.com/97931505/168715770-f2368fc9-6921-4659-b004-9e008692eba8.mov


Transcript: "only to post down in the damn ance you only to let you only to assoull yo yeur n his first some thing with you only tours startle in none do hat lik to let you only to let you only tirectrt of the pand ou ol".

### Single word containing multiple consonant phonemes 
Origin audio (5049-25947-0080 in Librispeech):


https://user-images.githubusercontent.com/97931505/152575370-ff2df804-1b10-4a48-9ef8-b856c95a7a42.mov


Ground truth: "as though we were at target practice and an irish sergeant byrne was assisting him by keeping up a continuous flow of comments and criticisms that showed the keenest enjoyment of the situation".

Transcript: "as though we were at target practice and in irish sargeant burn was the sisting him by keeping up ha continuous flow of comments an criticisms that showed the keenest injoyment of thi siuation".

Origin audio + Universal perturbaion (init status: mockingbird, SNR: 21.12dB):


https://user-images.githubusercontent.com/97931505/168715798-30b025f6-a780-4381-af6c-2373c0101cab.mov


Transcript: "uld have olo neler of bad par net he raftive have what he manded irish largein what he would hearn would have what he was the sisty we him of by healy wave in continuous flow of omment he would hear ousthat was he would have atshuwed himc enes to ujoyme a would has what yeash  he would have what h".

### Random combination of words containing multiple consonant phonemes
Origin audio (3436-172162-0005 in Librispeech):


https://user-images.githubusercontent.com/97931505/152575563-8bc3ac70-6ea9-4821-b74b-ddb14a45f4aa.mov


Ground truth: "so upon the morn they took their horses with the queen and rode a maying in woods and meadows as it pleased them in great joy and delight now there was a knight".

Transcript: "so upon the more they took their horses withe the queen and rode a maing in woods and meadows as it pleased them in great joy and delight now there was a night".

Origin audio + Universal perturbaion (init status: investigations rosenboom mockingbird, SNR: 26.42dB):


https://user-images.githubusercontent.com/97931505/168716044-a95f82f9-a917-48dd-8a3a-40cb50c3b9eb.mov


Transcript: "in they held them in they saw upon the mord thayed took their horsehes wwimenly helmen im help them in they had roawed them an unmanig old the ini oer anc an y meatows as if pleased  them in they helpd them in the in great that yoy and delight help them in they held them in they helpd them in they ano their was u night ti".

### Random-chunk UAP
Origin audio (1363-135842-0022 in Librispeech):


https://user-images.githubusercontent.com/97931505/168720913-6a396729-3553-4263-a8cd-166c93d25064.mov

Ground truth: "and forgotten to brush his hair it pointed every which way his legs were dark his feet black and his toes white his ears were without any hair at all".

Transcript: "and forgotten to brush his hair it pointed every which way his legs were dark his feet black and his toes white his ears were without any hair at all
".

Origin audio + Universal perturbaion (random-chunk, SNR: 30.18dB):


https://user-images.githubusercontent.com/97931505/168720955-5fb8a794-a975-4399-affb-50750f60c226.mov

Transcript: "the help in for a gut intol the riht he his hair be through tham n the hat the pointed every wich way would have ling with in aflick of the otheas le lags he would dar when think you took his with he would be glad the other thing you tened his cos would mi ly would have what he would have for the morning ame as fears tho here without  any hair at all ther the for the".



## Over-the-air Samples

We provide the random-chunk UAPs without over-the-air enhancement, cause there is little difference between the UAPs with and without enhancement from the hearing perspective. All the audios are recorded by real recording equipments and all of the given transcripts are the output of the robust DeepSpeech. Here we utilize distortion level to measure the noise-signal ratio. 

### Chatting scenario

In the chatting scenario, we provide audio examples of four different situations. Situations are described and differentiated by the distance between the user and
the microphone (UMD) and the distance between the jammer and the microphone (JMD).

#### UMD = 1m, JMD = 1m
Origin audio (1221-135767-0005 in Librispeech):


https://user-images.githubusercontent.com/97931505/168979733-4554c11e-36cf-41ee-98d2-fb927c05e8c5.mov



Ground truth: "it was the scarlet letter in another form the scarlet letter endowed with life".

Transcript: "it was the scar of letter in hanother form the scar ed letter in dowled with lighes".


Origin audio + Universal perturbaion (random-chunk, distortion level: -44.5dB):


https://user-images.githubusercontent.com/97931505/168981050-e6b28fba-e6a7-4352-a471-576eaabde09a.mov


Transcript: "take with his wo t it he a scares flatter af in anoth fi lotok o the a par at letter i his owl to his life the ol".

#### UMD = 4m, JMD = 4m
Origin audio (1284-134647-0000 in Librispeech):

https://user-images.githubusercontent.com/97931505/168983698-4369214e-f6c5-4bc7-a290-21805582912f.mov

Ground truth: "the grateful applause of the clergy has consecrated the memory of a prince who indulged their passions and promoted their interest".

Transcript: "the greateful flaws of the clerity has cauneecrated the memory of a crince who andulged their passes and promoted their interest".

Origin audio + Universal perturbaion (random-chunk, distortion level: -44.5dB):

https://user-images.githubusercontent.com/97931505/168981099-a76626e2-b2e6-4771-9f7e-5d3f19c1e028.mov

Transcript: "wold i to them for they arathfle bow  is aclerd the on the hitconstetrated  men wir ye was his trame singu to a induli f i ha tracti wood throughthe andpormiliwas erfol to reflute would have".

#### UMD = 0m, JMD = 1m
Origin audio (237-126133-0017 in Librispeech):

https://user-images.githubusercontent.com/97931505/168979862-66a6b56d-5d34-4773-824f-89334685061e.mov

Ground truth: "there jap you've caught it laughed percy while the others screamed at the sight of jasper's face".

Transcript:  "there jap you'v cot it laughed fircy while the other spreamed at the sigde of jaskes face".


Origin audio + Universal perturbaion (random-chunk, distortion level: -44.5dB):

https://user-images.githubusercontent.com/97931505/168981156-8820f44d-a865-49d0-806b-7b47d1d52af1.mov

Transcript: "liok a the othr tere jaf you've cot itthrough laugh wer the ole walthe others freen but exated jasplet ay".

#### UMD = 0m, JMD = 4m


Origin audio (2094-142345-0039 in Librispeech):

https://user-images.githubusercontent.com/97931505/168979955-154633a4-a575-4fc9-9070-cbfe07cc6c62.mov

Ground truth: "it is the head of a parrot with a little flower in his beak from a picture of carpaccio's one of his series of the life of saint george".

Transcript: "des the head of a parot of the little flowering he seat from a pictureof propotious one of his series of the life of santjurge".

Origin audio + Universal perturbaion (random-chunk, distortion level: -42dB):

https://user-images.githubusercontent.com/97931505/168981206-081481c9-7c3e-4bae-a7a7-9164e58104e4.mov

Transcript: "cos the heal marth the wilfflows bea frome feture tak osrias the hod them i fonly seriously the light wo sane clul".

### Walking scenario

We provide a picture and a video to show how the experiment in walking scenario was conducted. 

![walking_scenario_mosaic](https://user-images.githubusercontent.com/97931505/151647536-1fce9d39-9ab7-4faf-bed5-78c2ee735ac4.png)

https://user-images.githubusercontent.com/97931505/151294873-daee34eb-b221-400c-ad14-e014b18c0e50.mov

Origin audio (2094-142345-0039 in Librispeech):



https://user-images.githubusercontent.com/97931505/169000330-69acde04-4a62-4d93-8509-7cd62bed7dc4.mov



Ground truth: "the delaware dog he said leaning forward and peering through the dim light to catch the expression of the other's features is he afraid".

Transcript: "the delaware dork he said leaving forward and perang through the dim light to catch the expression of the other speechors dis het rad".

Origin audio + Universal perturbaion (random-chunk, distortion level: -44.5dB):


https://user-images.githubusercontent.com/97931505/169000396-4be485c8-961a-47c6-a0ef-ebc037b9a803.mov


Transcript: "pror they was take with his petedelawere dog he says wea in forwas in piams his cosem fing with jaction which gressiono be o tewisis is flimeref quat
".

### Voice call scenario

In the voice call scenario, we provide audio examples of both louder perturbation (L) and quieter perturbation (Q). Distortion-S is measured at the location of the speaker and Distortion-R is measured with the recorded perturbation and audio, that is to say, distortion-S represents the actual strength of distortion perceived by the speaker (user) and distortion-R represents the strength of distortion perceived by the receiver of the voice message.

Origin audio (2961-960-0001 in Librispeech):


https://user-images.githubusercontent.com/97931505/168986285-bd494a5e-e25d-4be3-8951-8e35a79bbfdb.mov


Ground truth: "the influence with the timaeus has exercised upon posterity is due partly to a misunderstanding".

Transcript: "at the influence which the to me us has ex recised the pon desterity is duehartly to a misenderstanding".

Origin audio + Universal perturbaion (Q, random-chunk, distortion-S: -46.07dB, distortion-R: -31.3dB):


https://user-images.githubusercontent.com/97931505/168986645-1161b7a8-ef9b-49ac-a376-ca63b7c57314.mov


Transcript: "would be ther them the influles which the e to me is has exerecised he bon bessparity from they would isdobed hard le to a missilir standir". 

Origin audio + Universal perturbaion (L, random-chunk, distortion-S: -44.97dB, distortion-R: -22.9dB):


https://user-images.githubusercontent.com/97931505/168986668-9f34bdcf-b50b-4e96-8a31-436f701f097f.mov


Transcript: "wul have like of the other o thet ol fuents which thed te me i with hes edrers rised the boy of thry to i re though them is do whithordly to olittender stand er".

