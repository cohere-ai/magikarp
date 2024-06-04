# Report for `microsoft/Phi-3-mini-128k-instruct`

## Model info

* Tied embeddings: no
* LM head uses bias: no
* Indicator for under-trained tokens: E_{in} L2 Norm
  * Overall distribution 1.558 +/- 0.305
  * Token used for verification prompt building: `springframework`
  * Verification threshold: 0.588
  * Threshold for showing candidate under-trained tokens: 0.209
  * Median verified threshold (for bytes, unreachable and special tokens): 0.182
* Embeddings shape: (32064, 3072)
* Vocabulary size: 32011
  * Number of single byte tokens: 351, of which 110 below indicator threshold
  * Number of special tokens: 14, of which 6 below indicator threshold
  * Number of tested under-trained tokens: 620, 620 non-special, 172 below p = 0.01 threshold, 102 below soft indicator threshold

## Under-trained token indicators plot
![Indicators scatter plots](../indicators_pairplot_byid/microsoft_Phi_3_mini_128k_instruct.png)

## Verification plot
![Verification plot](../verifications_scatterplot/microsoft_Phi_3_mini_128k_instruct.png)

## Under-trained token verification results
102 entries below threshold of 0.209

|   token_id | token                       |   indicator | max_prob                                                         | in_other_tokens                                                                 |
|------------|-----------------------------|-------------|------------------------------------------------------------------|---------------------------------------------------------------------------------|
|      16110 | ````` ▁Спољашње `````       |  0.00201051 | <span style='border: 1px solid rgb(169, 68, 66);'>6.4e-06</span> |                                                                                 |
|      28574 | ````` ▁Mediabestanden ````` |  0.00201276 | <span style='border: 1px solid rgb(169, 68, 66);'>6.4e-06</span> |                                                                                 |
|      20528 | ````` ▁autorytatywna `````  |  0.00202321 | <span style='border: 1px solid rgb(169, 68, 66);'>6.4e-06</span> |                                                                                 |
|      27918 | ````` ▁Хронологија `````    |  0.002026   | <span style='border: 1px solid rgb(169, 68, 66);'>6.3e-06</span> |                                                                                 |
|      20609 | ````` ▁Portály `````        |  0.00204529 | <span style='border: 1px solid rgb(169, 68, 66);'>6.4e-06</span> |                                                                                 |
|      11804 | ````` Архівовано `````      |  0.00206332 | <span style='border: 1px solid rgb(169, 68, 66);'>6.3e-06</span> |                                                                                 |
|      21836 | ````` ▁надморској `````     |  0.00566266 | <span style='border: 1px solid rgb(169, 68, 66);'>3.9e-06</span> |                                                                                 |
|      23996 | ````` ▁живело `````         |  0.00888786 | <span style='border: 1px solid rgb(169, 68, 66);'>5.7e-06</span> |                                                                                 |
|      24294 | ````` Webachiv `````        |  0.00948074 | <span style='border: 1px solid rgb(169, 68, 66);'>5.3e-06</span> |                                                                                 |
|      28653 | ````` ▁regnigaste `````     |  0.0114744  | <span style='border: 1px solid rgb(169, 68, 66);'>3.9e-06</span> |                                                                                 |
|      18051 | ````` ▁савезној `````       |  0.014531   | <span style='border: 1px solid rgb(169, 68, 66);'>2.8e-06</span> |                                                                                 |
|      28649 | ````` ▁årsnederbörd `````   |  0.0146256  | <span style='border: 1px solid rgb(169, 68, 66);'>8.3e-06</span> |                                                                                 |
|      27914 | ````` ▁archiválva `````     |  0.0150005  | <span style='border: 1px solid rgb(169, 68, 66);'>8.1e-06</span> |                                                                                 |
|      27900 | ````` ▁eredetiből `````     |  0.0232916  | <span style='border: 1px solid rgb(169, 68, 66);'>5.6e-06</span> |                                                                                 |
|      26821 | ````` ▁Enllaços `````       |  0.0239937  | <span style='border: 1px solid rgb(169, 68, 66);'>9.5e-06</span> |                                                                                 |
|      11766 | ````` хівовано `````        |  0.0250883  | <span style='border: 1px solid rgb(169, 68, 66);'>3.8e-06</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` Архівовано `````</span> |
|      21673 | ````` ▁висини `````         |  0.0259494  | <span style='border: 1px solid rgb(169, 68, 66);'>7.2e-06</span> |                                                                                 |
|      23654 | ````` ▁dátummal `````       |  0.0295117  | <span style='border: 1px solid rgb(169, 68, 66);'>5.1e-06</span> |                                                                                 |
|      28416 | ````` ▁Мексичка `````       |  0.0512673  | <span style='border: 1px solid rgb(169, 68, 66);'>5.5e-06</span> |                                                                                 |
|      26734 | ````` ▁Årsmed `````         |  0.0571039  | <span style='border: 1px solid rgb(169, 68, 66);'>3.2e-06</span> |                                                                                 |
<details><summary>82 additional entries below threshold</summary>

