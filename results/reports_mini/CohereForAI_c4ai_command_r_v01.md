# Report for `CohereForAI/c4ai-command-r-v01`

## Model info

* Model Info: 
  * Tied embeddings: True
  * LM head uses bias: False
  * Embeddings shape: [256000, 8192]
* Tokenizer Info: 
  * Vocab Size: 255029
  * Tokenizer Class: CohereTokenizer
  * Tokenizer Type: BPE
  * Bytes handling: Byte Input
  * Token for verification prompt building: InvalidProtocolBufferException
  * Token id for verification prompt building: 148416
* Indicator summary: 
  * Indicator for under-trained tokens: E_{out} Cosine Distance
  * Overall distribution: 0.685 +/- 0.167
* Detected Token Counts: 
  * Number of tested under-trained tokens: 5012, 4963 non-special, 278 below p = 0.01 threshold, 158 below soft indicator threshold
  * Number of single byte tokens: 256, of which 13 below indicator threshold
  * Number of special tokens: 1403, of which 1403 below indicator threshold
  * Number of non-single-byte unreachable tokens: 1403, of which 1403 below indicator threshold
  * Number of non-single-byte UTF-fragment tokens:  2956, of which 16 below soft indicator threshold

## Under-trained token indicators plot
![Indicators scatter plots](../indicators_pairplot_byid/CohereForAI_c4ai_command_r_v01.png)

## Verification plot
![Verification plot](../verifications_scatterplot/CohereForAI_c4ai_command_r_v01.png)

## Under-trained token verification results
158 entries below threshold of 0.089

