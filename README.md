# UniAP
This is the code corresponding to the paper "UniAP: Protect Speech Privacy with Non-targeted Universal Adversarial Perturbations"

//# Universal Adversarial Perturbations


## digital domain

We generate multiple non-targeted UAPs from different initialization status to defend against template subtracting method. We set the initialization status to be one of the following categories: random combination of sentence starter words, words containing multiple vowel phonemes, words containing multiple consonant phonemes and their combination. We also include a random-chunk perturbation.

### random combination of sentence starter words 
Origin audio 19-198-0034 in Librispeech):






https://user-images.githubusercontent.com/97931505/152574075-a27166b7-1052-492a-a302-31c7e3034eeb.mov





Ground truth: "there was not one family among their acquaintance who had reared and supported a boy accidentally found at their door not one young man whose origin was unknown her father had no ward and the squire of the parish no children".

Origin audio + Universal perturbaion (init status: especially namely furthermore, SNR: 24.47):






https://user-images.githubusercontent.com/97931505/168715163-c8d7760f-e848-4ec1-b2f0-e92ce8eb9362.mov







Transcript: "uldn't from they would new as not win family among  their acquaintant roh scho had t reared and some ported an they accidentally found at vendorm an they wouldn't from they wouldn't not onrun young than whose arigen was on knoone from they wouldn't from the carfather had now thy ware an they wouldn't from and at the squired of the parish we now children  from they wouldn't".

### single word containing multiple vowel phonemes 
Origin audio (5703-47198-0056 in Librispeech):



https://user-images.githubusercontent.com/97931505/152574625-3e0a07a0-75e1-4cad-940d-7ace8aa7f770.mov





Ground truth: "scandalized at the idea of such a precious garment being put on before breakfast that very one juliet assured her undaunted and was arrayed in it in spite of obvious disapproval after breakfast they went out".

Origin audio + Universal perturbaion (init status: aduliadae, SNR: 22.80):






https://user-images.githubusercontent.com/97931505/168715252-e7e7c0b3-1eb5-4f48-b3ac-cbbefe568c36.mov




Transcript: "the other plank of skindalrose than the oveia round sucaly a recious grment of the onther guonanian  fling of the ro plentoy other plank of the upler in the one on the other to of the other churan her upon in the antod of the other plack of the enewas or rave in a the plican supplid them ith on of the other slus an o the rillng of the other plank of the other catheron lar cloce t tey one aly other".

### random combination of words containing multiple vowel phonemes
Origin audio (7517-100429-0009 in Librispeech):






https://user-images.githubusercontent.com/97931505/152575161-73f8f86c-14f7-4a73-95c5-f9fe21917764.mov




Ground truth: "has done the damage the soul yearns for something more startling than that the record of the pond".

Origin audio + Universal perturbaion (init status: kobayashi odonohue, SNR: 25.16):








https://user-images.githubusercontent.com/97931505/168715770-f2368fc9-6921-4659-b004-9e008692eba8.mov








Transcript: "only to post down in the damn ance you only to let you only to assoull yo yeur n his first some thing with you only tours startle in none do hat lik to let you only to let you only tirectrt of the pand ou ol".

### single word containing multiple consonant phonemes 
Origin audio (5049-25947-0080 in Librispeech):





https://user-images.githubusercontent.com/97931505/152575370-ff2df804-1b10-4a48-9ef8-b856c95a7a42.mov





Ground truth: "as though we were at target practice and an irish sergeant byrne was assisting him by keeping up a continuous flow of comments and criticisms that showed the keenest enjoyment of the situation".

Origin audio + Universal perturbaion (init status: mockingbird, SNR: 21.12):







https://user-images.githubusercontent.com/97931505/168715798-30b025f6-a780-4381-af6c-2373c0101cab.mov







Transcript: "uld have olo neler of bad par net he raftive have what he manded irish largein what he would hearn would have what he was the sisty we him of by healy wave in continuous flow of omment he would hear ousthat was he would have atshuwed himc enes to ujoyme a would has what yeash  he would have what h".

### random combination of words containing multiple consonant phonemes
Origin audio (3436-172162-0005 in Librispeech):


https://user-images.githubusercontent.com/97931505/152575563-8bc3ac70-6ea9-4821-b74b-ddb14a45f4aa.mov


Ground truth: "so upon the morn they took their horses with the queen and rode a maying in woods and meadows as it pleased them in great joy and delight now there was a knight".

Origin audio + Universal perturbaion (init status: investigations rosenboom mockingbird, SNR:  26.42):







https://user-images.githubusercontent.com/97931505/168716044-a95f82f9-a917-48dd-8a3a-40cb50c3b9eb.mov







Transcript: "in they held them in they saw upon the mord thayed took their horsehes wwimenly helmen im help them in they had roawed them an unmanig old the ini oer anc an y meatows as if pleased  them in they helpd them in the in great that yoy and delight help them in they held them in they helpd them in they ano their was u night ti".

### random-chunk UAP
Origin audio (1363-135842-0022 in Librispeech):


https://user-images.githubusercontent.com/97931505/168720913-6a396729-3553-4263-a8cd-166c93d25064.mov

Ground truth: "and forgotten to brush his hair it pointed every which way his legs were dark his feet black and his toes white his ears were without any hair at all".

