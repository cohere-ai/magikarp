# Report for `microsoft/Phi-3-mini-128k-instruct`

## Model info

* Model Info: 
  * Tied embeddings: False
  * LM head uses bias: False
  * Embeddings shape: [32064, 3072]
* Tokenizer Info: 
  * Vocab Size: 32011
  * Tokenizer Class: LlamaTokenizer
  * Tokenizer Type: BPE
  * Bytes handling: Byte Fallback
  * Token for verification prompt building: springframework
  * Token id for verification prompt building: 6688
* Indicator summary: 
  * Indicator for under-trained tokens: E_{in} L2 Norm
  * Overall distribution: 2.028 +/- 0.382
* Detected Token Counts: 
  * Number of tested under-trained tokens: 636, 635 non-special, 169 below p = 0.01 threshold, 97 below soft indicator threshold
  * Number of single byte tokens: 351, of which 110 below indicator threshold
  * Number of special tokens: 0, of which 0 below indicator threshold

## Under-trained token indicators plot
![Indicators scatter plots](../indicators_pairplot_byid/microsoft_Phi_3_mini_128k_instruct.png)

## Verification plot
![Verification plot](../verifications_scatterplot/microsoft_Phi_3_mini_128k_instruct.png)

## Under-trained token verification results
97 entries below threshold of 0.261

|   token_id | token                       |   indicator | max_prob                                                         | in_other_tokens                                                                     |
|------------|-----------------------------|-------------|------------------------------------------------------------------|-------------------------------------------------------------------------------------|
|      28574 | ````` ▁Mediabestanden ````` |  0.00199483 | <span style='border: 1px solid rgb(169, 68, 66);'>6.4e-06</span> |                                                                                     |
|      20528 | ````` ▁autorytatywna `````  |  0.00200511 | <span style='border: 1px solid rgb(169, 68, 66);'>6.4e-06</span> |                                                                                     |
|      27918 | ````` ▁Хронологија `````    |  0.0020083  | <span style='border: 1px solid rgb(169, 68, 66);'>6.3e-06</span> |                                                                                     |
|      20609 | ````` ▁Portály `````        |  0.00202689 | <span style='border: 1px solid rgb(169, 68, 66);'>6.4e-06</span> |                                                                                     |
|      11804 | ````` Архівовано `````      |  0.00204477 | <span style='border: 1px solid rgb(169, 68, 66);'>6.3e-06</span> |                                                                                     |
|      24294 | ````` Webachiv `````        |  0.00939883 | <span style='border: 1px solid rgb(169, 68, 66);'>5.3e-06</span> |                                                                                     |
|      16110 | ````` ▁Спољашње `````       |  0.0110712  | <span style='border: 1px solid rgb(169, 68, 66);'>6.4e-06</span> |                                                                                     |
|      27914 | ````` ▁archiválva `````     |  0.0148674  | <span style='border: 1px solid rgb(169, 68, 66);'>8.1e-06</span> |                                                                                     |
|      11766 | ````` хівовано `````        |  0.0249311  | <span style='border: 1px solid rgb(169, 68, 66);'>3.8e-06</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` Архівовано `````</span>     |
|      28653 | ````` ▁regnigaste `````     |  0.0403179  | <span style='border: 1px solid rgb(169, 68, 66);'>3.9e-06</span> |                                                                                     |
|      21836 | ````` ▁надморској `````     |  0.0489446  | <span style='border: 1px solid rgb(169, 68, 66);'>3.9e-06</span> |                                                                                     |
|      18051 | ````` ▁савезној `````       |  0.0577595  | <span style='border: 1px solid rgb(169, 68, 66);'>2.8e-06</span> |                                                                                     |
|      28649 | ````` ▁årsnederbörd `````   |  0.0602276  | <span style='border: 1px solid rgb(169, 68, 66);'>8.3e-06</span> |                                                                                     |
|      21673 | ````` ▁висини `````         |  0.063432   | <span style='border: 1px solid rgb(169, 68, 66);'>7.2e-06</span> |                                                                                     |
|      26821 | ````` ▁Enllaços `````       |  0.0747744  | <span style='border: 1px solid rgb(169, 68, 66);'>9.5e-06</span> |                                                                                     |
|      23996 | ````` ▁живело `````         |  0.0822947  | <span style='border: 1px solid rgb(169, 68, 66);'>5.7e-06</span> |                                                                                     |
|      16056 | ````` љашње `````           |  0.0844199  | <span style='border: 1px solid rgb(169, 68, 66);'>4.8e-06</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁Спољашње `````</span>      |
|      28623 | ````` ▁Genomsnitt `````     |  0.0889924  | <span style='border: 1px solid rgb(169, 68, 66);'>1.5e-06</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁Genomsnittlig `````</span> |
|      17981 | ````` ▁Externí `````        |  0.0889966  | <span style='border: 1px solid rgb(169, 68, 66);'>1.4e-06</span> |                                                                                     |
|      27900 | ````` ▁eredetiből `````     |  0.0895897  | <span style='border: 1px solid rgb(169, 68, 66);'>5.6e-06</span> |                                                                                     |
<details><summary>77 additional entries below threshold</summary>

