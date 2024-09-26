# Report for `utter-project/EuroLLM-1.7B`

## Model info

* Model Info: 
  * Tied embeddings: False
  * LM head uses bias: False
  * Embeddings shape: [128000, 2048]
* Tokenizer Info: 
  * Vocab Size: 128000
  * Tokenizer Class: LlamaTokenizer
  * Tokenizer Type: BPE
  * Bytes handling: Byte Fallback
  * Token for verification prompt building: includegraphics
  * Token id for verification prompt building: 8997
* Indicator summary: 
  * Indicator for under-trained tokens: E_{in} L2 Norm
  * Overall distribution: 1.399 +/- 0.114
* Detected Token Counts: 
  * Number of tested under-trained tokens: 2559, 2260 non-special, 101 below p = 0.01 threshold, 11 below soft indicator threshold
  * Number of single byte tokens: 354, of which 120 below indicator threshold
  * Number of special tokens: 1, of which 0 below indicator threshold
  * Number of non-single-byte unreachable tokens: 1, of which 0 below indicator threshold

## Under-trained token indicators plot
![Indicators scatter plots](../indicators_pairplot_byid/utter_project_EuroLLM_1_7B.png)

## Verification plot
![Verification plot](../verifications_scatterplot/utter_project_EuroLLM_1_7B.png)

## Under-trained token verification results
11 entries below threshold of 0.475