|   token_id | token                      |   indicator | max_prob                                                         | in_other_tokens                                                                                                                                                                                                                                     |
|------------|----------------------------|-------------|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      28623 | ````` ▁Genomsnitt `````    |   0.0620495 | <span style='border: 1px solid rgb(169, 68, 66);'>1.5e-06</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁Genomsnittlig `````</span>                                                                                                                                                                 |
|      28650 | ````` ▁Genomsnittlig ````` |   0.0628445 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-06</span> |                                                                                                                                                                                                                                                     |
|      28354 | ````` ▁Расподела `````     |   0.0647205 | <span style='border: 1px solid rgb(169, 68, 66);'>1.8e-06</span> |                                                                                                                                                                                                                                                     |
|      16056 | ````` љашње `````          |   0.0661741 | <span style='border: 1px solid rgb(169, 68, 66);'>4.8e-06</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁Спољашње `````</span>                                                                                                                                                                      |
|      17981 | ````` ▁Externí `````       |   0.0701503 | <span style='border: 1px solid rgb(169, 68, 66);'>1.4e-06</span> |                                                                                                                                                                                                                                                     |
|       7651 | ````` ▁släktet `````       |   0.0792316 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-05</span> |                                                                                                                                                                                                                                                     |
|      22011 | ````` ▁насељу `````        |   0.0807262 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-05</span> |                                                                                                                                                                                                                                                     |
|      28642 | ````` ▁regnig `````        |   0.0808125 | <span style='border: 1px solid rgb(169, 68, 66);'>2.1e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁regnigaste `````</span>                                                                                                                                                                    |
|       7784 | ````` ▁underarter `````    |   0.0854089 | <span style='border: 1px solid rgb(169, 68, 66);'>2.4e-05</span> |                                                                                                                                                                                                                                                     |
|      28263 | ````` ▁Odkazy `````        |   0.0865755 | <span style='border: 1px solid rgb(169, 68, 66);'>1.4e-05</span> |                                                                                                                                                                                                                                                     |
|      24029 | ````` ▁Jegyzetek `````     |   0.0929318 | <span style='border: 1px solid rgb(169, 68, 66);'>4.9e-06</span> |                                                                                                                                                                                                                                                     |
|      20486 | ````` tatywna `````        |   0.0953065 | <span style='border: 1px solid rgb(169, 68, 66);'>2.7e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁autorytatywna `````</span>                                                                                                                                                                 |
|      28090 | ````` ▁Савезне `````       |   0.096245  | <span style='border: 1px solid rgb(169, 68, 66);'>5.7e-06</span> |                                                                                                                                                                                                                                                     |
|      20422 | ````` ніципалі `````       |   0.0966726 | <span style='border: 1px solid rgb(169, 68, 66);'>3.2e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁муніципалі `````</span>                                                                                                                                                                    |
|      23117 | ````` brázky `````         |   0.0973689 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` Obrázky `````</span>                                                                                                                                                                        |
|      22835 | ````` ▁муніципалі `````    |   0.0983095 | <span style='border: 1px solid rgb(169, 68, 66);'>4e-05</span>   |                                                                                                                                                                                                                                                     |
|      24401 | ````` ▁подацима `````      |   0.0983596 | <span style='border: 1px solid rgb(169, 68, 66);'>3e-06</span>   |                                                                                                                                                                                                                                                     |
|      28647 | ````` ▁torraste `````      |   0.104481  | <span style='border: 1px solid rgb(169, 68, 66);'>1.6e-06</span> |                                                                                                                                                                                                                                                     |
|      23406 | ````` ▁општини `````       |   0.105034  | <span style='border: 1px solid rgb(169, 68, 66);'>1e-05</span>   |                                                                                                                                                                                                                                                     |
|      19837 | ````` ▁Населення `````     |   0.10536   | <span style='border: 1px solid rgb(169, 68, 66);'>6.7e-06</span> |                                                                                                                                                                                                                                                     |
|      24631 | ````` ▁Források `````      |   0.106376  | <span style='border: 1px solid rgb(169, 68, 66);'>4.9e-06</span> |                                                                                                                                                                                                                                                     |
|      14562 | ````` ▁Посилання `````     |   0.107502  | <span style='border: 1px solid rgb(169, 68, 66);'>5.1e-06</span> |                                                                                                                                                                                                                                                     |
|      27645 | ````` ▁Попис `````         |   0.107614  | <span style='border: 1px solid rgb(169, 68, 66);'>2.2e-05</span> |                                                                                                                                                                                                                                                     |
|      20739 | ````` ▁надмор `````        |   0.107973  | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁надморској `````</span>                                                                                                                                                                    |
|      17916 | ````` abestanden `````     |   0.109997  | <span style='border: 1px solid rgb(169, 68, 66);'>2.1e-06</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁Mediabestanden `````</span>                                                                                                                                                                |
|       7718 | ````` ▁beskrevs `````      |   0.110645  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-05</span> |                                                                                                                                                                                                                                                     |
|       9462 | ````` Hozzáférés `````     |   0.111895  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00023</span> |                                                                                                                                                                                                                                                     |
|      20180 | ````` ▁Мексику `````       |   0.114557  | <span style='border: 1px solid rgb(169, 68, 66);'>7.8e-05</span> |                                                                                                                                                                                                                                                     |
|      11229 | ````` ▁становника `````    |   0.1168    | <span style='border: 1px solid rgb(169, 68, 66);'>3.3e-05</span> |                                                                                                                                                                                                                                                     |
|      23726 | ````` ▁насеља `````        |   0.123727  | <span style='border: 1px solid rgb(169, 68, 66);'>2.9e-05</span> |                                                                                                                                                                                                                                                     |
|      26011 | ````` ▁Архивная `````      |   0.126411  | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-06</span> |                                                                                                                                                                                                                                                     |
|      23715 | ````` ▁Källor `````        |   0.130737  | <span style='border: 1px solid rgb(169, 68, 66);'>6.8e-05</span> |                                                                                                                                                                                                                                                     |
|      18044 | ````` ▁Становништво `````  |   0.131513  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-05</span> |                                                                                                                                                                                                                                                     |
|      26847 | ````` .:\u200a `````       |   0.132821  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-05</span> |                                                                                                                                                                                                                                                     |
|      24971 | ````` ▁Джерела `````       |   0.135934  | <span style='border: 1px solid rgb(169, 68, 66);'>9.9e-06</span> |                                                                                                                                                                                                                                                     |
|      20645 | ````` ▁Przypisy `````      |   0.138476  | <span style='border: 1px solid rgb(169, 68, 66);'>6.6e-06</span> |                                                                                                                                                                                                                                                     |
|      25283 | ````` ▁липня `````         |   0.139258  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00022</span> |                                                                                                                                                                                                                                                     |
|      23875 | ````` ▁Насеље `````        |   0.140676  | <span style='border: 1px solid rgb(251, 189, 8);'>0.036</span>   |                                                                                                                                                                                                                                                     |
|      26964 | ````` ▁Хронологи `````     |   0.141754  | <span style='border: 1px solid rgb(169, 68, 66);'>2.3e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁Хронологија `````</span>                                                                                                                                                                   |
|      10688 | ````` ▁gepublic `````      |   0.143958  | <span style='border: 1px solid rgb(169, 68, 66);'>6.4e-05</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁gepubliceerd `````</span>                                                                                                                                                                  |
|      25840 | ````` ▁државе `````        |   0.145544  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00026</span> |                                                                                                                                                                                                                                                     |
|      28906 | ````` ▁листопада `````     |   0.145551  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00025</span> |                                                                                                                                                                                                                                                     |
|      28633 | ````` nederbörd `````      |   0.149653  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00011</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁årsnederbörd `````</span>                                                                                                                                                                  |
|      23313 | ````` Obrázky `````        |   0.150916  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00064</span> |                                                                                                                                                                                                                                                     |
|      19196 | ````` ▁Према `````         |   0.151589  | <span style='border: 1px solid rgb(169, 68, 66);'>2.2e-06</span> |                                                                                                                                                                                                                                                     |
|      27610 | ````` ▁gminie `````        |   0.152853  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00096</span> |                                                                                                                                                                                                                                                     |
|      18140 | ````` rinningsområ `````   |   0.154067  | <span style='border: 1px solid rgb(169, 68, 66);'>4.7e-05</span> |                                                                                                                                                                                                                                                     |
|      12731 | ````` ederbörd `````       |   0.15512   | <span style='border: 1px solid rgb(255, 145, 0);'>0.0032</span>  | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁nederbörd `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` nederbörd `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁årsnederbörd `````</span> |
|      16916 | ````` ▁invån `````         |   0.156367  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00015</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁invånare `````</span>                                                                                                                                                                      |
|      23015 | ````` ▁tématu `````        |   0.157348  | <span style='border: 1px solid rgb(169, 68, 66);'>9.6e-05</span> |                                                                                                                                                                                                                                                     |
|      26502 | ````` ▁вересня `````       |   0.158219  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00037</span> |                                                                                                                                                                                                                                                     |
|      25460 | ````` ▁жовтня `````        |   0.159329  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00016</span> |                                                                                                                                                                                                                                                     |
|      14414 | ````` ▁Archivlink `````    |   0.159843  | <span style='border: 1px solid rgb(169, 68, 66);'>4e-05</span>   |                                                                                                                                                                                                                                                     |
|      27061 | ````` ▁Резултати `````     |   0.160475  | <span style='border: 1px solid rgb(169, 68, 66);'>3.2e-05</span> |                                                                                                                                                                                                                                                     |
|      24852 | ````` ▁грудня `````        |   0.160779  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0013</span>  |                                                                                                                                                                                                                                                     |
|      26334 | ````` ▁квітня `````        |   0.163826  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0023</span>  |                                                                                                                                                                                                                                                     |
|      16068 | ````` eltemperaturen ````` |   0.163958  | <span style='border: 1px solid rgb(169, 68, 66);'>3.4e-06</span> |                                                                                                                                                                                                                                                     |
|      26527 | ````` ▁червня `````        |   0.165224  | <span style='border: 1px solid rgb(169, 68, 66);'>9.5e-05</span> |                                                                                                                                                                                                                                                     |
|      25696 | ````` ▁роках `````         |   0.165628  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00018</span> |                                                                                                                                                                                                                                                     |
|      18676 | ````` ніципа `````         |   0.16571   | <span style='border: 1px solid rgb(255, 145, 0);'>0.0011</span>  | <span style='border: 1px solid rgb(169, 68, 66);'>````` ніципалі `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁муніципалі `````</span>                                                                                     |
|      28044 | ````` ▁округу `````        |   0.168744  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0093</span>  |                                                                                                                                                                                                                                                     |
|      26675 | ````` ▁kallaste `````      |   0.173566  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0023</span>  |                                                                                                                                                                                                                                                     |
|      20568 | ````` ▁сайті `````         |   0.17471   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00033</span> |                                                                                                                                                                                                                                                     |
|      28498 | ````` ▁лютого `````        |   0.174927  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0036</span>  |                                                                                                                                                                                                                                                     |
|      25528 | ````` ▁серпня `````        |   0.17548   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00011</span> |                                                                                                                                                                                                                                                     |
|      22768 | ````` ▁жовт `````          |   0.176428  | <span style='border: 1px solid rgb(169, 68, 66);'>3.3e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁жовтня `````</span>                                                                                                                                                                        |
|      24708 | ````` ▁січня `````         |   0.180815  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00071</span> |                                                                                                                                                                                                                                                     |
|      28365 | ````` ▁розташ `````        |   0.18377   | <span style='border: 1px solid rgb(169, 68, 66);'>6.8e-05</span> |                                                                                                                                                                                                                                                     |
|      31899 | ````` ⥤ `````              |   0.184028  | <span style='border: 1px solid rgb(40, 167, 69);'>0.8</span>     |                                                                                                                                                                                                                                                     |
|      26782 | ````` ▁пописа `````        |   0.184427  | <span style='border: 1px solid rgb(169, 68, 66);'>2.2e-05</span> |                                                                                                                                                                                                                                                     |
|      24309 | ````` ▁чемпі `````         |   0.189381  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0023</span>  |                                                                                                                                                                                                                                                     |
|      26335 | ````` llaços `````         |   0.189978  | <span style='border: 1px solid rgb(169, 68, 66);'>7.6e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁Enllaços `````</span>                                                                                                                                                                      |
|      16194 | ````` ▁Биография `````     |   0.19031   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00019</span> |                                                                                                                                                                                                                                                     |
|      18328 | ````` ▁trakten `````       |   0.190743  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0049</span>  |                                                                                                                                                                                                                                                     |
|      24576 | ````` ▁estaven `````       |   0.191031  | <span style='border: 1px solid rgb(169, 68, 66);'>1.4e-05</span> |                                                                                                                                                                                                                                                     |
|      28791 | ````` ▁віці `````          |   0.191254  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0095</span>  |                                                                                                                                                                                                                                                     |
|      24097 | ````` ▁huvudstaden `````   |   0.199273  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00035</span> |                                                                                                                                                                                                                                                     |
|      21284 | ````` ▁березня `````       |   0.20056   | <span style='border: 1px solid rgb(255, 145, 0);'>0.0011</span>  |                                                                                                                                                                                                                                                     |
|       9147 | ````` ozzáférés `````      |   0.203452  | <span style='border: 1px solid rgb(251, 189, 8);'>0.015</span>   | <span style='border: 1px solid rgb(169, 68, 66);'>````` Hozzáférés `````</span>                                                                                                                                                                     |
|      17871 | ````` ▁odkazy `````        |   0.205296  | <span style='border: 1px solid rgb(40, 167, 69);'>0.22</span>    |                                                                                                                                                                                                                                                     |
|      26662 | ````` ▁varmaste `````      |   0.205717  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00043</span> |                                                                                                                                                                                                                                                     |
|      15887 | ````` ▁још `````           |   0.207694  | <span style='border: 1px solid rgb(169, 68, 66);'>0.0004</span>  |                                                                                                                                                                                                                                                     |
</details>