|   token_id | token                      |   indicator | max_prob                                                         | in_other_tokens                                                                                                                                                                                                                                     |
|------------|----------------------------|-------------|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      20486 | ````` tatywna `````        |   0.0953026 | <span style='border: 1px solid rgb(169, 68, 66);'>2.7e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁autorytatywna `````</span>                                                                                                                                                                 |
|      28354 | ````` ▁Расподела `````     |   0.0970301 | <span style='border: 1px solid rgb(169, 68, 66);'>1.8e-06</span> |                                                                                                                                                                                                                                                     |
|      28416 | ````` ▁Мексичка `````      |   0.0973658 | <span style='border: 1px solid rgb(169, 68, 66);'>5.5e-06</span> |                                                                                                                                                                                                                                                     |
|      20422 | ````` ніципалі `````       |   0.104245  | <span style='border: 1px solid rgb(169, 68, 66);'>3.2e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁муніципалі `````</span>                                                                                                                                                                    |
|      23654 | ````` ▁dátummal `````      |   0.104587  | <span style='border: 1px solid rgb(169, 68, 66);'>5.1e-06</span> |                                                                                                                                                                                                                                                     |
|      22835 | ````` ▁муніципалі `````    |   0.105292  | <span style='border: 1px solid rgb(169, 68, 66);'>4e-05</span>   |                                                                                                                                                                                                                                                     |
|      28642 | ````` ▁regnig `````        |   0.106802  | <span style='border: 1px solid rgb(169, 68, 66);'>2.1e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁regnigaste `````</span>                                                                                                                                                                    |
|      26847 | ````` .:\u200a `````       |   0.108869  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-05</span> |                                                                                                                                                                                                                                                     |
|      24029 | ````` ▁Jegyzetek `````     |   0.109509  | <span style='border: 1px solid rgb(169, 68, 66);'>4.9e-06</span> |                                                                                                                                                                                                                                                     |
|      28650 | ````` ▁Genomsnittlig ````` |   0.115266  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-06</span> |                                                                                                                                                                                                                                                     |
|      27645 | ````` ▁Попис `````         |   0.118672  | <span style='border: 1px solid rgb(169, 68, 66);'>2.2e-05</span> |                                                                                                                                                                                                                                                     |
|       7784 | ````` ▁underarter `````    |   0.125647  | <span style='border: 1px solid rgb(169, 68, 66);'>2.4e-05</span> |                                                                                                                                                                                                                                                     |
|      26011 | ````` ▁Архивная `````      |   0.128281  | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-06</span> |                                                                                                                                                                                                                                                     |
|      19837 | ````` ▁Населення `````     |   0.131483  | <span style='border: 1px solid rgb(169, 68, 66);'>6.7e-06</span> |                                                                                                                                                                                                                                                     |
|      22011 | ````` ▁насељу `````        |   0.132251  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-05</span> |                                                                                                                                                                                                                                                     |
|      14562 | ````` ▁Посилання `````     |   0.135106  | <span style='border: 1px solid rgb(169, 68, 66);'>5.1e-06</span> |                                                                                                                                                                                                                                                     |
|      26734 | ````` ▁Årsmed `````        |   0.137241  | <span style='border: 1px solid rgb(169, 68, 66);'>3.2e-06</span> |                                                                                                                                                                                                                                                     |
|       9462 | ````` Hozzáférés `````     |   0.137987  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00023</span> |                                                                                                                                                                                                                                                     |
|      28647 | ````` ▁torraste `````      |   0.13958   | <span style='border: 1px solid rgb(169, 68, 66);'>1.6e-06</span> |                                                                                                                                                                                                                                                     |
|       7651 | ````` ▁släktet `````       |   0.139762  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-05</span> |                                                                                                                                                                                                                                                     |
|      24631 | ````` ▁Források `````      |   0.140626  | <span style='border: 1px solid rgb(169, 68, 66);'>4.9e-06</span> |                                                                                                                                                                                                                                                     |
|      20180 | ````` ▁Мексику `````       |   0.142628  | <span style='border: 1px solid rgb(169, 68, 66);'>7.8e-05</span> |                                                                                                                                                                                                                                                     |
|      28263 | ````` ▁Odkazy `````        |   0.142864  | <span style='border: 1px solid rgb(169, 68, 66);'>1.4e-05</span> |                                                                                                                                                                                                                                                     |
|      24971 | ````` ▁Джерела `````       |   0.145297  | <span style='border: 1px solid rgb(169, 68, 66);'>9.9e-06</span> |                                                                                                                                                                                                                                                     |
|      20739 | ````` ▁надмор `````        |   0.148667  | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁надморској `````</span>                                                                                                                                                                    |
|      11229 | ````` ▁становника `````    |   0.149832  | <span style='border: 1px solid rgb(169, 68, 66);'>3.3e-05</span> |                                                                                                                                                                                                                                                     |
|      28090 | ````` ▁Савезне `````       |   0.150406  | <span style='border: 1px solid rgb(169, 68, 66);'>5.7e-06</span> |                                                                                                                                                                                                                                                     |
|      23406 | ````` ▁општини `````       |   0.150545  | <span style='border: 1px solid rgb(169, 68, 66);'>1e-05</span>   |                                                                                                                                                                                                                                                     |
|      28633 | ````` nederbörd `````      |   0.158638  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00011</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁årsnederbörd `````</span>                                                                                                                                                                  |
|      23875 | ````` ▁Насеље `````        |   0.160807  | <span style='border: 1px solid rgb(251, 189, 8);'>0.036</span>   |                                                                                                                                                                                                                                                     |
|      14414 | ````` ▁Archivlink `````    |   0.161014  | <span style='border: 1px solid rgb(169, 68, 66);'>4e-05</span>   |                                                                                                                                                                                                                                                     |
|      23726 | ````` ▁насеља `````        |   0.161063  | <span style='border: 1px solid rgb(169, 68, 66);'>2.9e-05</span> |                                                                                                                                                                                                                                                     |
|      17916 | ````` abestanden `````     |   0.16379   | <span style='border: 1px solid rgb(169, 68, 66);'>2.1e-06</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁Mediabestanden `````</span>                                                                                                                                                                |
|      18044 | ````` ▁Становништво `````  |   0.17093   | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-05</span> |                                                                                                                                                                                                                                                     |
|      25840 | ````` ▁државе `````        |   0.178857  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00026</span> |                                                                                                                                                                                                                                                     |
|      18140 | ````` rinningsområ `````   |   0.181259  | <span style='border: 1px solid rgb(169, 68, 66);'>4.7e-05</span> |                                                                                                                                                                                                                                                     |
|      20645 | ````` ▁Przypisy `````      |   0.183177  | <span style='border: 1px solid rgb(169, 68, 66);'>6.6e-06</span> |                                                                                                                                                                                                                                                     |
|      18676 | ````` ніципа `````         |   0.184698  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0011</span>  | <span style='border: 1px solid rgb(169, 68, 66);'>````` ніципалі `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁муніципалі `````</span>                                                                                     |
|      24291 | ````` IABot `````          |   0.187117  | <span style='border: 1px solid rgb(40, 167, 69);'>1</span>       |                                                                                                                                                                                                                                                     |
|      16916 | ````` ▁invån `````         |   0.188034  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00015</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁invånare `````</span>                                                                                                                                                                      |
|      27610 | ````` ▁gminie `````        |   0.189999  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00096</span> |                                                                                                                                                                                                                                                     |
|      23117 | ````` brázky `````         |   0.190894  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` Obrázky `````</span>                                                                                                                                                                        |
|      10688 | ````` ▁gepublic `````      |   0.197517  | <span style='border: 1px solid rgb(169, 68, 66);'>6.4e-05</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁gepubliceerd `````</span>                                                                                                                                                                  |
|      23715 | ````` ▁Källor `````        |   0.19757   | <span style='border: 1px solid rgb(169, 68, 66);'>6.8e-05</span> |                                                                                                                                                                                                                                                     |
|      12731 | ````` ederbörd `````       |   0.197678  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0032</span>  | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁nederbörd `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` nederbörd `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁årsnederbörd `````</span> |
|      25283 | ````` ▁липня `````         |   0.198478  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00022</span> |                                                                                                                                                                                                                                                     |
|      22768 | ````` ▁жовт `````          |   0.200147  | <span style='border: 1px solid rgb(169, 68, 66);'>3.3e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁жовтня `````</span>                                                                                                                                                                        |
|       7718 | ````` ▁beskrevs `````      |   0.201887  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-05</span> |                                                                                                                                                                                                                                                     |
|      28906 | ````` ▁листопада `````     |   0.20466   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00025</span> |                                                                                                                                                                                                                                                     |
|      24309 | ````` ▁чемпі `````         |   0.208272  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0023</span>  |                                                                                                                                                                                                                                                     |
|      26782 | ````` ▁пописа `````        |   0.209006  | <span style='border: 1px solid rgb(169, 68, 66);'>2.2e-05</span> |                                                                                                                                                                                                                                                     |
|      26964 | ````` ▁Хронологи `````     |   0.21286   | <span style='border: 1px solid rgb(169, 68, 66);'>2.3e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁Хронологија `````</span>                                                                                                                                                                   |
|      28791 | ````` ▁віці `````          |   0.213572  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0095</span>  |                                                                                                                                                                                                                                                     |
|      26527 | ````` ▁червня `````        |   0.216537  | <span style='border: 1px solid rgb(169, 68, 66);'>9.5e-05</span> |                                                                                                                                                                                                                                                     |
|      18328 | ````` ▁trakten `````       |   0.216854  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0049</span>  |                                                                                                                                                                                                                                                     |
|      24852 | ````` ▁грудня `````        |   0.217065  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0013</span>  |                                                                                                                                                                                                                                                     |
|      25460 | ````` ▁жовтня `````        |   0.217765  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00016</span> |                                                                                                                                                                                                                                                     |
|      24097 | ````` ▁huvudstaden `````   |   0.219299  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00035</span> |                                                                                                                                                                                                                                                     |
|      24401 | ````` ▁подацима `````      |   0.220262  | <span style='border: 1px solid rgb(169, 68, 66);'>3e-06</span>   |                                                                                                                                                                                                                                                     |
|      23313 | ````` Obrázky `````        |   0.221171  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00064</span> |                                                                                                                                                                                                                                                     |
|      26334 | ````` ▁квітня `````        |   0.222318  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0023</span>  |                                                                                                                                                                                                                                                     |
|      26502 | ````` ▁вересня `````       |   0.222429  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00037</span> |                                                                                                                                                                                                                                                     |
|      27061 | ````` ▁Резултати `````     |   0.223467  | <span style='border: 1px solid rgb(169, 68, 66);'>3.2e-05</span> |                                                                                                                                                                                                                                                     |
|      25696 | ````` ▁роках `````         |   0.224173  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00018</span> |                                                                                                                                                                                                                                                     |
|      26675 | ````` ▁kallaste `````      |   0.227604  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0023</span>  |                                                                                                                                                                                                                                                     |
|      25528 | ````` ▁серпня `````        |   0.229016  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00011</span> |                                                                                                                                                                                                                                                     |
|      23015 | ````` ▁tématu `````        |   0.233542  | <span style='border: 1px solid rgb(169, 68, 66);'>9.6e-05</span> |                                                                                                                                                                                                                                                     |
|      28365 | ````` ▁розташ `````        |   0.236781  | <span style='border: 1px solid rgb(169, 68, 66);'>6.8e-05</span> |                                                                                                                                                                                                                                                     |
|      19196 | ````` ▁Према `````         |   0.23914   | <span style='border: 1px solid rgb(169, 68, 66);'>2.2e-06</span> |                                                                                                                                                                                                                                                     |
|      26662 | ````` ▁varmaste `````      |   0.24112   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00043</span> |                                                                                                                                                                                                                                                     |
|      20568 | ````` ▁сайті `````         |   0.247995  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00033</span> |                                                                                                                                                                                                                                                     |
|      28044 | ````` ▁округу `````        |   0.248123  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0093</span>  |                                                                                                                                                                                                                                                     |
|      25145 | ````` ▁kwiet `````         |   0.250032  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0032</span>  | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁kwietnia `````</span>                                                                                                                                                                      |
|      21284 | ````` ▁березня `````       |   0.251841  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0011</span>  |                                                                                                                                                                                                                                                     |
|      16194 | ````` ▁Биография `````     |   0.254009  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00019</span> |                                                                                                                                                                                                                                                     |
|      29451 | ````` ▁piłkar `````        |   0.255623  | <span style='border: 1px solid rgb(251, 189, 8);'>0.087</span>   |                                                                                                                                                                                                                                                     |
|      23217 | ````` ▁zvuky `````         |   0.255865  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-05</span> |                                                                                                                                                                                                                                                     |
</details>