|   token_id | token                       |   indicator | max_prob                                                         | in_other_tokens                                                                                                                                                                                                                                                                                                                                               |
|------------|-----------------------------|-------------|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      56539 | ````` funsio `````          |   0.0607532 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00043</span> |                                                                                                                                                                                                                                                                                                                                                               |
|      75613 | ````` urasGeneral `````     |   0.091315  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00032</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` FacturasGeneral `````</span>                                                                                                                                                                                                                                                                          |
|      35236 | ````` ▁funsio `````         |   0.10297   | <span style='border: 1px solid rgb(251, 189, 8);'>0.025</span>   |                                                                                                                                                                                                                                                                                                                                                               |
|      77603 | ````` FacturasGeneral ````` |   0.186482  | <span style='border: 1px solid rgb(40, 167, 69);'>0.75</span>    |                                                                                                                                                                                                                                                                                                                                                               |
|      58072 | ````` ▁momč `````           |   0.197107  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-05</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁momčadi `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁momčad `````</span>                                                                                                                                                                                                   |
|     114185 | ````` asaíne `````          |   0.199322  | <span style='border: 1px solid rgb(169, 68, 66);'>9.1e-09</span> | <span style='border: 1px solid rgb(255, 145, 0);'>````` asaíneonna `````</span>                                                                                                                                                                                                                                                                               |
|      26610 | ````` jetain `````          |   0.217722  | <span style='border: 1px solid rgb(169, 68, 66);'>4.1e-05</span> | ````` ▁dvejetain `````, <span style='border: 1px solid rgb(255, 145, 0);'>````` vejetain `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁dvejetainių `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Dvejetain `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁dvejetainiai `````</span> |
|      43175 | ````` ▁compéten `````       |   0.410877  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00091</span> | ````` ▁compétences `````, ````` ▁compétence `````                                                                                                                                                                                                                                                                                                             |
|      56988 | ````` ▁meais `````          |   0.439491  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00062</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁meaisín `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁meaisíní `````</span>                                                                                                                                                                                                 |
|      33200 | ````` ħtie `````            |   0.454049  | <span style='border: 1px solid rgb(169, 68, 66);'>1.2e-07</span> | ````` ħtieġ `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` ħtieġa `````</span>, ````` ▁meħtieġa `````, ````` ▁jeħtieġ `````                                                                                                                                                                                                                   |
|      37963 | ````` ▁voormal `````        |   0.469258  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0021</span>  | ````` ▁voormalige `````, ````` ▁voormalig `````                                                                                                                                                                                                                                                                                                               |


## Byte tokens
120 entries below threshold of 1.066

|   token_id | token              |   indicator |   ord | hex   | byte_type   | reencoded             |
|------------|--------------------|-------------|-------|-------|-------------|-----------------------|
|        346 | ````` <0x55> ````` | 0.000150553 |    85 | 0x55  | ascii       | 119830: ````` U ````` |
|        384 | ````` <0x7B> ````` | 0.000150566 |   123 | 0x7B  | ascii       | 119828: ````` { ````` |
|        338 | ````` <0x4D> ````` | 0.000150676 |    77 | 0x4D  | ascii       | 119770: ````` M ````` |
|        366 | ````` <0x69> ````` | 0.000151151 |   105 | 0x69  | ascii       | 119718: ````` i ````` |
|        362 | ````` <0x65> ````` | 0.000151514 |   101 | 0x65  | ascii       | 119716: ````` e ````` |
|        315 | ````` <0x36> ````` | 0.000152729 |    54 | 0x36  | ascii       | 119805: ````` 6 ````` |
|        319 | ````` <0x3A> ````` | 0.00015282  |    58 | 0x3A  | ascii       | 119782: ````` : ````` |
|        335 | ````` <0x4A> ````` | 0.000152908 |    74 | 0x4A  | ascii       | 119820: ````` J ````` |
|        341 | ````` <0x50> ````` | 0.000153085 |    80 | 0x50  | ascii       | 119769: ````` P ````` |
|        373 | ````` <0x70> ````` | 0.00015318  |   112 | 0x70  | ascii       | 119730: ````` p ````` |
|        336 | ````` <0x4B> ````` | 0.000153787 |    75 | 0x4B  | ascii       | 119804: ````` K ````` |
|        330 | ````` <0x45> ````` | 0.000153884 |    69 | 0x45  | ascii       | 119775: ````` E ````` |
|        299 | ````` <0x26> ````` | 0.000153955 |    38 | 0x26  | ascii       | 119945: ````` & ````` |
|        340 | ````` <0x4F> ````` | 0.000154011 |    79 | 0x4F  | ascii       | 119802: ````` O ````` |
|        296 | ````` <0x23> ````` | 0.000154265 |    35 | 0x23  | ascii       | 120135: ````` # ````` |
|        318 | ````` <0x39> ````` | 0.000154479 |    57 | 0x39  | ascii       | 119772: ````` 9 ````` |
|        323 | ````` <0x3E> ````` | 0.000154527 |    62 | 0x3E  | ascii       | 120057: ````` > ````` |
|        310 | ````` <0x31> ````` | 0.000154533 |    49 | 0x31  | ascii       | 119749: ````` 1 ````` |
|        376 | ````` <0x73> ````` | 0.000154611 |   115 | 0x73  | ascii       | 119723: ````` s ````` |
|        317 | ````` <0x38> ````` | 0.000154834 |    56 | 0x38  | ascii       | 119793: ````` 8 ````` |
<details><summary>100 additional entries below threshold</summary>

|   token_id | token              |   indicator |   ord | hex   | byte_type   | reencoded                |
|------------|--------------------|-------------|-------|-------|-------------|--------------------------|
|        329 | ````` <0x44> ````` | 0.000154885 |    68 | 0x44  | ascii       | 119774: ````` D `````    |
|        348 | ````` <0x57> ````` | 0.00015489  |    87 | 0x57  | ascii       | 119812: ````` W `````    |
|        363 | ````` <0x66> ````` | 0.000154899 |   102 | 0x66  | ascii       | 119737: ````` f `````    |
|        513 | ````` <0xFC> ````` | 0.000154916 |   252 | 0xFC  | unused_utf8 |                          |
|        370 | ````` <0x6D> ````` | 0.000155309 |   109 | 0x6D  | ascii       | 119728: ````` m `````    |
|        328 | ````` <0x43> ````` | 0.000155339 |    67 | 0x43  | ascii       | 119771: ````` C `````    |
|        326 | ````` <0x41> ````` | 0.000155529 |    65 | 0x41  | ascii       | 119758: ````` A `````    |
|        512 | ````` <0xFB> ````` | 0.000155604 |   251 | 0xFB  | unused_utf8 |                          |
|        385 | ````` <0x7C> ````` | 0.000155625 |   124 | 0x7C  | ascii       | 119920: ````` \| `````   |
|        379 | ````` <0x76> ````` | 0.000155658 |   118 | 0x76  | ascii       | 119734: ````` v `````    |
|        334 | ````` <0x49> ````` | 0.000155664 |    73 | 0x49  | ascii       | 119768: ````` I `````    |
|        355 | ````` <0x5E> ````` | 0.000155727 |    94 | 0x5E  | ascii       | 119952: ````` ^ `````    |
|        311 | ````` <0x32> ````` | 0.000155943 |    50 | 0x32  | ascii       | 119759: ````` 2 `````    |
|        309 | ````` <0x30> ````` | 0.000155978 |    48 | 0x30  | ascii       | 119752: ````` 0 `````    |
|        305 | ````` <0x2C> ````` | 0.000155989 |    44 | 0x2C  | ascii       | 119732: ````` , `````    |
|        353 | ````` <0x5C> ````` | 0.000155992 |    92 | 0x5C  | ascii       | 119765: ````` \ `````    |
|        382 | ````` <0x79> ````` | 0.000156002 |   121 | 0x79  | ascii       | 119738: ````` y `````    |
|        303 | ````` <0x2A> ````` | 0.000156058 |    42 | 0x2A  | ascii       | 119997: ````` * `````    |
|        456 | ````` <0xC3> ````` | 0.000156105 |   195 | 0xC3  | utf8        |                          |
|        352 | ````` <0x5B> ````` | 0.000156158 |    91 | 0x5B  | ascii       | 119980: ````` [ `````    |
|        510 | ````` <0xF9> ````` | 0.000156178 |   249 | 0xF9  | unused_utf8 |                          |
|        378 | ````` <0x75> ````` | 0.000156193 |   117 | 0x75  | ascii       | 119726: ````` u `````    |
|        369 | ````` <0x6C> ````` | 0.000156287 |   108 | 0x6C  | ascii       | 119724: ````` l `````    |
|        516 | ````` <0xFF> ````` | 0.000156289 |   255 | 0xFF  | unused_utf8 |                          |
|        350 | ````` <0x59> ````` | 0.000156299 |    89 | 0x59  | ascii       | 119928: ````` Y `````    |
|        312 | ````` <0x33> ````` | 0.000156305 |    51 | 0x33  | ascii       | 119790: ````` 3 `````    |
|        347 | ````` <0x56> ````` | 0.000156373 |    86 | 0x56  | ascii       | 119807: ````` V `````    |
|        300 | ````` <0x27> ````` | 0.000156489 |    39 | 0x27  | ascii       | 119792: ````` ' `````    |
|        304 | ````` <0x2B> ````` | 0.000156527 |    43 | 0x2B  | ascii       | 119994: ````` + `````    |
|        313 | ````` <0x34> ````` | 0.000156537 |    52 | 0x34  | ascii       | 119799: ````` 4 `````    |
|        381 | ````` <0x78> ````` | 0.000156616 |   120 | 0x78  | ascii       | 119778: ````` x `````    |
|        321 | ````` <0x3C> ````` | 0.000156644 |    60 | 0x3C  | ascii       | 120155: ````` < `````    |
|        327 | ````` <0x42> ````` | 0.000156674 |    66 | 0x42  | ascii       | 119776: ````` B `````    |
|        325 | ````` <0x40> ````` | 0.000156831 |    64 | 0x40  | ascii       | 120286: ````` @ `````    |
|        344 | ````` <0x53> ````` | 0.000156849 |    83 | 0x53  | ascii       | 119755: ````` S `````    |
|        367 | ````` <0x6A> ````` | 0.000156875 |   106 | 0x6A  | ascii       | 119744: ````` j `````    |
|        511 | ````` <0xFA> ````` | 0.000157028 |   250 | 0xFA  | unused_utf8 |                          |
|        383 | ````` <0x7A> ````` | 0.000157051 |   122 | 0x7A  | ascii       | 119740: ````` z `````    |
|        365 | ````` <0x68> ````` | 0.000157079 |   104 | 0x68  | ascii       | 119729: ````` h `````    |
|        356 | ````` <0x5F> ````` | 0.000157132 |    95 | 0x5F  | ascii       | 119839: ````` _ `````    |
|        316 | ````` <0x37> ````` | 0.00015714  |    55 | 0x37  | ascii       | 119806: ````` 7 `````    |
|        337 | ````` <0x4C> ````` | 0.00015715  |    76 | 0x4C  | ascii       | 119779: ````` L `````    |
|        357 | ````` <0x60> ````` | 0.000157286 |    96 | 0x60  | ascii       | 120355: ````` ` `````    |
|        374 | ````` <0x71> ````` | 0.000157301 |   113 | 0x71  | ascii       | 119764: ````` q `````    |
|        364 | ````` <0x67> ````` | 0.000157325 |   103 | 0x67  | ascii       | 119731: ````` g `````    |
|        273 | ````` <0x0C> ````` | 0.000157345 |    12 | 0x0C  | ascii       | 127915: ````` \x0c ````` |
|        293 | ````` <0x20> ````` | 0.000157412 |    32 | 0x20  | ascii       | 119715: ````` ▁ `````    |
|        333 | ````` <0x48> ````` | 0.000157644 |    72 | 0x48  | ascii       | 119795: ````` H `````    |
|        302 | ````` <0x29> ````` | 0.0001577   |    41 | 0x29  | ascii       | 119762: ````` ) `````    |
|        345 | ````` <0x54> ````` | 0.000157865 |    84 | 0x54  | ascii       | 119766: ````` T `````    |
|        515 | ````` <0xFE> ````` | 0.000157981 |   254 | 0xFE  | unused_utf8 |                          |
|        332 | ````` <0x47> ````` | 0.000158239 |    71 | 0x47  | ascii       | 119796: ````` G `````    |
|        361 | ````` <0x64> ````` | 0.000158293 |   100 | 0x64  | ascii       | 119725: ````` d `````    |
|        308 | ````` <0x2F> ````` | 0.000158306 |    47 | 0x2F  | ascii       | 119858: ````` / `````    |
|        292 | ````` <0x1F> ````` | 0.000158338 |    31 | 0x1F  | ascii       | 127739: ````` \x1f ````` |
|        339 | ````` <0x4E> ````` | 0.000158457 |    78 | 0x4E  | ascii       | 119787: ````` N `````    |
|        320 | ````` <0x3B> ````` | 0.000158511 |    59 | 0x3B  | ascii       | 119852: ````` ; `````    |
|        368 | ````` <0x6B> ````` | 0.00015856  |   107 | 0x6B  | ascii       | 119733: ````` k `````    |
|        507 | ````` <0xF6> ````` | 0.000158566 |   246 | 0xF6  | unused_utf8 |                          |
|        306 | ````` <0x2D> ````` | 0.000158598 |    45 | 0x2D  | ascii       | 119754: ````` - `````    |
|        331 | ````` <0x46> ````` | 0.00015861  |    70 | 0x46  | ascii       | 119794: ````` F `````    |
|        301 | ````` <0x28> ````` | 0.00015864  |    40 | 0x28  | ascii       | 119763: ````` ( `````    |
|        508 | ````` <0xF7> ````` | 0.000158794 |   247 | 0xF7  | unused_utf8 |                          |
|        360 | ````` <0x63> ````` | 0.000158862 |    99 | 0x63  | ascii       | 119727: ````` c `````    |
|        453 | ````` <0xC0> ````` | 0.000159183 |   192 | 0xC0  | unused_utf8 |                          |
|        454 | ````` <0xC1> ````` | 0.000159282 |   193 | 0xC1  | unused_utf8 |                          |
|        297 | ````` <0x24> ````` | 0.000159306 |    36 | 0x24  | ascii       | 119822: ````` $ `````    |
|        269 | ````` <0x08> ````` | 0.000159367 |     8 | 0x08  | ascii       | 127515: ````` \x08 ````` |
|        298 | ````` <0x25> ````` | 0.000159395 |    37 | 0x25  | ascii       | 119941: ````` % `````    |
|        268 | ````` <0x07> ````` | 0.000159493 |     7 | 0x07  | ascii       | 126478: ````` \x07 ````` |
|        322 | ````` <0x3D> ````` | 0.00015959  |    61 | 0x3D  | ascii       | 119926: ````` = `````    |
|        506 | ````` <0xF5> ````` | 0.000159622 |   245 | 0xF5  | unused_utf8 |                          |
|        307 | ````` <0x2E> ````` | 0.000159699 |    46 | 0x2E  | ascii       | 119735: ````` . `````    |
|        358 | ````` <0x61> ````` | 0.00015971  |    97 | 0x61  | ascii       | 119717: ````` a `````    |
|        314 | ````` <0x35> ````` | 0.000159863 |    53 | 0x35  | ascii       | 119791: ````` 5 `````    |
|        375 | ````` <0x72> ````` | 0.000160078 |   114 | 0x72  | ascii       | 119722: ````` r `````    |
|        354 | ````` <0x5D> ````` | 0.000160147 |    93 | 0x5D  | ascii       | 119979: ````` ] `````    |
|        349 | ````` <0x58> ````` | 0.000160236 |    88 | 0x58  | ascii       | 119931: ````` X `````    |
|        343 | ````` <0x52> ````` | 0.000160256 |    82 | 0x52  | ascii       | 119785: ````` R `````    |
|        295 | ````` <0x22> ````` | 0.00016034  |    34 | 0x22  | ascii       | 119813: ````` " `````    |
|        387 | ````` <0x7E> ````` | 0.000160362 |   126 | 0x7E  | ascii       | 120038: ````` ~ `````    |
|        351 | ````` <0x5A> ````` | 0.000160468 |    90 | 0x5A  | ascii       | 119874: ````` Z `````    |
|        342 | ````` <0x51> ````` | 0.000160472 |    81 | 0x51  | ascii       | 119961: ````` Q `````    |
|        386 | ````` <0x7D> ````` | 0.000160632 |   125 | 0x7D  | ascii       | 119829: ````` } `````    |
|        377 | ````` <0x74> ````` | 0.000160665 |   116 | 0x74  | ascii       | 119721: ````` t `````    |
|        372 | ````` <0x6F> ````` | 0.000160684 |   111 | 0x6F  | ascii       | 119720: ````` o `````    |
|        371 | ````` <0x6E> ````` | 0.000160759 |   110 | 0x6E  | ascii       | 119719: ````` n `````    |
|        509 | ````` <0xF8> ````` | 0.000160818 |   248 | 0xF8  | unused_utf8 |                          |
|        380 | ````` <0x77> ````` | 0.000161466 |   119 | 0x77  | ascii       | 119741: ````` w `````    |
|        324 | ````` <0x3F> ````` | 0.000161788 |    63 | 0x3F  | ascii       | 119882: ````` ? `````    |
|        514 | ````` <0xFD> ````` | 0.000162028 |   253 | 0xFD  | unused_utf8 |                          |
|        359 | ````` <0x62> ````` | 0.000163305 |    98 | 0x62  | ascii       | 119736: ````` b `````    |
|        294 | ````` <0x21> ````` | 0.000163937 |    33 | 0x21  | ascii       | 119906: ````` ! `````    |
|     119732 | ````` , `````      | 0.660469    |    44 | 0x2C  | ascii       |                          |
|     119735 | ````` . `````      | 0.668391    |    46 | 0x2E  | ascii       |                          |
|        271 | ````` <0x0A> ````` | 0.679881    |    10 | 0x0A  | ascii       |                          |
|     119782 | ````` : `````      | 0.920423    |    58 | 0x3A  | ascii       |                          |
|        401 | ````` <0x8C> ````` | 0.929337    |   140 | 0x8C  | utf8        |                          |
|     119765 | ````` \ `````      | 0.975955    |    92 | 0x5C  | ascii       |                          |
|        272 | ````` <0x0B> ````` | 1.03585     |    11 | 0x0B  | ascii       |                          |
</details>