Origin audio + Universal perturbaion (random-chunk, SNR:  30.18):


https://user-images.githubusercontent.com/97931505/168720955-5fb8a794-a975-4399-affb-50750f60c226.mov

Transcript: "the help in for a gut intol the riht he his hair be through tham n the hat the pointed every wich way would have ling with in aflick of the otheas le lags he would dar when think you took his with he would be glad the other thing you tened his cos would mi ly would have what he would have for the morning ame as fears tho here without  any hair at all ther the for the".

## over-the-air



### chatting scenario

In the 

#### UMD = 1m, JMD = 1m
Origin audio (2961-960-0001 in Librispeech):


https://user-images.githubusercontent.com/97931505/168979733-4554c11e-36cf-41ee-98d2-fb927c05e8c5.mov



Ground truth: "it was the scarlet letter in another form the scarlet letter endowed with life".

Transcript: "it was the scar of letter in hanother form the scar ed letter in dowled with lighes".


Origin audio + Universal perturbaion (init status: kobayashi_loiacano, SNR: 42.21dB):


https://user-images.githubusercontent.com/97931505/168981050-e6b28fba-e6a7-4352-a471-576eaabde09a.mov



Transcript: "take with his wo t at es e scards flatter as interele fil butk o the a far that letter as  dou h his life theyl".

#### UMD = 4m, JMD = 4m
Origin audio (1320-122617-0037 in Librispeech):






https://user-images.githubusercontent.com/97931505/168983698-4369214e-f6c5-4bc7-a290-21805582912f.mov






Ground truth: "the grateful applause of the clergy has consecrated the memory of a prince who indulged their passions and promoted their interest".

Transcript: "the greateful flaws of the clerity has cauneecrated the memory of a crince who andulged their passes and promoted their interest".

Origin audio + Universal perturbaion (init status: notwithstanding_moreover_unusually, SNR: 42.11dB):




https://user-images.githubusercontent.com/97931505/168981099-a76626e2-b2e6-4771-9f7e-5d3f19c1e028.mov




Transcript: "wut is rison n for the ratful douses aclergey on the poscositrateds and mouas his trin singue tocal induly mintachi god through the and permiliis ther on to re leu ws".

#### UMD = 0m, JMD = 1m
Origin audio (1284-134647-0000 in Librispeech):



https://user-images.githubusercontent.com/97931505/168979862-66a6b56d-5d34-4773-824f-89334685061e.mov



Ground truth: "there jap you've caught it laughed percy while the others screamed at the sight of jasper's face".

Transcript:  "there jap you'v cot it laughed fircy while the other spreamed at the sigde of jaskes face".


Origin audio + Universal perturbaion (init status: notwithstanding_moreover_unusually, SNR: 42.11dB):



https://user-images.githubusercontent.com/97931505/168981156-8820f44d-a865-49d0-806b-7b47d1d52af1.mov


Transcript: "i  the other tair jaftes cothis s re lagh wir he ol clallty others sreem bat e cesteve jasp bes mamed".

#### UMD = 0m, JMD = 4m
![walking_scenario_mosaic](https://user-images.githubusercontent.com/97931505/151647536-1fce9d39-9ab7-4faf-bed5-78c2ee735ac4.png)

https://user-images.githubusercontent.com/97931505/151294873-daee34eb-b221-400c-ad14-e014b18c0e50.mov

Origin audio (2094-142345-0039 in Librispeech):



https://user-images.githubusercontent.com/97931505/168979955-154633a4-a575-4fc9-9070-cbfe07cc6c62.mov


Ground truth: "it is the head of a parrot with a little flower in his beak from a picture of carpaccio's one of his series of the life of saint george".

Transcript: "des the head of a parot of the little flowering he seat from a pictureof propotious one of his series of the life of santjurge".

Origin audio + Universal perturbaion (init status: notwithstanding_moreover_unusually, SNR: 42.71dB):



https://user-images.githubusercontent.com/97931505/168981206-081481c9-7c3e-4bae-a7a7-9164e58104e4.mov



Transcript: "goo the heado mareth othe loaflolly is be it fron e fitule take osyous they af them i forther seriously de lighte sane re as".

### voice call scenario
Origin audio (2094-142345-0039 in Librispeech):


https://user-images.githubusercontent.com/97931505/168986285-bd494a5e-e25d-4be3-8951-8e35a79bbfdb.mov


Ground truth: "the influence with the timaeus has exercised upon posterity is due partly to a misunderstanding".

Transcript: "at the influence which the to me us has ex recised the pon desterity is duehartly to a misenderstanding".

Origin audio + Universal perturbaion (Q):



https://user-images.githubusercontent.com/97931505/168986645-1161b7a8-ef9b-49ac-a376-ca63b7c57314.mov



Transcript: "prob wold be thorgh them but influlers which no to ne is has es recised the pontes perity from they would misdobe hards re to a misular standing". 

Origin audio + Universal perturbaion (L):



https://user-images.githubusercontent.com/97931505/168986668-9f34bdcf-b50b-4e96-8a31-436f701f097f.mov



Transcript: "would have ikeof the other tut olfuanc which thed pe may i with has exercised the pon o threre to wul bethew theim is dom hartly to omistunderstand it
".