## Byte tokens
110 entries below threshold of 0.234

|   token_id | token              |   indicator |   ord | hex   | byte_type   | reencoded             |
|------------|--------------------|-------------|-------|-------|-------------|-----------------------|
|         67 | ````` <0x40> ````` |  0.00192622 |    64 | 0x40  | ascii       | 29992: ````` @ `````  |
|         75 | ````` <0x48> ````` |  0.00193883 |    72 | 0x48  | ascii       | 29950: ````` H `````  |
|        127 | ````` <0x7C> ````` |  0.00194765 |   124 | 0x7C  | ascii       | 29989: ````` \| ````` |
|         95 | ````` <0x5C> ````` |  0.00194926 |    92 | 0x5C  | ascii       | 29905: ````` \ `````  |
|        109 | ````` <0x6A> ````` |  0.00195508 |   106 | 0x6A  | ascii       | 29926: ````` j `````  |
|         66 | ````` <0x3F> ````` |  0.00195511 |    63 | 0x3F  | ascii       | 29973: ````` ? `````  |
|         43 | ````` <0x28> ````` |  0.0019565  |    40 | 0x28  | ascii       | 29898: ````` ( `````  |
|         65 | ````` <0x3E> ````` |  0.00196026 |    62 | 0x3E  | ascii       | 29958: ````` > `````  |
|        123 | ````` <0x78> ````` |  0.00196048 |   120 | 0x78  | ascii       | 29916: ````` x `````  |
|        112 | ````` <0x6D> ````` |  0.00196374 |   109 | 0x6D  | ascii       | 29885: ````` m `````  |
|         96 | ````` <0x5D> ````` |  0.00196398 |    93 | 0x5D  | ascii       | 29962: ````` ] `````  |
|         41 | ````` <0x26> ````` |  0.00196404 |    38 | 0x26  | ascii       | 29987: ````` & `````  |
|         63 | ````` <0x3C> ````` |  0.00196526 |    60 | 0x3C  | ascii       | 29966: ````` < `````  |
|        129 | ````` <0x7E> ````` |  0.00196626 |   126 | 0x7E  | ascii       | 30022: ````` ~ `````  |
|        118 | ````` <0x73> ````` |  0.00196629 |   115 | 0x73  | ascii       | 29879: ````` s `````  |
|        255 | ````` <0xFC> ````` |  0.00196815 |   252 | 0xFC  | unused_utf8 |                       |
|        103 | ````` <0x64> ````` |  0.00196995 |   100 | 0x64  | ascii       | 29881: ````` d `````  |
|         53 | ````` <0x32> ````` |  0.00197103 |    50 | 0x32  | ascii       | 29906: ````` 2 `````  |
|         35 | ````` <0x20> ````` |  0.00197223 |    32 | 0x20  | ascii       | 29871: ````` ▁ `````  |
|         86 | ````` <0x53> ````` |  0.00197231 |    83 | 0x53  | ascii       | 29903: ````` S `````  |
<details><summary>90 additional entries below threshold</summary>