## Special tokens
261 entries below threshold of 1.066

|   token_id | token                      |   indicator | max_prob                                                         |
|------------|----------------------------|-------------|------------------------------------------------------------------|
|        123 | ````` <extra_id_118> ````` | 0.000151795 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        214 | ````` <extra_id_209> ````` | 0.000151952 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        206 | ````` <extra_id_201> ````` | 0.000152535 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        104 | ````` <extra_id_99> `````  | 0.000152541 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        220 | ````` <extra_id_215> ````` | 0.000152555 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        164 | ````` <extra_id_159> ````` | 0.000152687 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        254 | ````` <extra_id_249> ````` | 0.000152697 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        208 | ````` <extra_id_203> ````` | 0.000152903 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        112 | ````` <extra_id_107> ````` | 0.000153096 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        140 | ````` <extra_id_135> ````` | 0.000153185 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        101 | ````` <extra_id_96> `````  | 0.000153276 | <span style='border: 1px solid rgb(169, 68, 66);'>1.2e-08</span> |
|        225 | ````` <extra_id_220> ````` | 0.000153321 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         96 | ````` <extra_id_91> `````  | 0.000153463 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        135 | ````` <extra_id_130> ````` | 0.000153482 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        237 | ````` <extra_id_232> ````` | 0.000153542 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         76 | ````` <extra_id_71> `````  | 0.000153544 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         30 | ````` <extra_id_25> `````  | 0.000153808 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         58 | ````` <extra_id_53> `````  | 0.000153842 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         44 | ````` <extra_id_39> `````  | 0.000153979 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        248 | ````` <extra_id_243> ````` | 0.000153982 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
<details><summary>241 additional entries below threshold</summary>