## Byte tokens
110 entries below threshold of 0.182

|   token_id | token              |   indicator |   ord | hex   | byte_type   | reencoded             |
|------------|--------------------|-------------|-------|-------|-------------|-----------------------|
|         67 | ````` <0x40> ````` |  0.00194363 |    64 | 0x40  | ascii       | 29992: ````` @ `````  |
|         75 | ````` <0x48> ````` |  0.00195629 |    72 | 0x48  | ascii       | 29950: ````` H `````  |
|        127 | ````` <0x7C> ````` |  0.0019651  |   124 | 0x7C  | ascii       | 29989: ````` \| ````` |
|         95 | ````` <0x5C> ````` |  0.00196687 |    92 | 0x5C  | ascii       | 29905: ````` \ `````  |
|        109 | ````` <0x6A> ````` |  0.00197249 |   106 | 0x6A  | ascii       | 29926: ````` j `````  |
|         66 | ````` <0x3F> ````` |  0.00197267 |    63 | 0x3F  | ascii       | 29973: ````` ? `````  |
|         43 | ````` <0x28> ````` |  0.00197391 |    40 | 0x28  | ascii       | 29898: ````` ( `````  |
|         65 | ````` <0x3E> ````` |  0.00197781 |    62 | 0x3E  | ascii       | 29958: ````` > `````  |
|        123 | ````` <0x78> ````` |  0.00197809 |   120 | 0x78  | ascii       | 29916: ````` x `````  |
|         41 | ````` <0x26> ````` |  0.0019814  |    38 | 0x26  | ascii       | 29987: ````` & `````  |
|        112 | ````` <0x6D> ````` |  0.0019816  |   109 | 0x6D  | ascii       | 29885: ````` m `````  |
|         96 | ````` <0x5D> ````` |  0.00198174 |    93 | 0x5D  | ascii       | 29962: ````` ] `````  |
|         63 | ````` <0x3C> ````` |  0.0019828  |    60 | 0x3C  | ascii       | 29966: ````` < `````  |
|        129 | ````` <0x7E> ````` |  0.00198395 |   126 | 0x7E  | ascii       | 30022: ````` ~ `````  |
|        118 | ````` <0x73> ````` |  0.00198417 |   115 | 0x73  | ascii       | 29879: ````` s `````  |
|        255 | ````` <0xFC> ````` |  0.00198543 |   252 | 0xFC  | unused_utf8 |                       |
|        103 | ````` <0x64> ````` |  0.00198736 |   100 | 0x64  | ascii       | 29881: ````` d `````  |
|         53 | ````` <0x32> ````` |  0.00198865 |    50 | 0x32  | ascii       | 29906: ````` 2 `````  |
|         35 | ````` <0x20> ````` |  0.00198964 |    32 | 0x20  | ascii       | 29871: ````` ▁ `````  |
|         86 | ````` <0x53> ````` |  0.00199001 |    83 | 0x53  | ascii       | 29903: ````` S `````  |
<details><summary>90 additional entries below threshold</summary>