|   token_id | token              |   indicator |   ord | hex   | byte_type   | reencoded             |
|------------|--------------------|-------------|-------|-------|-------------|-----------------------|
|         98 | ````` <0x5F> ````` |  0.00197643 |    95 | 0x5F  | ascii       | 29918: ````` _ `````  |
|         16 | ````` <0x0D> ````` |  0.00197673 |    13 | 0x0D  | ascii       | 30004: ````` \r ````` |
|         71 | ````` <0x44> ````` |  0.00197709 |    68 | 0x44  | ascii       | 29928: ````` D `````  |
|         51 | ````` <0x30> ````` |  0.00197873 |    48 | 0x30  | ascii       | 29900: ````` 0 `````  |
|        104 | ````` <0x65> ````` |  0.00197959 |   101 | 0x65  | ascii       | 29872: ````` e `````  |
|        102 | ````` <0x63> ````` |  0.0019796  |    99 | 0x63  | ascii       | 29883: ````` c `````  |
|         55 | ````` <0x34> ````` |  0.0019797  |    52 | 0x34  | ascii       | 29946: ````` 4 `````  |
|        106 | ````` <0x67> ````` |  0.00198126 |   103 | 0x67  | ascii       | 29887: ````` g `````  |
|         74 | ````` <0x47> ````` |  0.00198159 |    71 | 0x47  | ascii       | 29954: ````` G `````  |
|        122 | ````` <0x77> ````` |  0.00198283 |   119 | 0x77  | ascii       | 29893: ````` w `````  |
|         88 | ````` <0x55> ````` |  0.00198376 |    85 | 0x55  | ascii       | 29965: ````` U `````  |
|         42 | ````` <0x27> ````` |  0.0019839  |    39 | 0x27  | ascii       | 29915: ````` ' `````  |
|        111 | ````` <0x6C> ````` |  0.00198434 |   108 | 0x6C  | ascii       | 29880: ````` l `````  |
|         37 | ````` <0x22> ````` |  0.00198492 |    34 | 0x22  | ascii       | 29908: ````` " `````  |
|        249 | ````` <0xF6> ````` |  0.00198568 |   246 | 0xF6  | unused_utf8 |                       |
|        116 | ````` <0x71> ````` |  0.0019861  |   113 | 0x71  | ascii       | 29939: ````` q `````  |
|         82 | ````` <0x4F> ````` |  0.00198651 |    79 | 0x4F  | ascii       | 29949: ````` O `````  |
|        115 | ````` <0x70> ````` |  0.00198724 |   112 | 0x70  | ascii       | 29886: ````` p `````  |
|         90 | ````` <0x57> ````` |  0.00198818 |    87 | 0x57  | ascii       | 29956: ````` W `````  |
|         49 | ````` <0x2E> ````` |  0.00199185 |    46 | 0x2E  | ascii       | 29889: ````` . `````  |
|         87 | ````` <0x54> ````` |  0.00199193 |    84 | 0x54  | ascii       | 29911: ````` T `````  |
|         40 | ````` <0x25> ````` |  0.00199279 |    37 | 0x25  | ascii       | 29995: ````` % `````  |
|        250 | ````` <0xF7> ````` |  0.00199385 |   247 | 0xF7  | unused_utf8 |                       |
|         61 | ````` <0x3A> ````` |  0.00199542 |    58 | 0x3A  | ascii       | 29901: ````` : `````  |
|         93 | ````` <0x5A> ````` |  0.00199569 |    90 | 0x5A  | ascii       | 29999: ````` Z `````  |
|        195 | ````` <0xC0> ````` |  0.00199586 |   192 | 0xC0  | unused_utf8 |                       |
|         91 | ````` <0x58> ````` |  0.00199589 |    88 | 0x58  | ascii       | 29990: ````` X `````  |
|        128 | ````` <0x7D> ````` |  0.00199677 |   125 | 0x7D  | ascii       | 29913: ````` } `````  |
|         78 | ````` <0x4B> ````` |  0.00199791 |    75 | 0x4B  | ascii       | 29968: ````` K `````  |
|        101 | ````` <0x62> ````` |  0.00200054 |    98 | 0x62  | ascii       | 29890: ````` b `````  |
|        254 | ````` <0xFB> ````` |  0.00200079 |   251 | 0xFB  | unused_utf8 |                       |
|         52 | ````` <0x31> ````` |  0.00200166 |    49 | 0x31  | ascii       | 29896: ````` 1 `````  |
|         50 | ````` <0x2F> ````` |  0.00200203 |    47 | 0x2F  | ascii       | 29914: ````` / `````  |
|         39 | ````` <0x24> ````` |  0.00200253 |    36 | 0x24  | ascii       | 29938: ````` $ `````  |
|        252 | ````` <0xF9> ````` |  0.00200263 |   249 | 0xF9  | unused_utf8 |                       |
|        117 | ````` <0x72> ````` |  0.00200282 |   114 | 0x72  | ascii       | 29878: ````` r `````  |
|         72 | ````` <0x45> ````` |  0.00200421 |    69 | 0x45  | ascii       | 29923: ````` E `````  |
|        124 | ````` <0x79> ````` |  0.00200427 |   121 | 0x79  | ascii       | 29891: ````` y `````  |
|         38 | ````` <0x23> ````` |  0.00200528 |    35 | 0x23  | ascii       | 29937: ````` # `````  |
|        258 | ````` <0xFF> ````` |  0.0020059  |   255 | 0xFF  | unused_utf8 |                       |
|        107 | ````` <0x68> ````` |  0.00200598 |   104 | 0x68  | ascii       | 29882: ````` h `````  |
|         46 | ````` <0x2B> ````` |  0.00200688 |    43 | 0x2B  | ascii       | 29974: ````` + `````  |
|         47 | ````` <0x2C> ````` |  0.00200691 |    44 | 0x2C  | ascii       | 29892: ````` , `````  |
|         73 | ````` <0x46> ````` |  0.00200711 |    70 | 0x46  | ascii       | 29943: ````` F `````  |
|         69 | ````` <0x42> ````` |  0.00200755 |    66 | 0x42  | ascii       | 29933: ````` B `````  |
|         80 | ````` <0x4D> ````` |  0.00200853 |    77 | 0x4D  | ascii       | 29924: ````` M `````  |
|         85 | ````` <0x52> ````` |  0.00200891 |    82 | 0x52  | ascii       | 29934: ````` R `````  |
|         62 | ````` <0x3B> ````` |  0.0020096  |    59 | 0x3B  | ascii       | 29936: ````` ; `````  |
|         77 | ````` <0x4A> ````` |  0.00200961 |    74 | 0x4A  | ascii       | 29967: ````` J `````  |
|        251 | ````` <0xF8> ````` |  0.00200994 |   248 | 0xF8  | unused_utf8 |                       |
|         56 | ````` <0x35> ````` |  0.00201105 |    53 | 0x35  | ascii       | 29945: ````` 5 `````  |
|         58 | ````` <0x37> ````` |  0.00201147 |    55 | 0x37  | ascii       | 29955: ````` 7 `````  |
|         92 | ````` <0x59> ````` |  0.00201192 |    89 | 0x59  | ascii       | 29979: ````` Y `````  |
|         99 | ````` <0x60> ````` |  0.00201198 |    96 | 0x60  | ascii       | 29952: ````` ` `````  |
|         89 | ````` <0x56> ````` |  0.00201286 |    86 | 0x56  | ascii       | 29963: ````` V `````  |
|         59 | ````` <0x38> ````` |  0.00201333 |    56 | 0x38  | ascii       | 29947: ````` 8 `````  |
|        196 | ````` <0xC1> ````` |  0.00201401 |   193 | 0xC1  | unused_utf8 |                       |
|         68 | ````` <0x41> ````` |  0.0020148  |    65 | 0x41  | ascii       | 29909: ````` A `````  |
|         48 | ````` <0x2D> ````` |  0.00201658 |    45 | 0x2D  | ascii       | 29899: ````` - `````  |
|        256 | ````` <0xFD> ````` |  0.00201672 |   253 | 0xFD  | unused_utf8 |                       |
|         70 | ````` <0x43> ````` |  0.00201754 |    67 | 0x43  | ascii       | 29907: ````` C `````  |
|         54 | ````` <0x33> ````` |  0.00201761 |    51 | 0x33  | ascii       | 29941: ````` 3 `````  |
|         97 | ````` <0x5E> ````` |  0.00201832 |    94 | 0x5E  | ascii       | 29985: ````` ^ `````  |
|         60 | ````` <0x39> ````` |  0.00201925 |    57 | 0x39  | ascii       | 29929: ````` 9 `````  |
|         36 | ````` <0x21> ````` |  0.00201926 |    33 | 0x21  | ascii       | 29991: ````` ! `````  |
|         64 | ````` <0x3D> ````` |  0.00202062 |    61 | 0x3D  | ascii       | 29922: ````` = `````  |
|        253 | ````` <0xFA> ````` |  0.00202105 |   250 | 0xFA  | unused_utf8 |                       |
|        198 | ````` <0xC3> ````` |  0.00202128 |   195 | 0xC3  | utf8        |                       |
|        121 | ````` <0x76> ````` |  0.00202135 |   118 | 0x76  | ascii       | 29894: ````` v `````  |
|        120 | ````` <0x75> ````` |  0.00202297 |   117 | 0x75  | ascii       | 29884: ````` u `````  |
|         83 | ````` <0x50> ````` |  0.00202334 |    80 | 0x50  | ascii       | 29925: ````` P `````  |
|         79 | ````` <0x4C> ````` |  0.00202405 |    76 | 0x4C  | ascii       | 29931: ````` L `````  |
|        257 | ````` <0xFE> ````` |  0.0020246  |   254 | 0xFE  | unused_utf8 |                       |
|        100 | ````` <0x61> ````` |  0.00202484 |    97 | 0x61  | ascii       | 29874: ````` a `````  |
|        108 | ````` <0x69> ````` |  0.00202518 |   105 | 0x69  | ascii       | 29875: ````` i `````  |
|        248 | ````` <0xF5> ````` |  0.00202536 |   245 | 0xF5  | unused_utf8 |                       |
|        110 | ````` <0x6B> ````` |  0.00202738 |   107 | 0x6B  | ascii       | 29895: ````` k `````  |
|        126 | ````` <0x7B> ````` |  0.00202792 |   123 | 0x7B  | ascii       | 29912: ````` { `````  |
|        119 | ````` <0x74> ````` |  0.00202865 |   116 | 0x74  | ascii       | 29873: ````` t `````  |
|        113 | ````` <0x6E> ````` |  0.0020289  |   110 | 0x6E  | ascii       | 29876: ````` n `````  |
|         57 | ````` <0x36> ````` |  0.00202909 |    54 | 0x36  | ascii       | 29953: ````` 6 `````  |
|        125 | ````` <0x7A> ````` |  0.00202911 |   122 | 0x7A  | ascii       | 29920: ````` z `````  |
|         44 | ````` <0x29> ````` |  0.00203289 |    41 | 0x29  | ascii       | 29897: ````` ) `````  |
|        105 | ````` <0x66> ````` |  0.00203565 |   102 | 0x66  | ascii       | 29888: ````` f `````  |
|         76 | ````` <0x49> ````` |  0.00203871 |    73 | 0x49  | ascii       | 29902: ````` I `````  |
|        114 | ````` <0x6F> ````` |  0.00204017 |   111 | 0x6F  | ascii       | 29877: ````` o `````  |
|         81 | ````` <0x4E> ````` |  0.00204544 |    78 | 0x4E  | ascii       | 29940: ````` N `````  |
|         45 | ````` <0x2A> ````` |  0.00204599 |    42 | 0x2A  | ascii       | 29930: ````` * `````  |
|         94 | ````` <0x5B> ````` |  0.0020465  |    91 | 0x5B  | ascii       | 29961: ````` [ `````  |
|         84 | ````` <0x51> ````` |  0.00205725 |    81 | 0x51  | ascii       | 29984: ````` Q `````  |
</details>


## Special tokens
3 entries below threshold of 0.234

|   token_id | token                          |   indicator | reencoded                                                   |
|------------|--------------------------------|-------------|-------------------------------------------------------------|
|      32002 | ````` <\|placeholder1\|> ````` |  0.00197536 | 29871: ````` ▁ `````, 32002: ````` <\|placeholder1\|> ````` |
|      32004 | ````` <\|placeholder3\|> ````` |  0.00198296 | 29871: ````` ▁ `````, 32004: ````` <\|placeholder3\|> ````` |
|      32003 | ````` <\|placeholder2\|> ````` |  0.00201634 | 29871: ````` ▁ `````, 32003: ````` <\|placeholder2\|> ````` |