|   token_id | token                      |   indicator | max_prob                                                         |
|------------|----------------------------|-------------|------------------------------------------------------------------|
|        204 | ````` <extra_id_199> ````` | 0.000154017 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        165 | ````` <extra_id_160> ````` | 0.000154085 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        244 | ````` <extra_id_239> ````` | 0.000154132 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         92 | ````` <extra_id_87> `````  | 0.000154156 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         78 | ````` <extra_id_73> `````  | 0.000154214 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        136 | ````` <extra_id_131> ````` | 0.000154312 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        118 | ````` <extra_id_113> ````` | 0.000154335 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        184 | ````` <extra_id_179> ````` | 0.00015434  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         93 | ````` <extra_id_88> `````  | 0.000154391 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         54 | ````` <extra_id_49> `````  | 0.000154447 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         46 | ````` <extra_id_41> `````  | 0.000154468 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         79 | ````` <extra_id_74> `````  | 0.0001545   | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        181 | ````` <extra_id_176> ````` | 0.000154502 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         59 | ````` <extra_id_54> `````  | 0.000154544 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         14 | ````` <extra_id_9> `````   | 0.000154563 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        191 | ````` <extra_id_186> ````` | 0.000154581 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        106 | ````` <extra_id_101> ````` | 0.000154599 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        256 | ````` <extra_id_251> ````` | 0.000154612 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        158 | ````` <extra_id_153> ````` | 0.000154623 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        110 | ````` <extra_id_105> ````` | 0.000154637 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         86 | ````` <extra_id_81> `````  | 0.000154684 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         13 | ````` <extra_id_8> `````   | 0.000154747 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         19 | ````` <extra_id_14> `````  | 0.000154749 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         97 | ````` <extra_id_92> `````  | 0.000154756 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        186 | ````` <extra_id_181> ````` | 0.000154821 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         49 | ````` <extra_id_44> `````  | 0.000154846 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         90 | ````` <extra_id_85> `````  | 0.000154847 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        125 | ````` <extra_id_120> ````` | 0.00015491  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        222 | ````` <extra_id_217> ````` | 0.000154957 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        152 | ````` <extra_id_147> ````` | 0.000154993 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|          9 | ````` <extra_id_4> `````   | 0.000155011 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        129 | ````` <extra_id_124> ````` | 0.000155027 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        198 | ````` <extra_id_193> ````` | 0.000155083 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         83 | ````` <extra_id_78> `````  | 0.00015512  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        141 | ````` <extra_id_136> ````` | 0.000155122 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        137 | ````` <extra_id_132> ````` | 0.000155124 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        226 | ````` <extra_id_221> ````` | 0.000155166 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         61 | ````` <extra_id_56> `````  | 0.000155167 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        149 | ````` <extra_id_144> ````` | 0.000155193 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         40 | ````` <extra_id_35> `````  | 0.000155214 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         70 | ````` <extra_id_65> `````  | 0.000155301 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         95 | ````` <extra_id_90> `````  | 0.000155301 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         94 | ````` <extra_id_89> `````  | 0.00015537  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|          7 | ````` <extra_id_2> `````   | 0.000155465 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        235 | ````` <extra_id_230> ````` | 0.000155495 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         11 | ````` <extra_id_6> `````   | 0.000155534 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        139 | ````` <extra_id_134> ````` | 0.000155561 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        128 | ````` <extra_id_123> ````` | 0.000155635 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        124 | ````` <extra_id_119> ````` | 0.00015568  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        148 | ````` <extra_id_143> ````` | 0.000155732 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        240 | ````` <extra_id_235> ````` | 0.000155744 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        119 | ````` <extra_id_114> ````` | 0.000155749 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         32 | ````` <extra_id_27> `````  | 0.000155766 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         41 | ````` <extra_id_36> `````  | 0.000155794 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         65 | ````` <extra_id_60> `````  | 0.000155813 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         52 | ````` <extra_id_47> `````  | 0.000155847 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        218 | ````` <extra_id_213> ````` | 0.000155847 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|          3 | ````` <\|im_start\|> ````` | 0.000155892 |                                                                  |
|        103 | ````` <extra_id_98> `````  | 0.000155998 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         71 | ````` <extra_id_66> `````  | 0.000156098 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        192 | ````` <extra_id_187> ````` | 0.000156141 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        180 | ````` <extra_id_175> ````` | 0.000156212 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        102 | ````` <extra_id_97> `````  | 0.000156227 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        178 | ````` <extra_id_173> ````` | 0.000156239 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        199 | ````` <extra_id_194> ````` | 0.00015626  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        144 | ````` <extra_id_139> ````` | 0.000156263 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         18 | ````` <extra_id_13> `````  | 0.000156327 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         33 | ````` <extra_id_28> `````  | 0.000156337 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         42 | ````` <extra_id_37> `````  | 0.00015635  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        241 | ````` <extra_id_236> ````` | 0.000156356 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        156 | ````` <extra_id_151> ````` | 0.000156361 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|          6 | ````` <extra_id_1> `````   | 0.000156374 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         51 | ````` <extra_id_46> `````  | 0.000156402 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        205 | ````` <extra_id_200> ````` | 0.000156516 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        167 | ````` <extra_id_162> ````` | 0.00015655  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        183 | ````` <extra_id_178> ````` | 0.000156558 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        232 | ````` <extra_id_227> ````` | 0.000156567 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        157 | ````` <extra_id_152> ````` | 0.000156628 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        150 | ````` <extra_id_145> ````` | 0.00015665  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        174 | ````` <extra_id_169> ````` | 0.000156674 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         16 | ````` <extra_id_11> `````  | 0.000156687 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        257 | ````` <extra_id_252> ````` | 0.000156718 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        115 | ````` <extra_id_110> ````` | 0.000156761 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         50 | ````` <extra_id_45> `````  | 0.000156813 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        239 | ````` <extra_id_234> ````` | 0.000156816 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        182 | ````` <extra_id_177> ````` | 0.000156831 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         73 | ````` <extra_id_68> `````  | 0.000157029 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        215 | ````` <extra_id_210> ````` | 0.000157051 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        130 | ````` <extra_id_125> ````` | 0.000157053 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         85 | ````` <extra_id_80> `````  | 0.000157079 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        223 | ````` <extra_id_218> ````` | 0.000157112 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        131 | ````` <extra_id_126> ````` | 0.000157154 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        201 | ````` <extra_id_196> ````` | 0.000157167 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        253 | ````` <extra_id_248> ````` | 0.000157172 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        188 | ````` <extra_id_183> ````` | 0.000157209 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         26 | ````` <extra_id_21> `````  | 0.000157216 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        247 | ````` <extra_id_242> ````` | 0.00015725  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        213 | ````` <extra_id_208> ````` | 0.000157323 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        219 | ````` <extra_id_214> ````` | 0.000157327 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         27 | ````` <extra_id_22> `````  | 0.000157352 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        153 | ````` <extra_id_148> ````` | 0.000157358 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        260 | ````` <extra_id_255> ````` | 0.00015736  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        166 | ````` <extra_id_161> ````` | 0.000157377 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        105 | ````` <extra_id_100> ````` | 0.00015739  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        126 | ````` <extra_id_121> ````` | 0.000157421 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        168 | ````` <extra_id_163> ````` | 0.000157435 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        122 | ````` <extra_id_117> ````` | 0.000157446 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        231 | ````` <extra_id_226> ````` | 0.000157467 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        211 | ````` <extra_id_206> ````` | 0.00015751  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        111 | ````` <extra_id_106> ````` | 0.000157522 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         35 | ````` <extra_id_30> `````  | 0.000157537 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        108 | ````` <extra_id_103> ````` | 0.000157558 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        216 | ````` <extra_id_211> ````` | 0.00015756  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        193 | ````` <extra_id_188> ````` | 0.000157578 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        179 | ````` <extra_id_174> ````` | 0.000157609 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         81 | ````` <extra_id_76> `````  | 0.000157638 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        155 | ````` <extra_id_150> ````` | 0.000157677 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        159 | ````` <extra_id_154> ````` | 0.00015775  | <span style='border: 1px solid rgb(169, 68, 66);'>1.2e-08</span> |
|        109 | ````` <extra_id_104> ````` | 0.000157763 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        189 | ````` <extra_id_184> ````` | 0.000157795 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        234 | ````` <extra_id_229> ````` | 0.000157818 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        233 | ````` <extra_id_228> ````` | 0.000157849 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        258 | ````` <extra_id_253> ````` | 0.000157869 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        200 | ````` <extra_id_195> ````` | 0.000157876 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         84 | ````` <extra_id_79> `````  | 0.000157979 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        229 | ````` <extra_id_224> ````` | 0.000158037 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        202 | ````` <extra_id_197> ````` | 0.000158048 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        163 | ````` <extra_id_158> ````` | 0.000158079 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        245 | ````` <extra_id_240> ````` | 0.000158094 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         37 | ````` <extra_id_32> `````  | 0.000158144 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         23 | ````` <extra_id_18> `````  | 0.000158153 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        161 | ````` <extra_id_156> ````` | 0.000158168 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        146 | ````` <extra_id_141> ````` | 0.000158181 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        230 | ````` <extra_id_225> ````` | 0.000158213 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        243 | ````` <extra_id_238> ````` | 0.000158286 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        142 | ````` <extra_id_137> ````` | 0.000158349 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         75 | ````` <extra_id_70> `````  | 0.000158353 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        209 | ````` <extra_id_204> ````` | 0.000158371 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         39 | ````` <extra_id_34> `````  | 0.000158395 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        217 | ````` <extra_id_212> ````` | 0.000158404 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        250 | ````` <extra_id_245> ````` | 0.000158429 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        238 | ````` <extra_id_233> ````` | 0.000158495 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        194 | ````` <extra_id_189> ````` | 0.000158544 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        195 | ````` <extra_id_190> ````` | 0.000158548 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        116 | ````` <extra_id_111> ````` | 0.000158581 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         63 | ````` <extra_id_58> `````  | 0.000158612 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         62 | ````` <extra_id_57> `````  | 0.000158635 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         67 | ````` <extra_id_62> `````  | 0.000158674 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         24 | ````` <extra_id_19> `````  | 0.000158696 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         56 | ````` <extra_id_51> `````  | 0.000158716 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         74 | ````` <extra_id_69> `````  | 0.00015882  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        169 | ````` <extra_id_164> ````` | 0.000158853 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        212 | ````` <extra_id_207> ````` | 0.000158897 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         53 | ````` <extra_id_48> `````  | 0.000158922 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         47 | ````` <extra_id_42> `````  | 0.000158925 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        190 | ````` <extra_id_185> ````` | 0.000158928 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         34 | ````` <extra_id_29> `````  | 0.000158929 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         28 | ````` <extra_id_23> `````  | 0.000158933 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         69 | ````` <extra_id_64> `````  | 0.000158964 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        172 | ````` <extra_id_167> ````` | 0.000158981 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         98 | ````` <extra_id_93> `````  | 0.000159002 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        224 | ````` <extra_id_219> ````` | 0.000159053 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         60 | ````` <extra_id_55> `````  | 0.000159105 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         29 | ````` <extra_id_24> `````  | 0.000159151 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        114 | ````` <extra_id_109> ````` | 0.000159167 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         20 | ````` <extra_id_15> `````  | 0.000159208 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         25 | ````` <extra_id_20> `````  | 0.000159216 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        162 | ````` <extra_id_157> ````` | 0.000159283 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        249 | ````` <extra_id_244> ````` | 0.000159289 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        251 | ````` <extra_id_246> ````` | 0.000159337 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        197 | ````` <extra_id_192> ````` | 0.000159437 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        185 | ````` <extra_id_180> ````` | 0.000159469 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        175 | ````` <extra_id_170> ````` | 0.000159507 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        259 | ````` <extra_id_254> ````` | 0.000159526 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        121 | ````` <extra_id_116> ````` | 0.000159624 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        227 | ````` <extra_id_222> ````` | 0.000159679 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         80 | ````` <extra_id_75> `````  | 0.000159692 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        127 | ````` <extra_id_122> ````` | 0.000159719 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        196 | ````` <extra_id_191> ````` | 0.000159753 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         88 | ````` <extra_id_83> `````  | 0.00015976  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         22 | ````` <extra_id_17> `````  | 0.000159841 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         15 | ````` <extra_id_10> `````  | 0.000159894 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        242 | ````` <extra_id_237> ````` | 0.000159899 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        203 | ````` <extra_id_198> ````` | 0.00015998  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        236 | ````` <extra_id_231> ````` | 0.000159996 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        210 | ````` <extra_id_205> ````` | 0.00016007  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        117 | ````` <extra_id_112> ````` | 0.000160091 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         57 | ````` <extra_id_52> `````  | 0.000160102 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        252 | ````` <extra_id_247> ````` | 0.000160104 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         99 | ````` <extra_id_94> `````  | 0.000160112 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        145 | ````` <extra_id_140> ````` | 0.000160136 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        154 | ````` <extra_id_149> ````` | 0.000160202 | <span style='border: 1px solid rgb(169, 68, 66);'>1.2e-08</span> |
|        171 | ````` <extra_id_166> ````` | 0.000160258 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        100 | ````` <extra_id_95> `````  | 0.00016043  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         68 | ````` <extra_id_63> `````  | 0.00016046  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        177 | ````` <extra_id_172> ````` | 0.000160468 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         45 | ````` <extra_id_40> `````  | 0.000160479 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         89 | ````` <extra_id_84> `````  | 0.000160543 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         87 | ````` <extra_id_82> `````  | 0.000160558 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         38 | ````` <extra_id_33> `````  | 0.000160583 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        143 | ````` <extra_id_138> ````` | 0.00016063  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         36 | ````` <extra_id_31> `````  | 0.000160763 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        134 | ````` <extra_id_129> ````` | 0.000160899 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         43 | ````` <extra_id_38> `````  | 0.000160981 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        246 | ````` <extra_id_241> ````` | 0.000161018 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        176 | ````` <extra_id_171> ````` | 0.000161243 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         31 | ````` <extra_id_26> `````  | 0.0001613   | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|          4 | ````` <\|im_end\|> `````   | 0.000161343 |                                                                  |
|        170 | ````` <extra_id_165> ````` | 0.000161397 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        120 | ````` <extra_id_115> ````` | 0.000161465 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        221 | ````` <extra_id_216> ````` | 0.000161477 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|          8 | ````` <extra_id_3> `````   | 0.000161513 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         10 | ````` <extra_id_5> `````   | 0.000161548 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        160 | ````` <extra_id_155> ````` | 0.000161587 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|          5 | ````` <extra_id_0> `````   | 0.000161617 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        207 | ````` <extra_id_202> ````` | 0.000161703 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        255 | ````` <extra_id_250> ````` | 0.000161708 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        138 | ````` <extra_id_133> ````` | 0.000161776 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         12 | ````` <extra_id_7> `````   | 0.000161781 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        107 | ````` <extra_id_102> ````` | 0.000161995 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         66 | ````` <extra_id_61> `````  | 0.000162016 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         64 | ````` <extra_id_59> `````  | 0.000162064 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        133 | ````` <extra_id_128> ````` | 0.000162151 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        132 | ````` <extra_id_127> ````` | 0.00016226  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         72 | ````` <extra_id_67> `````  | 0.000162282 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        151 | ````` <extra_id_146> ````` | 0.000162282 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        228 | ````` <extra_id_223> ````` | 0.000162434 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         91 | ````` <extra_id_86> `````  | 0.000162442 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        173 | ````` <extra_id_168> ````` | 0.000162505 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         82 | ````` <extra_id_77> `````  | 0.000162623 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        147 | ````` <extra_id_142> ````` | 0.000162677 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        187 | ````` <extra_id_182> ````` | 0.000162689 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         55 | ````` <extra_id_50> `````  | 0.00016286  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         77 | ````` <extra_id_72> `````  | 0.000162872 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         48 | ````` <extra_id_43> `````  | 0.00016333  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         17 | ````` <extra_id_12> `````  | 0.000163558 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|         21 | ````` <extra_id_16> `````  | 0.000164425 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|        113 | ````` <extra_id_108> ````` | 0.000164672 | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-08</span> |
|          1 | ````` <s> `````            | 0.97711     | <span style='border: 1px solid rgb(40, 167, 69);'>0.13</span>    |
|          0 | ````` <unk> `````          | 0.987323    | <span style='border: 1px solid rgb(40, 167, 69);'>1</span>       |
|          2 | ````` </s> `````           | 1.00525     | <span style='border: 1px solid rgb(251, 189, 8);'>0.041</span>   |
</details>


## Unreachable tokens
0 entries below threshold of 1.066