|   token_id | token              |   indicator |   ord | hex   | byte_type   | reencoded             |
|------------|--------------------|-------------|-------|-------|-------------|-----------------------|
|         98 | ````` <0x5F> ````` |  0.00199416 |    95 | 0x5F  | ascii       | 29918: ````` _ `````  |
|         16 | ````` <0x0D> ````` |  0.00199429 |    13 | 0x0D  | ascii       | 30004: ````` \r ````` |
|         71 | ````` <0x44> ````` |  0.00199478 |    68 | 0x44  | ascii       | 29928: ````` D `````  |
|         51 | ````` <0x30> ````` |  0.00199635 |    48 | 0x30  | ascii       | 29900: ````` 0 `````  |
|        102 | ````` <0x63> ````` |  0.00199725 |    99 | 0x63  | ascii       | 29883: ````` c `````  |
|        104 | ````` <0x65> ````` |  0.00199735 |   101 | 0x65  | ascii       | 29872: ````` e `````  |
|         55 | ````` <0x34> ````` |  0.00199755 |    52 | 0x34  | ascii       | 29946: ````` 4 `````  |
|        106 | ````` <0x67> ````` |  0.00199884 |   103 | 0x67  | ascii       | 29887: ````` g `````  |
|         74 | ````` <0x47> ````` |  0.0019991  |    71 | 0x47  | ascii       | 29954: ````` G `````  |
|        122 | ````` <0x77> ````` |  0.00200095 |   119 | 0x77  | ascii       | 29893: ````` w `````  |
|         88 | ````` <0x55> ````` |  0.00200146 |    85 | 0x55  | ascii       | 29965: ````` U `````  |
|         42 | ````` <0x27> ````` |  0.00200162 |    39 | 0x27  | ascii       | 29915: ````` ' `````  |
|        111 | ````` <0x6C> ````` |  0.00200224 |   108 | 0x6C  | ascii       | 29880: ````` l `````  |
|         37 | ````` <0x22> ````` |  0.00200274 |    34 | 0x22  | ascii       | 29908: ````` " `````  |
|        249 | ````` <0xF6> ````` |  0.00200337 |   246 | 0xF6  | unused_utf8 |                       |
|        116 | ````` <0x71> ````` |  0.00200368 |   113 | 0x71  | ascii       | 29939: ````` q `````  |
|         82 | ````` <0x4F> ````` |  0.00200416 |    79 | 0x4F  | ascii       | 29949: ````` O `````  |
|        115 | ````` <0x70> ````` |  0.00200493 |   112 | 0x70  | ascii       | 29886: ````` p `````  |
|         90 | ````` <0x57> ````` |  0.0020058  |    87 | 0x57  | ascii       | 29956: ````` W `````  |
|         87 | ````` <0x54> ````` |  0.00200968 |    84 | 0x54  | ascii       | 29911: ````` T `````  |
|         49 | ````` <0x2E> ````` |  0.0020097  |    46 | 0x2E  | ascii       | 29889: ````` . `````  |
|         40 | ````` <0x25> ````` |  0.00201061 |    37 | 0x25  | ascii       | 29995: ````` % `````  |
|        250 | ````` <0xF7> ````` |  0.00201154 |   247 | 0xF7  | unused_utf8 |                       |
|         61 | ````` <0x3A> ````` |  0.00201311 |    58 | 0x3A  | ascii       | 29901: ````` : `````  |
|         93 | ````` <0x5A> ````` |  0.00201363 |    90 | 0x5A  | ascii       | 29999: ````` Z `````  |
|        195 | ````` <0xC0> ````` |  0.00201367 |   192 | 0xC0  | unused_utf8 |                       |
|         91 | ````` <0x58> ````` |  0.00201377 |    88 | 0x58  | ascii       | 29990: ````` X `````  |
|        128 | ````` <0x7D> ````` |  0.00201461 |   125 | 0x7D  | ascii       | 29913: ````` } `````  |
|         78 | ````` <0x4B> ````` |  0.00201553 |    75 | 0x4B  | ascii       | 29968: ````` K `````  |
|        101 | ````` <0x62> ````` |  0.00201845 |    98 | 0x62  | ascii       | 29890: ````` b `````  |
|        254 | ````` <0xFB> ````` |  0.00201851 |   251 | 0xFB  | unused_utf8 |                       |
|         52 | ````` <0x31> ````` |  0.00201926 |    49 | 0x31  | ascii       | 29896: ````` 1 `````  |
|         50 | ````` <0x2F> ````` |  0.00201974 |    47 | 0x2F  | ascii       | 29914: ````` / `````  |
|        117 | ````` <0x72> ````` |  0.00202046 |   114 | 0x72  | ascii       | 29878: ````` r `````  |
|         39 | ````` <0x24> ````` |  0.00202049 |    36 | 0x24  | ascii       | 29938: ````` $ `````  |
|        252 | ````` <0xF9> ````` |  0.00202058 |   249 | 0xF9  | unused_utf8 |                       |
|        124 | ````` <0x79> ````` |  0.0020219  |   121 | 0x79  | ascii       | 29891: ````` y `````  |
|         72 | ````` <0x45> ````` |  0.0020222  |    69 | 0x45  | ascii       | 29923: ````` E `````  |
|         38 | ````` <0x23> ````` |  0.00202324 |    35 | 0x23  | ascii       | 29937: ````` # `````  |
|        107 | ````` <0x68> ````` |  0.00202398 |   104 | 0x68  | ascii       | 29882: ````` h `````  |
|        258 | ````` <0xFF> ````` |  0.00202403 |   255 | 0xFF  | unused_utf8 |                       |
|         47 | ````` <0x2C> ````` |  0.00202474 |    44 | 0x2C  | ascii       | 29892: ````` , `````  |
|         46 | ````` <0x2B> ````` |  0.002025   |    43 | 0x2B  | ascii       | 29974: ````` + `````  |
|         73 | ````` <0x46> ````` |  0.00202518 |    70 | 0x46  | ascii       | 29943: ````` F `````  |
|         69 | ````` <0x42> ````` |  0.00202533 |    66 | 0x42  | ascii       | 29933: ````` B `````  |
|         80 | ````` <0x4D> ````` |  0.00202639 |    77 | 0x4D  | ascii       | 29924: ````` M `````  |
|         85 | ````` <0x52> ````` |  0.00202704 |    82 | 0x52  | ascii       | 29934: ````` R `````  |
|         62 | ````` <0x3B> ````` |  0.00202753 |    59 | 0x3B  | ascii       | 29936: ````` ; `````  |
|         77 | ````` <0x4A> ````` |  0.00202763 |    74 | 0x4A  | ascii       | 29967: ````` J `````  |
|        251 | ````` <0xF8> ````` |  0.00202812 |   248 | 0xF8  | unused_utf8 |                       |
|         56 | ````` <0x35> ````` |  0.0020287  |    53 | 0x35  | ascii       | 29945: ````` 5 `````  |
|         58 | ````` <0x37> ````` |  0.00202913 |    55 | 0x37  | ascii       | 29955: ````` 7 `````  |
|         92 | ````` <0x59> ````` |  0.00202966 |    89 | 0x59  | ascii       | 29979: ````` Y `````  |
|         99 | ````` <0x60> ````` |  0.00202998 |    96 | 0x60  | ascii       | 29952: ````` ` `````  |
|         89 | ````` <0x56> ````` |  0.00203097 |    86 | 0x56  | ascii       | 29963: ````` V `````  |
|         59 | ````` <0x38> ````` |  0.00203117 |    56 | 0x38  | ascii       | 29947: ````` 8 `````  |
|        196 | ````` <0xC1> ````` |  0.00203206 |   193 | 0xC1  | unused_utf8 |                       |
|         68 | ````` <0x41> ````` |  0.00203242 |    65 | 0x41  | ascii       | 29909: ````` A `````  |
|         48 | ````` <0x2D> ````` |  0.0020347  |    45 | 0x2D  | ascii       | 29899: ````` - `````  |
|        256 | ````` <0xFD> ````` |  0.0020349  |   253 | 0xFD  | unused_utf8 |                       |
|         70 | ````` <0x43> ````` |  0.00203577 |    67 | 0x43  | ascii       | 29907: ````` C `````  |
|         54 | ````` <0x33> ````` |  0.00203583 |    51 | 0x33  | ascii       | 29941: ````` 3 `````  |
|         97 | ````` <0x5E> ````` |  0.00203642 |    94 | 0x5E  | ascii       | 29985: ````` ^ `````  |
|         36 | ````` <0x21> ````` |  0.00203712 |    33 | 0x21  | ascii       | 29991: ````` ! `````  |
|         60 | ````` <0x39> ````` |  0.00203725 |    57 | 0x39  | ascii       | 29929: ````` 9 `````  |
|         64 | ````` <0x3D> ````` |  0.00203859 |    61 | 0x3D  | ascii       | 29922: ````` = `````  |
|        253 | ````` <0xFA> ````` |  0.00203878 |   250 | 0xFA  | unused_utf8 |                       |
|        121 | ````` <0x76> ````` |  0.00203927 |   118 | 0x76  | ascii       | 29894: ````` v `````  |
|        198 | ````` <0xC3> ````` |  0.00203949 |   195 | 0xC3  | utf8        |                       |
|        120 | ````` <0x75> ````` |  0.00204085 |   117 | 0x75  | ascii       | 29884: ````` u `````  |
|         83 | ````` <0x50> ````` |  0.0020415  |    80 | 0x50  | ascii       | 29925: ````` P `````  |
|         79 | ````` <0x4C> ````` |  0.0020419  |    76 | 0x4C  | ascii       | 29931: ````` L `````  |
|        257 | ````` <0xFE> ````` |  0.00204268 |   254 | 0xFE  | unused_utf8 |                       |
|        100 | ````` <0x61> ````` |  0.00204287 |    97 | 0x61  | ascii       | 29874: ````` a `````  |
|        108 | ````` <0x69> ````` |  0.00204354 |   105 | 0x69  | ascii       | 29875: ````` i `````  |
|        248 | ````` <0xF5> ````` |  0.00204377 |   245 | 0xF5  | unused_utf8 |                       |
|        110 | ````` <0x6B> ````` |  0.00204598 |   107 | 0x6B  | ascii       | 29895: ````` k `````  |
|        126 | ````` <0x7B> ````` |  0.00204621 |   123 | 0x7B  | ascii       | 29912: ````` { `````  |
|        119 | ````` <0x74> ````` |  0.00204692 |   116 | 0x74  | ascii       | 29873: ````` t `````  |
|         57 | ````` <0x36> ````` |  0.00204713 |    54 | 0x36  | ascii       | 29953: ````` 6 `````  |
|        113 | ````` <0x6E> ````` |  0.00204715 |   110 | 0x6E  | ascii       | 29876: ````` n `````  |
|        125 | ````` <0x7A> ````` |  0.00204734 |   122 | 0x7A  | ascii       | 29920: ````` z `````  |
|         44 | ````` <0x29> ````` |  0.00205088 |    41 | 0x29  | ascii       | 29897: ````` ) `````  |
|        105 | ````` <0x66> ````` |  0.00205401 |   102 | 0x66  | ascii       | 29888: ````` f `````  |
|         76 | ````` <0x49> ````` |  0.00205695 |    73 | 0x49  | ascii       | 29902: ````` I `````  |
|        114 | ````` <0x6F> ````` |  0.00205833 |   111 | 0x6F  | ascii       | 29877: ````` o `````  |
|         81 | ````` <0x4E> ````` |  0.00206368 |    78 | 0x4E  | ascii       | 29940: ````` N `````  |
|         45 | ````` <0x2A> ````` |  0.00206432 |    42 | 0x2A  | ascii       | 29930: ````` * `````  |
|         94 | ````` <0x5B> ````` |  0.00206441 |    91 | 0x5B  | ascii       | 29961: ````` [ `````  |
|         84 | ````` <0x51> ````` |  0.00207566 |    81 | 0x51  | ascii       | 29984: ````` Q `````  |
</details>


## Special tokens
6 entries below threshold of 0.182

|   token_id | token                          |   indicator | reencoded                                                   |
|------------|--------------------------------|-------------|-------------------------------------------------------------|
|      32002 | ````` <\|placeholder1\|> ````` |           0 | 29871: ````` ▁ `````, 32002: ````` <\|placeholder1\|> ````` |
|      32003 | ````` <\|placeholder2\|> ````` |           0 | 29871: ````` ▁ `````, 32003: ````` <\|placeholder2\|> ````` |
|      32004 | ````` <\|placeholder3\|> ````` |           0 | 29871: ````` ▁ `````, 32004: ````` <\|placeholder3\|> ````` |
|      32005 | ````` <\|placeholder4\|> ````` |           0 | 29871: ````` ▁ `````, 32005: ````` <\|placeholder4\|> ````` |
|      32008 | ````` <\|placeholder5\|> ````` |           0 | 29871: ````` ▁ `````, 32008: ````` <\|placeholder5\|> ````` |
|      32009 | ````` <\|placeholder6\|> ````` |           0 | 29871: ````` ▁ `````, 32009: ````` <\|placeholder6\|> ````` |