|   token_id | token                                                                                                                                |    indicator | max_prob                                                         | in_other_tokens                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      51386 | ````` ▁ARStdSong `````                                                                                                               | -2.38419e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     208149 | ````` AddLanguageSpecificText `````                                                                                                  | -2.38419e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` AddLanguageSpecificTextSet `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     127300 | ````` tocguid `````                                                                                                                  | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|      72754 | ````` ageryears `````                                                                                                                | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | ````` manageryears `````, ````` ▁manageryears `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|     177875 | ````` tochassubtree `````                                                                                                            | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|      22188 | ````` ▁林肯近地小行星研究小 `````                                                                                                    | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁林肯近地小行星研究小组 `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁林肯近地小行星研究小組 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                        |
|     239520 | ````` ▁hbBiddersParams `````                                                                                                         | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     140485 | ````` 目前尚未由人工引 `````                                                                                                         |  0           | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | <span style='border: 1px solid rgb(255, 145, 0);'>````` 目前尚未由人工引種栽培 `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` 目前尚未由人工引种栽培 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                          |
|      84176 | ````` recDocCases `````                                                                                                              |  0           | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|      15675 | ````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f ````` |  1.66893e-06 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````                                                                                                                                                                                                                                                                                                                                   |
|     145442 | ````` 》（）， `````                                                                                                                 |  3.22461e-05 | <span style='border: 1px solid rgb(169, 68, 66);'>3e-07</span>   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     141168 | ````` ephritidae `````                                                                                                               |  0.000151098 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Tephritidae `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` Tephritidae `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|     139462 | ````` 和人口皆未知 `````                                                                                                             |  0.000177979 | <span style='border: 1px solid rgb(169, 68, 66);'>3.2e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` 该地的面积和人口皆未知 `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` 面积和人口皆未知 `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` 該地的面積和人口皆未知 `````</span>                                                                                                                                                                                                                                                                                                                                   |
|     224223 | ````` 面积和人口皆未知 `````                                                                                                         |  0.00019145  | <span style='border: 1px solid rgb(169, 68, 66);'>3.2e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` 该地的面积和人口皆未知 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|      71049 | ````` tocectory `````                                                                                                                |  0.000221193 | <span style='border: 1px solid rgb(169, 68, 66);'>3.3e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     190228 | ````` ▁Hmelnî `````                                                                                                                  |  0.000252664 | <span style='border: 1px solid rgb(169, 68, 66);'>3e-07</span>   | <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁Hmelnîțkîi `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|     141246 | ````` locatorSection `````                                                                                                           |  0.000267982 | <span style='border: 1px solid rgb(169, 68, 66);'>3e-07</span>   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|       9741 | ````` \U000e0067\U000e0062\U000e0065\U000e006e `````                                                                                 |  0.000414312 | <span style='border: 1px solid rgb(169, 68, 66);'>3e-07</span>   | ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` ▁🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f ````` |
|     149800 | ````` 年建立的教育 `````                                                                                                             |  0.000468671 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` 年建立的教育機構 `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` 年建立的教育机构 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|     208151 | ````` AddLanguageSpecificTextSet `````                                                                                               |  0.000566423 | <span style='border: 1px solid rgb(169, 68, 66);'>2.5e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
<details><summary>138 additional entries below threshold</summary>

|   token_id | token                                    |   indicator | max_prob                                                         | in_other_tokens                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------|------------------------------------------|-------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     190437 | ````` BiddersParams `````                | 0.00057435  | <span style='border: 1px solid rgb(169, 68, 66);'>3e-07</span>   | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁hbBiddersParams `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|      51385 | ````` ▁ARStd `````                       | 0.000937343 | <span style='border: 1px solid rgb(169, 68, 66);'>2.4e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁ARStdSong `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     100190 | ````` Desambigua `````                   | 0.00101489  | <span style='border: 1px solid rgb(169, 68, 66);'>3.4e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` Desambiguação `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` Desambiguações `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|      94747 | ````` OnSearchSelect `````               | 0.00118101  | <span style='border: 1px solid rgb(169, 68, 66);'>1.5e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` OnSearchSelectHide `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` OnSearchSelectKey `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` OnSearchSelectShow `````</span>                                                                                                                                                                                                                                                                                                                                                   |
|     127290 | ````` srguid `````                       | 0.00181144  | <span style='border: 1px solid rgb(169, 68, 66);'>1.4e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     177855 | ````` assubtree `````                    | 0.0019446   | <span style='border: 1px solid rgb(169, 68, 66);'>1.7e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` tochassubtree `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|     228399 | ````` цыкла `````                        | 0.00220001  | <span style='border: 1px solid rgb(169, 68, 66);'>1.5e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` цыклапедыя `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` цыклапед `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Энцыклапедыя `````</span>                                                                                                                                                                                                                                                                                                                                                                         |
|      37757 | ````` （，）， `````                     | 0.00234509  | <span style='border: 1px solid rgb(169, 68, 66);'>2.4e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     172752 | ````` ablytyped `````                    | 0.00250292  | <span style='border: 1px solid rgb(169, 68, 66);'>1.4e-07</span> | ````` scalablytyped `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|     114578 | ````` inyphiidae `````                   | 0.00257373  | <span style='border: 1px solid rgb(169, 68, 66);'>2.5e-07</span> | ````` ▁Linyphiidae `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` Linyphiidae `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|     228872 | ````` ”（） `````                        | 0.00314629  | <span style='border: 1px solid rgb(169, 68, 66);'>2.7e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     223425 | ````` 而人口密度為 `````                 | 0.00333655  | <span style='border: 1px solid rgb(169, 68, 66);'>1.3e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` 而人口密度為每平方千米 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|      74789 | ````` stdtemplate `````                  | 0.00377572  | <span style='border: 1px solid rgb(169, 68, 66);'>2.4e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     119253 | ````` écosl `````                        | 0.00412083  | <span style='border: 1px solid rgb(169, 68, 66);'>2.5e-07</span> | ````` ▁Tchécoslovaquie `````, <span style='border: 1px solid rgb(251, 189, 8);'>````` écoslova `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` écoslovaquie `````</span>, ````` ▁tchécoslova `````                                                                                                                                                                                                                                                                                                                                                                                                   |
|     144020 | ````` оспоживача `````                   | 0.00440383  | <span style='border: 1px solid rgb(169, 68, 66);'>2.3e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁особоспоживача `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     100216 | ````` ▁μυθισ `````                       | 0.00441271  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁μυθιστό `````</span>, ````` ▁μυθιστο `````, ````` ▁μυθιστόρημα `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|     214699 | ````` 平均海拔高度為 `````               | 0.00468338  | <span style='border: 1px solid rgb(169, 68, 66);'>1e-07</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` 而該地的平均海拔高度為 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     249467 | ````` Тісс `````                         | 0.00484276  | <span style='border: 1px solid rgb(169, 68, 66);'>1.2e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` Тіссеранів `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      71714 | ````` 所属的省级 `````                   | 0.00510621  | <span style='border: 1px solid rgb(169, 68, 66);'>1e-07</span>   | <span style='border: 1px solid rgb(251, 189, 8);'>````` 所属的省级选区为 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|     157335 | ````` cetophilidae `````                 | 0.00515151  | <span style='border: 1px solid rgb(169, 68, 66);'>2.3e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Mycetophilidae `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` Mycetophilidae `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|      31886 | ````` docguid `````                      | 0.00570589  | <span style='border: 1px solid rgb(169, 68, 66);'>9.6e-08</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     223844 | ````` 該地的面積 `````                   | 0.00579876  | <span style='border: 1px solid rgb(169, 68, 66);'>2.4e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` 該地的面積和人口皆未知 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     127302 | ````` deliveryTarget `````               | 0.00625497  | <span style='border: 1px solid rgb(169, 68, 66);'>1e-07</span>   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     188002 | ````` țkîi `````                         | 0.0063017   | <span style='border: 1px solid rgb(169, 68, 66);'>1.7e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁Hmelnîțkîi `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|     202267 | ````` \U000e0074\U000e007f `````         | 0.00659168  | <span style='border: 1px solid rgb(169, 68, 66);'>1.4e-07</span> | ````` <0xB3>\U000e0063\U000e0074\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|     143921 | ````` 而水域 `````                       | 0.00671548  | <span style='border: 1px solid rgb(169, 68, 66);'>1.2e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` 而水域面積為 `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` 而水域面积为 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     127301 | ````` deliveryLink `````                 | 0.00713462  | <span style='border: 1px solid rgb(169, 68, 66);'>7.6e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     149474 | ````` 」（） `````                       | 0.0076924   | <span style='border: 1px solid rgb(169, 68, 66);'>2.5e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     152127 | ````` Rolver `````                       | 0.00788748  | <span style='border: 1px solid rgb(169, 68, 66);'>1e-07</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` Rolverdeling `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|      63146 | ````` 》（） `````                       | 0.00825226  | <span style='border: 1px solid rgb(169, 68, 66);'>2.6e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` 》（）， `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|      69100 | ````` \U000e0073\U000e007f `````         | 0.00882059  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00014</span> | ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````, ````` <0xB7>\U000e006c\U000e0073\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|     165878 | ````` ▁Jît `````                         | 0.00899625  | <span style='border: 1px solid rgb(169, 68, 66);'>1.5e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁Jîtomîr `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|     163225 | ````` 俄亥 `````                         | 0.00909454  | <span style='border: 1px solid rgb(169, 68, 66);'>1.2e-07</span> | ````` 俄亥俄 `````, ````` 俄亥俄州 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     138155 | ````` byliidae `````                     | 0.0103469   | <span style='border: 1px solid rgb(169, 68, 66);'>8.2e-08</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Bombyliidae `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` Bombyliidae `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|      29307 | ````` memItem `````                      | 0.0107573   | <span style='border: 1px solid rgb(169, 68, 66);'>1.5e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` memItemRight `````</span>, ````` memItemLeft `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|      75649 | ````` μοσπο `````                        | 0.0114875   | <span style='border: 1px solid rgb(169, 68, 66);'>9.6e-08</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` μοσπονδ `````</span>, ````` ▁Ομοσπονδίας `````, ````` μοσπονδια `````, ````` ▁Ομοσπονδία `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Ομοσπονδ `````</span>, ...                                                                                                                                                                                                                                                                                                                                                                                |
|     215450 | ````` 是一颗围绕太阳公 `````             | 0.0120146   | <span style='border: 1px solid rgb(169, 68, 66);'>7.2e-08</span> | ````` 是一颗围绕太阳公转的小行星 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|      98281 | ````` 天文台近地小行星 `````             | 0.0120566   | <span style='border: 1px solid rgb(169, 68, 66);'>8.2e-08</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁洛厄尔天文台近地小行星搜寻计划 `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` 天文台近地小行星搜寻计划 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                        |
|     132755 | ````` Сокор `````                        | 0.0120993   | <span style='border: 1px solid rgb(169, 68, 66);'>1e-07</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` Сокорро `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|      57843 | ````` NdEx `````                         | 0.0122942   | <span style='border: 1px solid rgb(169, 68, 66);'>8.1e-08</span> | ````` iNdEx `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁iNdEx `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|      21048 | ````` yrıca `````                        | 0.0123368   | <span style='border: 1px solid rgb(169, 68, 66);'>2.9e-07</span> | ````` ▁ayrıca `````, ````` Ayrıca `````, ````` ▁Ayrıca `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|      87763 | ````` 덜란드 `````                       | 0.0123856   | <span style='border: 1px solid rgb(169, 68, 66);'>6.4e-06</span> | ````` 네덜란드 `````, ````` ▁네덜란드 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     234076 | ````` ▁Άντζελ `````                      | 0.013365    | <span style='border: 1px solid rgb(169, 68, 66);'>1e-06</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Άντζελες `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|      16811 | ````` 한민국의 `````                     | 0.0135859   | <span style='border: 1px solid rgb(169, 68, 66);'>4.2e-07</span> | ````` 대한민국의 `````, ````` ▁대한민국의 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      85423 | ````` езультаты `````                    | 0.0137519   | <span style='border: 1px solid rgb(169, 68, 66);'>9e-08</span>   | ````` ▁результаты `````, ````` ▁Результаты `````, ````` Результаты `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|      28088 | ````` ервые `````                        | 0.0139876   | <span style='border: 1px solid rgb(169, 68, 66);'>9.4e-06</span> | ````` ▁впервые `````, ````` первые `````, ````` Впервые `````, ````` ▁первые `````, ````` ▁Первые `````, ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|     104486 | ````` ούθησε `````                       | 0.0140874   | <span style='border: 1px solid rgb(169, 68, 66);'>7.8e-06</span> | ````` κολούθησε `````, ````` ▁ακολούθησε `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|      71316 | ````` 市镇编码为 `````                   | 0.0145054   | <span style='border: 1px solid rgb(169, 68, 66);'>7e-08</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` INSEE市镇编码为 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     165176 | ````` foolcdn `````                      | 0.0149491   | <span style='border: 1px solid rgb(169, 68, 66);'>1.4e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      71269 | ````` aravant `````                      | 0.0154468   | <span style='border: 1px solid rgb(169, 68, 66);'>6.2e-05</span> | ````` uparavant `````, ````` ▁auparavant `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|      61835 | ````` есмотря `````                      | 0.0157058   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00013</span> | ````` ▁несмотря `````, ````` ▁Несмотря `````, ````` Несмотря `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|      49349 | ````` （，） `````                       | 0.0157582   | <span style='border: 1px solid rgb(169, 68, 66);'>6.5e-05</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     113299 | ````` ▁Υόρ `````                         | 0.0160672   | <span style='border: 1px solid rgb(169, 68, 66);'>5.7e-05</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Υόρκη `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Υόρκης `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|      72073 | ````` eskipun `````                      | 0.0170404   | <span style='border: 1px solid rgb(169, 68, 66);'>9.2e-05</span> | ````` ▁Meskipun `````, ````` Meskipun `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     112496 | ````` ▁předcho `````                     | 0.0172572   | <span style='border: 1px solid rgb(169, 68, 66);'>7e-05</span>   | ````` ▁předchozí `````, ````` ▁předchoz `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|       9740 | ````` \U000e0067\U000e007f `````         | 0.0172623   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00033</span> | ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` ▁🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````          |
|     177869 | ````` ▁tocid `````                       | 0.0180357   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00019</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     114974 | ````` ▁auxqu `````                       | 0.0184579   | <span style='border: 1px solid rgb(169, 68, 66);'>8.6e-07</span> | ````` ▁auxquelles `````, ````` ▁auxquels `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|      60667 | ````` ▁sconfit `````                     | 0.0186383   | <span style='border: 1px solid rgb(169, 68, 66);'>8.5e-06</span> | ````` ▁sconfitto `````, ````` ▁sconfitta `````, ````` ▁sconfitte `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|      58491 | ````` DFBEF `````                        | 0.018805    | <span style='border: 1px solid rgb(169, 68, 66);'>9.3e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     176101 | ````` jsdel `````                        | 0.0197907   | <span style='border: 1px solid rgb(169, 68, 66);'>7.5e-05</span> | ````` jsdelivr `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|      42729 | ````` ▁Indlaw `````                      | 0.0203013   | <span style='border: 1px solid rgb(169, 68, 66);'>9.3e-05</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     113886 | ````` ▁kardy `````                       | 0.0204585   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00015</span> | ````` ▁kardynał `````, ````` ▁kardyna `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     173398 | ````` rowborder `````                    | 0.0213152   | <span style='border: 1px solid rgb(169, 68, 66);'>5.7e-05</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` cellrowborder `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|     232240 | ````` ουσαλή `````                       | 0.0221089   | <span style='border: 1px solid rgb(169, 68, 66);'>3.3e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Ιερουσαλήμ `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` ουσαλήμ `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|      88149 | ````` 蒙山巡天 `````                     | 0.0224239   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00017</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁莱蒙山巡天 `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁萊蒙山巡天 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|     109027 | ````` ▁fême `````                        | 0.0226392   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00015</span> | ````` ▁fêmeas `````, ````` ▁fêmea `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|      67872 | ````` recDoc `````                       | 0.0229452   | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` recDocCases `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|     249873 | ````` codeSnippetContainer `````         | 0.0237278   | <span style='border: 1px solid rgb(169, 68, 66);'>2.7e-05</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     127296 | ````` altview `````                      | 0.0242277   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00038</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     229503 | ````` 密歇 `````                         | 0.0242589   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00041</span> | ````` 密歇根 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|     250514 | ````` [✓]( `````                         | 0.0243678   | <span style='border: 1px solid rgb(169, 68, 66);'>8.6e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      98314 | ````` 天文台近地小行星搜寻计划 `````     | 0.0244097   | <span style='border: 1px solid rgb(169, 68, 66);'>8.6e-08</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁洛厄尔天文台近地小行星搜寻计划 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     232390 | ````` Wikicon `````                      | 0.0252566   | <span style='border: 1px solid rgb(169, 68, 66);'>4e-07</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` Wikiconcurso `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|     248801 | ````` AlreadyInited `````                | 0.0266783   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00027</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` GetEmptyStringAlreadyInited `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|     202213 | ````` \U000e0063 `````                   | 0.0272274   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00075</span> | ````` <0xB3>\U000e0063\U000e0074\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````, ````` <0xB3>\U000e0063 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     139412 | ````` 皆未知 `````                       | 0.0278487   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00021</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` 该地的面积和人口皆未知 `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` 面积和人口皆未知 `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` 該地的面積和人口皆未知 `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` 和人口皆未知 `````</span>                                                                                                                                                                                                                                                         |
|     191064 | ````` AoAKACgAoAKACgAoAKACgAoAKACg ````` | 0.028109    | <span style='border: 1px solid rgb(169, 68, 66);'>0.00044</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     182239 | ````` （）（ `````                       | 0.0287033   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00029</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      17586 | ````` льбом `````                        | 0.0288575   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00019</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` Альбомы `````</span>, ````` ▁альбомов `````, ````` ▁Альбом `````, ````` ▁альбому `````, ````` ▁альбоме `````, ...                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|     141408 | ````` cellinside `````                   | 0.0298864   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00064</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     102360 | ````` AoAKACg `````                      | 0.030281    | <span style='border: 1px solid rgb(169, 68, 66);'>0.00026</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` AoAKACgAoAKACgAoAKACgAoAKACg `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` AoAKACgAoAKACg `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|     152313 | ````` SnippetContainer `````             | 0.0312876   | <span style='border: 1px solid rgb(169, 68, 66);'>7.5e-06</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` codeSnippetContainer `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` CodeSnippetContainer `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|      90334 | ````` ▁Башкорт `````                     | 0.0314993   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00034</span> | ````` ▁Башкортостана `````, ````` ▁Башкортостан `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Башкортост `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|      54193 | ````` ▁近地小行星 `````                  | 0.0320907   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00027</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁近地小行星追踪 `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁近地小行星追蹤 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|     239797 | ````` CodeSnippetContainer `````         | 0.0334247   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00057</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|       9738 | ````` \U000e006e `````                   | 0.0345665   | <span style='border: 1px solid rgb(169, 68, 66);'>6e-05</span>   | ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` <0xA5>\U000e006e `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ... |
|     202195 | ````` \U000e0074 `````                   | 0.035921    | <span style='border: 1px solid rgb(255, 145, 0);'>0.0017</span>  | <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0074\U000e007f `````</span>, ````` <0xB3>\U000e0063\U000e0074\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                   |
|     101279 | ````` AKACg `````                        | 0.0359275   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00034</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` AoAKACgAoAKACgAoAKACgAoAKACg `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` AoAKACgAoAKACg `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` AoAKACg `````</span>                                                                                                                                                                                                                                                                                                                                                       |
|     117753 | ````` ▁военнослуж `````                  | 0.0369521   | <span style='border: 1px solid rgb(169, 68, 66);'>0.0003</span>  | ````` ▁военнослужащих `````, ````` ▁военнослужащ `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|      55304 | ````` ▁коллект `````                     | 0.0371375   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00057</span> | ````` ▁коллектив `````, ````` ▁коллектива `````, ````` ▁коллективы `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     162582 | ````` omîr `````                         | 0.0373952   | <span style='border: 1px solid rgb(169, 68, 66);'>2.6e-05</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁Jîtomîr `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|      98082 | ````` ▁洛厄尔 `````                      | 0.037731    | <span style='border: 1px solid rgb(169, 68, 66);'>0.00047</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁洛厄尔天文台近地小行星搜寻计划 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     108955 | ````` AoAKACgAoAKACg `````               | 0.0381254   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00057</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` AoAKACgAoAKACgAoAKACgAoAKACg `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|      98512 | ````` ▁zawodn `````                      | 0.0383753   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00034</span> | ````` ▁zawodnicy `````, ````` ▁zawodnik `````, ````` ▁zawodnikiem `````, ````` ▁zawodnicz `````, ````` ▁zawodników `````, ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|     168004 | ````` deliveryFormat `````               | 0.0385362   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00014</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      71539 | ````` 时的人口数量为人 `````             | 0.0392631   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00021</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` 于时的人口数量为人 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|     141235 | ````` subSelected `````                  | 0.0394912   | <span style='border: 1px solid rgb(255, 145, 0);'>0.0016</span>  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      47407 | ````` ▁voormal `````                     | 0.0397072   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00019</span> | ````` ▁voormalig `````, ````` ▁voormalige `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     153159 | ````` ▁двен `````                        | 0.0406054   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00048</span> | ````` ▁двенадц `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|      69092 | ````` \U000e006c `````                   | 0.0417386   | <span style='border: 1px solid rgb(255, 145, 0);'>0.0011</span>  | ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````, ````` <0xB7>\U000e006c `````, ````` <0xB7>\U000e006c\U000e0073\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     126598 | ````` ▁orquí `````                       | 0.0418922   | <span style='border: 1px solid rgb(169, 68, 66);'>0.0003</span>  | ````` ▁orquídea `````, ````` ▁orquídeas `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|      68163 | ````` ▁hvě `````                         | 0.0426952   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00038</span> | ````` ▁hvěz `````, ````` ▁hvězdy `````, ````` ▁hvězd `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|     137635 | ````` ▁Λουδοβ `````                      | 0.0428526   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00049</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Λουδοβίκος `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Λουδοβίκου `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|     202631 | ````` ▁Mîkolai `````                     | 0.0453103   | <span style='border: 1px solid rgb(169, 68, 66);'>1.6e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁Mîkolaiiv `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     249185 | ````` ▁BĞ `````                          | 0.0468049   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00036</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁BĞMSZ `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     139250 | ````` 而人口密度 `````                   | 0.0493024   | <span style='border: 1px solid rgb(169, 68, 66);'>0.0003</span>  | <span style='border: 1px solid rgb(40, 167, 69);'>````` 而人口密度为每平方千米 `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` 而人口密度為 `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` 而人口密度為每平方千米 `````</span>                                                                                                                                                                                                                                                                                                                                                |
|      79368 | ````` ▁баскет `````                      | 0.0523369   | <span style='border: 1px solid rgb(255, 145, 0);'>0.0011</span>  | ````` ▁баскетболь `````, ````` ▁баскетбол `````, ````` ▁баскетболу `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     214270 | ````` 平均海拔高度为 `````               | 0.0530336   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00022</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` 而该地的平均海拔高度为 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|      40115 | ````` uslararası `````                   | 0.0539107   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00038</span> | ````` ▁Uluslararası `````, ````` ▁uluslararası `````, ````` Uluslararası `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|      69089 | ````` \U000e0073 `````                   | 0.054805    | <span style='border: 1px solid rgb(255, 145, 0);'>0.0059</span>  | <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0073\U000e007f `````</span>, ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````, ````` <0xB7>\U000e006c\U000e0073\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````                                                                                                                                                                                                                                                                                                                      |
|     105682 | ````` ishockeyspieler `````              | 0.0555152   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00063</span> | ````` ▁Eishockeyspieler `````, ````` Eishockeyspieler `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     110750 | ````` ▁κομμά `````                       | 0.0574614   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00045</span> | ````` ▁κομμάτια `````, ````` ▁κομμάτι `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     219726 | ````` ▁海勒 `````                        | 0.0596587   | <span style='border: 1px solid rgb(255, 145, 0);'>0.0022</span>  | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁海勒卡拉 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|     123576 | ````` ▁Αυστ `````                        | 0.0617248   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00049</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Αυστρίας `````</span>, ````` ▁Αυστρα `````, ````` ▁Αυστρία `````, ````` ▁Αυστραλία `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Αυστρια `````</span>                                                                                                                                                                                                                                                                                                                                                                                           |
|     175277 | ````` морозный `````                     | 0.0624213   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00028</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Безморозный `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|     233679 | ````` چوست `````                         | 0.0632702   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00036</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁ماساچوست `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|     100038 | ````` ▁spoluprá `````                    | 0.0641201   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00024</span> | ````` ▁spolupráci `````, ````` ▁spolupráce `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|     142131 | ````` ▁middeleeuw `````                  | 0.0654282   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00044</span> | ````` ▁middeleeuwse `````, ````` ▁middeleeuwen `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     114115 | ````` ▁πρίγκι `````                      | 0.067718    | <span style='border: 1px solid rgb(255, 145, 0);'>0.0033</span>  | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁πρίγκιπας `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁πρίγκιπα `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     167896 | ````` wluk `````                         | 0.0686558   | <span style='border: 1px solid rgb(255, 145, 0);'>0.0039</span>  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      81575 | ````` δοσφαίρου `````                    | 0.0716695   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00043</span> | ````` ▁ποδοσφαίρου `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Ποδοσφαίρου `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|      87941 | ````` ▁αντιμετ `````                     | 0.0728961   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00092</span> | ````` ▁αντιμετω `````, ````` ▁αντιμετώ `````, ````` ▁αντιμετώπ `````, ````` ▁αντιμετωπ `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|      69409 | ````` ahraga `````                       | 0.0731417   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00092</span> | ````` ▁Olahraga `````, ````` ▁olahraga `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|     196178 | ````` johnsnow `````                     | 0.0746502   | <span style='border: 1px solid rgb(251, 189, 8);'>0.042</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` johnsnowlabs `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|     144088 | ````` urtemberg `````                    | 0.076658    | <span style='border: 1px solid rgb(255, 145, 0);'>0.0014</span>  | ````` Wurtemberg `````, ````` ▁Wurtemberg `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     228624 | ````` δινάν `````                        | 0.0772313   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00065</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Φερδινάν `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|     160473 | ````` АТУУ `````                         | 0.0775049   | <span style='border: 1px solid rgb(169, 68, 66);'>0.0006</span>  | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁КОАТУУ `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|     228507 | ````` цыклапед `````                     | 0.0781655   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00068</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` цыклапедыя `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Энцыклапедыя `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|     121405 | ````` ▁ecclésiast `````                  | 0.080048    | <span style='border: 1px solid rgb(169, 68, 66);'>0.00083</span> | ````` ▁ecclésiastiques `````, ````` ▁ecclésiastique `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|     118022 | ````` erdapat `````                      | 0.0809146   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00045</span> | ````` ▁Terdapat `````, ````` Terdapat `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     211674 | ````` scoreDisplayMode `````             | 0.0838857   | <span style='border: 1px solid rgb(251, 189, 8);'>0.02</span>    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     248208 | ````` وجرسی `````                        | 0.0846838   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00051</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁نیوجرسی `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|      68073 | ````` ▁Českoslovens `````                | 0.08507     | <span style='border: 1px solid rgb(255, 145, 0);'>0.0071</span>  | ````` ▁Československé `````, ````` ▁Československo `````, ````` ▁Československu `````, ````` ▁Československa `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|     170688 | ````` fecie `````                        | 0.086238    | <span style='border: 1px solid rgb(255, 145, 0);'>0.0085</span>  | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁sztafecie `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     216345 | ````` ▁altimg `````                      | 0.0886432   | <span style='border: 1px solid rgb(251, 189, 8);'>0.02</span>    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      81478 | ````` δοσφαί `````                       | 0.089029    | <span style='border: 1px solid rgb(169, 68, 66);'>0.00046</span> | ````` ▁ποδοσφαίρου `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` δοσφαίρου `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Ποδοσφαίρου `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     111802 | ````` ▁πλαίσ `````                       | 0.0891462   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00069</span> | ````` ▁πλαίσιο `````, ````` ▁πλαίσια `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
</details>


## Tokens with partial UTF-8 sequences
16 entries below threshold of 0.089

|   token_id | token                                                 |    indicator | in_other_tokens                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------|-------------------------------------------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      97361 | ````` <0x95>시코 `````                                | -2.38419e-07 | ````` 멕시코 `````, ````` ▁멕시코 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|      70552 | ````` <0xB9><0x80><0xE0><0xB8> `````                  | -1.19209e-07 | ````` เ<0xE0><0xB8> `````, ````` ▁เ<0xE0><0xB8> `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      57888 | ````` <0x89>글랜드 `````                              | -1.19209e-07 | ````` 잉글랜드의 `````, ````` 잉글랜드 `````, ````` ▁잉글랜드 `````, ````` ▁잉글랜드의 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|     113772 | ````` <0x98>리포니아 `````                            | -1.19209e-07 | ````` ▁캘리포니아 `````, ````` 캘리포니아 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|     202233 | ````` <0xB3>\U000e0063 `````                          |  2.98023e-06 | ````` <0xB3>\U000e0063\U000e0074\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|      19460 | ````` ▁🇯<0xF0><0x9F><0x87> `````                      |  3.45707e-05 | ````` ▁🇯🇲 `````, ````` ▁🇯🇴 `````, ````` ▁🇯🇵 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|      69097 | ````` <0xB7>\U000e006c `````                          |  0.000421047 | ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````, ````` <0xB7>\U000e006c\U000e0073\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|      62442 | ````` ▁🏴\U000e0067\U000e0062<0xF3><0xA0><0x81> ````` |  0.000610292 | ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|       6132 | ````` <0xA7><0xF3><0xA0><0x81> `````                  |  0.00152338  | ````` \U000e0067<0xF3><0xA0><0x81> `````, ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e `````</span>, ````` \U000e0067\U000e0062<0xF3><0xA0><0x81> `````, ...                                                                                                                                                                                                                                                                                            |
|       9739 | ````` <0xA5>\U000e006e `````                          |  0.00746822  | ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` ▁🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f ````` |
|      33585 | ````` <0x94>레비전 `````                              |  0.00804347  | ````` ▁텔레비전 `````, ````` 텔레비전 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|     195191 | ````` "><0xEE><0x85> `````                            |  0.0239668   | <span style='border: 1px solid rgb(251, 189, 8);'>````` ">\ue157</ `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|       6133 | ````` \U000e0067<0xF3><0xA0><0x81> `````              |  0.0324408   | ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e `````</span>, ````` \U000e0067\U000e0062<0xF3><0xA0><0x81> `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e007f `````</span>, ...                                                                                                                                                                                                                                           |
|       9302 | ````` <0xA2><0xF3><0xA0><0x81> `````                  |  0.0327427   | ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e `````</span>, ````` \U000e0067\U000e0062<0xF3><0xA0><0x81> `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ...                                                                                                                                                                                                   |
|      53275 | ````` 特<0xE5><0xBE> `````                            |  0.0404994   | ````` 的特征 `````, ````` 特徴 `````, ````` 特征 `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` 特律 `````</span>, ````` 底特律 `````, ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     151735 | ````` 垃<0xE5><0x9C> `````                            |  0.0432829   | ````` 垃圾 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |


## Byte tokens
13 entries below threshold of 0.067

|   token_id | token              |    indicator |   ord | hex   | byte_type   |
|------------|--------------------|--------------|-------|-------|-------------|
|        191 | ````` <0xFB> ````` | -3.57628e-07 |   251 | 0xFB  | unused_utf8 |
|        185 | ````` <0xF5> ````` | -2.38419e-07 |   245 | 0xF5  | unused_utf8 |
|        189 | ````` <0xF9> ````` | -2.38419e-07 |   249 | 0xF9  | unused_utf8 |
|        193 | ````` <0xFD> ````` | -2.38419e-07 |   253 | 0xFD  | unused_utf8 |
|        186 | ````` <0xF6> ````` | -1.19209e-07 |   246 | 0xF6  | unused_utf8 |
|        195 | ````` <0xFF> ````` | -1.19209e-07 |   255 | 0xFF  | unused_utf8 |
|        132 | ````` <0xC0> ````` | -1.19209e-07 |   192 | 0xC0  | unused_utf8 |
|        192 | ````` <0xFC> ````` | -1.19209e-07 |   252 | 0xFC  | unused_utf8 |
|        187 | ````` <0xF7> ````` | -1.19209e-07 |   247 | 0xF7  | unused_utf8 |
|        133 | ````` <0xC1> ````` | -1.19209e-07 |   193 | 0xC1  | unused_utf8 |
|        188 | ````` <0xF8> ````` | -1.19209e-07 |   248 | 0xF8  | unused_utf8 |
|        190 | ````` <0xFA> ````` | -1.19209e-07 |   250 | 0xFA  | unused_utf8 |
|        194 | ````` <0xFE> ````` | -1.19209e-07 |   254 | 0xFE  | unused_utf8 |


## Special tokens
26 entries below threshold of 0.067

|   token_id | token                           |    indicator | max_prob                                                         |
|------------|---------------------------------|--------------|------------------------------------------------------------------|
|     255027 | ````` <\|EXTRA_8_TOKEN\|> ````` | -2.38419e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255012 | ````` <\|USER_3_TOKEN\|> `````  | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255005 | ````` <\|BAD_TOKEN\|> `````     | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255011 | ````` <\|USER_2_TOKEN\|> `````  | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255026 | ````` <\|EXTRA_7_TOKEN\|> ````` | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255025 | ````` <\|EXTRA_6_TOKEN\|> ````` | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255020 | ````` <\|EXTRA_1_TOKEN\|> ````` | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255018 | ````` <\|USER_9_TOKEN\|> `````  | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255023 | ````` <\|EXTRA_4_TOKEN\|> ````` | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255013 | ````` <\|USER_4_TOKEN\|> `````  | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255022 | ````` <\|EXTRA_3_TOKEN\|> ````` | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255010 | ````` <\|USER_1_TOKEN\|> `````  | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255024 | ````` <\|EXTRA_5_TOKEN\|> ````` | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255017 | ````` <\|USER_8_TOKEN\|> `````  | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|          4 | ````` <MASK_TOKEN> `````        | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255016 | ````` <\|USER_7_TOKEN\|> `````  |  0           | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255014 | ````` <\|USER_5_TOKEN\|> `````  |  0           | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255019 | ````` <\|EXTRA_0_TOKEN\|> ````` |  0           | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255009 | ````` <\|USER_0_TOKEN\|> `````  |  0           | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255003 | ````` <\|NO_TOKEN\|> `````      |  0           | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
<details><summary>6 additional entries below threshold</summary>

|   token_id | token                           |   indicator | max_prob                                                         |
|------------|---------------------------------|-------------|------------------------------------------------------------------|
|     255004 | ````` <\|GOOD_TOKEN\|> `````    | 0           | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255028 | ````` <\|EXTRA_9_TOKEN\|> ````` | 0           | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255015 | ````` <\|USER_6_TOKEN\|> `````  | 5.96046e-08 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255002 | ````` <\|YES_TOKEN\|> `````     | 5.96046e-08 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255021 | ````` <\|EXTRA_2_TOKEN\|> ````` | 5.96046e-08 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|          7 | ````` <EOP_TOKEN> `````         | 0.00548863  | <span style='border: 1px solid rgb(169, 68, 66);'>4.3e-07</span> |
</details>


## Unreachable tokens
1403 entries below threshold of 0.067

|   token_id | token            |    indicator | reencoded                                                                        |
|------------|------------------|--------------|----------------------------------------------------------------------------------|
|        295 | ````` ¿⏺? `````  | -4.76837e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 126: ````` <0xBA> `````        |
|        316 | ````` ¿☠? `````  | -3.57628e-07 | 34133: ````` <0xE2><0x98> `````, 262: ````` <0xA0> `````                         |
|        541 | ````` ¿🌲? ````` | -3.57628e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 118: ````` <0xB2> ````` |
|        406 | ````` ¿❇? `````  | -3.57628e-07 | 135523: ````` <0xE2><0x9D> `````, 237: ````` <0x87> `````                        |
|        521 | ````` ¿🌜? ````` | -3.57628e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 258: ````` <0x9C> ````` |
|        513 | ````` ¿🌔? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 250: ````` <0x94> ````` |
|        471 | ````` ¿🇹? `````  | -2.38419e-07 | 10591: ````` 🇹 `````                                                             |
|        836 | ````` ¿👡? ````` | -2.38419e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 102: ````` <0xA1> `````                  |
|        844 | ````` ¿👩? ````` | -2.38419e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 110: ````` <0xA9> `````                  |
|       1494 | ````` ¿🦵? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 121: ````` <0xB5> ````` |
|        569 | ````` ¿🍎? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 244: ````` <0x8E> ````` |
|        433 | ````` ¿㊙? ````` | -2.38419e-07 | 167: ````` <0xE3> `````, 240: ````` <0x8A> `````, 255: ````` <0x99> `````        |
|       1543 | ````` ¿🧦? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 107: ````` <0xA6> ````` |
|        566 | ````` ¿🍋? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 241: ````` <0x8B> ````` |
|       1151 | ````` ¿😕? ````` | -2.38419e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 251: ````` <0x95> `````                  |
|        712 | ````` ¿🏢? ````` | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 103: ````` <0xA2> `````                  |
|        320 | ````` ¿☪? `````  | -2.38419e-07 | 34133: ````` <0xE2><0x98> `````, 111: ````` <0xAA> `````                         |
|       1026 | ````` ¿🔠? ````` | -2.38419e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 262: ````` <0xA0> `````                  |
|       1569 | ````` ¿🩰? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 116: ````` <0xB0> ````` |
|       1474 | ````` ¿🦡? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 102: ````` <0xA1> ````` |
<details><summary>1383 additional entries below threshold</summary>

|   token_id | token                    |    indicator | reencoded                                                                        |
|------------|--------------------------|--------------|----------------------------------------------------------------------------------|
|        493 | ````` ¿🌀? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 3388: ````` <0x8C><0x80> `````                   |
|        574 | ````` ¿🍓? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 249: ````` <0x93> ````` |
|        339 | ````` ¿♓? `````         | -2.38419e-07 | 45687: ````` <0xE2><0x99> `````, 249: ````` <0x93> `````                         |
|        542 | ````` ¿🌳? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 119: ````` <0xB3> ````` |
|       1600 | ````` ¿🪞? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 260: ````` <0x9E> ````` |
|        532 | ````` ¿🌩? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 110: ````` <0xA9> ````` |
|        503 | ````` ¿🌊? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 240: ````` <0x8A> ````` |
|        914 | ````` ¿💯? `````         | -2.38419e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 115: ````` <0xAF> `````                  |
|        491 | ````` ¿🉐? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 239: ````` <0x89> `````, 246: ````` <0x90> ````` |
|        682 | ````` ¿🏄? `````         | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 234: ````` <0x84> `````                  |
|        279 | ````` ¿⌛? `````         | -2.38419e-07 | 166: ````` <0xE2> `````, 242: ````` <0x8C> `````, 257: ````` <0x9B> `````        |
|        538 | ````` ¿🌯? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 115: ````` <0xAF> ````` |
|        335 | ````` ¿♏? `````         | -2.38419e-07 | 45687: ````` <0xE2><0x99> `````, 245: ````` <0x8F> `````                         |
|        750 | ````` ¿🐋? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 241: ````` <0x8B> ````` |
|        467 | ````` ¿🇵? `````          | -2.38419e-07 | 137446: ````` 🇵 `````                                                            |
|       1408 | ````` ¿🥟? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 261: ````` <0x9F> ````` |
|        496 | ````` ¿🌃? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 233: ````` <0x83> ````` |
|       1105 | ````` ¿🖥? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 106: ````` <0xA5> ````` |
|       1119 | ````` ¿🗡? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 102: ````` <0xA1> ````` |
|        307 | ````` ¿☂? `````          | -2.38419e-07 | 34133: ````` <0xE2><0x98> `````, 232: ````` <0x82> `````                         |
|        338 | ````` ¿♒? `````         | -2.38419e-07 | 45687: ````` <0xE2><0x99> `````, 248: ````` <0x92> `````                         |
|        403 | ````` ¿✳? `````          | -2.38419e-07 | 70336: ````` <0xE2><0x9C> `````, 119: ````` <0xB3> `````                         |
|        466 | ````` ¿🇴? `````          | -2.38419e-07 | 40228: ````` 🇴 `````                                                             |
|        616 | ````` ¿🍽? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 129: ````` <0xBD> ````` |
|        719 | ````` ¿🏩? `````         | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 110: ````` <0xA9> `````                  |
|       1532 | ````` ¿🧛? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 257: ````` <0x9B> ````` |
|       1085 | ````` ¿🕧? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 108: ````` <0xA7> ````` |
|       1040 | ````` ¿🔮? `````         | -2.38419e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 114: ````` <0xAE> `````                  |
|        615 | ````` ¿🍼? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 22059: ````` <0x8D><0xBC> `````                  |
|        981 | ````` ¿📲? `````         | -2.38419e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 118: ````` <0xB2> `````                  |
|        484 | ````` ¿🈴? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 120: ````` <0xB4> ````` |
|        591 | ````` ¿🍤? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 105: ````` <0xA4> ````` |
|        568 | ````` ¿🍍? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 243: ````` <0x8D> ````` |
|        495 | ````` ¿🌂? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 232: ````` <0x82> ````` |
|        736 | ````` ¿🏽? `````           | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 129: ````` <0xBD> `````                  |
|        375 | ````` ¿⛩? `````          | -2.38419e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 110: ````` <0xA9> `````        |
|        524 | ````` ¿🌟? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 261: ````` <0x9F> ````` |
|        549 | ````` ¿🌺? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 126: ````` <0xBA> ````` |
|       1644 | ````` ¿\U0001fae2? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 103: ````` <0xA2> ````` |
|       1109 | ````` ¿🖼? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 128: ````` <0xBC> ````` |
|        344 | ````` ¿♦? `````          | -2.38419e-07 | 238161: ````` ♦ `````                                                            |
|        409 | ````` ¿❓? `````         | -2.38419e-07 | 135523: ````` <0xE2><0x9D> `````, 249: ````` <0x93> `````                        |
|        420 | ````` ¿➿? `````         | -2.38419e-07 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 131: ````` <0xBF> `````        |
|        434 | ````` ¿️? `````           | -2.38419e-07 | 57462: ````` ️ `````                                                              |
|        428 | ````` ¿⭐? `````         | -2.38419e-07 | 137546: ````` ⭐ `````                                                           |
|       1030 | ````` ¿🔤? `````         | -2.38419e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 105: ````` <0xA4> `````                  |
|        692 | ````` ¿🏎? `````          | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 244: ````` <0x8E> `````                  |
|       1477 | ````` ¿🦤? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 105: ````` <0xA4> ````` |
|       1661 | ````` ¿\U000e006c? ````` | -2.38419e-07 | 69092: ````` \U000e006c `````                                                    |
|        639 | ````` ¿🎖? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 252: ````` <0x96> ````` |
|        294 | ````` ¿⏹? `````          | -2.38419e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 125: ````` <0xB9> `````        |
|        314 | ````` ¿☘? `````          | -2.38419e-07 | 34133: ````` <0xE2><0x98> `````, 254: ````` <0x98> `````                         |
|        971 | ````` ¿📨? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 65064: ````` <0x93><0xA8> `````                  |
|       1184 | ````` ¿😶? `````         | -2.38419e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 122: ````` <0xB6> `````                  |
|        751 | ````` ¿🐌? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 242: ````` <0x8C> ````` |
|        482 | ````` ¿🈲? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 118: ````` <0xB2> ````` |
|       1563 | ````` ¿🧺? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 126: ````` <0xBA> ````` |
|       1597 | ````` ¿🪛? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 257: ````` <0x9B> ````` |
|       1042 | ````` ¿🔰? `````         | -2.38419e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 116: ````` <0xB0> `````                  |
|        517 | ````` ¿🌘? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 254: ````` <0x98> ````` |
|        998 | ````` ¿🔄? `````         | -2.38419e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 234: ````` <0x84> `````                  |
|        270 | ````` ¿↔? `````          | -2.38419e-07 | 76876: ````` <0xE2><0x86> `````, 250: ````` <0x94> `````                         |
|        424 | ````` ¿⬆? `````          | -2.38419e-07 | 166: ````` <0xE2> `````, 113: ````` <0xAC> `````, 236: ````` <0x86> `````        |
|        743 | ````` ¿🐄? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 234: ````` <0x84> ````` |
|        641 | ````` ¿🎙? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 255: ````` <0x99> ````` |
|       1564 | ````` ¿🧻? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 127: ````` <0xBB> ````` |
|        556 | ````` ¿🍁? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 231: ````` <0x81> ````` |
|        463 | ````` ¿🇱? `````          | -2.38419e-07 | 24385: ````` 🇱 `````                                                             |
|        266 | ````` ¿⁉? `````          | -2.38419e-07 | 36937: ````` <0xE2><0x81> `````, 239: ````` <0x89> `````                         |
|        645 | ````` ¿🎟? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 261: ````` <0x9F> ````` |
|        437 | ````` ¿🅰? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 235: ````` <0x85> `````, 116: ````` <0xB0> ````` |
|        663 | ````` ¿🎱? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 117: ````` <0xB1> ````` |
|        412 | ````` ¿❗? `````         | -2.38419e-07 | 135523: ````` <0xE2><0x9D> `````, 253: ````` <0x97> `````                        |
|        830 | ````` ¿👛? `````         | -2.38419e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 257: ````` <0x9B> `````                  |
|        963 | ````` ¿📠? `````         | -2.38419e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 262: ````` <0xA0> `````                  |
|       1646 | ````` ¿\U0001fae4? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 105: ````` <0xA4> ````` |
|        326 | ````` ¿♀? `````          | -2.38419e-07 | 45687: ````` <0xE2><0x99> `````, 230: ````` <0x80> `````                         |
|       1632 | ````` ¿🫐? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 246: ````` <0x90> ````` |
|        292 | ````` ¿⏳? `````         | -2.38419e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 119: ````` <0xB3> `````        |
|        653 | ````` ¿🎧? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 108: ````` <0xA7> ````` |
|        887 | ````` ¿💔? `````         | -2.38419e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 250: ````` <0x94> `````                  |
|        498 | ````` ¿🌅? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 235: ````` <0x85> ````` |
|       1094 | ````` ¿🕹? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 125: ````` <0xB9> ````` |
|        686 | ````` ¿🏈? `````         | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 238: ````` <0x88> `````                  |
|        452 | ````` ¿🇦? `````          | -2.38419e-07 | 21170: ````` 🇦 `````                                                             |
|        876 | ````` ¿💉? `````         | -2.38419e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 239: ````` <0x89> `````                  |
|       1070 | ````` ¿🕘? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 254: ````` <0x98> ````` |
|        766 | ````` ¿🐛? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 257: ````` <0x9B> ````` |
|        647 | ````` ¿🎡? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 102: ````` <0xA1> ````` |
|       1023 | ````` ¿🔝? `````         | -2.38419e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 259: ````` <0x9D> `````                  |
|        672 | ````` ¿🎺? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 126: ````` <0xBA> ````` |
|        293 | ````` ¿⏸? `````          | -2.38419e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 124: ````` <0xB8> `````        |
|       1034 | ````` ¿🔨? `````         | -2.38419e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 109: ````` <0xA8> `````                  |
|        905 | ````` ¿💦? `````         | -2.38419e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 107: ````` <0xA6> `````                  |
|        610 | ````` ¿🍷? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 123: ````` <0xB7> ````` |
|       1631 | ````` ¿\U0001fac5? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 235: ````` <0x85> ````` |
|        415 | ````` ¿➕? `````         | -2.38419e-07 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 251: ````` <0x95> `````        |
|       1386 | ````` ¿🥉? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 239: ````` <0x89> ````` |
|        637 | ````` ¿🎒? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 248: ````` <0x92> ````` |
|        516 | ````` ¿🌗? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 253: ````` <0x97> ````` |
|        564 | ````` ¿🍉? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 239: ````` <0x89> ````` |
|        423 | ````` ¿⬅? `````          | -2.38419e-07 | 166: ````` <0xE2> `````, 113: ````` <0xAC> `````, 235: ````` <0x85> `````        |
|        446 | ````` ¿🆕? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 251: ````` <0x95> ````` |
|        374 | ````` ¿⛔? `````         | -2.38419e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 250: ````` <0x94> `````        |
|        278 | ````` ¿⌚? `````         | -2.38419e-07 | 166: ````` <0xE2> `````, 242: ````` <0x8C> `````, 256: ````` <0x9A> `````        |
|        618 | ````` ¿🍿? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 131: ````` <0xBF> ````` |
|       1475 | ````` ¿🦢? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 103: ````` <0xA2> ````` |
|       1654 | ````` ¿\U0001faf4? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 120: ````` <0xB4> ````` |
|        811 | ````` ¿👈? `````         | -2.38419e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 238: ````` <0x88> `````                  |
|        705 | ````` ¿🏛? `````          | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 257: ````` <0x9B> `````                  |
|        345 | ````` ¿♨? `````          | -2.38419e-07 | 45687: ````` <0xE2><0x99> `````, 109: ````` <0xA8> `````                         |
|        704 | ````` ¿🏚? `````          | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 256: ````` <0x9A> `````                  |
|        626 | ````` ¿🎇? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 237: ````` <0x87> ````` |
|        442 | ````` ¿🆑? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 247: ````` <0x91> ````` |
|        910 | ````` ¿💫? `````         | -2.38419e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 112: ````` <0xAB> `````                  |
|        911 | ````` ¿💬? `````         | -2.38419e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 113: ````` <0xAC> `````                  |
|        441 | ````` ¿🆎? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 244: ````` <0x8E> ````` |
|        850 | ````` ¿👯? `````         | -2.38419e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 115: ````` <0xAF> `````                  |
|        745 | ````` ¿🐆? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 236: ````` <0x86> ````` |
|        965 | ````` ¿📢? `````         | -2.38419e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 103: ````` <0xA2> `````                  |
|        958 | ````` ¿📛? `````         | -2.38419e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 257: ````` <0x9B> `````                  |
|        396 | ````` ¿✏? `````          | -2.38419e-07 | 70336: ````` <0xE2><0x9C> `````, 245: ````` <0x8F> `````                         |
|        651 | ````` ¿🎥? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 106: ````` <0xA5> ````` |
|        447 | ````` ¿🆖? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 252: ````` <0x96> ````` |
|        304 | ````` ¿◾? `````         | -2.38419e-07 | 37357: ````` <0xE2><0x97> `````, 130: ````` <0xBE> `````                         |
|        296 | ````` ¿Ⓜ? `````          | -2.38419e-07 | 166: ````` <0xE2> `````, 249: ````` <0x93> `````, 232: ````` <0x82> `````        |
|        619 | ````` ¿🎀? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 230: ````` <0x80> ````` |
|        630 | ````` ¿🎋? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 241: ````` <0x8B> ````` |
|        506 | ````` ¿🌍? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 243: ````` <0x8D> ````` |
|       1511 | ````` ¿🧆? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 236: ````` <0x86> ````` |
|        596 | ````` ¿🍩? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 110: ````` <0xA9> ````` |
|        652 | ````` ¿🎦? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 107: ````` <0xA6> ````` |
|       1622 | ````` ¿\U0001fab7? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 123: ````` <0xB7> ````` |
|        528 | ````` ¿🌥? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 106: ````` <0xA5> ````` |
|        659 | ````` ¿🎭? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 263: ````` <0xAD> ````` |
|        554 | ````` ¿🌿? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 131: ````` <0xBF> ````` |
|       1180 | ````` ¿😲? `````         | -2.38419e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 118: ````` <0xB2> `````                  |
|        950 | ````` ¿📓? `````         | -2.38419e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 249: ````` <0x93> `````                  |
|       1645 | ````` ¿\U0001fae3? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 104: ````` <0xA3> ````` |
|        501 | ````` ¿🌈? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 238: ````` <0x88> ````` |
|       1652 | ````` ¿\U0001faf2? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 118: ````` <0xB2> ````` |
|       1535 | ````` ¿🧞? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 260: ````` <0x9E> ````` |
|       1545 | ````` ¿🧨? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 109: ````` <0xA8> ````` |
|        410 | ````` ¿❔? `````         | -2.38419e-07 | 135523: ````` <0xE2><0x9D> `````, 250: ````` <0x94> `````                        |
|       1518 | ````` ¿🧍? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 243: ````` <0x8D> ````` |
|        938 | ````` ¿📇? `````         | -2.38419e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 237: ````` <0x87> `````                  |
|        347 | ````` ¿♾? `````          | -2.38419e-07 | 45687: ````` <0xE2><0x99> `````, 130: ````` <0xBE> `````                         |
|        684 | ````` ¿🏆? `````         | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 236: ````` <0x86> `````                  |
|        553 | ````` ¿🌾? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 130: ````` <0xBE> ````` |
|       1125 | ````` ¿🗻? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 127: ````` <0xBB> ````` |
|        921 | ````` ¿💶? `````         | -2.38419e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 122: ````` <0xB6> `````                  |
|        299 | ````` ¿▶? `````          | -2.38419e-07 | 29034: ````` <0xE2><0x96> `````, 122: ````` <0xB6> `````                         |
|        327 | ````` ¿♂? `````          | -2.38419e-07 | 232883: ````` ♂ `````                                                            |
|        460 | ````` ¿🇮? `````          | -2.38419e-07 | 31122: ````` 🇮 `````                                                             |
|       1634 | ````` ¿🫒? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 248: ````` <0x92> ````` |
|        865 | ````` ¿👾? `````         | -2.38419e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 130: ````` <0xBE> `````                  |
|        727 | ````` ¿🏳? `````          | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 119: ````` <0xB3> `````                  |
|        422 | ````` ¿⤵? `````          | -2.38419e-07 | 166: ````` <0xE2> `````, 105: ````` <0xA4> `````, 121: ````` <0xB5> `````        |
|        386 | ````` ¿⛺? `````         | -2.38419e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 126: ````` <0xBA> `````        |
|        622 | ````` ¿🎃? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 233: ````` <0x83> ````` |
|       1164 | ````` ¿😢? `````         | -2.38419e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 103: ````` <0xA2> `````                  |
|       1550 | ````` ¿🧭? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 263: ````` <0xAD> ````` |
|       1616 | ````` ¿🪱? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 117: ````` <0xB1> ````` |
|       1528 | ````` ¿🧗? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 253: ````` <0x97> ````` |
|       1433 | ````` ¿🥸? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 124: ````` <0xB8> ````` |
|        889 | ````` ¿💖? `````         | -2.38419e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 252: ````` <0x96> `````                  |
|       1357 | ````` ¿🤪? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 111: ````` <0xAA> ````` |
|        585 | ````` ¿🍞? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 260: ````` <0x9E> ````` |
|        924 | ````` ¿💹? `````         | -2.38419e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 125: ````` <0xB9> `````                  |
|        814 | ````` ¿👋? `````         | -2.38419e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 241: ````` <0x8B> `````                  |
|        565 | ````` ¿🍊? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 240: ````` <0x8A> ````` |
|        435 | ````` ¿🀄? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 230: ````` <0x80> `````, 234: ````` <0x84> ````` |
|        400 | ````` ¿✝? `````          | -2.38419e-07 | 70336: ````` <0xE2><0x9C> `````, 259: ````` <0x9D> `````                         |
|       1479 | ````` ¿🦦? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 107: ````` <0xA6> ````` |
|        399 | ````` ¿✖? `````          | -2.38419e-07 | 70336: ````` <0xE2><0x9C> `````, 252: ````` <0x96> `````                         |
|       1141 | ````` ¿😋? `````         | -2.38419e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 241: ````` <0x8B> `````                  |
|        573 | ````` ¿🍒? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 248: ````` <0x92> ````` |
|        800 | ````` ¿🐽? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 129: ````` <0xBD> ````` |
|        558 | ````` ¿🍃? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 233: ````` <0x83> ````` |
|        550 | ````` ¿🌻? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 127: ````` <0xBB> ````` |
|        510 | ````` ¿🌑? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 247: ````` <0x91> ````` |
|        264 | ````` ¿\u200d? `````     | -2.38419e-07 | 35927: ````` \u200d `````                                                        |
|        392 | ````` ¿✊? `````         | -2.38419e-07 | 70336: ````` <0xE2><0x9C> `````, 240: ````` <0x8A> `````                         |
|        475 | ````` ¿🇽? `````          | -2.38419e-07 | 2244: ````` <0xF0><0x9F><0x87> `````, 129: ````` <0xBD> `````                    |
|        277 | ````` ¿↪? `````          | -2.38419e-07 | 76876: ````` <0xE2><0x86> `````, 111: ````` <0xAA> `````                         |
|        519 | ````` ¿🌚? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 256: ````` <0x9A> ````` |
|        753 | ````` ¿🐎? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 244: ````` <0x8E> ````` |
|        372 | ````` ¿⛑? `````          | -2.38419e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 247: ````` <0x91> `````        |
|        595 | ````` ¿🍨? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 49252: ````` <0x8D><0xA8> `````                  |
|        448 | ````` ¿🆗? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 253: ````` <0x97> ````` |
|        450 | ````` ¿🆙? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 255: ````` <0x99> ````` |
|        677 | ````` ¿🎿? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 131: ````` <0xBF> ````` |
|        300 | ````` ¿◀? `````          | -2.38419e-07 | 37357: ````` <0xE2><0x97> `````, 230: ````` <0x80> `````                         |
|        379 | ````` ¿⛲? `````         | -2.38419e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 118: ````` <0xB2> `````        |
|       1618 | ````` ¿🪳? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 119: ````` <0xB3> ````` |
|        644 | ````` ¿🎞? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 260: ````` <0x9E> ````` |
|        701 | ````` ¿🏗? `````          | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 253: ````` <0x97> `````                  |
|        816 | ````` ¿👍? `````         | -2.38419e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 243: ````` <0x8D> `````                  |
|        371 | ````` ¿⛏? `````          | -2.38419e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 245: ````` <0x8F> `````        |
|        903 | ````` ¿💤? `````         | -2.38419e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 105: ````` <0xA4> `````                  |
|       1625 | ````` ¿\U0001faba? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 126: ````` <0xBA> ````` |
|        861 | ````` ¿👺? `````         | -2.38419e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 126: ````` <0xBA> `````                  |
|        268 | ````` ¿™? `````          | -2.38419e-07 | 33572: ````` ™ `````                                                             |
|        733 | ````` ¿🏺? `````         | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 126: ````` <0xBA> `````                  |
|        472 | ````` ¿🇺? `````          | -2.38419e-07 | 9554: ````` 🇺 `````                                                              |
|        458 | ````` ¿🇬? `````          | -2.38419e-07 | 42828: ````` 🇬 `````                                                             |
|        587 | ````` ¿🍠? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 262: ````` <0xA0> ````` |
|       1179 | ````` ¿😱? `````         | -2.38419e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 117: ````` <0xB1> `````                  |
|        358 | ````` ¿⚠? `````          | -2.38419e-07 | 175142: ````` <0xE2><0x9A> `````, 262: ````` <0xA0> `````                        |
|       1527 | ````` ¿🧖? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 252: ````` <0x96> ````` |
|        551 | ````` ¿🌼? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 128: ````` <0xBC> ````` |
|       1498 | ````` ¿🦹? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 125: ````` <0xB9> ````` |
|       1520 | ````` ¿🧏? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 245: ````` <0x8F> ````` |
|        288 | ````` ¿⏯? `````          | -2.38419e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 115: ````` <0xAF> `````        |
|        600 | ````` ¿🍭? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 263: ````` <0xAD> ````` |
|        489 | ````` ¿🈹? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 125: ````` <0xB9> ````` |
|        497 | ````` ¿🌄? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 234: ````` <0x84> ````` |
|       1426 | ````` ¿🥱? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 117: ````` <0xB1> ````` |
|        582 | ````` ¿🍛? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 257: ````` <0x9B> ````` |
|       1250 | ````` ¿🚨? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 109: ````` <0xA8> ````` |
|        473 | ````` ¿🇻? `````          | -2.38419e-07 | 99202: ````` 🇻 `````                                                             |
|        543 | ````` ¿🌴? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 120: ````` <0xB4> ````` |
|       1491 | ````` ¿🦲? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 118: ````` <0xB2> ````` |
|        359 | ````` ¿⚡? `````         | -2.38419e-07 | 175142: ````` <0xE2><0x9A> `````, 102: ````` <0xA1> `````                        |
|        757 | ````` ¿🐒? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 248: ````` <0x92> ````` |
|       1054 | ````` ¿🔼? `````         | -2.38419e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 128: ````` <0xBC> `````                  |
|       1576 | ````` ¿🩺? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 126: ````` <0xBA> ````` |
|       1556 | ````` ¿🧳? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 119: ````` <0xB3> ````` |
|        953 | ````` ¿📖? `````         | -2.38419e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 252: ````` <0x96> `````                  |
|        966 | ````` ¿📣? `````         | -2.38419e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 104: ````` <0xA3> `````                  |
|        662 | ````` ¿🎰? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 116: ````` <0xB0> ````` |
|        894 | ````` ¿💛? `````         | -2.38419e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 257: ````` <0x9B> `````                  |
|        365 | ````` ¿⚽? `````         | -2.38419e-07 | 175142: ````` <0xE2><0x9A> `````, 129: ````` <0xBD> `````                        |
|       1575 | ````` ¿🩹? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 125: ````` <0xB9> ````` |
|       1638 | ````` ¿🫖? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 252: ````` <0x96> ````` |
|        343 | ````` ¿♥? `````          | -2.38419e-07 | 171540: ````` ♥ `````                                                            |
|       1339 | ````` ¿🤘? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 254: ````` <0x98> ````` |
|        265 | ````` ¿‼? `````          | -2.38419e-07 | 1773: ````` <0xE2><0x80> `````, 128: ````` <0xBC> `````                          |
|       1472 | ````` ¿🦟? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 261: ````` <0x9F> ````` |
|        511 | ````` ¿🌒? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 248: ````` <0x92> ````` |
|        490 | ````` ¿🈺? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 126: ````` <0xBA> ````` |
|       1158 | ````` ¿😜? `````         | -2.38419e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 258: ````` <0x9C> `````                  |
|       1193 | ````` ¿😿? `````         | -2.38419e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 131: ````` <0xBF> `````                  |
|        518 | ````` ¿🌙? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 255: ````` <0x99> ````` |
|       1495 | ````` ¿🦶? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 122: ````` <0xB6> ````` |
|       1653 | ````` ¿\U0001faf3? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 119: ````` <0xB3> ````` |
|       1376 | ````` ¿🤾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 130: ````` <0xBE> ````` |
|        773 | ````` ¿🐢? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 103: ````` <0xA2> ````` |
|       1144 | ````` ¿😎? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 244: ````` <0x8E> `````                  |
|        638 | ````` ¿🎓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 249: ````` <0x93> ````` |
|       1205 | ````` ¿🙋? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 241: ````` <0x8B> ````` |
|        886 | ````` ¿💓? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 249: ````` <0x93> `````                  |
|       1197 | ````` ¿🙃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 233: ````` <0x83> ````` |
|       1198 | ````` ¿🙄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 234: ````` <0x84> ````` |
|        913 | ````` ¿💮? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 114: ````` <0xAE> `````                  |
|       1066 | ````` ¿🕔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 250: ````` <0x94> ````` |
|        721 | ````` ¿🏫? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 112: ````` <0xAB> `````                  |
|        676 | ````` ¿🎾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 130: ````` <0xBE> ````` |
|        440 | ````` ¿🅿? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 235: ````` <0x85> `````, 131: ````` <0xBF> ````` |
|       1476 | ````` ¿🦣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 104: ````` <0xA3> ````` |
|        764 | ````` ¿🐙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 255: ````` <0x99> ````` |
|       1536 | ````` ¿🧟? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 261: ````` <0x9F> ````` |
|       1032 | ````` ¿🔦? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 107: ````` <0xA6> `````                  |
|       1359 | ````` ¿🤬? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 113: ````` <0xAC> ````` |
|        916 | ````` ¿💱? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 117: ````` <0xB1> `````                  |
|       1303 | ````` ¿🛰? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 71996: ````` <0x9B><0xB0> `````                  |
|        334 | ````` ¿♎? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 244: ````` <0x8E> `````                         |
|        795 | ````` ¿🐸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 124: ````` <0xB8> ````` |
|        827 | ````` ¿👘? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 254: ````` <0x98> `````                  |
|        646 | ````` ¿🎠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 262: ````` <0xA0> ````` |
|        726 | ````` ¿🏰? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 116: ````` <0xB0> `````                  |
|       1465 | ````` ¿🦘? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 254: ````` <0x98> ````` |
|       1101 | ````` ¿🖐? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 246: ````` <0x90> ````` |
|        322 | ````` ¿☯? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 115: ````` <0xAF> `````                         |
|        318 | ````` ¿☣? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 104: ````` <0xA3> `````                         |
|        419 | ````` ¿➰? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 116: ````` <0xB0> `````        |
|       1285 | ````` ¿🛐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 246: ````` <0x90> ````` |
|       1005 | ````` ¿🔋? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 241: ````` <0x8B> `````                  |
|       1194 | ````` ¿🙀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 230: ````` <0x80> ````` |
|       1461 | ````` ¿🦔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 250: ````` <0x94> ````` |
|       1660 | ````` ¿\U000e0067? ````` | -1.19209e-07 | 3330: ````` <0xF3><0xA0><0x81> `````, 108: ````` <0xA7> `````                    |
|       1508 | ````` ¿🧃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 233: ````` <0x83> ````` |
|        355 | ````` ¿⚙? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 255: ````` <0x99> `````                        |
|       1028 | ````` ¿🔢? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 103: ````` <0xA2> `````                  |
|       1591 | ````` ¿🪕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 251: ````` <0x95> ````` |
|       1000 | ````` ¿🔆? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 236: ````` <0x86> `````                  |
|       1012 | ````` ¿🔒? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 248: ````` <0x92> `````                  |
|        449 | ````` ¿🆘? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 254: ````` <0x98> ````` |
|        802 | ````` ¿🐿? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 131: ````` <0xBF> ````` |
|        878 | ````` ¿💋? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 241: ````` <0x8B> `````                  |
|        977 | ````` ¿📮? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 114: ````` <0xAE> `````                  |
|        578 | ````` ¿🍗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 253: ````` <0x97> ````` |
|       1604 | ````` ¿🪢? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 103: ````` <0xA2> ````` |
|        310 | ````` ¿☎? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 244: ````` <0x8E> `````                         |
|        980 | ````` ¿📱? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 117: ````` <0xB1> `````                  |
|        960 | ````` ¿📝? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 259: ````` <0x9D> `````                  |
|       1379 | ````` ¿🥁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 231: ````` <0x81> ````` |
|        588 | ````` ¿🍡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 102: ````` <0xA1> ````` |
|       1135 | ````` ¿😅? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 235: ````` <0x85> `````                  |
|       1453 | ````` ¿🦌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 242: ````` <0x8C> ````` |
|       1245 | ````` ¿🚣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 104: ````` <0xA3> ````` |
|       1052 | ````` ¿🔺? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 126: ````` <0xBA> `````                  |
|       1137 | ````` ¿😇? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 237: ````` <0x87> `````                  |
|       1055 | ````` ¿🔽? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 129: ````` <0xBD> `````                  |
|        923 | ````` ¿💸? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 124: ````` <0xB8> `````                  |
|       1130 | ````` ¿😀? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 230: ````` <0x80> `````                  |
|       1637 | ````` ¿🫕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 251: ````` <0x95> ````` |
|       1048 | ````` ¿🔶? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 122: ````` <0xB6> `````                  |
|        515 | ````` ¿🌖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 252: ````` <0x96> ````` |
|       1393 | ````` ¿🥐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 61365: ````` <0xA5><0x90> `````                  |
|        991 | ````` ¿📼? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 128: ````` <0xBC> `````                  |
|       1099 | ````` ¿🖌? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 242: ````` <0x8C> ````` |
|        302 | ````` ¿◼? `````          | -1.19209e-07 | 37357: ````` <0xE2><0x97> `````, 128: ````` <0xBC> `````                         |
|        867 | ````` ¿💀? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 230: ````` <0x80> `````                  |
|        681 | ````` ¿🏃? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 233: ````` <0x83> `````                  |
|       1611 | ````` ¿\U0001faa9? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 110: ````` <0xA9> ````` |
|        289 | ````` ¿⏰? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 116: ````` <0xB0> `````        |
|        842 | ````` ¿👧? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 108: ````` <0xA7> `````                  |
|        709 | ````` ¿🏟? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 261: ````` <0x9F> `````                  |
|       1566 | ````` ¿🧽? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 129: ````` <0xBD> ````` |
|       1033 | ````` ¿🔧? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 108: ````` <0xA7> `````                  |
|        874 | ````` ¿💇? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 237: ````` <0x87> `````                  |
|       1152 | ````` ¿😖? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 252: ````` <0x96> `````                  |
|        323 | ````` ¿☸? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 124: ````` <0xB8> `````                         |
|       1486 | ````` ¿🦭? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 263: ````` <0xAD> ````` |
|       1358 | ````` ¿🤫? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 112: ````` <0xAB> ````` |
|        673 | ````` ¿🎻? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 127: ````` <0xBB> ````` |
|        336 | ````` ¿♐? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 246: ````` <0x90> `````                         |
|        623 | ````` ¿🎄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 234: ````` <0x84> ````` |
|        812 | ````` ¿👉? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 239: ````` <0x89> `````                  |
|        961 | ````` ¿📞? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 260: ````` <0x9E> `````                  |
|       1554 | ````` ¿🧱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 117: ````` <0xB1> ````` |
|        487 | ````` ¿🈷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 123: ````` <0xB7> ````` |
|       1538 | ````` ¿🧡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 102: ````` <0xA1> ````` |
|       1444 | ````` ¿🦃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 233: ````` <0x83> ````` |
|        956 | ````` ¿📙? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 255: ````` <0x99> `````                  |
|        739 | ````` ¿🐀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 230: ````` <0x80> ````` |
|        398 | ````` ¿✔? `````          | -1.19209e-07 | 189894: ````` ✔ `````                                                            |
|       1655 | ````` ¿\U0001faf5? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 121: ````` <0xB5> ````` |
|        825 | ````` ¿👖? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 252: ````` <0x96> `````                  |
|        395 | ````` ¿✍? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 243: ````` <0x8D> `````                         |
|        979 | ````` ¿📰? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 22231: ````` <0x93><0xB0> `````                  |
|        370 | ````` ¿⛎? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 244: ````` <0x8E> `````        |
|       1555 | ````` ¿🧲? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 118: ````` <0xB2> ````` |
|       1317 | ````` ¿🟣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 104: ````` <0xA3> ````` |
|       1395 | ````` ¿🥒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 248: ````` <0x92> ````` |
|        691 | ````` ¿🏍? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 243: ````` <0x8D> `````                  |
|        509 | ````` ¿🌐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 246: ````` <0x90> ````` |
|       1394 | ````` ¿🥑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 247: ````` <0x91> ````` |
|        948 | ````` ¿📑? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 247: ````` <0x91> `````                  |
|       1540 | ````` ¿🧣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 104: ````` <0xA3> ````` |
|       1299 | ````` ¿🛥? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 106: ````` <0xA5> ````` |
|        502 | ````` ¿🌉? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 239: ````` <0x89> ````` |
|       1170 | ````` ¿😨? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 109: ````` <0xA8> `````                  |
|       1623 | ````` ¿\U0001fab8? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 124: ````` <0xB8> ````` |
|        809 | ````` ¿👆? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 236: ````` <0x86> `````                  |
|       1178 | ````` ¿😰? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 116: ````` <0xB0> `````                  |
|        561 | ````` ¿🍆? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 236: ````` <0x86> ````` |
|       1297 | ````` ¿🛣? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 104: ````` <0xA3> ````` |
|       1049 | ````` ¿🔷? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 123: ````` <0xB7> `````                  |
|       1091 | ````` ¿🕶? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 122: ````` <0xB6> ````` |
|       1449 | ````` ¿🦈? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 238: ````` <0x88> ````` |
|        274 | ````` ¿↘? `````          | -1.19209e-07 | 76876: ````` <0xE2><0x86> `````, 254: ````` <0x98> `````                         |
|       1100 | ````` ¿🖍? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 243: ````` <0x8D> ````` |
|       1073 | ````` ¿🕛? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 257: ````` <0x9B> ````` |
|        346 | ````` ¿♻? `````          | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 127: ````` <0xBB> `````                         |
|        474 | ````` ¿🇼? `````          | -1.19209e-07 | 108080: ````` 🇼 `````                                                            |
|       1492 | ````` ¿🦳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 119: ````` <0xB3> ````` |
|       1603 | ````` ¿🪡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 102: ````` <0xA1> ````` |
|       1088 | ````` ¿🕳? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 119: ````` <0xB3> ````` |
|        445 | ````` ¿🆔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 250: ````` <0x94> ````` |
|       1583 | ````` ¿🪄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 234: ````` <0x84> ````` |
|       1268 | ````` ¿🚺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 126: ````` <0xBA> ````` |
|       1459 | ````` ¿🦒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 248: ````` <0x92> ````` |
|       1027 | ````` ¿🔡? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 102: ````` <0xA1> `````                  |
|        720 | ````` ¿🏪? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 111: ````` <0xAA> `````                  |
|       1502 | ````` ¿🦽? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 129: ````` <0xBD> ````` |
|        781 | ````` ¿🐪? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 111: ````` <0xAA> ````` |
|       1534 | ````` ¿🧝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 259: ````` <0x9D> ````` |
|        534 | ````` ¿🌫? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 112: ````` <0xAB> ````` |
|       1161 | ````` ¿😟? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 261: ````` <0x9F> `````                  |
|        337 | ````` ¿♑? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 247: ````` <0x91> `````                         |
|        869 | ````` ¿💂? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 232: ````` <0x82> `````                  |
|        870 | ````` ¿💃? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 233: ````` <0x83> `````                  |
|       1163 | ````` ¿😡? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 102: ````` <0xA1> `````                  |
|       1293 | ````` ¿\U0001f6df? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 261: ````` <0x9F> ````` |
|        642 | ````` ¿🎚? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 256: ````` <0x9A> ````` |
|       1047 | ````` ¿🔵? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 121: ````` <0xB5> `````                  |
|       1258 | ````` ¿🚰? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 116: ````` <0xB0> ````` |
|       1090 | ````` ¿🕵? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 121: ````` <0xB5> ````` |
|        520 | ````` ¿🌛? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 257: ````` <0x9B> ````` |
|        888 | ````` ¿💕? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 251: ````` <0x95> `````                  |
|        325 | ````` ¿☺? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 126: ````` <0xBA> `````                         |
|        782 | ````` ¿🐫? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 112: ````` <0xAB> ````` |
|        881 | ````` ¿💎? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 244: ````` <0x8E> `````                  |
|       1531 | ````` ¿🧚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 256: ````` <0x9A> ````` |
|       1280 | ````` ¿🛋? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 241: ````` <0x8B> ````` |
|       1392 | ````` ¿🥏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 245: ````` <0x8F> ````` |
|        617 | ````` ¿🍾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 130: ````` <0xBE> ````` |
|        269 | ````` ¿ℹ? `````          | -1.19209e-07 | 27829: ````` <0xE2><0x84> `````, 125: ````` <0xB9> `````                         |
|       1177 | ````` ¿😯? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 115: ````` <0xAF> `````                  |
|        898 | ````` ¿💟? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 261: ````` <0x9F> `````                  |
|       1428 | ````` ¿🥳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 119: ````` <0xB3> ````` |
|       1174 | ````` ¿😬? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 113: ````` <0xAC> `````                  |
|        661 | ````` ¿🎯? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 115: ````` <0xAF> ````` |
|       1035 | ````` ¿🔩? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 110: ````` <0xA9> `````                  |
|       1619 | ````` ¿🪴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 120: ````` <0xB4> ````` |
|        734 | ````` ¿🏻? `````           | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 127: ````` <0xBB> `````                  |
|        583 | ````` ¿🍜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 258: ````` <0x9C> ````` |
|        654 | ````` ¿🎨? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 109: ````` <0xA8> ````` |
|       1412 | ````` ¿🥣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 104: ````` <0xA3> ````` |
|        385 | ````` ¿⛹? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 125: ````` <0xB9> `````        |
|        287 | ````` ¿⏮? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 114: ````` <0xAE> `````        |
|       1650 | ````` ¿\U0001faf0? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 116: ````` <0xB0> ````` |
|        427 | ````` ¿⬜? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 113: ````` <0xAC> `````, 258: ````` <0x9C> `````        |
|       1231 | ````` ¿🚕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 251: ````` <0x95> ````` |
|        631 | ````` ¿🎌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 242: ````` <0x8C> ````` |
|        834 | ````` ¿👟? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 261: ````` <0x9F> `````                  |
|       1589 | ````` ¿🪓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 249: ````` <0x93> ````` |
|       1434 | ````` ¿\U0001f979? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 125: ````` <0xB9> ````` |
|       1346 | ````` ¿🤟? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 261: ````` <0x9F> ````` |
|        407 | ````` ¿❌? `````         | -1.19209e-07 | 135523: ````` <0xE2><0x9D> `````, 242: ````` <0x8C> `````                        |
|        873 | ````` ¿💆? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 236: ````` <0x86> `````                  |
|       1513 | ````` ¿🧈? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 238: ````` <0x88> ````` |
|       1399 | ````` ¿🥖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 252: ````` <0x96> ````` |
|       1131 | ````` ¿😁? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 231: ````` <0x81> `````                  |
|        388 | ````` ¿✂? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 232: ````` <0x82> `````                         |
|       1560 | ````` ¿🧷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 123: ````` <0xB7> ````` |
|        931 | ````` ¿📀? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 230: ````` <0x80> `````                  |
|        504 | ````` ¿🌋? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 241: ````` <0x8B> ````` |
|        413 | ````` ¿❣? `````          | -1.19209e-07 | 135523: ````` <0xE2><0x9D> `````, 104: ````` <0xA3> `````                        |
|       1173 | ````` ¿😫? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 112: ````` <0xAB> `````                  |
|        729 | ````` ¿🏵? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 121: ````` <0xB5> `````                  |
|        724 | ````` ¿🏮? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 114: ````` <0xAE> `````                  |
|        715 | ````` ¿🏥? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 106: ````` <0xA5> `````                  |
|       1562 | ````` ¿🧹? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 125: ````` <0xB9> ````` |
|       1113 | ````` ¿🗑? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 247: ````` <0x91> ````` |
|        604 | ````` ¿🍱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 117: ````` <0xB1> ````` |
|       1134 | ````` ¿😄? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 234: ````` <0x84> `````                  |
|        563 | ````` ¿🍈? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 238: ````` <0x88> ````` |
|        904 | ````` ¿💥? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 106: ````` <0xA5> `````                  |
|       1429 | ````` ¿🥴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 120: ````` <0xB4> ````` |
|        308 | ````` ¿☃? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 233: ````` <0x83> `````                         |
|        598 | ````` ¿🍫? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 112: ````` <0xAB> ````` |
|       1470 | ````` ¿🦝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 259: ````` <0x9D> ````` |
|       1642 | ````` ¿\U0001fae0? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 262: ````` <0xA0> ````` |
|        376 | ````` ¿⛪? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 111: ````` <0xAA> `````        |
|        290 | ````` ¿⏱? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 117: ````` <0xB1> `````        |
|       1398 | ````` ¿🥕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 251: ````` <0x95> ````` |
|        763 | ````` ¿🐘? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 254: ````` <0x98> ````` |
|        707 | ````` ¿🏝? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 259: ````` <0x9D> `````                  |
|        540 | ````` ¿🌱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 117: ````` <0xB1> ````` |
|       1378 | ````` ¿🥀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 230: ````` <0x80> ````` |
|        951 | ````` ¿📔? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 250: ````` <0x94> `````                  |
|       1276 | ````` ¿🛂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 232: ````` <0x82> ````` |
|       1601 | ````` ¿🪟? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 261: ````` <0x9F> ````` |
|       1439 | ````` ¿🥾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 130: ````` <0xBE> ````` |
|        769 | ````` ¿🐞? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 260: ````` <0x9E> ````` |
|        987 | ````` ¿📸? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 124: ````` <0xB8> `````                  |
|        362 | ````` ¿⚫? `````         | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 112: ````` <0xAB> `````                        |
|        481 | ````` ¿🈯? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 115: ````` <0xAF> ````` |
|        559 | ````` ¿🍄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 234: ````` <0x84> ````` |
|        679 | ````` ¿🏁? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 231: ````` <0x81> `````                  |
|       1116 | ````` ¿🗜? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 258: ````` <0x9C> ````` |
|       1438 | ````` ¿🥽? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 129: ````` <0xBD> ````` |
|        742 | ````` ¿🐃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 233: ````` <0x83> ````` |
|       1350 | ````` ¿🤣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 104: ````` <0xA3> ````` |
|       1345 | ````` ¿🤞? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 260: ````` <0x9E> ````` |
|       1076 | ````` ¿🕞? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 260: ````` <0x9E> ````` |
|        892 | ````` ¿💙? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 255: ````` <0x99> `````                  |
|        369 | ````` ¿⛈? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 32197: ````` <0x9B><0x88> `````                         |
|       1504 | ````` ¿🦿? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 131: ````` <0xBF> ````` |
|        714 | ````` ¿🏤? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 105: ````` <0xA4> `````                  |
|       1500 | ````` ¿🦻? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 127: ````` <0xBB> ````` |
|        839 | ````` ¿👤? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 105: ````` <0xA4> `````                  |
|       1628 | ````` ¿🫂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 232: ````` <0x82> ````` |
|       1419 | ````` ¿🥪? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 111: ````` <0xAA> ````` |
|        694 | ````` ¿🏐? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 246: ````` <0x90> `````                  |
|       1051 | ````` ¿🔹? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 125: ````` <0xB9> `````                  |
|       1121 | ````` ¿🗨? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 109: ````` <0xA8> ````` |
|        891 | ````` ¿💘? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 254: ````` <0x98> `````                  |
|       1547 | ````` ¿🧪? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 111: ````` <0xAA> ````` |
|        317 | ````` ¿☢? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 103: ````` <0xA2> `````                         |
|        352 | ````` ¿⚕? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 251: ````` <0x95> `````                        |
|        284 | ````` ¿⏫? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 112: ````` <0xAB> `````        |
|       1146 | ````` ¿😐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 15468: ````` <0x98><0x90> `````                  |
|        625 | ````` ¿🎆? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 236: ````` <0x86> ````` |
|       1352 | ````` ¿🤥? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 106: ````` <0xA5> ````` |
|        680 | ````` ¿🏂? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 232: ````` <0x82> `````                  |
|       1229 | ````` ¿🚓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 249: ````` <0x93> ````` |
|        499 | ````` ¿🌆? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 236: ````` <0x86> ````` |
|        996 | ````` ¿🔂? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 232: ````` <0x82> `````                  |
|        804 | ````` ¿👁? `````          | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 231: ````` <0x81> `````                  |
|       1580 | ````` ¿🪁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 231: ````` <0x81> ````` |
|        547 | ````` ¿🌸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 124: ````` <0xB8> ````` |
|        545 | ````` ¿🌶? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 122: ````` <0xB6> ````` |
|        544 | ````` ¿🌵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 121: ````` <0xB5> ````` |
|       1651 | ````` ¿\U0001faf1? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 117: ````` <0xB1> ````` |
|       1018 | ````` ¿🔘? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 254: ````` <0x98> `````                  |
|       1263 | ````` ¿🚵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 121: ````` <0xB5> ````` |
|       1416 | ````` ¿🥧? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 108: ````` <0xA7> ````` |
|       1112 | ````` ¿🗄? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 234: ````` <0x84> ````` |
|        570 | ````` ¿🍏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 245: ````` <0x8F> ````` |
|       1519 | ````` ¿🧎? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 244: ````` <0x8E> ````` |
|       1590 | ````` ¿🪔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 250: ````` <0x94> ````` |
|       1568 | ````` ¿🧿? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 131: ````` <0xBF> ````` |
|       1259 | ````` ¿🚱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 117: ````` <0xB1> ````` |
|       1069 | ````` ¿🕗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 253: ````` <0x97> ````` |
|       1503 | ````` ¿🦾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 130: ````` <0xBE> ````` |
|        581 | ````` ¿🍚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 256: ````` <0x9A> ````` |
|       1074 | ````` ¿🕜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 258: ````` <0x9C> ````` |
|       1367 | ````` ¿🤴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 120: ````` <0xB4> ````` |
|        986 | ````` ¿📷? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 123: ````` <0xB7> `````                  |
|        847 | ````` ¿👬? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 113: ````` <0xAC> `````                  |
|       1009 | ````` ¿🔏? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 245: ````` <0x8F> `````                  |
|       1501 | ````` ¿🦼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 128: ````` <0xBC> ````` |
|       1021 | ````` ¿🔛? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 257: ````` <0x9B> `````                  |
|       1127 | ````` ¿🗽? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 129: ````` <0xBD> ````` |
|        580 | ````` ¿🍙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 255: ````` <0x99> ````` |
|       1377 | ````` ¿🤿? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 131: ````` <0xBF> ````` |
|       1454 | ````` ¿🦍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 243: ````` <0x8D> ````` |
|        843 | ````` ¿👨? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 109: ````` <0xA8> `````                  |
|        267 | ````` ¿⃣? `````           | -1.19209e-07 | 166: ````` <0xE2> `````, 233: ````` <0x83> `````, 104: ````` <0xA3> `````        |
|       1481 | ````` ¿🦨? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 109: ````` <0xA8> ````` |
|       1038 | ````` ¿🔬? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 113: ````` <0xAC> `````                  |
|        746 | ````` ¿🐇? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 237: ````` <0x87> ````` |
|        577 | ````` ¿🍖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 252: ````` <0x96> ````` |
|        522 | ````` ¿🌝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 259: ````` <0x9D> ````` |
|        666 | ````` ¿🎴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 120: ````` <0xB4> ````` |
|       1630 | ````` ¿\U0001fac4? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 234: ````` <0x84> ````` |
|        465 | ````` ¿🇳? `````          | -1.19209e-07 | 29878: ````` 🇳 `````                                                             |
|        940 | ````` ¿📉? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 239: ````` <0x89> `````                  |
|       1605 | ````` ¿🪣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 104: ````` <0xA3> ````` |
|        444 | ````` ¿🆓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 249: ````` <0x93> ````` |
|        808 | ````` ¿👅? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 235: ````` <0x85> `````                  |
|        660 | ````` ¿🎮? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 114: ````` <0xAE> ````` |
|       1599 | ````` ¿🪝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 259: ````` <0x9D> ````` |
|       1252 | ````` ¿🚪? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 111: ````` <0xAA> ````` |
|        988 | ````` ¿📹? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 125: ````` <0xB9> `````                  |
|       1608 | ````` ¿🪦? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 107: ````` <0xA6> ````` |
|       1340 | ````` ¿🤙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 255: ````` <0x99> ````` |
|       1542 | ````` ¿🧥? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 106: ````` <0xA5> ````` |
|        312 | ````` ¿☔? `````         | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 250: ````` <0x94> `````                         |
|       1581 | ````` ¿🪂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 232: ````` <0x82> ````` |
|        841 | ````` ¿👦? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 107: ````` <0xA6> `````                  |
|       1561 | ````` ¿🧸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 124: ````` <0xB8> ````` |
|        589 | ````` ¿🍢? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 103: ````` <0xA2> ````` |
|        508 | ````` ¿🌏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 245: ````` <0x8F> ````` |
|        425 | ````` ¿⬇? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 113: ````` <0xAC> `````, 237: ````` <0x87> `````        |
|        949 | ````` ¿📒? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 248: ````` <0x92> `````                  |
|       1424 | ````` ¿🥯? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 115: ````` <0xAF> ````` |
|       1665 | ````` ¿\U000e0077? ````` | -1.19209e-07 | 3330: ````` <0xF3><0xA0><0x81> `````, 123: ````` <0xB7> `````                    |
|       1287 | ````` ¿🛒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 248: ````` <0x92> ````` |
|        725 | ````` ¿🏯? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 115: ````` <0xAF> `````                  |
|       1031 | ````` ¿🔥? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 106: ````` <0xA5> `````                  |
|       1239 | ````` ¿🚝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 259: ````` <0x9D> ````` |
|       1318 | ````` ¿🟤? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 105: ````` <0xA4> ````` |
|        328 | ````` ¿♈? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 238: ````` <0x88> `````                         |
|       1341 | ````` ¿🤚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 256: ````` <0x9A> ````` |
|        364 | ````` ¿⚱? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 117: ````` <0xB1> `````                        |
|        382 | ````` ¿⛵? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 121: ````` <0xB5> `````        |
|        871 | ````` ¿💄? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 234: ````` <0x84> `````                  |
|       1606 | ````` ¿🪤? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 105: ````` <0xA4> ````` |
|       1643 | ````` ¿\U0001fae1? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 102: ````` <0xA1> ````` |
|       1539 | ````` ¿🧢? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 103: ````` <0xA2> ````` |
|       1255 | ````` ¿🚭? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 263: ````` <0xAD> ````` |
|        716 | ````` ¿🏦? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 107: ````` <0xA6> `````                  |
|        470 | ````` ¿🇸? `````          | -1.19209e-07 | 6705: ````` 🇸 `````                                                              |
|       1278 | ````` ¿🛄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 7840: ````` <0x9B><0x84> `````                   |
|        276 | ````` ¿↩? `````          | -1.19209e-07 | 76876: ````` <0xE2><0x86> `````, 110: ````` <0xA9> `````                         |
|       1269 | ````` ¿🚻? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 127: ````` <0xBB> ````` |
|       1304 | ````` ¿🛳? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 119: ````` <0xB3> ````` |
|       1102 | ````` ¿🖕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 251: ````` <0x95> ````` |
|        606 | ````` ¿🍳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 119: ````` <0xB3> ````` |
|        636 | ````` ¿🎑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 247: ````` <0x91> ````` |
|        801 | ````` ¿🐾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 130: ````` <0xBE> ````` |
|        857 | ````` ¿👶? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 122: ````` <0xB6> `````                  |
|        964 | ````` ¿📡? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 102: ````` <0xA1> `````                  |
|        877 | ````` ¿💊? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 240: ````` <0x8A> `````                  |
|       1366 | ````` ¿🤳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 119: ````` <0xB3> ````` |
|        989 | ````` ¿📺? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 126: ````` <0xBA> `````                  |
|        514 | ````` ¿🌕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 251: ````` <0x95> ````` |
|        297 | ````` ¿▪? `````          | -1.19209e-07 | 237072: ````` ▪ `````                                                            |
|       1186 | ````` ¿😸? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 124: ````` <0xB8> `````                  |
|        572 | ````` ¿🍑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 247: ````` <0x91> ````` |
|        728 | ````` ¿🏴? `````         | -1.19209e-07 | 148987: ````` 🏴 `````                                                           |
|       1405 | ````` ¿🥜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 258: ````` <0x9C> ````` |
|        648 | ````` ¿🎢? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 103: ````` <0xA2> ````` |
|        469 | ````` ¿🇷? `````          | -1.19209e-07 | 7534: ````` 🇷 `````                                                              |
|       1010 | ````` ¿🔐? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 246: ````` <0x90> `````                  |
|       1506 | ````` ¿🧁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 231: ````` <0x81> ````` |
|        494 | ````` ¿🌁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 231: ````` <0x81> ````` |
|       1592 | ````` ¿🪖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 252: ````` <0x96> ````` |
|        333 | ````` ¿♍? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 243: ````` <0x8D> `````                         |
|       1321 | ````` ¿🟧? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 108: ````` <0xA7> ````` |
|       1065 | ````` ¿🕓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 249: ````` <0x93> ````` |
|        822 | ````` ¿👓? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 249: ````` <0x93> `````                  |
|        439 | ````` ¿🅾? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 235: ````` <0x85> `````, 130: ````` <0xBE> ````` |
|        414 | ````` ¿❤? `````          | -1.19209e-07 | 135523: ````` <0xE2><0x9D> `````, 105: ````` <0xA4> `````                        |
|       1549 | ````` ¿🧬? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 113: ````` <0xAC> ````` |
|        367 | ````` ¿⛄? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 7840: ````` <0x9B><0x84> `````                          |
|       1406 | ````` ¿🥝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 259: ````` <0x9D> ````` |
|        431 | ````` ¿〽? `````         | -1.19209e-07 | 1800: ````` <0xE3><0x80> `````, 129: ````` <0xBD> `````                          |
|       1570 | ````` ¿🩱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 117: ````` <0xB1> ````` |
|        273 | ````` ¿↗? `````          | -1.19209e-07 | 76876: ````` <0xE2><0x86> `````, 253: ````` <0x97> `````                         |
|        920 | ````` ¿💵? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 121: ````` <0xB5> `````                  |
|       1244 | ````` ¿🚢? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 103: ````` <0xA2> ````` |
|        945 | ````` ¿📎? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 244: ````` <0x8E> `````                  |
|        627 | ````` ¿🎈? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 238: ````` <0x88> ````` |
|        779 | ````` ¿🐨? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 109: ````` <0xA8> ````` |
|       1308 | ````` ¿🛷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 123: ````` <0xB7> ````` |
|       1185 | ````` ¿😷? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 123: ````` <0xB7> `````                  |
|       1202 | ````` ¿🙈? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 238: ````` <0x88> ````` |
|        664 | ````` ¿🎲? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 118: ````` <0xB2> ````` |
|        315 | ````` ¿☝? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 259: ````` <0x9D> `````                         |
|        535 | ````` ¿🌬? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 113: ````` <0xAC> ````` |
|        613 | ````` ¿🍺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 126: ````` <0xBA> ````` |
|        650 | ````` ¿🎤? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 105: ````` <0xA4> ````` |
|        783 | ````` ¿🐬? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 113: ````` <0xAC> ````` |
|       1222 | ````` ¿🚌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 6617: ````` <0x9A><0x8C> `````                   |
|        455 | ````` ¿🇩? `````          | -1.19209e-07 | 66360: ````` 🇩 `````                                                             |
|       1451 | ````` ¿🦊? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 240: ````` <0x8A> ````` |
|        601 | ````` ¿🍮? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 114: ````` <0xAE> ````` |
|       1663 | ````` ¿\U000e0073? ````` | -1.19209e-07 | 69089: ````` \U000e0073 `````                                                    |
|        584 | ````` ¿🍝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 259: ````` <0x9D> ````` |
|        832 | ````` ¿👝? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 259: ````` <0x9D> `````                  |
|       1464 | ````` ¿🦗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 253: ````` <0x97> ````` |
|       1588 | ````` ¿🪒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 248: ````` <0x92> ````` |
|        752 | ````` ¿🐍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 243: ````` <0x8D> ````` |
|        668 | ````` ¿🎶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 122: ````` <0xB6> ````` |
|       1104 | ````` ¿🖤? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 105: ````` <0xA4> ````` |
|        968 | ````` ¿📥? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 106: ````` <0xA5> `````                  |
|       1578 | ````` ¿\U0001fa7c? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 128: ````` <0xBC> ````` |
|        421 | ````` ¿⤴? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 105: ````` <0xA4> `````, 120: ````` <0xB4> `````        |
|       1577 | ````` ¿\U0001fa7b? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 127: ````` <0xBB> ````` |
|       1427 | ````` ¿🥲? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 118: ````` <0xB2> ````` |
|       1369 | ````` ¿🤶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 122: ````` <0xB6> ````` |
|        837 | ````` ¿👢? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 103: ````` <0xA2> `````                  |
|        722 | ````` ¿🏬? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 113: ````` <0xAC> `````                  |
|       1496 | ````` ¿🦷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 123: ````` <0xB7> ````` |
|       1473 | ````` ¿🦠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 262: ````` <0xA0> ````` |
|        862 | ````` ¿👻? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 127: ````` <0xBB> `````                  |
|        394 | ````` ¿✌? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 242: ````` <0x8C> `````                         |
|       1024 | ````` ¿🔞? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 260: ````` <0x9E> `````                  |
|       1647 | ````` ¿\U0001fae5? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 106: ````` <0xA5> ````` |
|        275 | ````` ¿↙? `````          | -1.19209e-07 | 76876: ````` <0xE2><0x86> `````, 255: ````` <0x99> `````                         |
|       1387 | ````` ¿🥊? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 240: ````` <0x8A> ````` |
|        485 | ````` ¿🈵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 121: ````` <0xB5> ````` |
|        634 | ````` ¿🎏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 245: ````` <0x8F> ````` |
|        649 | ````` ¿🎣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 104: ````` <0xA3> ````` |
|        667 | ````` ¿🎵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 121: ````` <0xB5> ````` |
|       1523 | ````` ¿🧒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 248: ````` <0x92> ````` |
|        614 | ````` ¿🍻? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 127: ````` <0xBB> ````` |
|       1182 | ````` ¿😴? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 120: ````` <0xB4> `````                  |
|        536 | ````` ¿🌭? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 263: ````` <0xAD> ````` |
|        829 | ````` ¿👚? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 256: ````` <0x9A> `````                  |
|        342 | ````` ¿♣? `````          | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 104: ````` <0xA3> `````                         |
|        835 | ````` ¿👠? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 262: ````` <0xA0> `````                  |
|        758 | ````` ¿🐓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 249: ````` <0x93> ````` |
|        897 | ````` ¿💞? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 260: ````` <0x9E> `````                  |
|        744 | ````` ¿🐅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 235: ````` <0x85> ````` |
|        500 | ````` ¿🌇? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 237: ````` <0x87> ````` |
|       1442 | ````` ¿🦁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 231: ````` <0x81> ````` |
|       1218 | ````` ¿🚈? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 238: ````` <0x88> ````` |
|       1347 | ````` ¿🤠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 262: ````` <0xA0> ````` |
|       1271 | ````` ¿🚽? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 129: ````` <0xBD> ````` |
|       1143 | ````` ¿😍? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 243: ````` <0x8D> `````                  |
|        770 | ````` ¿🐟? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 261: ````` <0x9F> ````` |
|       1362 | ````` ¿🤯? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 115: ````` <0xAF> ````` |
|        539 | ````` ¿🌰? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 116: ````` <0xB0> ````` |
|       1098 | ````` ¿🖋? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 241: ````` <0x8B> ````` |
|       1639 | ````` ¿\U0001fad7? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 253: ````` <0x97> ````` |
|       1072 | ````` ¿🕚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 256: ````` <0x9A> ````` |
|        947 | ````` ¿📐? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 246: ````` <0x90> `````                  |
|       1126 | ````` ¿🗼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 128: ````` <0xBC> ````` |
|        453 | ````` ¿🇧? `````          | -1.19209e-07 | 90978: ````` 🇧 `````                                                             |
|        405 | ````` ¿❄? `````          | -1.19209e-07 | 135523: ````` <0xE2><0x9D> `````, 234: ````` <0x84> `````                        |
|       1636 | ````` ¿🫔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 250: ````` <0x94> ````` |
|        703 | ````` ¿🏙? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 255: ````` <0x99> `````                  |
|        533 | ````` ¿🌪? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 111: ````` <0xAA> ````` |
|        943 | ````` ¿📌? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 242: ````` <0x8C> `````                  |
|        760 | ````` ¿🐕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 251: ````` <0x95> ````` |
|        354 | ````` ¿⚗? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 253: ````` <0x97> `````                        |
|        527 | ````` ¿🌤? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 105: ````` <0xA4> ````` |
|       1083 | ````` ¿🕥? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 106: ````` <0xA5> ````` |
|       1053 | ````` ¿🔻? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 127: ````` <0xBB> `````                  |
|       1172 | ````` ¿😪? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 111: ````` <0xAA> `````                  |
|       1044 | ````` ¿🔲? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 118: ````` <0xB2> `````                  |
|       1624 | ````` ¿\U0001fab9? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 125: ````` <0xB9> ````` |
|        885 | ````` ¿💒? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 248: ````` <0x92> `````                  |
|        794 | ````` ¿🐷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 123: ````` <0xB7> ````` |
|       1122 | ````` ¿🗯? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 115: ````` <0xAF> ````` |
|        657 | ````` ¿🎫? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 112: ````` <0xAB> ````` |
|       1132 | ````` ¿😂? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 232: ````` <0x82> `````                  |
|        393 | ````` ¿✋? `````         | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 241: ````` <0x8B> `````                         |
|        313 | ````` ¿☕? `````         | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 251: ````` <0x95> `````                         |
|       1008 | ````` ¿🔎? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 244: ````` <0x8E> `````                  |
|       1155 | ````` ¿😙? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 255: ````` <0x99> `````                  |
|        687 | ````` ¿🏉? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 239: ````` <0x89> `````                  |
|        537 | ````` ¿🌮? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 114: ````` <0xAE> ````` |
|       1529 | ````` ¿🧘? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 254: ````` <0x98> ````` |
|        488 | ````` ¿🈸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 124: ````` <0xB8> ````` |
|        454 | ````` ¿🇨? `````          | -1.19209e-07 | 62600: ````` 🇨 `````                                                             |
|       1057 | ````` ¿🕊? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 240: ````` <0x8A> ````` |
|       1167 | ````` ¿😥? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 106: ````` <0xA5> `````                  |
|        363 | ````` ¿⚰? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 116: ````` <0xB0> `````                        |
|        366 | ````` ¿⚾? `````         | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 130: ````` <0xBE> `````                        |
|        975 | ````` ¿📬? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 113: ````` <0xAC> `````                  |
|       1409 | ````` ¿🥠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 262: ````` <0xA0> ````` |
|        298 | ````` ¿▫? `````          | -1.19209e-07 | 29034: ````` <0xE2><0x96> `````, 112: ````` <0xAB> `````                         |
|        696 | ````` ¿🏒? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 248: ````` <0x92> `````                  |
|       1425 | ````` ¿🥰? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 116: ````` <0xB0> ````` |
|        906 | ````` ¿💧? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 108: ````` <0xA7> `````                  |
|       1140 | ````` ¿😊? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 240: ````` <0x8A> `````                  |
|       1572 | ````` ¿🩳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 119: ````` <0xB3> ````` |
|        402 | ````` ¿✨? `````         | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 109: ````` <0xA8> `````                         |
|        919 | ````` ¿💴? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 120: ````` <0xB4> `````                  |
|       1166 | ````` ¿😤? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 105: ````` <0xA4> `````                  |
|       1421 | ````` ¿🥬? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 178448: ````` <0xA5><0xAC> `````                 |
|       1145 | ````` ¿😏? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 245: ````` <0x8F> `````                  |
|        408 | ````` ¿❎? `````         | -1.19209e-07 | 135523: ````` <0xE2><0x9D> `````, 244: ````` <0x8E> `````                        |
|        360 | ````` ¿⚧? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 108: ````` <0xA7> `````                        |
|        480 | ````` ¿🈚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 256: ````` <0x9A> ````` |
|        286 | ````` ¿⏭? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 263: ````` <0xAD> `````        |
|       1372 | ````` ¿🤹? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 125: ````` <0xB9> ````` |
|        884 | ````` ¿💑? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 247: ````` <0x91> `````                  |
|        993 | ````` ¿📿? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 131: ````` <0xBF> `````                  |
|       1348 | ````` ¿🤡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 102: ````` <0xA1> ````` |
|       1302 | ````` ¿🛬? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 113: ````` <0xAC> ````` |
|        303 | ````` ¿◽? `````         | -1.19209e-07 | 37357: ````` <0xE2><0x97> `````, 129: ````` <0xBD> `````                         |
|       1620 | ````` ¿🪵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 121: ````` <0xB5> ````` |
|        932 | ````` ¿📁? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 231: ````` <0x81> `````                  |
|        785 | ````` ¿🐮? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 114: ````` <0xAE> ````` |
|        952 | ````` ¿📕? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 251: ````` <0x95> `````                  |
|       1331 | ````` ¿🤐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 246: ````` <0x90> ````` |
|        436 | ````` ¿🃏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 233: ````` <0x83> `````, 245: ````` <0x8F> ````` |
|       1490 | ````` ¿🦱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 117: ````` <0xB1> ````` |
|        430 | ````` ¿〰? `````         | -1.19209e-07 | 1800: ````` <0xE3><0x80> `````, 116: ````` <0xB0> `````                          |
|       1223 | ````` ¿🚍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 243: ````` <0x8D> ````` |
|        982 | ````` ¿📳? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 119: ````` <0xB3> `````                  |
|        955 | ````` ¿📘? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 254: ````` <0x98> `````                  |
|        341 | ````` ¿♠? `````          | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 262: ````` <0xA0> `````                         |
|       1309 | ````` ¿🛸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 124: ````` <0xB8> ````` |
|       1313 | ````` ¿🛼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 128: ````` <0xBC> ````` |
|        772 | ````` ¿🐡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 102: ````` <0xA1> ````` |
|       1664 | ````` ¿\U000e0074? ````` | -1.19209e-07 | 202195: ````` \U000e0074 `````                                                   |
|        796 | ````` ¿🐹? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 125: ````` <0xB9> ````` |
|        281 | ````` ¿⏏? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 245: ````` <0x8F> `````        |
|        670 | ````` ¿🎸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 124: ````` <0xB8> ````` |
|        351 | ````` ¿⚔? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 250: ````` <0x94> `````                        |
|       1039 | ````` ¿🔭? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 263: ````` <0xAD> `````                  |
|        860 | ````` ¿👹? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 125: ````` <0xB9> `````                  |
|       1418 | ````` ¿🥩? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 110: ````` <0xA9> ````` |
|       1666 | ````` ¿\U000e007f? ````` | -1.19209e-07 | 60446: ````` \U000e007f `````                                                    |
|       1512 | ````` ¿🧇? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 237: ````` <0x87> ````` |
|       1063 | ````` ¿🕑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 247: ````` <0x91> ````` |
|       1059 | ````` ¿🕌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 12443: ````` <0x95><0x8C> `````                  |
|        997 | ````` ¿🔃? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 233: ````` <0x83> `````                  |
|       1256 | ````` ¿🚮? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 114: ````` <0xAE> ````` |
|        609 | ````` ¿🍶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 122: ````` <0xB6> ````` |
|       1187 | ````` ¿😹? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 125: ````` <0xB9> `````                  |
|       1325 | ````` ¿🟫? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 112: ````` <0xAB> ````` |
|        391 | ````` ¿✉? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 239: ````` <0x89> `````                         |
|       1483 | ````` ¿🦪? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 111: ````` <0xAA> ````` |
|       1382 | ````` ¿🥄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 234: ````` <0x84> ````` |
|        858 | ````` ¿👷? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 123: ````` <0xB7> `````                  |
|       1334 | ````` ¿🤓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 249: ````` <0x93> ````` |
|       1462 | ````` ¿🦕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 251: ````` <0x95> ````` |
|        387 | ````` ¿⛽? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 129: ````` <0xBD> `````        |
|       1385 | ````` ¿🥈? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 238: ````` <0x88> ````` |
|        974 | ````` ¿📫? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 112: ````` <0xAB> `````                  |
|        699 | ````` ¿🏕? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 251: ````` <0x95> `````                  |
|       1233 | ````` ¿🚗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 253: ````` <0x97> ````` |
|        555 | ````` ¿🍀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 230: ````` <0x80> ````` |
|       1213 | ````` ¿🚃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 233: ````` <0x83> ````` |
|        329 | ````` ¿♉? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 239: ````` <0x89> `````                         |
|       1355 | ````` ¿🤨? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 109: ````` <0xA8> ````` |
|        507 | ````` ¿🌎? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 244: ````` <0x8E> ````` |
|       1153 | ````` ¿😗? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 253: ````` <0x97> `````                  |
|        477 | ````` ¿🇿? `````          | -1.19209e-07 | 42240: ````` 🇿 `````                                                             |
|        853 | ````` ¿👲? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 118: ````` <0xB2> `````                  |
|        665 | ````` ¿🎳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 119: ````` <0xB3> ````` |
|       1283 | ````` ¿🛎? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 244: ````` <0x8E> ````` |
|       1582 | ````` ¿🪃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 233: ````` <0x83> ````` |
|       1626 | ````` ¿🫀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 230: ````` <0x80> ````` |
|       1234 | ````` ¿🚘? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 254: ````` <0x98> ````` |
|       1092 | ````` ¿🕷? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 123: ````` <0xB7> ````` |
|       1482 | ````` ¿🦩? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 110: ````` <0xA9> ````` |
|        629 | ````` ¿🎊? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 240: ````` <0x8A> ````` |
|       1509 | ````` ¿🧄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 234: ````` <0x84> ````` |
|        655 | ````` ¿🎩? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 110: ````` <0xA9> ````` |
|        548 | ````` ¿🌹? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 125: ````` <0xB9> ````` |
|       1452 | ````` ¿🦋? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 241: ````` <0x8B> ````` |
|       1041 | ````` ¿🔯? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 115: ````` <0xAF> `````                  |
|        717 | ````` ¿🏧? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 108: ````` <0xA7> `````                  |
|        880 | ````` ¿💍? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 243: ````` <0x8D> `````                  |
|       1595 | ````` ¿🪙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 255: ````` <0x99> ````` |
|        457 | ````` ¿🇫? `````          | -1.19209e-07 | 106104: ````` 🇫 `````                                                            |
|        824 | ````` ¿👕? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 251: ````` <0x95> `````                  |
|        688 | ````` ¿🏊? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 240: ````` <0x8A> `````                  |
|        377 | ````` ¿⛰? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 71996: ````` <0x9B><0xB0> `````                         |
|        552 | ````` ¿🌽? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 129: ````` <0xBD> ````` |
|        866 | ````` ¿👿? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 131: ````` <0xBF> `````                  |
|        478 | ````` ¿🈁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 231: ````` <0x81> ````` |
|        959 | ````` ¿📜? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 258: ````` <0x9C> `````                  |
|       1468 | ````` ¿🦛? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 257: ````` <0x9B> ````` |
|       1201 | ````` ¿🙇? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 237: ````` <0x87> ````` |
|       1176 | ````` ¿😮? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 114: ````` <0xAE> `````                  |
|       1573 | ````` ¿🩴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 120: ````` <0xB4> ````` |
|       1061 | ````` ¿🕎? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 244: ````` <0x8E> ````` |
|        872 | ````` ¿💅? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 235: ````` <0x85> `````                  |
|        378 | ````` ¿⛱? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 117: ````` <0xB1> `````        |
|       1289 | ````` ¿🛖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 252: ````` <0x96> ````` |
|        907 | ````` ¿💨? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 109: ````` <0xA8> `````                  |
|        593 | ````` ¿🍦? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 107: ````` <0xA6> ````` |
|        984 | ````` ¿📵? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 121: ````` <0xB5> `````                  |
|        464 | ````` ¿🇲? `````          | -1.19209e-07 | 62579: ````` 🇲 `````                                                             |
|        928 | ````` ¿💽? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 129: ````` <0xBD> `````                  |
|        512 | ````` ¿🌓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 249: ````` <0x93> ````` |
|       1587 | ````` ¿🪑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 247: ````` <0x91> ````` |
|        737 | ````` ¿🏾? `````           | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 130: ````` <0xBE> `````                  |
|       1448 | ````` ¿🦇? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 237: ````` <0x87> ````` |
|       1136 | ````` ¿😆? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 236: ````` <0x86> `````                  |
|        864 | ````` ¿👽? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 129: ````` <0xBD> `````                  |
|        348 | ````` ¿♿? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 131: ````` <0xBF> `````                         |
|        567 | ````` ¿🍌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 242: ````` <0x8C> ````` |
|        985 | ````` ¿📶? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 122: ````` <0xB6> `````                  |
|       1294 | ````` ¿🛠? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 262: ````` <0xA0> ````` |
|       1314 | ````` ¿🟠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 262: ````` <0xA0> ````` |
|       1248 | ````` ¿🚦? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 107: ````` <0xA6> ````` |
|       1488 | ````` ¿🦯? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 115: ````` <0xAF> ````` |
|        708 | ````` ¿🏞? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 260: ````` <0x9E> `````                  |
|        332 | ````` ¿♌? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 242: ````` <0x8C> `````                         |
|        790 | ````` ¿🐳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 119: ````` <0xB3> ````` |
|       1181 | ````` ¿😳? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 119: ````` <0xB3> `````                  |
|        397 | ````` ¿✒? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 248: ````` <0x92> `````                         |
|       1364 | ````` ¿🤱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 117: ````` <0xB1> ````` |
|       1123 | ````` ¿🗳? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 119: ````` <0xB3> ````` |
|        848 | ````` ¿👭? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 263: ````` <0xAD> `````                  |
|       1484 | ````` ¿🦫? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 112: ````` <0xAB> ````` |
|        599 | ````` ¿🍬? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 113: ````` <0xAC> ````` |
|       1189 | ````` ¿😻? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 127: ````` <0xBB> `````                  |
|       1209 | ````` ¿🙏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 245: ````` <0x8F> ````` |
|       1466 | ````` ¿🦙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 255: ````` <0x99> ````` |
|        815 | ````` ¿👌? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 242: ````` <0x8C> `````                  |
|       1266 | ````` ¿🚸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 124: ````` <0xB8> ````` |
|       1610 | ````` ¿🪨? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 109: ````` <0xA8> ````` |
|       1227 | ````` ¿🚑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 247: ````` <0x91> ````` |
|       1458 | ````` ¿🦑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 247: ````` <0x91> ````` |
|       1437 | ````` ¿🥼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 128: ````` <0xBC> ````` |
|        605 | ````` ¿🍲? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 118: ````` <0xB2> ````` |
|       1037 | ````` ¿🔫? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 112: ````` <0xAB> `````                  |
|        611 | ````` ¿🍸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 124: ````` <0xB8> ````` |
|       1050 | ````` ¿🔸? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 124: ````` <0xB8> `````                  |
|       1659 | ````` ¿\U000e0065? ````` | -1.19209e-07 | 3330: ````` <0xF3><0xA0><0x81> `````, 106: ````` <0xA5> `````                    |
|       1593 | ````` ¿🪗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 253: ````` <0x97> ````` |
|       1381 | ````` ¿🥃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 233: ````` <0x83> ````` |
|        546 | ````` ¿🌷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 123: ````` <0xB7> ````` |
|       1375 | ````` ¿🤽? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 129: ````` <0xBD> ````` |
|        525 | ````` ¿🌠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 262: ````` <0xA0> ````` |
|        381 | ````` ¿⛴? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 120: ````` <0xB4> `````        |
|        798 | ````` ¿🐻? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 127: ````` <0xBB> ````` |
|        896 | ````` ¿💝? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 259: ````` <0x9D> `````                  |
|        754 | ````` ¿🐏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 245: ````` <0x8F> ````` |
|        633 | ````` ¿🎎? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 244: ````` <0x8E> ````` |
|        291 | ````` ¿⏲? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 118: ````` <0xB2> `````        |
|        723 | ````` ¿🏭? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 263: ````` <0xAD> `````                  |
|        762 | ````` ¿🐗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 253: ````` <0x97> ````` |
|       1410 | ````` ¿🥡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 102: ````` <0xA1> ````` |
|        748 | ````` ¿🐉? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 239: ````` <0x89> ````` |
|        597 | ````` ¿🍪? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 111: ````` <0xAA> ````` |
|       1516 | ````` ¿🧋? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 241: ````` <0x8B> ````` |
|        443 | ````` ¿🆒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 9519: ````` <0x86><0x92> `````                   |
|        799 | ````` ¿🐼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 128: ````` <0xBC> ````` |
|       1649 | ````` ¿\U0001fae7? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 108: ````` <0xA7> ````` |
|        319 | ````` ¿☦? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 107: ````` <0xA6> `````                         |
|        929 | ````` ¿💾? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 130: ````` <0xBE> `````                  |
|        992 | ````` ¿📽? `````          | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 129: ````` <0xBD> `````                  |
|       1142 | ````` ¿😌? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 242: ````` <0x8C> `````                  |
|        957 | ````` ¿📚? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 256: ````` <0x9A> `````                  |
|       1594 | ````` ¿🪘? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 254: ````` <0x98> ````` |
|       1211 | ````` ¿🚁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 231: ````` <0x81> ````` |
|        789 | ````` ¿🐲? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 118: ````` <0xB2> ````` |
|        411 | ````` ¿❕? `````         | -1.19209e-07 | 135523: ````` <0xE2><0x9D> `````, 251: ````` <0x95> `````                        |
|        788 | ````` ¿🐱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 117: ````` <0xB1> ````` |
|       1275 | ````` ¿🛁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 231: ````` <0x81> ````` |
|        856 | ````` ¿👵? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 121: ````` <0xB5> `````                  |
|        693 | ````` ¿🏏? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 245: ````` <0x8F> `````                  |
|        706 | ````` ¿🏜? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 258: ````` <0x9C> `````                  |
|       1344 | ````` ¿🤝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 259: ````` <0x9D> ````` |
|        908 | ````` ¿💩? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 110: ````` <0xA9> `````                  |
|       1199 | ````` ¿🙅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 235: ````` <0x85> ````` |
|       1567 | ````` ¿🧾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 130: ````` <0xBE> ````` |
|        922 | ````` ¿💷? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 123: ````` <0xB7> `````                  |
|        658 | ````` ¿🎬? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 113: ````` <0xAC> ````` |
|       1241 | ````` ¿🚟? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 261: ````` <0x9F> ````` |
|        531 | ````` ¿🌨? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 109: ````` <0xA8> ````` |
|       1169 | ````` ¿😧? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 108: ````` <0xA7> `````                  |
|       1432 | ````` ¿🥷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 123: ````` <0xB7> ````` |
|       1489 | ````` ¿🦰? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 116: ````` <0xB0> ````` |
|       1507 | ````` ¿🧂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 232: ````` <0x82> ````` |
|       1457 | ````` ¿🦐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 246: ````` <0x90> ````` |
|       1648 | ````` ¿\U0001fae6? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 107: ````` <0xA6> ````` |
|        461 | ````` ¿🇯? `````          | -1.19209e-07 | 169789: ````` 🇯 `````                                                            |
|       1338 | ````` ¿🤗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 253: ````` <0x97> ````` |
|        771 | ````` ¿🐠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 262: ````` <0xA0> ````` |
|        849 | ````` ¿👮? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 114: ````` <0xAE> `````                  |
|       1374 | ````` ¿🤼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 139814: ````` <0xA4><0xBC> `````                 |
|        417 | ````` ¿➗? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 253: ````` <0x97> `````        |
|        901 | ````` ¿💢? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 103: ````` <0xA2> `````                  |
|        767 | ````` ¿🐜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 258: ````` <0x9C> ````` |
|        368 | ````` ¿⛅? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 235: ````` <0x85> `````        |
|        389 | ````` ¿✅? `````         | -1.19209e-07 | 214871: ````` ✅ `````                                                           |
|       1056 | ````` ¿🕉? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 239: ````` <0x89> ````` |
|       1559 | ````` ¿🧶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 122: ````` <0xB6> ````` |
|       1400 | ````` ¿🥗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 253: ````` <0x97> ````` |
|       1096 | ````` ¿🖇? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 237: ````` <0x87> ````` |
|       1168 | ````` ¿😦? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 107: ````` <0xA6> `````                  |
|        749 | ````` ¿🐊? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 240: ````` <0x8A> ````` |
|        787 | ````` ¿🐰? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 116: ````` <0xB0> ````` |
|        608 | ````` ¿🍵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 121: ````` <0xB5> ````` |
|        792 | ````` ¿🐵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 121: ````` <0xB5> ````` |
|       1635 | ````` ¿🫓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 171080: ````` <0xAB><0x93> `````                 |
|       1251 | ````` ¿🚩? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 110: ````` <0xA9> ````` |
|        283 | ````` ¿⏪? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 111: ````` <0xAA> `````        |
|       1281 | ````` ¿🛌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 242: ````` <0x8C> ````` |
|       1300 | ````` ¿🛩? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 110: ````` <0xA9> ````` |
|        969 | ````` ¿📦? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 107: ````` <0xA6> `````                  |
|        899 | ````` ¿💠? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 262: ````` <0xA0> `````                  |
|        560 | ````` ¿🍅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 235: ````` <0x85> ````` |
|       1422 | ````` ¿🥭? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 263: ````` <0xAD> ````` |
|       1315 | ````` ¿🟡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 102: ````` <0xA1> ````` |
|       1497 | ````` ¿🦸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 124: ````` <0xB8> ````` |
|       1150 | ````` ¿😔? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 250: ````` <0x94> `````                  |
|       1446 | ````` ¿🦅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 235: ````` <0x85> ````` |
|        416 | ````` ¿➖? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 252: ````` <0x96> `````        |
|        451 | ````` ¿🆚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 256: ````` <0x9A> ````` |
|        456 | ````` ¿🇪? `````          | -1.19209e-07 | 8548: ````` 🇪 `````                                                              |
|        592 | ````` ¿🍥? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 106: ````` <0xA5> ````` |
|       1103 | ````` ¿🖖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 252: ````` <0x96> ````` |
|        761 | ````` ¿🐖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 252: ````` <0x96> ````` |
|        730 | ````` ¿🏷? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 123: ````` <0xB7> `````                  |
|        401 | ````` ¿✡? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 102: ````` <0xA1> `````                         |
|        995 | ````` ¿🔁? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 231: ````` <0x81> `````                  |
|        840 | ````` ¿👥? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 106: ````` <0xA5> `````                  |
|        671 | ````` ¿🎹? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 125: ````` <0xB9> ````` |
|        689 | ````` ¿🏋? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 241: ````` <0x8B> `````                  |
|       1064 | ````` ¿🕒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 248: ````` <0x92> ````` |
|        331 | ````` ¿♋? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 241: ````` <0x8B> `````                         |
|        917 | ````` ¿💲? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 118: ````` <0xB2> `````                  |
|        576 | ````` ¿🍕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 251: ````` <0x95> ````` |
|       1388 | ````` ¿🥋? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 241: ````` <0x8B> ````` |
|        468 | ````` ¿🇶? `````          | -1.19209e-07 | 144576: ````` 🇶 `````                                                            |
|       1565 | ````` ¿🧼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 128: ````` <0xBC> ````` |
|        505 | ````` ¿🌌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 242: ````` <0x8C> ````` |
|        309 | ````` ¿☄? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 234: ````` <0x84> `````                         |
|       1226 | ````` ¿🚐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 246: ````` <0x90> ````` |
|       1148 | ````` ¿😒? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 248: ````` <0x92> `````                  |
|       1029 | ````` ¿🔣? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 104: ````` <0xA3> `````                  |
|       1613 | ````` ¿\U0001faab? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 112: ````` <0xAB> ````` |
|        879 | ````` ¿💌? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 242: ````` <0x8C> `````                  |
|        579 | ````` ¿🍘? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 254: ````` <0x98> ````` |
|       1609 | ````` ¿🪧? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 108: ````` <0xA7> ````` |
|       1607 | ````` ¿🪥? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 106: ````` <0xA5> ````` |
|        713 | ````` ¿🏣? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 104: ````` <0xA3> `````                  |
|       1106 | ````` ¿🖨? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 109: ````` <0xA8> ````` |
|        731 | ````` ¿🏸? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 124: ````` <0xB8> `````                  |
|       1086 | ````` ¿🕯? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 115: ````` <0xAF> ````` |
|        621 | ````` ¿🎂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 232: ````` <0x82> ````` |
|        777 | ````` ¿🐦? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 107: ````` <0xA6> ````` |
|        306 | ````` ¿☁? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 231: ````` <0x81> `````                         |
|        978 | ````` ¿📯? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 115: ````` <0xAF> `````                  |
|        700 | ````` ¿🏖? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 252: ````` <0x96> `````                  |
|        711 | ````` ¿🏡? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 102: ````` <0xA1> `````                  |
|        462 | ````` ¿🇰? `````          | -1.19209e-07 | 30269: ````` 🇰 `````                                                             |
|       1602 | ````` ¿🪠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 262: ````` <0xA0> ````` |
|        831 | ````` ¿👜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 11524: ````` <0x91><0x9C> `````                  |
|        349 | ````` ¿⚒? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 248: ````` <0x92> `````                        |
|        852 | ````` ¿👱? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 117: ````` <0xB1> `````                  |
|       1295 | ````` ¿🛡? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 102: ````` <0xA1> ````` |
|        918 | ````` ¿💳? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 119: ````` <0xB3> `````                  |
|        607 | ````` ¿🍴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 120: ````` <0xB4> ````` |
|        685 | ````` ¿🏇? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 237: ````` <0x87> `````                  |
|       1450 | ````` ¿🦉? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 239: ````` <0x89> ````` |
|        967 | ````` ¿📤? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 105: ````` <0xA4> `````                  |
|       1020 | ````` ¿🔚? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 256: ````` <0x9A> `````                  |
|        976 | ````` ¿📭? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 263: ````` <0xAD> `````                  |
|       1467 | ````` ¿🦚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 256: ````` <0x9A> ````` |
|        523 | ````` ¿🌞? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 260: ````` <0x9E> ````` |
|       1656 | ````` ¿\U0001faf6? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 122: ````` <0xB6> ````` |
|       1045 | ````` ¿🔳? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 119: ````` <0xB3> `````                  |
|        383 | ````` ¿⛷? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 123: ````` <0xB7> `````        |
|       1337 | ````` ¿🤖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 252: ````` <0x96> ````` |
|        780 | ````` ¿🐩? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 110: ````` <0xA9> ````` |
|        846 | ````` ¿👫? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 112: ````` <0xAB> `````                  |
|       1025 | ````` ¿🔟? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 261: ````` <0x9F> `````                  |
|        486 | ````` ¿🈶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 122: ````` <0xB6> ````` |
|        833 | ````` ¿👞? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 260: ````` <0x9E> `````                  |
|       1320 | ````` ¿🟦? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 107: ````` <0xA6> ````` |
|        380 | ````` ¿⛳? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 119: ````` <0xB3> `````        |
|       1290 | ````` ¿🛗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 253: ````` <0x97> ````` |
|        936 | ````` ¿📅? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 235: ````` <0x85> `````                  |
|       1311 | ````` ¿🛺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 126: ````` <0xBA> ````` |
|        863 | ````` ¿👼? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 128: ````` <0xBC> `````                  |
|        926 | ````` ¿💻? `````         | -1.19209e-07 | 251116: ````` 💻 `````                                                           |
|       1617 | ````` ¿🪲? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 118: ````` <0xB2> ````` |
|        900 | ````` ¿💡? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 102: ````` <0xA1> `````                  |
|       1548 | ````` ¿🧫? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 112: ````` <0xAB> ````` |
|       1230 | ````` ¿🚔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 250: ````` <0x94> ````` |
|        859 | ````` ¿👸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 44125: ````` <0x91><0xB8> `````                  |
|       1391 | ````` ¿🥎? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 244: ````` <0x8E> ````` |
|       1111 | ````` ¿🗃? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 233: ````` <0x83> ````` |
|        669 | ````` ¿🎷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 123: ````` <0xB7> ````` |
|       1515 | ````` ¿🧊? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 240: ````` <0x8A> ````` |
|        285 | ````` ¿⏬? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 113: ````` <0xAC> `````        |
|        768 | ````` ¿🐝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 259: ````` <0x9D> ````` |
|        823 | ````` ¿👔? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 250: ````` <0x94> `````                  |
|        759 | ````` ¿🐔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 250: ````` <0x94> ````` |
|        855 | ````` ¿👴? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 120: ````` <0xB4> `````                  |
|        373 | ````` ¿⛓? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 249: ````` <0x93> `````        |
|        893 | ````` ¿💚? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 256: ````` <0x9A> `````                  |
|        390 | ````` ¿✈? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 238: ````` <0x88> `````                         |
|        895 | ````` ¿💜? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 258: ````` <0x9C> `````                  |
|       1162 | ````` ¿😠? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 262: ````` <0xA0> `````                  |
|       1165 | ````` ¿😣? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 104: ````` <0xA3> `````                  |
|        432 | ````` ¿㊗? `````         | -1.19209e-07 | 167: ````` <0xE3> `````, 240: ````` <0x8A> `````, 253: ````` <0x97> `````        |
|        883 | ````` ¿💐? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 246: ````` <0x90> `````                  |
|       1584 | ````` ¿🪅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 235: ````` <0x85> ````` |
|       1537 | ````` ¿🧠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 262: ````` <0xA0> ````` |
|       1156 | ````` ¿😚? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 256: ````` <0x9A> `````                  |
|       1060 | ````` ¿🕍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 243: ````` <0x8D> ````` |
|       1456 | ````` ¿🦏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 245: ````` <0x8F> ````` |
|       1062 | ````` ¿🕐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 246: ````` <0x90> ````` |
|       1192 | ````` ¿😾? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 130: ````` <0xBE> `````                  |
|       1641 | ````` ¿\U0001fad9? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 255: ````` <0x99> ````` |
|       1200 | ````` ¿🙆? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 236: ````` <0x86> ````` |
|        340 | ````` ¿♟? `````          | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 261: ````` <0x9F> `````                         |
|        483 | ````` ¿🈳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 119: ````` <0xB3> ````` |
|        710 | ````` ¿🏠? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 262: ````` <0xA0> `````                  |
|       1154 | ````` ¿😘? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 254: ````` <0x98> `````                  |
|       1078 | ````` ¿🕠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 262: ````` <0xA0> ````` |
|       1435 | ````` ¿🥺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 126: ````` <0xBA> ````` |
|       1212 | ````` ¿🚂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 232: ````` <0x82> ````` |
|       1349 | ````` ¿🤢? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 103: ````` <0xA2> ````` |
|        357 | ````` ¿⚜? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 258: ````` <0x9C> `````                        |
|        755 | ````` ¿🐐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 246: ````` <0x90> ````` |
|       1224 | ````` ¿🚎? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 244: ````` <0x8E> ````` |
|        426 | ````` ¿⬛? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 113: ````` <0xAC> `````, 257: ````` <0x9B> `````        |
|        690 | ````` ¿🏌? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 242: ````` <0x8C> `````                  |
|       1533 | ````` ¿🧜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 258: ````` <0x9C> ````` |
|       1383 | ````` ¿🥅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 235: ````` <0x85> ````` |
|        272 | ````` ¿↖? `````          | -1.19209e-07 | 76876: ````` <0xE2><0x86> `````, 252: ````` <0x96> `````                         |
|       1316 | ````` ¿🟢? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 103: ````` <0xA2> ````` |
|        384 | ````` ¿⛸? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 124: ````` <0xB8> `````        |
|       1272 | ````` ¿🚾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 130: ````` <0xBE> ````` |
|        678 | ````` ¿🏀? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 230: ````` <0x80> `````                  |
|        909 | ````` ¿💪? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 111: ````` <0xAA> `````                  |
|        418 | ````` ¿➡? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 102: ````` <0xA1> `````        |
|        476 | ````` ¿🇾? `````          | -1.19209e-07 | 100210: ````` 🇾 `````                                                            |
|       1335 | ````` ¿🤔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 250: ````` <0x94> ````` |
|        819 | ````` ¿👐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 11948: ````` <0x91><0x90> `````                  |
|        854 | ````` ¿👳? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 119: ````` <0xB3> `````                  |
|       1171 | ````` ¿😩? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 110: ````` <0xA9> `````                  |
|        942 | ````` ¿📋? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 241: ````` <0x8B> `````                  |
|       1124 | ````` ¿🗺? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 126: ````` <0xBA> ````` |
|        805 | ````` ¿👂? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 232: ````` <0x82> `````                  |
|       1237 | ````` ¿🚛? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 257: ````` <0x9B> ````` |
|       1077 | ````` ¿🕟? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 261: ````` <0x9F> ````` |
|        321 | ````` ¿☮? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 114: ````` <0xAE> `````                         |
|        479 | ````` ¿🈂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 232: ````` <0x82> ````` |
|       1612 | ````` ¿\U0001faaa? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 111: ````` <0xAA> ````` |
|       1007 | ````` ¿🔍? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 243: ````` <0x8D> `````                  |
|        635 | ````` ¿🎐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 246: ````` <0x90> ````` |
|       1614 | ````` ¿\U0001faac? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 113: ````` <0xAC> ````` |
|        557 | ````` ¿🍂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 232: ````` <0x82> ````` |
|       1282 | ````` ¿🛍? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 243: ````` <0x8D> ````` |
|       1510 | ````` ¿🧅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 235: ````` <0x85> ````` |
|       1380 | ````` ¿🥂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 232: ````` <0x82> ````` |
|        937 | ````` ¿📆? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 236: ````` <0x86> `````                  |
|       1210 | ````` ¿🚀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 230: ````` <0x80> ````` |
|       1247 | ````` ¿🚥? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 106: ````` <0xA5> ````` |
|        280 | ````` ¿⌨? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 242: ````` <0x8C> `````, 109: ````` <0xA8> `````        |
|       1265 | ````` ¿🚷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 123: ````` <0xB7> ````` |
|        656 | ````` ¿🎪? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 111: ````` <0xAA> ````` |
|        492 | ````` ¿🉑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 239: ````` <0x89> `````, 247: ````` <0x91> ````` |
|        562 | ````` ¿🍇? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 237: ````` <0x87> ````` |
|        954 | ````` ¿📗? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 253: ````` <0x97> `````                  |
|        590 | ````` ¿🍣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 104: ````` <0xA3> ````` |
|       1326 | ````` ¿\U0001f7f0? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 116: ````` <0xB0> ````` |
|       1640 | ````` ¿\U0001fad8? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 254: ````` <0x98> ````` |
|        946 | ````` ¿📏? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 245: ````` <0x8F> `````                  |
|        882 | ````` ¿💏? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 245: ````` <0x8F> `````                  |
|        747 | ````` ¿🐈? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 238: ````` <0x88> ````` |
|       1368 | ````` ¿🤵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 121: ````` <0xB5> ````` |
|        459 | ````` ¿🇭? `````          | -1.19209e-07 | 39476: ````` 🇭 `````                                                             |
|       1487 | ````` ¿🦮? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 114: ````` <0xAE> ````` |
|       1463 | ````` ¿🦖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 252: ````` <0x96> ````` |
|       1526 | ````` ¿🧕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 251: ````` <0x95> ````` |
|        778 | ````` ¿🐧? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 108: ````` <0xA7> ````` |
|       1312 | ````` ¿🛻? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 127: ````` <0xBB> ````` |
|       1254 | ````` ¿🚬? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 113: ````` <0xAC> ````` |
|       1262 | ````` ¿🚴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 120: ````` <0xB4> ````` |
|       1332 | ````` ¿🤑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 6605: ````` <0xA4><0x91> `````                   |
|        311 | ````` ¿☑? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 247: ````` <0x91> `````                         |
|       1003 | ````` ¿🔉? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 239: ````` <0x89> `````                  |
|        718 | ````` ¿🏨? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 109: ````` <0xA8> `````                  |
|       1447 | ````` ¿🦆? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 236: ````` <0x86> ````` |
|       1079 | ````` ¿🕡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 102: ````` <0xA1> ````` |
|       1546 | ````` ¿🧩? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 110: ````` <0xA9> ````` |
|       1097 | ````` ¿🖊? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 240: ````` <0x8A> ````` |
|       1389 | ````` ¿🥌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 242: ````` <0x8C> ````` |
|       1521 | ````` ¿🧐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 246: ````` <0x90> ````` |
|       1291 | ````` ¿\U0001f6dd? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 259: ````` <0x9D> ````` |
|       1553 | ````` ¿🧰? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 116: ````` <0xB0> ````` |
|       1360 | ````` ¿🤭? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 263: ````` <0xAD> ````` |
|       1238 | ````` ¿🚜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 258: ````` <0x9C> ````` |
|       1107 | ````` ¿🖱? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 117: ````` <0xB1> ````` |
|        350 | ````` ¿⚓? `````         | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 249: ````` <0x93> `````                        |
|       1129 | ````` ¿🗿? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 131: ````` <0xBF> ````` |
|        740 | ````` ¿🐁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 245332: ````` <0x90><0x81> `````                 |
|        698 | ````` ¿🏔? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 250: ````` <0x94> `````                  |
|       1277 | ````` ¿🛃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 233: ````` <0x83> ````` |
|       1196 | ````` ¿🙂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 232: ````` <0x82> ````` |
|       1206 | ````` ¿🙌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 242: ````` <0x8C> ````` |
|       1087 | ````` ¿🕰? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 116: ````` <0xB0> ````` |
|       1284 | ````` ¿🛏? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 245: ````` <0x8F> ````` |
|       1530 | ````` ¿🧙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 255: ````` <0x99> ````` |
|       1240 | ````` ¿🚞? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 260: ````` <0x9E> ````` |
|       1260 | ````` ¿🚲? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 118: ````` <0xB2> ````` |
|       1353 | ````` ¿🤦? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 107: ````` <0xA6> ````` |
|        624 | ````` ¿🎅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 235: ````` <0x85> ````` |
|        602 | ````` ¿🍯? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 115: ````` <0xAF> ````` |
|       1514 | ````` ¿🧉? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 239: ````` <0x89> ````` |
|       1480 | ````` ¿🦧? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 108: ````` <0xA7> ````` |
|        571 | ````` ¿🍐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 246: ````` <0x90> ````` |
|       1228 | ````` ¿🚒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 248: ````` <0x92> ````` |
|       1036 | ````` ¿🔪? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 111: ````` <0xAA> `````                  |
|        620 | ````` ¿🎁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 231: ````` <0x81> ````` |
|        817 | ````` ¿👎? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 244: ````` <0x8E> `````                  |
|        994 | ````` ¿🔀? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 230: ````` <0x80> `````                  |
|        353 | ````` ¿⚖? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 252: ````` <0x96> `````                        |
|        838 | ````` ¿👣? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 104: ````` <0xA3> `````                  |
|        324 | ````` ¿☹? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 125: ````` <0xB9> `````                         |
|       1413 | ````` ¿🥤? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 105: ````` <0xA4> ````` |
|       1190 | ````` ¿😼? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 128: ````` <0xBC> `````                  |
|        756 | ````` ¿🐑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 247: ````` <0x91> ````` |
|        774 | ````` ¿🐣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 104: ````` <0xA3> ````` |
|        784 | ````` ¿🐭? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 263: ````` <0xAD> ````` |
|        603 | ````` ¿🍰? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 116: ````` <0xB0> ````` |
|        973 | ````` ¿📪? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 111: ````` <0xAA> `````                  |
|       1081 | ````` ¿🕣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 104: ````` <0xA3> ````` |
|        983 | ````` ¿📴? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 120: ````` <0xB4> `````                  |
|       1397 | ````` ¿🥔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 250: ````` <0x94> ````` |
|       1401 | ````` ¿🥘? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 254: ````` <0x98> ````` |
|        632 | ````` ¿🎍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 243: ````` <0x8D> ````` |
|       1115 | ````` ¿🗓? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 249: ````` <0x93> ````` |
|        851 | ````` ¿👰? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 116: ````` <0xB0> `````                  |
|       1235 | ````` ¿🚙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 255: ````` <0x99> ````` |
|        738 | ````` ¿🏿? `````           | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 131: ````` <0xBF> `````                  |
|        776 | ````` ¿🐥? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 106: ````` <0xA5> ````` |
|       1267 | ````` ¿🚹? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 125: ````` <0xB9> ````` |
|       1046 | ````` ¿🔴? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 120: ````` <0xB4> `````                  |
|       1460 | ````` ¿🦓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 249: ````` <0x93> ````` |
|       1558 | ````` ¿🧵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 121: ````` <0xB5> ````` |
|       1499 | ````` ¿🦺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 126: ````` <0xBA> ````` |
|        735 | ````` ¿🏼? `````           | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 128: ````` <0xBC> `````                  |
|        575 | ````` ¿🍔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 250: ````` <0x94> ````` |
|       1110 | ````` ¿🗂? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 232: ````` <0x82> ````` |
|       1525 | ````` ¿🧔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 250: ````` <0x94> ````` |
|        529 | ````` ¿🌦? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 107: ````` <0xA6> ````` |
|        429 | ````` ¿⭕? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 263: ````` <0xAD> `````, 251: ````` <0x95> `````        |
|        305 | ````` ¿☀? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 230: ````` <0x80> `````                         |
|       1485 | ````` ¿🦬? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 113: ````` <0xAC> ````` |
|       1371 | ````` ¿🤸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 124: ````` <0xB8> ````` |
|        813 | ````` ¿👊? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 240: ````` <0x8A> `````                  |
|        786 | ````` ¿🐯? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 115: ````` <0xAF> ````` |
|        930 | ````` ¿💿? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 131: ````` <0xBF> `````                  |
|       1552 | ````` ¿🧯? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 115: ````` <0xAF> ````` |
|       1310 | ````` ¿🛹? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 125: ````` <0xB9> ````` |
|       1207 | ````` ¿🙍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 243: ````` <0x8D> ````` |
|       1579 | ````` ¿🪀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 230: ````` <0x80> ````` |
|        586 | ````` ¿🍟? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 261: ````` <0x9F> ````` |
|        828 | ````` ¿👙? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 255: ````` <0x99> `````                  |
|        282 | ````` ¿⏩? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 110: ````` <0xA9> `````        |
|       1403 | ````` ¿🥚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 256: ````` <0x9A> ````` |
|        643 | ````` ¿🎛? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 257: ````` <0x9B> ````` |
|        404 | ````` ¿✴? `````          |  0           | 70336: ````` <0xE2><0x9C> `````, 120: ````` <0xB4> `````                         |
|        845 | ````` ¿👪? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 111: ````` <0xAA> `````                  |
|       1396 | ````` ¿🥓? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 249: ````` <0x93> ````` |
|       1430 | ````` ¿🥵? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 121: ````` <0xB5> ````` |
|        775 | ````` ¿🐤? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 105: ````` <0xA4> ````` |
|        927 | ````` ¿💼? `````         |  0           | 106024: ````` <0xF0><0x9F><0x92> `````, 128: ````` <0xBC> `````                  |
|       1215 | ````` ¿🚅? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 235: ````` <0x85> ````` |
|       1082 | ````` ¿🕤? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 105: ````` <0xA4> ````` |
|       1298 | ````` ¿🛤? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 105: ````` <0xA4> ````` |
|       1216 | ````` ¿🚆? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 236: ````` <0x86> ````` |
|       1089 | ````` ¿🕴? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 120: ````` <0xB4> ````` |
|        741 | ````` ¿🐂? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 232: ````` <0x82> ````` |
|       1522 | ````` ¿🧑? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 247: ````` <0x91> ````` |
|       1469 | ````` ¿🦜? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 258: ````` <0x9C> ````` |
|       1586 | ````` ¿🪐? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 246: ````` <0x90> ````` |
|        793 | ````` ¿🐶? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 122: ````` <0xB6> ````` |
|       1149 | ````` ¿😓? `````         |  0           | 188568: ````` <0xF0><0x9F><0x98> `````, 249: ````` <0x93> `````                  |
|       1327 | ````` ¿🤌? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 242: ````` <0x8C> ````` |
|       1493 | ````` ¿🦴? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 120: ````` <0xB4> ````` |
|        868 | ````` ¿💁? `````         |  0           | 106024: ````` <0xF0><0x9F><0x92> `````, 231: ````` <0x81> `````                  |
|        330 | ````` ¿♊? `````         |  0           | 45687: ````` <0xE2><0x99> `````, 240: ````` <0x8A> `````                         |
|       1319 | ````` ¿🟥? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 106: ````` <0xA5> ````` |
|        797 | ````` ¿🐺? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 126: ````` <0xBA> ````` |
|        271 | ````` ¿↕? `````          |  0           | 76876: ````` <0xE2><0x86> `````, 251: ````` <0x95> `````                         |
|       1370 | ````` ¿🤷? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 123: ````` <0xB7> ````` |
|       1004 | ````` ¿🔊? `````         |  0           | 205860: ````` <0xF0><0x9F><0x94> `````, 240: ````` <0x8A> `````                  |
|       1013 | ````` ¿🔓? `````         |  0           | 205860: ````` <0xF0><0x9F><0x94> `````, 249: ````` <0x93> `````                  |
|       1108 | ````` ¿🖲? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 118: ````` <0xB2> ````` |
|       1160 | ````` ¿😞? `````         |  0           | 188568: ````` <0xF0><0x9F><0x98> `````, 260: ````` <0x9E> `````                  |
|        925 | ````` ¿💺? `````         |  0           | 106024: ````` <0xF0><0x9F><0x92> `````, 126: ````` <0xBA> `````                  |
|       1236 | ````` ¿🚚? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 256: ````` <0x9A> ````` |
|       1343 | ````` ¿🤜? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 258: ````` <0x9C> ````` |
|       1411 | ````` ¿🥢? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 103: ````` <0xA2> ````` |
|       1333 | ````` ¿🤒? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 248: ````` <0x92> ````` |
|        941 | ````` ¿📊? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 240: ````` <0x8A> `````                  |
|       1571 | ````` ¿🩲? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 118: ````` <0xB2> ````` |
|       1017 | ````` ¿🔗? `````         |  0           | 205860: ````` <0xF0><0x9F><0x94> `````, 253: ````` <0x97> `````                  |
|       1015 | ````` ¿🔕? `````         |  0           | 205860: ````` <0xF0><0x9F><0x94> `````, 251: ````` <0x95> `````                  |
|        915 | ````` ¿💰? `````         |  0           | 106024: ````` <0xF0><0x9F><0x92> `````, 116: ````` <0xB0> `````                  |
|        674 | ````` ¿🎼? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 128: ````` <0xBC> ````` |
|       1404 | ````` ¿🥛? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 257: ````` <0x9B> ````` |
|       1204 | ````` ¿🙊? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 240: ````` <0x8A> ````` |
|       1596 | ````` ¿🪚? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 256: ````` <0x9A> ````` |
|       1195 | ````` ¿🙁? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 231: ````` <0x81> ````` |
|        628 | ````` ¿🎉? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 239: ````` <0x89> ````` |
|        990 | ````` ¿📻? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 127: ````` <0xBB> `````                  |
|       1264 | ````` ¿🚶? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 122: ````` <0xB6> ````` |
|       1242 | ````` ¿🚠? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 262: ````` <0xA0> ````` |
|       1114 | ````` ¿🗒? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 248: ````` <0x92> ````` |
|       1292 | ````` ¿\U0001f6de? ````` |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 260: ````` <0x9E> ````` |
|       1147 | ````` ¿😑? `````         |  0           | 188568: ````` <0xF0><0x9F><0x98> `````, 247: ````` <0x91> `````                  |
|       1274 | ````` ¿🛀? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 230: ````` <0x80> ````` |
|       1440 | ````` ¿🥿? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 131: ````` <0xBF> ````` |
|        683 | ````` ¿🏅? `````         |  0           | 216125: ````` <0xF0><0x9F><0x8F> `````, 235: ````` <0x85> `````                  |
|       1128 | ````` ¿🗾? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 130: ````` <0xBE> ````` |
|       1517 | ````` ¿\U0001f9cc? ````` |  0           | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 242: ````` <0x8C> ````` |
|       1365 | ````` ¿🤲? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 118: ````` <0xB2> ````` |
|       1243 | ````` ¿🚡? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 102: ````` <0xA1> ````` |
|       1022 | ````` ¿🔜? `````         |  0           | 205860: ````` <0xF0><0x9F><0x94> `````, 258: ````` <0x9C> `````                  |
|       1249 | ````` ¿🚧? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 108: ````` <0xA7> ````` |
|       1058 | ````` ¿🕋? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 241: ````` <0x8B> ````` |
|        526 | ````` ¿🌡? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 102: ````` <0xA1> ````` |
|        791 | ````` ¿🐴? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 120: ````` <0xB4> ````` |
|        933 | ````` ¿📂? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 232: ````` <0x82> `````                  |
|       1324 | ````` ¿🟪? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 111: ````` <0xAA> ````` |
|       1420 | ````` ¿🥫? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 112: ````` <0xAB> ````` |
|        702 | ````` ¿🏘? `````          |  0           | 216125: ````` <0xF0><0x9F><0x8F> `````, 254: ````` <0x98> `````                  |
|        807 | ````` ¿👄? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 234: ````` <0x84> `````                  |
|       1117 | ````` ¿🗝? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 259: ````` <0x9D> ````` |
|       1615 | ````` ¿🪰? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 116: ````` <0xB0> ````` |
|        999 | ````` ¿🔅? `````         |  0           | 205860: ````` <0xF0><0x9F><0x94> `````, 235: ````` <0x85> `````                  |
|       1390 | ````` ¿🥍? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 243: ````` <0x8D> ````` |
|       1658 | ````` ¿\U000e0063? ````` |  0           | 202213: ````` \U000e0063 `````                                                   |
|        810 | ````` ¿👇? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 237: ````` <0x87> `````                  |
|        962 | ````` ¿📟? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 261: ````` <0x9F> `````                  |
|       1629 | ````` ¿\U0001fac3? ````` |  0           | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 233: ````` <0x83> ````` |
|        970 | ````` ¿📧? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 108: ````` <0xA7> `````                  |
|        939 | ````` ¿📈? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 238: ````` <0x88> `````                  |
|       1019 | ````` ¿🔙? `````         |  0           | 205860: ````` <0xF0><0x9F><0x94> `````, 255: ````` <0x99> `````                  |
|       1414 | ````` ¿🥥? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 106: ````` <0xA5> ````` |
|       1322 | ````` ¿🟨? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 109: ````` <0xA8> ````` |
|       1084 | ````` ¿🕦? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 107: ````` <0xA6> ````` |
|       1478 | ````` ¿🦥? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 106: ````` <0xA5> ````` |
|        875 | ````` ¿💈? `````         |  0           | 106024: ````` <0xF0><0x9F><0x92> `````, 238: ````` <0x88> `````                  |
|       1203 | ````` ¿🙉? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 239: ````` <0x89> ````` |
|       1627 | ````` ¿🫁? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 231: ````` <0x81> ````` |
|       1288 | ````` ¿🛕? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 251: ````` <0x95> ````` |
|       1006 | ````` ¿🔌? `````         |  0           | 205860: ````` <0xF0><0x9F><0x94> `````, 242: ````` <0x8C> `````                  |
|       1415 | ````` ¿🥦? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 107: ````` <0xA6> ````` |
|       1455 | ````` ¿🦎? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 244: ````` <0x8E> ````` |
|        826 | ````` ¿👗? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 253: ````` <0x97> `````                  |
|       1598 | ````` ¿🪜? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 258: ````` <0x9C> ````` |
|        765 | ````` ¿🐚? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 256: ````` <0x9A> ````` |
|       1323 | ````` ¿🟩? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 110: ````` <0xA9> ````` |
|       1407 | ````` ¿🥞? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 260: ````` <0x9E> ````` |
|        301 | ````` ¿◻? `````          |  0           | 37357: ````` <0xE2><0x97> `````, 127: ````` <0xBB> `````                         |
|       1328 | ````` ¿🤍? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 243: ````` <0x8D> ````` |
|       1363 | ````` ¿🤰? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 116: ````` <0xB0> ````` |
|       1384 | ````` ¿🥇? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 237: ````` <0x87> ````` |
|        594 | ````` ¿🍧? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 108: ````` <0xA7> ````` |
|       1423 | ````` ¿🥮? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 114: ````` <0xAE> ````` |
|       1139 | ````` ¿😉? `````         |  0           | 188568: ````` <0xF0><0x9F><0x98> `````, 239: ````` <0x89> `````                  |
|       1067 | ````` ¿🕕? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 251: ````` <0x95> ````` |
|        820 | ````` ¿👑? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 247: ````` <0x91> `````                  |
|        612 | ````` ¿🍹? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 125: ````` <0xB9> ````` |
|       1657 | ````` ¿\U000e0062? ````` |  0           | 3330: ````` <0xF3><0xA0><0x81> `````, 103: ````` <0xA2> `````                    |
|       1001 | ````` ¿🔇? `````         |  0           | 205860: ````` <0xF0><0x9F><0x94> `````, 237: ````` <0x87> `````                  |
|       1621 | ````` ¿🪶? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 122: ````` <0xB6> ````` |
|       1261 | ````` ¿🚳? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 119: ````` <0xB3> ````` |
|       1471 | ````` ¿🦞? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 260: ````` <0x9E> ````` |
|       1301 | ````` ¿🛫? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 112: ````` <0xAB> ````` |
|       1286 | ````` ¿🛑? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 247: ````` <0x91> ````` |
|       1445 | ````` ¿🦄? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 234: ````` <0x84> ````` |
|       1257 | ````` ¿🚯? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 115: ````` <0xAF> ````` |
|        935 | ````` ¿📄? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 234: ````` <0x84> `````                  |
|        821 | ````` ¿👒? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 248: ````` <0x92> `````                  |
|       1351 | ````` ¿🤤? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 105: ````` <0xA4> ````` |
|       1191 | ````` ¿😽? `````         |  0           | 188568: ````` <0xF0><0x9F><0x98> `````, 129: ````` <0xBD> `````                  |
|       1305 | ````` ¿🛴? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 120: ````` <0xB4> ````` |
|       1541 | ````` ¿🧤? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 105: ````` <0xA4> ````` |
|       1043 | ````` ¿🔱? `````         |  0           | 205860: ````` <0xF0><0x9F><0x94> `````, 117: ````` <0xB1> `````                  |
|        732 | ````` ¿🏹? `````         |  0           | 216125: ````` <0xF0><0x9F><0x8F> `````, 125: ````` <0xB9> `````                  |
|       1524 | ````` ¿🧓? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 249: ````` <0x93> ````` |
|       1183 | ````` ¿😵? `````         |  0           | 188568: ````` <0xF0><0x9F><0x98> `````, 121: ````` <0xB5> `````                  |
|       1175 | ````` ¿😭? `````         |  0           | 188568: ````` <0xF0><0x9F><0x98> `````, 263: ````` <0xAD> `````                  |
|       1296 | ````` ¿🛢? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 103: ````` <0xA2> ````` |
|       1330 | ````` ¿🤏? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 245: ````` <0x8F> ````` |
|        361 | ````` ¿⚪? `````         |  0           | 175142: ````` <0xE2><0x9A> `````, 111: ````` <0xAA> `````                        |
|       1551 | ````` ¿🧮? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 114: ````` <0xAE> ````` |
|       1232 | ````` ¿🚖? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 252: ````` <0x96> ````` |
|       1221 | ````` ¿🚋? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 241: ````` <0x8B> ````` |
|       1306 | ````` ¿🛵? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 121: ````` <0xB5> ````` |
|       1329 | ````` ¿🤎? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 244: ````` <0x8E> ````` |
|       1441 | ````` ¿🦀? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 230: ````` <0x80> ````` |
|       1270 | ````` ¿🚼? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 128: ````` <0xBC> ````` |
|       1279 | ````` ¿🛅? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 235: ````` <0x85> ````` |
|        356 | ````` ¿⚛? `````          |  0           | 175142: ````` <0xE2><0x9A> `````, 257: ````` <0x9B> `````                        |
|       1157 | ````` ¿😛? `````         |  0           | 188568: ````` <0xF0><0x9F><0x98> `````, 257: ````` <0x9B> `````                  |
|       1219 | ````` ¿🚉? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 239: ````` <0x89> ````` |
|       1002 | ````` ¿🔈? `````         |  0           | 205860: ````` <0xF0><0x9F><0x94> `````, 238: ````` <0x88> `````                  |
|        934 | ````` ¿📃? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 233: ````` <0x83> `````                  |
|       1662 | ````` ¿\U000e006e? ````` |  0           | 9738: ````` \U000e006e `````                                                     |
|       1373 | ````` ¿🤺? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 126: ````` <0xBA> ````` |
|       1307 | ````` ¿🛶? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 122: ````` <0xB6> ````` |
|       1225 | ````` ¿🚏? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 245: ````` <0x8F> ````` |
|       1208 | ````` ¿🙎? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 244: ````` <0x8E> ````` |
|       1574 | ````` ¿🩸? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 124: ````` <0xB8> ````` |
|       1118 | ````` ¿🗞? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 260: ````` <0x9E> ````` |
|       1557 | ````` ¿🧴? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 120: ````` <0xB4> ````` |
|        530 | ````` ¿🌧? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 108: ````` <0xA7> ````` |
|       1133 | ````` ¿😃? `````         |  0           | 188568: ````` <0xF0><0x9F><0x98> `````, 233: ````` <0x83> `````                  |
|       1217 | ````` ¿🚇? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 237: ````` <0x87> ````` |
|       1417 | ````` ¿🥨? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 109: ````` <0xA8> ````` |
|       1138 | ````` ¿😈? `````         |  0           | 188568: ````` <0xF0><0x9F><0x98> `````, 238: ````` <0x88> `````                  |
|       1093 | ````` ¿🕸? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 124: ````` <0xB8> ````` |
|        803 | ````` ¿👀? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 230: ````` <0x80> `````                  |
|       1431 | ````` ¿🥶? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 122: ````` <0xB6> ````` |
|        944 | ````` ¿📍? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 243: ````` <0x8D> `````                  |
|        890 | ````` ¿💗? `````         |  0           | 106024: ````` <0xF0><0x9F><0x92> `````, 253: ````` <0x97> `````                  |
|       1402 | ````` ¿🥙? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 255: ````` <0x99> ````` |
|        697 | ````` ¿🏓? `````         |  0           | 216125: ````` <0xF0><0x9F><0x8F> `````, 249: ````` <0x93> `````                  |
|       1080 | ````` ¿🕢? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 103: ````` <0xA2> ````` |
|       1068 | ````` ¿🕖? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 252: ````` <0x96> ````` |
|       1188 | ````` ¿😺? `````         |  0           | 188568: ````` <0xF0><0x9F><0x98> `````, 126: ````` <0xBA> `````                  |
|        438 | ````` ¿🅱? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 235: ````` <0x85> `````, 117: ````` <0xB1> ````` |
|       1354 | ````` ¿🤧? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 108: ````` <0xA7> ````` |
|        675 | ````` ¿🎽? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 129: ````` <0xBD> ````` |
|       1220 | ````` ¿🚊? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 240: ````` <0x8A> ````` |
|        695 | ````` ¿🏑? `````         |  5.96046e-08 | 216125: ````` <0xF0><0x9F><0x8F> `````, 247: ````` <0x91> `````                  |
|       1336 | ````` ¿🤕? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 251: ````` <0x95> ````` |
|       1075 | ````` ¿🕝? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 259: ````` <0x9D> ````` |
|       1443 | ````` ¿🦂? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 232: ````` <0x82> ````` |
|       1633 | ````` ¿🫑? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 247: ````` <0x91> ````` |
|       1011 | ````` ¿🔑? `````         |  5.96046e-08 | 205860: ````` <0xF0><0x9F><0x94> `````, 247: ````` <0x91> `````                  |
|       1095 | ````` ¿🕺? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 126: ````` <0xBA> ````` |
|       1120 | ````` ¿🗣? `````          |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 104: ````` <0xA3> ````` |
|       1585 | ````` ¿🪆? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 236: ````` <0x86> ````` |
|       1273 | ````` ¿🚿? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 131: ````` <0xBF> ````` |
|       1505 | ````` ¿🧀? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 230: ````` <0x80> ````` |
|        806 | ````` ¿👃? `````         |  5.96046e-08 | 154565: ````` <0xF0><0x9F><0x91> `````, 233: ````` <0x83> `````                  |
|        818 | ````` ¿👏? `````         |  5.96046e-08 | 154565: ````` <0xF0><0x9F><0x91> `````, 245: ````` <0x8F> `````                  |
|       1014 | ````` ¿🔔? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 10121: ````` <0x94><0x94> `````                  |
|        972 | ````` ¿📩? `````         |  5.96046e-08 | 185981: ````` <0xF0><0x9F><0x93> `````, 110: ````` <0xA9> `````                  |
|       1436 | ````` ¿🥻? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 127: ````` <0xBB> ````` |
|       1356 | ````` ¿🤩? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 110: ````` <0xA9> ````` |
|       1159 | ````` ¿😝? `````         |  5.96046e-08 | 188568: ````` <0xF0><0x9F><0x98> `````, 259: ````` <0x9D> `````                  |
|       1016 | ````` ¿🔖? `````         |  5.96046e-08 | 205860: ````` <0xF0><0x9F><0x94> `````, 252: ````` <0x96> `````                  |
|        912 | ````` ¿💭? `````         |  5.96046e-08 | 106024: ````` <0xF0><0x9F><0x92> `````, 263: ````` <0xAD> `````                  |
|       1361 | ````` ¿🤮? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 114: ````` <0xAE> ````` |
|       1253 | ````` ¿🚫? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 112: ````` <0xAB> ````` |
|       1071 | ````` ¿🕙? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 255: ````` <0x99> ````` |
|       1544 | ````` ¿🧧? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 108: ````` <0xA7> ````` |
|       1214 | ````` ¿🚄? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 234: ````` <0x84> ````` |
|       1246 | ````` ¿🚤? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 105: ````` <0xA4> ````` |
|        640 | ````` ¿🎗? `````          |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 253: ````` <0x97> ````` |
|        902 | ````` ¿💣? `````         |  5.96046e-08 | 106024: ````` <0xF0><0x9F><0x92> `````, 104: ````` <0xA3> `````                  |
|       1342 | ````` ¿🤛? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 257: ````` <0x9B> ````` |
</details>

