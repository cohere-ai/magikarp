# Report for `CohereForAI/c4ai-command-r-v01`

## Model info

* Tied embeddings: yes
* LM head uses bias: no
* Indicator for under-trained tokens: E_{out} L2 Distance
  * Overall distribution 2.272 +/- 0.519
  * Token used for verification prompt building: `InvalidProtocolBufferException`
  * Verification threshold: 1.356
  * Threshold for showing candidate under-trained tokens: 0.557
  * Median verified threshold (for bytes, unreachable and special tokens): 0.492
* Embeddings shape: (256000, 8192)
* Vocabulary size: 255029
  * Number of single byte tokens: 256, of which 13 below indicator threshold
  * Number of special tokens: 37, of which 26 below indicator threshold
  * Number of non-single-byte unreachable tokens: 1403, of which 1403 below indicator threshold
  * Number of non-single-byte UTF-fragment tokens: 2956, 16 below soft indicator threshold
  * Number of tested under-trained tokens: 5012, 4961 non-special, 281 below p = 0.01 threshold, 154 below soft indicator threshold

## Under-trained token indicators plot
![Indicators scatter plots](../indicators_pairplot_byid/CohereForAI_c4ai_command_r_v01.png)

## Verification plot
![Verification plot](../verifications_scatterplot/CohereForAI_c4ai_command_r_v01.png)

## Under-trained token verification results
154 entries below threshold of 0.557

|   token_id | token                                                                                                                                |   indicator | max_prob                                                         | in_other_tokens                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------|--------------------------------------------------------------------------------------------------------------------------------------|-------------|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     239520 | ````` ▁hbBiddersParams `````                                                                                                         | 0.00015466  | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     208149 | ````` AddLanguageSpecificText `````                                                                                                  | 0.000159452 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` AddLanguageSpecificTextSet `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     127300 | ````` tocguid `````                                                                                                                  | 0.000162081 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|      51386 | ````` ▁ARStdSong `````                                                                                                               | 0.000164476 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|      22188 | ````` ▁林肯近地小行星研究小 `````                                                                                                    | 0.000168334 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁林肯近地小行星研究小组 `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁林肯近地小行星研究小組 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                        |
|     140485 | ````` 目前尚未由人工引 `````                                                                                                         | 0.000169476 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` 目前尚未由人工引种栽培 `````</span>, <span style='border: 1px solid rgb(255, 145, 0);'>````` 目前尚未由人工引種栽培 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                          |
|      72754 | ````` ageryears `````                                                                                                                | 0.000221197 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | ````` manageryears `````, ````` ▁manageryears `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|      84176 | ````` recDocCases `````                                                                                                              | 0.000234136 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     177875 | ````` tochassubtree `````                                                                                                            | 0.000274712 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|      15675 | ````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f ````` | 0.00235927  | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````                                                                                                                                                                                                                                                                                                                                   |
|     145442 | ````` 》（）， `````                                                                                                                 | 0.0103921   | <span style='border: 1px solid rgb(169, 68, 66);'>3e-07</span>   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     141168 | ````` ephritidae `````                                                                                                               | 0.0224668   | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` Tephritidae `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Tephritidae `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|     139462 | ````` 和人口皆未知 `````                                                                                                             | 0.0243845   | <span style='border: 1px solid rgb(169, 68, 66);'>3.2e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` 该地的面积和人口皆未知 `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` 該地的面積和人口皆未知 `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` 面积和人口皆未知 `````</span>                                                                                                                                                                                                                                                                                                                                   |
|     224223 | ````` 面积和人口皆未知 `````                                                                                                         | 0.0252942   | <span style='border: 1px solid rgb(169, 68, 66);'>3.2e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` 该地的面积和人口皆未知 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|      71049 | ````` tocectory `````                                                                                                                | 0.0272563   | <span style='border: 1px solid rgb(169, 68, 66);'>3.3e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     190228 | ````` ▁Hmelnî `````                                                                                                                  | 0.0290728   | <span style='border: 1px solid rgb(169, 68, 66);'>3e-07</span>   | <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁Hmelnîțkîi `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|     141246 | ````` locatorSection `````                                                                                                           | 0.0299165   | <span style='border: 1px solid rgb(169, 68, 66);'>3e-07</span>   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|       9741 | ````` \U000e0067\U000e0062\U000e0065\U000e006e `````                                                                                 | 0.0372116   | <span style='border: 1px solid rgb(169, 68, 66);'>3e-07</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` ▁🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f ````` |
|     149800 | ````` 年建立的教育 `````                                                                                                             | 0.0395958   | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` 年建立的教育機構 `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` 年建立的教育机构 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|     208151 | ````` AddLanguageSpecificTextSet `````                                                                                               | 0.0434841   | <span style='border: 1px solid rgb(169, 68, 66);'>2.5e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
<details><summary>134 additional entries below threshold</summary>

|   token_id | token                                    |   indicator | max_prob                                                         | in_other_tokens                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------|------------------------------------------|-------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     190437 | ````` BiddersParams `````                |   0.0439359 | <span style='border: 1px solid rgb(169, 68, 66);'>3e-07</span>   | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁hbBiddersParams `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|      51385 | ````` ▁ARStd `````                       |   0.0559382 | <span style='border: 1px solid rgb(169, 68, 66);'>2.4e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁ARStdSong `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     100190 | ````` Desambigua `````                   |   0.05825   | <span style='border: 1px solid rgb(169, 68, 66);'>3.4e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` Desambiguações `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` Desambiguação `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|      94747 | ````` OnSearchSelect `````               |   0.0628027 | <span style='border: 1px solid rgb(169, 68, 66);'>1.5e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` OnSearchSelectShow `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` OnSearchSelectHide `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` OnSearchSelectKey `````</span>                                                                                                                                                                                                                                                                                                                                                   |
|     127290 | ````` srguid `````                       |   0.0777912 | <span style='border: 1px solid rgb(169, 68, 66);'>1.4e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     177855 | ````` assubtree `````                    |   0.0805532 | <span style='border: 1px solid rgb(169, 68, 66);'>1.7e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` tochassubtree `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|     228399 | ````` цыкла `````                        |   0.0856902 | <span style='border: 1px solid rgb(169, 68, 66);'>1.5e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` цыклапед `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` цыклапедыя `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Энцыклапедыя `````</span>                                                                                                                                                                                                                                                                                                                                                                         |
|      37757 | ````` （，）， `````                     |   0.0884548 | <span style='border: 1px solid rgb(169, 68, 66);'>2.4e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     172752 | ````` ablytyped `````                    |   0.0913916 | <span style='border: 1px solid rgb(169, 68, 66);'>1.4e-07</span> | ````` scalablytyped `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|     114578 | ````` inyphiidae `````                   |   0.0928686 | <span style='border: 1px solid rgb(169, 68, 66);'>2.5e-07</span> | ````` ▁Linyphiidae `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` Linyphiidae `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|     228872 | ````` ”（） `````                        |   0.102472  | <span style='border: 1px solid rgb(169, 68, 66);'>2.7e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     223425 | ````` 而人口密度為 `````                 |   0.105687  | <span style='border: 1px solid rgb(169, 68, 66);'>1.3e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` 而人口密度為每平方千米 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|      74789 | ````` stdtemplate `````                  |   0.112474  | <span style='border: 1px solid rgb(169, 68, 66);'>2.4e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     119253 | ````` écosl `````                        |   0.117454  | <span style='border: 1px solid rgb(169, 68, 66);'>2.5e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` écoslova `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` écoslovaquie `````</span>, ````` ▁Tchécoslovaquie `````, ````` ▁tchécoslova `````                                                                                                                                                                                                                                                                                                                                                                                                   |
|     144020 | ````` оспоживача `````                   |   0.121497  | <span style='border: 1px solid rgb(169, 68, 66);'>2.3e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁особоспоживача `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     100216 | ````` ▁μυθισ `````                       |   0.122008  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-07</span> | ````` ▁μυθιστο `````, ````` ▁μυθιστόρημα `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁μυθιστό `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|     214699 | ````` 平均海拔高度為 `````               |   0.125007  | <span style='border: 1px solid rgb(169, 68, 66);'>1e-07</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` 而該地的平均海拔高度為 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     249467 | ````` Тісс `````                         |   0.127579  | <span style='border: 1px solid rgb(169, 68, 66);'>1.2e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` Тіссеранів `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      71714 | ````` 所属的省级 `````                   |   0.130669  | <span style='border: 1px solid rgb(169, 68, 66);'>1e-07</span>   | <span style='border: 1px solid rgb(251, 189, 8);'>````` 所属的省级选区为 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|     157335 | ````` cetophilidae `````                 |   0.131394  | <span style='border: 1px solid rgb(169, 68, 66);'>2.3e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Mycetophilidae `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` Mycetophilidae `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|      31886 | ````` docguid `````                      |   0.138     | <span style='border: 1px solid rgb(169, 68, 66);'>9.6e-08</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     223844 | ````` 該地的面積 `````                   |   0.139505  | <span style='border: 1px solid rgb(169, 68, 66);'>2.4e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` 該地的面積和人口皆未知 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     127302 | ````` deliveryTarget `````               |   0.144523  | <span style='border: 1px solid rgb(169, 68, 66);'>1e-07</span>   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     188002 | ````` țkîi `````                         |   0.145601  | <span style='border: 1px solid rgb(169, 68, 66);'>1.7e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁Hmelnîțkîi `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|     202267 | ````` \U000e0074\U000e007f `````         |   0.148202  | <span style='border: 1px solid rgb(169, 68, 66);'>1.4e-07</span> | ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````, ````` <0xB3>\U000e0063\U000e0074\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|     143921 | ````` 而水域 `````                       |   0.150456  | <span style='border: 1px solid rgb(169, 68, 66);'>1.2e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` 而水域面积为 `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` 而水域面積為 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     127301 | ````` deliveryLink `````                 |   0.154373  | <span style='border: 1px solid rgb(169, 68, 66);'>7.6e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     149474 | ````` 」（） `````                       |   0.160286  | <span style='border: 1px solid rgb(169, 68, 66);'>2.5e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     152127 | ````` Rolver `````                       |   0.162699  | <span style='border: 1px solid rgb(169, 68, 66);'>1e-07</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` Rolverdeling `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|      63146 | ````` 》（） `````                       |   0.165893  | <span style='border: 1px solid rgb(169, 68, 66);'>2.6e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` 》（）， `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|      69100 | ````` \U000e0073\U000e007f `````         |   0.171451  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00014</span> | ````` <0xB7>\U000e006c\U000e0073\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|     165878 | ````` ▁Jît `````                         |   0.173867  | <span style='border: 1px solid rgb(169, 68, 66);'>1.5e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁Jîtomîr `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|     163225 | ````` 俄亥 `````                         |   0.174811  | <span style='border: 1px solid rgb(169, 68, 66);'>1.2e-07</span> | ````` 俄亥俄 `````, ````` 俄亥俄州 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     138155 | ````` byliidae `````                     |   0.186623  | <span style='border: 1px solid rgb(169, 68, 66);'>8.2e-08</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Bombyliidae `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` Bombyliidae `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|      29307 | ````` memItem `````                      |   0.189497  | <span style='border: 1px solid rgb(169, 68, 66);'>1.5e-07</span> | ````` memItemLeft `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` memItemRight `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|      75649 | ````` μοσπο `````                        |   0.19684   | <span style='border: 1px solid rgb(169, 68, 66);'>9.6e-08</span> | ````` μοσπονδια `````, ````` ▁Ομοσπονδία `````, ````` ▁Ομοσπονδίας `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` μοσπονδ `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Ομοσπονδ `````</span>, ...                                                                                                                                                                                                                                                                                                                                                                                |
|     215450 | ````` 是一颗围绕太阳公 `````             |   0.201137  | <span style='border: 1px solid rgb(169, 68, 66);'>7.2e-08</span> | ````` 是一颗围绕太阳公转的小行星 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|     132755 | ````` Сокор `````                        |   0.201328  | <span style='border: 1px solid rgb(169, 68, 66);'>1e-07</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` Сокорро `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|      98281 | ````` 天文台近地小行星 `````             |   0.201577  | <span style='border: 1px solid rgb(169, 68, 66);'>8.2e-08</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁洛厄尔天文台近地小行星搜寻计划 `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` 天文台近地小行星搜寻计划 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                        |
|      57843 | ````` NdEx `````                         |   0.202579  | <span style='border: 1px solid rgb(169, 68, 66);'>8.1e-08</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁iNdEx `````</span>, ````` iNdEx `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|      87763 | ````` 덜란드 `````                       |   0.203645  | <span style='border: 1px solid rgb(169, 68, 66);'>6.4e-06</span> | ````` 네덜란드 `````, ````` ▁네덜란드 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|      21048 | ````` yrıca `````                        |   0.203712  | <span style='border: 1px solid rgb(169, 68, 66);'>2.9e-07</span> | ````` Ayrıca `````, ````` ▁ayrıca `````, ````` ▁Ayrıca `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|     234076 | ````` ▁Άντζελ `````                      |   0.212314  | <span style='border: 1px solid rgb(169, 68, 66);'>1e-06</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Άντζελες `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|      16811 | ````` 한민국의 `````                     |   0.213522  | <span style='border: 1px solid rgb(169, 68, 66);'>4.2e-07</span> | ````` ▁대한민국의 `````, ````` 대한민국의 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      85423 | ````` езультаты `````                    |   0.215754  | <span style='border: 1px solid rgb(169, 68, 66);'>9e-08</span>   | ````` ▁результаты `````, ````` Результаты `````, ````` ▁Результаты `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|      28088 | ````` ервые `````                        |   0.216569  | <span style='border: 1px solid rgb(169, 68, 66);'>9.4e-06</span> | ````` первые `````, ````` ▁Первые `````, ````` Впервые `````, ````` ▁Впервые `````, ````` Первые `````, ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     104486 | ````` ούθησε `````                       |   0.217946  | <span style='border: 1px solid rgb(169, 68, 66);'>7.8e-06</span> | ````` κολούθησε `````, ````` ▁ακολούθησε `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|      71316 | ````` 市镇编码为 `````                   |   0.222526  | <span style='border: 1px solid rgb(169, 68, 66);'>7e-08</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` INSEE市镇编码为 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     165176 | ````` foolcdn `````                      |   0.224816  | <span style='border: 1px solid rgb(169, 68, 66);'>1.4e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      71269 | ````` aravant `````                      |   0.227644  | <span style='border: 1px solid rgb(169, 68, 66);'>6.2e-05</span> | ````` ▁auparavant `````, ````` uparavant `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|      61835 | ````` есмотря `````                      |   0.229268  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00013</span> | ````` ▁несмотря `````, ````` Несмотря `````, ````` ▁Несмотря `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|      49349 | ````` （，） `````                       |   0.229847  | <span style='border: 1px solid rgb(169, 68, 66);'>6.5e-05</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     113299 | ````` ▁Υόρ `````                         |   0.233186  | <span style='border: 1px solid rgb(169, 68, 66);'>5.7e-05</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Υόρκη `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Υόρκης `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|      72073 | ````` eskipun `````                      |   0.239987  | <span style='border: 1px solid rgb(169, 68, 66);'>9.2e-05</span> | ````` Meskipun `````, ````` ▁Meskipun `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|       9740 | ````` \U000e0067\U000e007f `````         |   0.240337  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00033</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` ▁🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````          |
|     112496 | ````` ▁předcho `````                     |   0.241611  | <span style='border: 1px solid rgb(169, 68, 66);'>7e-05</span>   | ````` ▁předchoz `````, ````` ▁předchozí `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|     177869 | ````` ▁tocid `````                       |   0.245001  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00019</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     114974 | ````` ▁auxqu `````                       |   0.250031  | <span style='border: 1px solid rgb(169, 68, 66);'>8.6e-07</span> | ````` ▁auxquelles `````, ````` ▁auxquels `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|      58491 | ````` DFBEF `````                        |   0.251345  | <span style='border: 1px solid rgb(169, 68, 66);'>9.3e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      60667 | ````` ▁sconfit `````                     |   0.251759  | <span style='border: 1px solid rgb(169, 68, 66);'>8.5e-06</span> | ````` ▁sconfitte `````, ````` ▁sconfitta `````, ````` ▁sconfitto `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|     176101 | ````` jsdel `````                        |   0.258027  | <span style='border: 1px solid rgb(169, 68, 66);'>7.5e-05</span> | ````` jsdelivr `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|      42729 | ````` ▁Indlaw `````                      |   0.262512  | <span style='border: 1px solid rgb(169, 68, 66);'>9.3e-05</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     113886 | ````` ▁kardy `````                       |   0.263951  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00015</span> | ````` ▁kardyna `````, ````` ▁kardynał `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     173398 | ````` rowborder `````                    |   0.268224  | <span style='border: 1px solid rgb(169, 68, 66);'>5.7e-05</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` cellrowborder `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|     232240 | ````` ουσαλή `````                       |   0.274647  | <span style='border: 1px solid rgb(169, 68, 66);'>3.3e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Ιερουσαλήμ `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` ουσαλήμ `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|      88149 | ````` 蒙山巡天 `````                     |   0.275287  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00017</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁萊蒙山巡天 `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁莱蒙山巡天 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|     109027 | ````` ▁fême `````                        |   0.276545  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00015</span> | ````` ▁fêmeas `````, ````` ▁fêmea `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|      67872 | ````` recDoc `````                       |   0.279374  | <span style='border: 1px solid rgb(169, 68, 66);'>1.1e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` recDocCases `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|     249873 | ````` codeSnippetContainer `````         |   0.283486  | <span style='border: 1px solid rgb(169, 68, 66);'>2.7e-05</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     127296 | ````` altview `````                      |   0.285996  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00038</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     229503 | ````` 密歇 `````                         |   0.286053  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00041</span> | ````` 密歇根 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|     250514 | ````` [✓]( `````                         |   0.286817  | <span style='border: 1px solid rgb(169, 68, 66);'>8.6e-07</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      98314 | ````` 天文台近地小行星搜寻计划 `````     |   0.28954   | <span style='border: 1px solid rgb(169, 68, 66);'>8.6e-08</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁洛厄尔天文台近地小行星搜寻计划 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     232390 | ````` Wikicon `````                      |   0.294365  | <span style='border: 1px solid rgb(169, 68, 66);'>4e-07</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` Wikiconcurso `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|     248801 | ````` AlreadyInited `````                |   0.299182  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00027</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` GetEmptyStringAlreadyInited `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|     202213 | ````` \U000e0063 `````                   |   0.301737  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00075</span> | ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````, ````` <0xB3>\U000e0063 `````, ````` <0xB3>\U000e0063\U000e0074\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     191064 | ````` AoAKACgAoAKACgAoAKACgAoAKACg ````` |   0.307118  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00044</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     139412 | ````` 皆未知 `````                       |   0.307439  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00021</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` 该地的面积和人口皆未知 `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` 和人口皆未知 `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` 該地的面積和人口皆未知 `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` 面积和人口皆未知 `````</span>                                                                                                                                                                                                                                                         |
|     182239 | ````` （）（ `````                       |   0.310776  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00029</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      17586 | ````` льбом `````                        |   0.313334  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00019</span> | ````` ▁альбому `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` Альбомы `````</span>, ````` ▁альбомов `````, ````` ▁альбом `````, ````` ▁альбоме `````, ...                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|     141408 | ````` cellinside `````                   |   0.316865  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00064</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     102360 | ````` AoAKACg `````                      |   0.319744  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00026</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` AoAKACgAoAKACgAoAKACgAoAKACg `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` AoAKACgAoAKACg `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|     152313 | ````` SnippetContainer `````             |   0.326573  | <span style='border: 1px solid rgb(169, 68, 66);'>7.5e-06</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` codeSnippetContainer `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` CodeSnippetContainer `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|      90334 | ````` ▁Башкорт `````                     |   0.327946  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00034</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Башкортост `````</span>, ````` ▁Башкортостан `````, ````` ▁Башкортостана `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|      54193 | ````` ▁近地小行星 `````                  |   0.330641  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00027</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁近地小行星追踪 `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁近地小行星追蹤 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|     239797 | ````` CodeSnippetContainer `````         |   0.335971  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00057</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|       9738 | ````` \U000e006e `````                   |   0.342464  | <span style='border: 1px solid rgb(169, 68, 66);'>6e-05</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, ````` <0xA5>\U000e006e `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ... |
|     202195 | ````` \U000e0074 `````                   |   0.347287  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0017</span>  | <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0074\U000e007f `````</span>, ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````, ````` <0xB3>\U000e0063\U000e0074\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                   |
|     101279 | ````` AKACg `````                        |   0.349061  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00034</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` AoAKACgAoAKACgAoAKACgAoAKACg `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` AoAKACg `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` AoAKACgAoAKACg `````</span>                                                                                                                                                                                                                                                                                                                                                       |
|     117753 | ````` ▁военнослуж `````                  |   0.355609  | <span style='border: 1px solid rgb(169, 68, 66);'>0.0003</span>  | ````` ▁военнослужащ `````, ````` ▁военнослужащих `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|      55304 | ````` ▁коллект `````                     |   0.355765  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00057</span> | ````` ▁коллектива `````, ````` ▁коллектив `````, ````` ▁коллективы `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     108955 | ````` AoAKACgAoAKACg `````               |   0.358357  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00057</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` AoAKACgAoAKACgAoAKACgAoAKACg `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|     162582 | ````` omîr `````                         |   0.359036  | <span style='border: 1px solid rgb(169, 68, 66);'>2.6e-05</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁Jîtomîr `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|      98082 | ````` ▁洛厄尔 `````                      |   0.359478  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00047</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁洛厄尔天文台近地小行星搜寻计划 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|      98512 | ````` ▁zawodn `````                      |   0.361638  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00034</span> | ````` ▁zawodnicz `````, ````` ▁zawodnika `````, ````` ▁zawodnicy `````, ````` ▁zawodników `````, ````` ▁zawodnikiem `````, ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|     168004 | ````` deliveryFormat `````               |   0.36189   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00014</span> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      71539 | ````` 时的人口数量为人 `````             |   0.365155  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00021</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` 于时的人口数量为人 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|     141235 | ````` subSelected `````                  |   0.367161  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0016</span>  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      47407 | ````` ▁voormal `````                     |   0.368594  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00019</span> | ````` ▁voormalig `````, ````` ▁voormalige `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     153159 | ````` ▁двен `````                        |   0.372295  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00048</span> | ````` ▁двенадц `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|      69092 | ````` \U000e006c `````                   |   0.375196  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0011</span>  | ````` <0xB7>\U000e006c\U000e0073\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````, ````` <0xB7>\U000e006c `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     126598 | ````` ▁orquí `````                       |   0.377869  | <span style='border: 1px solid rgb(169, 68, 66);'>0.0003</span>  | ````` ▁orquídea `````, ````` ▁orquídeas `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|      68163 | ````` ▁hvě `````                         |   0.382868  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00038</span> | ````` ▁hvěz `````, ````` ▁hvězd `````, ````` ▁hvězdy `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|     137635 | ````` ▁Λουδοβ `````                      |   0.383649  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00049</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Λουδοβίκου `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Λουδοβίκος `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|     202631 | ````` ▁Mîkolai `````                     |   0.398675  | <span style='border: 1px solid rgb(169, 68, 66);'>1.6e-07</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁Mîkolaiiv `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     249185 | ````` ▁BĞ `````                          |   0.399844  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00036</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁BĞMSZ `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     139250 | ````` 而人口密度 `````                   |   0.412953  | <span style='border: 1px solid rgb(169, 68, 66);'>0.0003</span>  | <span style='border: 1px solid rgb(40, 167, 69);'>````` 而人口密度为每平方千米 `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` 而人口密度為 `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` 而人口密度為每平方千米 `````</span>                                                                                                                                                                                                                                                                                                                                                |
|      79368 | ````` ▁баскет `````                      |   0.427678  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0011</span>  | ````` ▁баскетболь `````, ````` ▁баскетболу `````, ````` ▁баскетбол `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     214270 | ````` 平均海拔高度为 `````               |   0.430674  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00022</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` 而该地的平均海拔高度为 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|      40115 | ````` uslararası `````                   |   0.431784  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00038</span> | ````` ▁Uluslararası `````, ````` Uluslararası `````, ````` ▁uluslararası `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|      69089 | ````` \U000e0073 `````                   |   0.432312  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0059</span>  | ````` <0xB7>\U000e006c\U000e0073\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0073\U000e007f `````</span>                                                                                                                                                                                                                                                                                                                      |
|     105682 | ````` ishockeyspieler `````              |   0.442919  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00063</span> | ````` ▁Eishockeyspieler `````, ````` Eishockeyspieler `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     110750 | ````` ▁κομμά `````                       |   0.449334  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00045</span> | ````` ▁κομμάτι `````, ````` ▁κομμάτια `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     219726 | ````` ▁海勒 `````                        |   0.458001  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0022</span>  | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁海勒卡拉 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|     123576 | ````` ▁Αυστ `````                        |   0.466516  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00049</span> | ````` ▁Αυστρα `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Αυστρίας `````</span>, ````` ▁Αυστραλία `````, ````` ▁Αυστρία `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Αυστρια `````</span>                                                                                                                                                                                                                                                                                                                                                                                           |
|     175277 | ````` морозный `````                     |   0.470153  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00028</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Безморозный `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|     233679 | ````` چوست `````                         |   0.474163  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00036</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁ماساچوست `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|     100038 | ````` ▁spoluprá `````                    |   0.479523  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00024</span> | ````` ▁spolupráci `````, ````` ▁spolupráce `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|     142131 | ````` ▁middeleeuw `````                  |   0.480523  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00044</span> | ````` ▁middeleeuwse `````, ````` ▁middeleeuwen `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     167896 | ````` wluk `````                         |   0.491109  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0039</span>  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     114115 | ````` ▁πρίγκι `````                      |   0.491787  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0033</span>  | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁πρίγκιπα `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁πρίγκιπας `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      81575 | ````` δοσφαίρου `````                    |   0.509518  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00043</span> | ````` ▁ποδοσφαίρου `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Ποδοσφαίρου `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|      87941 | ````` ▁αντιμετ `````                     |   0.509786  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00092</span> | ````` ▁αντιμετωπ `````, ````` ▁αντιμετω `````, ````` ▁αντιμετώπ `````, ````` ▁αντιμετώ `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|      69409 | ````` ahraga `````                       |   0.512131  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00092</span> | ````` ▁Olahraga `````, ````` ▁olahraga `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|     196178 | ````` johnsnow `````                     |   0.514958  | <span style='border: 1px solid rgb(251, 189, 8);'>0.042</span>   | <span style='border: 1px solid rgb(40, 167, 69);'>````` johnsnowlabs `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|     144088 | ````` urtemberg `````                    |   0.52372   | <span style='border: 1px solid rgb(255, 145, 0);'>0.0014</span>  | ````` Wurtemberg `````, ````` ▁Wurtemberg `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     228507 | ````` цыклапед `````                     |   0.527141  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00068</span> | <span style='border: 1px solid rgb(251, 189, 8);'>````` цыклапедыя `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Энцыклапедыя `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|     160473 | ````` АТУУ `````                         |   0.528817  | <span style='border: 1px solid rgb(169, 68, 66);'>0.0006</span>  | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁КОАТУУ `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|     228624 | ````` δινάν `````                        |   0.52942   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00065</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Φερδινάν `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|     121405 | ````` ▁ecclésiast `````                  |   0.535814  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00083</span> | ````` ▁ecclésiastiques `````, ````` ▁ecclésiastique `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|     118022 | ````` erdapat `````                      |   0.536716  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00045</span> | ````` ▁Terdapat `````, ````` Terdapat `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     211674 | ````` scoreDisplayMode `````             |   0.54805   | <span style='border: 1px solid rgb(251, 189, 8);'>0.02</span>    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     248208 | ````` وجرسی `````                        |   0.551332  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00051</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁نیوجرسی `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|      68073 | ````` ▁Českoslovens `````                |   0.554582  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0071</span>  | ````` ▁Československa `````, ````` ▁Československo `````, ````` ▁Československu `````, ````` ▁Československé `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
</details>


## Partial UTF-8 tokens
16 entries below threshold of 0.557

|   token_id | token                                                 |   indicator | in_other_tokens                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------|-------------------------------------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      57888 | ````` <0x89>글랜드 `````                              | 0.000159591 | ````` ▁잉글랜드의 `````, ````` ▁잉글랜드 `````, ````` 잉글랜드의 `````, ````` 잉글랜드 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|     113772 | ````` <0x98>리포니아 `````                            | 0.000163453 | ````` 캘리포니아 `````, ````` ▁캘리포니아 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|      70552 | ````` <0xB9><0x80><0xE0><0xB8> `````                  | 0.000170583 | ````` ▁เ<0xE0><0xB8> `````, ````` เ<0xE0><0xB8> `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|      97361 | ````` <0x95>시코 `````                                | 0.000186192 | ````` ▁멕시코 `````, ````` 멕시코 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|     202233 | ````` <0xB3>\U000e0063 `````                          | 0.00315435  | ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````, ````` <0xB3>\U000e0063\U000e0074\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|      19460 | ````` ▁🇯<0xF0><0x9F><0x87> `````                      | 0.0107318   | ````` ▁🇯🇲 `````, ````` ▁🇯🇴 `````, ````` ▁🇯🇵 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|      69097 | ````` <0xB7>\U000e006c `````                          | 0.0375009   | ````` <0xB7>\U000e006c\U000e0073\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|      62442 | ````` ▁🏴\U000e0067\U000e0062<0xF3><0xA0><0x81> ````` | 0.0451447   | ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|       6132 | ````` <0xA7><0xF3><0xA0><0x81> `````                  | 0.0713283   | ````` \U000e0067<0xF3><0xA0><0x81> `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e007f `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````, ...                                                                                                                                                                                                                                 |
|       9739 | ````` <0xA5>\U000e006e `````                          | 0.157974    | <span style='border: 1px solid rgb(40, 167, 69);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` ▁🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f ````` |
|      33585 | ````` <0x94>레비전 `````                              | 0.164439    | ````` 텔레비전 `````, ````` ▁텔레비전 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|     195191 | ````` "><0xEE><0x85> `````                            | 0.284727    | <span style='border: 1px solid rgb(251, 189, 8);'>````` ">\ue157</ `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|       6133 | ````` \U000e0067<0xF3><0xA0><0x81> `````              | 0.330891    | <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e007f `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062<0xF3><0xA0><0x81> `````, ...                                                                                                                                                                                                                    |
|       9302 | ````` <0xA2><0xF3><0xA0><0x81> `````                  | 0.333447    | <span style='border: 1px solid rgb(40, 167, 69);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062<0xF3><0xA0><0x81> `````, ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````, ...                                                                                                                                                                                                                                  |
|      53275 | ````` 特<0xE5><0xBE> `````                            | 0.372824    | ````` 特徵 `````, ````` 的特征 `````, ````` が特徴 `````, ````` 特征 `````, ````` 特徴 `````, ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     151735 | ````` 垃<0xE5><0x9C> `````                            | 0.388467    | ````` 垃圾 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |


## Byte tokens
13 entries below threshold of 0.492

|   token_id | token              |   indicator |   ord | hex   | byte_type   |
|------------|--------------------|-------------|-------|-------|-------------|
|        190 | ````` <0xFA> ````` | 0.000160242 |   250 | 0xFA  | unused_utf8 |
|        195 | ````` <0xFF> ````` | 0.000161521 |   255 | 0xFF  | unused_utf8 |
|        133 | ````` <0xC1> ````` | 0.000162296 |   193 | 0xC1  | unused_utf8 |
|        187 | ````` <0xF7> ````` | 0.000162337 |   247 | 0xF7  | unused_utf8 |
|        185 | ````` <0xF5> ````` | 0.000163905 |   245 | 0xF5  | unused_utf8 |
|        186 | ````` <0xF6> ````` | 0.000166617 |   246 | 0xF6  | unused_utf8 |
|        193 | ````` <0xFD> ````` | 0.000167524 |   253 | 0xFD  | unused_utf8 |
|        192 | ````` <0xFC> ````` | 0.000169357 |   252 | 0xFC  | unused_utf8 |
|        194 | ````` <0xFE> ````` | 0.000172051 |   254 | 0xFE  | unused_utf8 |
|        132 | ````` <0xC0> ````` | 0.000173093 |   192 | 0xC0  | unused_utf8 |
|        191 | ````` <0xFB> ````` | 0.000176365 |   251 | 0xFB  | unused_utf8 |
|        189 | ````` <0xF9> ````` | 0.000177613 |   249 | 0xF9  | unused_utf8 |
|        188 | ````` <0xF8> ````` | 0.000181585 |   248 | 0xF8  | unused_utf8 |


## Special tokens
26 entries below threshold of 0.492

|   token_id | token                           |   indicator | max_prob                                                         |
|------------|---------------------------------|-------------|------------------------------------------------------------------|
|     255028 | ````` <\|EXTRA_9_TOKEN\|> ````` | 0.000147134 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255027 | ````` <\|EXTRA_8_TOKEN\|> ````` | 0.000147686 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255025 | ````` <\|EXTRA_6_TOKEN\|> ````` | 0.000149227 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255024 | ````` <\|EXTRA_5_TOKEN\|> ````` | 0.000150401 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255026 | ````` <\|EXTRA_7_TOKEN\|> ````` | 0.000155593 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|          4 | ````` <MASK_TOKEN> `````        | 0.000171596 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255022 | ````` <\|EXTRA_3_TOKEN\|> ````` | 0.000187505 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255004 | ````` <\|GOOD_TOKEN\|> `````    | 0.000188973 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255018 | ````` <\|USER_9_TOKEN\|> `````  | 0.000190429 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255012 | ````` <\|USER_3_TOKEN\|> `````  | 0.000222025 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255011 | ````` <\|USER_2_TOKEN\|> `````  | 0.000222055 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255013 | ````` <\|USER_4_TOKEN\|> `````  | 0.000222136 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255005 | ````` <\|BAD_TOKEN\|> `````     | 0.000223386 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255020 | ````` <\|EXTRA_1_TOKEN\|> ````` | 0.00022344  | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255014 | ````` <\|USER_5_TOKEN\|> `````  | 0.000224174 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255019 | ````` <\|EXTRA_0_TOKEN\|> ````` | 0.000224631 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255016 | ````` <\|USER_7_TOKEN\|> `````  | 0.000225225 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255023 | ````` <\|EXTRA_4_TOKEN\|> ````` | 0.000225498 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255003 | ````` <\|NO_TOKEN\|> `````      | 0.000225528 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255009 | ````` <\|USER_0_TOKEN\|> `````  | 0.000225718 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
<details><summary>6 additional entries below threshold</summary>

|   token_id | token                           |   indicator | max_prob                                                         |
|------------|---------------------------------|-------------|------------------------------------------------------------------|
|     255021 | ````` <\|EXTRA_2_TOKEN\|> ````` | 0.000225797 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255015 | ````` <\|USER_6_TOKEN\|> `````  | 0.000228018 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255010 | ````` <\|USER_1_TOKEN\|> `````  | 0.000228198 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255017 | ````` <\|USER_8_TOKEN\|> `````  | 0.000228818 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|     255002 | ````` <\|YES_TOKEN\|> `````     | 0.000232713 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> |
|          7 | ````` <EOP_TOKEN> `````         | 0.135308    | <span style='border: 1px solid rgb(169, 68, 66);'>4.3e-07</span> |
</details>


## Unreachable tokens
1403 entries below threshold of 0.492

|   token_id | token            |   indicator | reencoded                                                                        |
|------------|------------------|-------------|----------------------------------------------------------------------------------|
|        344 | ````` ¿♦? `````  | 0.000160212 | 238161: ````` ♦ `````                                                            |
|        275 | ````` ¿↙? `````  | 0.000161483 | 76876: ````` <0xE2><0x86> `````, 255: ````` <0x99> `````                         |
|        289 | ````` ¿⏰? ````` | 0.000161622 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 116: ````` <0xB0> `````        |
|        445 | ````` ¿🆔? ````` | 0.000162919 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 250: ````` <0x94> ````` |
|        522 | ````` ¿🌝? ````` | 0.000163306 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 259: ````` <0x9D> ````` |
|        430 | ````` ¿〰? ````` | 0.000163704 | 1800: ````` <0xE3><0x80> `````, 116: ````` <0xB0> `````                          |
|        460 | ````` ¿🇮? `````  | 0.000164286 | 31122: ````` 🇮 `````                                                             |
|        293 | ````` ¿⏸? `````  | 0.000164356 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 124: ````` <0xB8> `````        |
|        346 | ````` ¿♻? `````  | 0.000164944 | 45687: ````` <0xE2><0x99> `````, 127: ````` <0xBB> `````                         |
|        305 | ````` ¿☀? `````  | 0.000164997 | 34133: ````` <0xE2><0x98> `````, 230: ````` <0x80> `````                         |
|        405 | ````` ¿❄? `````  | 0.000165057 | 135523: ````` <0xE2><0x9D> `````, 234: ````` <0x84> `````                        |
|        326 | ````` ¿♀? `````  | 0.000165116 | 45687: ````` <0xE2><0x99> `````, 230: ````` <0x80> `````                         |
|        426 | ````` ¿⬛? ````` | 0.000165237 | 166: ````` <0xE2> `````, 113: ````` <0xAC> `````, 257: ````` <0x9B> `````        |
|        306 | ````` ¿☁? `````  | 0.000165257 | 34133: ````` <0xE2><0x98> `````, 231: ````` <0x81> `````                         |
|        301 | ````` ¿◻? `````  | 0.000165421 | 37357: ````` <0xE2><0x97> `````, 127: ````` <0xBB> `````                         |
|        526 | ````` ¿🌡? `````  | 0.000165706 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 102: ````` <0xA1> ````` |
|        284 | ````` ¿⏫? ````` | 0.000165912 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 112: ````` <0xAB> `````        |
|        328 | ````` ¿♈? ````` | 0.000165975 | 45687: ````` <0xE2><0x99> `````, 238: ````` <0x88> `````                         |
|        437 | ````` ¿🅰? `````  | 0.000166041 | 2226: ````` <0xF0><0x9F> `````, 235: ````` <0x85> `````, 116: ````` <0xB0> ````` |
|        317 | ````` ¿☢? `````  | 0.00016617  | 34133: ````` <0xE2><0x98> `````, 103: ````` <0xA2> `````                         |
<details><summary>1383 additional entries below threshold</summary>

|   token_id | token                    |   indicator | reencoded                                                                        |
|------------|--------------------------|-------------|----------------------------------------------------------------------------------|
|        332 | ````` ¿♌? `````         | 0.000166249 | 45687: ````` <0xE2><0x99> `````, 242: ````` <0x8C> `````                         |
|        268 | ````` ¿™? `````          | 0.000166314 | 33572: ````` ™ `````                                                             |
|        298 | ````` ¿▫? `````          | 0.0001664   | 29034: ````` <0xE2><0x96> `````, 112: ````` <0xAB> `````                         |
|        279 | ````` ¿⌛? `````         | 0.000166599 | 166: ````` <0xE2> `````, 242: ````` <0x8C> `````, 257: ````` <0x9B> `````        |
|        439 | ````` ¿🅾? `````          | 0.00016669  | 2226: ````` <0xF0><0x9F> `````, 235: ````` <0x85> `````, 130: ````` <0xBE> ````` |
|        442 | ````` ¿🆑? `````         | 0.000166971 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 247: ````` <0x91> ````` |
|        465 | ````` ¿🇳? `````          | 0.000167032 | 29878: ````` 🇳 `````                                                             |
|        518 | ````` ¿🌙? `````         | 0.000167042 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 255: ````` <0x99> ````` |
|        422 | ````` ¿⤵? `````          | 0.000167181 | 166: ````` <0xE2> `````, 105: ````` <0xA4> `````, 121: ````` <0xB5> `````        |
|        313 | ````` ¿☕? `````         | 0.000167293 | 34133: ````` <0xE2><0x98> `````, 251: ````` <0x95> `````                         |
|        435 | ````` ¿🀄? `````         | 0.000167372 | 2226: ````` <0xF0><0x9F> `````, 230: ````` <0x80> `````, 234: ````` <0x84> ````` |
|        503 | ````` ¿🌊? `````         | 0.000167385 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 240: ````` <0x8A> ````` |
|        294 | ````` ¿⏹? `````          | 0.000167426 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 125: ````` <0xB9> `````        |
|        300 | ````` ¿◀? `````          | 0.000167459 | 37357: ````` <0xE2><0x97> `````, 230: ````` <0x80> `````                         |
|        541 | ````` ¿🌲? `````         | 0.000167558 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 118: ````` <0xB2> ````` |
|        450 | ````` ¿🆙? `````         | 0.000167568 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 255: ````` <0x99> ````` |
|        528 | ````` ¿🌥? `````          | 0.00016759  | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 106: ````` <0xA5> ````` |
|        327 | ````` ¿♂? `````          | 0.000167634 | 232883: ````` ♂ `````                                                            |
|        495 | ````` ¿🌂? `````         | 0.000167662 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 232: ````` <0x82> ````` |
|        290 | ````` ¿⏱? `````          | 0.000167695 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 117: ````` <0xB1> `````        |
|        312 | ````` ¿☔? `````         | 0.000167754 | 34133: ````` <0xE2><0x98> `````, 250: ````` <0x94> `````                         |
|        283 | ````` ¿⏪? `````         | 0.000167766 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 111: ````` <0xAA> `````        |
|        423 | ````` ¿⬅? `````          | 0.000167834 | 166: ````` <0xE2> `````, 113: ````` <0xAC> `````, 235: ````` <0x85> `````        |
|        549 | ````` ¿🌺? `````         | 0.00016791  | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 126: ````` <0xBA> ````` |
|        373 | ````` ¿⛓? `````          | 0.000167966 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 249: ````` <0x93> `````        |
|        546 | ````` ¿🌷? `````         | 0.000168025 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 123: ````` <0xB7> ````` |
|        365 | ````` ¿⚽? `````         | 0.000168119 | 175142: ````` <0xE2><0x9A> `````, 129: ````` <0xBD> `````                        |
|        534 | ````` ¿🌫? `````          | 0.000168361 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 112: ````` <0xAB> ````` |
|        466 | ````` ¿🇴? `````          | 0.000168365 | 40228: ````` 🇴 `````                                                             |
|        494 | ````` ¿🌁? `````         | 0.000168445 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 231: ````` <0x81> ````` |
|        342 | ````` ¿♣? `````          | 0.000168535 | 45687: ````` <0xE2><0x99> `````, 104: ````` <0xA3> `````                         |
|        334 | ````` ¿♎? `````         | 0.000168577 | 45687: ````` <0xE2><0x99> `````, 244: ````` <0x8E> `````                         |
|        550 | ````` ¿🌻? `````         | 0.000168578 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 127: ````` <0xBB> ````` |
|        492 | ````` ¿🉑? `````         | 0.000168586 | 2226: ````` <0xF0><0x9F> `````, 239: ````` <0x89> `````, 247: ````` <0x91> ````` |
|        481 | ````` ¿🈯? `````         | 0.000168708 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 115: ````` <0xAF> ````` |
|        402 | ````` ¿✨? `````         | 0.000168792 | 70336: ````` <0xE2><0x9C> `````, 109: ````` <0xA8> `````                         |
|        266 | ````` ¿⁉? `````          | 0.000168795 | 36937: ````` <0xE2><0x81> `````, 239: ````` <0x89> `````                         |
|        484 | ````` ¿🈴? `````         | 0.000169017 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 120: ````` <0xB4> ````` |
|        424 | ````` ¿⬆? `````          | 0.000169038 | 166: ````` <0xE2> `````, 113: ````` <0xAC> `````, 236: ````` <0x86> `````        |
|        468 | ````` ¿🇶? `````          | 0.000169064 | 144576: ````` 🇶 `````                                                            |
|        307 | ````` ¿☂? `````          | 0.000169119 | 34133: ````` <0xE2><0x98> `````, 232: ````` <0x82> `````                         |
|        497 | ````` ¿🌄? `````         | 0.000169124 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 234: ````` <0x84> ````` |
|        272 | ````` ¿↖? `````          | 0.000169221 | 76876: ````` <0xE2><0x86> `````, 252: ````` <0x96> `````                         |
|        502 | ````` ¿🌉? `````         | 0.000169327 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 239: ````` <0x89> ````` |
|        542 | ````` ¿🌳? `````         | 0.00016933  | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 119: ````` <0xB3> ````` |
|        493 | ````` ¿🌀? `````         | 0.000169452 | 2226: ````` <0xF0><0x9F> `````, 3388: ````` <0x8C><0x80> `````                   |
|        364 | ````` ¿⚱? `````          | 0.000169459 | 175142: ````` <0xE2><0x9A> `````, 117: ````` <0xB1> `````                        |
|        436 | ````` ¿🃏? `````         | 0.000169547 | 2226: ````` <0xF0><0x9F> `````, 233: ````` <0x83> `````, 245: ````` <0x8F> ````` |
|        341 | ````` ¿♠? `````          | 0.000169701 | 45687: ````` <0xE2><0x99> `````, 262: ````` <0xA0> `````                         |
|        444 | ````` ¿🆓? `````         | 0.000169724 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 249: ````` <0x93> ````` |
|        396 | ````` ¿✏? `````          | 0.000169735 | 70336: ````` <0xE2><0x9C> `````, 245: ````` <0x8F> `````                         |
|        409 | ````` ¿❓? `````         | 0.000169752 | 135523: ````` <0xE2><0x9D> `````, 249: ````` <0x93> `````                        |
|        463 | ````` ¿🇱? `````          | 0.000169789 | 24385: ````` 🇱 `````                                                             |
|        496 | ````` ¿🌃? `````         | 0.000169814 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 233: ````` <0x83> ````` |
|        548 | ````` ¿🌹? `````         | 0.000170047 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 125: ````` <0xB9> ````` |
|        397 | ````` ¿✒? `````          | 0.000170127 | 70336: ````` <0xE2><0x9C> `````, 248: ````` <0x92> `````                         |
|        505 | ````` ¿🌌? `````         | 0.000170164 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 242: ````` <0x8C> ````` |
|        406 | ````` ¿❇? `````          | 0.000170167 | 135523: ````` <0xE2><0x9D> `````, 237: ````` <0x87> `````                        |
|        352 | ````` ¿⚕? `````          | 0.00017023  | 175142: ````` <0xE2><0x9A> `````, 251: ````` <0x95> `````                        |
|        386 | ````` ¿⛺? `````         | 0.000170361 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 126: ````` <0xBA> `````        |
|        543 | ````` ¿🌴? `````         | 0.000170363 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 120: ````` <0xB4> ````` |
|        453 | ````` ¿🇧? `````          | 0.000170465 | 90978: ````` 🇧 `````                                                             |
|        425 | ````` ¿⬇? `````          | 0.000170501 | 166: ````` <0xE2> `````, 113: ````` <0xAC> `````, 237: ````` <0x87> `````        |
|        388 | ````` ¿✂? `````          | 0.000170537 | 70336: ````` <0xE2><0x9C> `````, 232: ````` <0x82> `````                         |
|        372 | ````` ¿⛑? `````          | 0.00017056  | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 247: ````` <0x91> `````        |
|        532 | ````` ¿🌩? `````          | 0.00017063  | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 110: ````` <0xA9> ````` |
|        523 | ````` ¿🌞? `````         | 0.000170735 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 260: ````` <0x9E> ````` |
|        499 | ````` ¿🌆? `````         | 0.000170867 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 236: ````` <0x86> ````` |
|        478 | ````` ¿🈁? `````         | 0.000170892 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 231: ````` <0x81> ````` |
|        363 | ````` ¿⚰? `````          | 0.000171015 | 175142: ````` <0xE2><0x9A> `````, 116: ````` <0xB0> `````                        |
|        270 | ````` ¿↔? `````          | 0.000171064 | 76876: ````` <0xE2><0x86> `````, 250: ````` <0x94> `````                         |
|        475 | ````` ¿🇽? `````          | 0.000171079 | 2244: ````` <0xF0><0x9F><0x87> `````, 129: ````` <0xBD> `````                    |
|        336 | ````` ¿♐? `````         | 0.000171142 | 45687: ````` <0xE2><0x99> `````, 246: ````` <0x90> `````                         |
|        420 | ````` ¿➿? `````         | 0.000171164 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 131: ````` <0xBF> `````        |
|        519 | ````` ¿🌚? `````         | 0.00017122  | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 256: ````` <0x9A> ````` |
|        433 | ````` ¿㊙? `````         | 0.000171309 | 167: ````` <0xE3> `````, 240: ````` <0x8A> `````, 255: ````` <0x99> `````        |
|        368 | ````` ¿⛅? `````         | 0.000171344 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 235: ````` <0x85> `````        |
|        357 | ````` ¿⚜? `````          | 0.000171493 | 175142: ````` <0xE2><0x9A> `````, 258: ````` <0x9C> `````                        |
|        339 | ````` ¿♓? `````         | 0.000171496 | 45687: ````` <0xE2><0x99> `````, 249: ````` <0x93> `````                         |
|        432 | ````` ¿㊗? `````         | 0.000171516 | 167: ````` <0xE3> `````, 240: ````` <0x8A> `````, 253: ````` <0x97> `````        |
|        315 | ````` ¿☝? `````          | 0.000171738 | 34133: ````` <0xE2><0x98> `````, 259: ````` <0x9D> `````                         |
|        319 | ````` ¿☦? `````          | 0.00017177  | 34133: ````` <0xE2><0x98> `````, 107: ````` <0xA6> `````                         |
|        476 | ````` ¿🇾? `````          | 0.000171831 | 100210: ````` 🇾 `````                                                            |
|        443 | ````` ¿🆒? `````         | 0.000171896 | 2226: ````` <0xF0><0x9F> `````, 9519: ````` <0x86><0x92> `````                   |
|        309 | ````` ¿☄? `````          | 0.000171953 | 34133: ````` <0xE2><0x98> `````, 234: ````` <0x84> `````                         |
|        513 | ````` ¿🌔? `````         | 0.00017206  | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 250: ````` <0x94> ````` |
|        330 | ````` ¿♊? `````         | 0.000172132 | 45687: ````` <0xE2><0x99> `````, 240: ````` <0x8A> `````                         |
|        459 | ````` ¿🇭? `````          | 0.000172161 | 39476: ````` 🇭 `````                                                             |
|        316 | ````` ¿☠? `````          | 0.000172172 | 34133: ````` <0xE2><0x98> `````, 262: ````` <0xA0> `````                         |
|        398 | ````` ¿✔? `````          | 0.000172231 | 189894: ````` ✔ `````                                                            |
|        415 | ````` ¿➕? `````         | 0.000172353 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 251: ````` <0x95> `````        |
|        517 | ````` ¿🌘? `````         | 0.000172432 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 254: ````` <0x98> ````` |
|        380 | ````` ¿⛳? `````         | 0.000172448 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 119: ````` <0xB3> `````        |
|        349 | ````` ¿⚒? `````          | 0.000172465 | 175142: ````` <0xE2><0x9A> `````, 248: ````` <0x92> `````                        |
|        485 | ````` ¿🈵? `````         | 0.000172486 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 121: ````` <0xB5> ````` |
|        524 | ````` ¿🌟? `````         | 0.000172559 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 261: ````` <0x9F> ````` |
|        507 | ````` ¿🌎? `````         | 0.00017264  | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 244: ````` <0x8E> ````` |
|        462 | ````` ¿🇰? `````          | 0.000172642 | 30269: ````` 🇰 `````                                                             |
|        438 | ````` ¿🅱? `````          | 0.000172663 | 2226: ````` <0xF0><0x9F> `````, 235: ````` <0x85> `````, 117: ````` <0xB1> ````` |
|        418 | ````` ¿➡? `````          | 0.000172702 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 102: ````` <0xA1> `````        |
|        483 | ````` ¿🈳? `````         | 0.000172817 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 119: ````` <0xB3> ````` |
|        547 | ````` ¿🌸? `````         | 0.000172862 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 124: ````` <0xB8> ````` |
|        474 | ````` ¿🇼? `````          | 0.000172928 | 108080: ````` 🇼 `````                                                            |
|        545 | ````` ¿🌶? `````          | 0.000172932 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 122: ````` <0xB6> ````` |
|        417 | ````` ¿➗? `````         | 0.000172967 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 253: ````` <0x97> `````        |
|        370 | ````` ¿⛎? `````         | 0.000173102 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 244: ````` <0x8E> `````        |
|        347 | ````` ¿♾? `````          | 0.000173115 | 45687: ````` <0xE2><0x99> `````, 130: ````` <0xBE> `````                         |
|        535 | ````` ¿🌬? `````          | 0.000173118 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 113: ````` <0xAC> ````` |
|        274 | ````` ¿↘? `````          | 0.000173218 | 76876: ````` <0xE2><0x86> `````, 254: ````` <0x98> `````                         |
|        308 | ````` ¿☃? `````          | 0.000173235 | 34133: ````` <0xE2><0x98> `````, 233: ````` <0x83> `````                         |
|        458 | ````` ¿🇬? `````          | 0.000173287 | 42828: ````` 🇬 `````                                                             |
|        288 | ````` ¿⏯? `````          | 0.000173347 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 115: ````` <0xAF> `````        |
|        375 | ````` ¿⛩? `````          | 0.000173375 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 110: ````` <0xA9> `````        |
|        381 | ````` ¿⛴? `````          | 0.000173448 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 120: ````` <0xB4> `````        |
|        389 | ````` ¿✅? `````         | 0.000173482 | 214871: ````` ✅ `````                                                           |
|        340 | ````` ¿♟? `````          | 0.000173545 | 45687: ````` <0xE2><0x99> `````, 261: ````` <0x9F> `````                         |
|        414 | ````` ¿❤? `````          | 0.000173583 | 135523: ````` <0xE2><0x9D> `````, 105: ````` <0xA4> `````                        |
|        311 | ````` ¿☑? `````          | 0.000173599 | 34133: ````` <0xE2><0x98> `````, 247: ````` <0x91> `````                         |
|        419 | ````` ¿➰? `````         | 0.000173722 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 116: ````` <0xB0> `````        |
|        451 | ````` ¿🆚? `````         | 0.000173742 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 256: ````` <0x9A> ````` |
|        520 | ````` ¿🌛? `````         | 0.000173998 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 257: ````` <0x9B> ````` |
|        401 | ````` ¿✡? `````          | 0.000174062 | 70336: ````` <0xE2><0x9C> `````, 102: ````` <0xA1> `````                         |
|        469 | ````` ¿🇷? `````          | 0.0001741   | 7534: ````` 🇷 `````                                                              |
|        383 | ````` ¿⛷? `````          | 0.000174152 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 123: ````` <0xB7> `````        |
|        514 | ````` ¿🌕? `````         | 0.000174154 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 251: ````` <0x95> ````` |
|        351 | ````` ¿⚔? `````          | 0.000174188 | 175142: ````` <0xE2><0x9A> `````, 250: ````` <0x94> `````                        |
|        318 | ````` ¿☣? `````          | 0.000174206 | 34133: ````` <0xE2><0x98> `````, 104: ````` <0xA3> `````                         |
|        366 | ````` ¿⚾? `````         | 0.000174311 | 175142: ````` <0xE2><0x9A> `````, 130: ````` <0xBE> `````                        |
|        291 | ````` ¿⏲? `````          | 0.000174435 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 118: ````` <0xB2> `````        |
|        411 | ````` ¿❕? `````         | 0.000174803 | 135523: ````` <0xE2><0x9D> `````, 251: ````` <0x95> `````                        |
|        516 | ````` ¿🌗? `````         | 0.000175029 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 253: ````` <0x97> ````` |
|        395 | ````` ¿✍? `````          | 0.000175029 | 70336: ````` <0xE2><0x9C> `````, 243: ````` <0x8D> `````                         |
|        521 | ````` ¿🌜? `````         | 0.000175069 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 258: ````` <0x9C> ````` |
|        333 | ````` ¿♍? `````         | 0.000175186 | 45687: ````` <0xE2><0x99> `````, 243: ````` <0x8D> `````                         |
|        525 | ````` ¿🌠? `````         | 0.0001752   | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 262: ````` <0xA0> ````` |
|        491 | ````` ¿🉐? `````         | 0.000175284 | 2226: ````` <0xF0><0x9F> `````, 239: ````` <0x89> `````, 246: ````` <0x90> ````` |
|        286 | ````` ¿⏭? `````          | 0.000175303 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 263: ````` <0xAD> `````        |
|        399 | ````` ¿✖? `````          | 0.000175371 | 70336: ````` <0xE2><0x9C> `````, 252: ````` <0x96> `````                         |
|        320 | ````` ¿☪? `````          | 0.000175935 | 34133: ````` <0xE2><0x98> `````, 111: ````` <0xAA> `````                         |
|        511 | ````` ¿🌒? `````         | 0.000175963 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 248: ````` <0x92> ````` |
|        403 | ````` ¿✳? `````          | 0.000176155 | 70336: ````` <0xE2><0x9C> `````, 119: ````` <0xB3> `````                         |
|        295 | ````` ¿⏺? `````          | 0.00017616  | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 126: ````` <0xBA> `````        |
|        506 | ````` ¿🌍? `````         | 0.000176194 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 243: ````` <0x8D> ````` |
|        486 | ````` ¿🈶? `````         | 0.000176248 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 122: ````` <0xB6> ````` |
|        427 | ````` ¿⬜? `````         | 0.00017632  | 166: ````` <0xE2> `````, 113: ````` <0xAC> `````, 258: ````` <0x9C> `````        |
|        446 | ````` ¿🆕? `````         | 0.000176355 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 251: ````` <0x95> ````` |
|        508 | ````` ¿🌏? `````         | 0.000176516 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 245: ````` <0x8F> ````` |
|        413 | ````` ¿❣? `````          | 0.00017652  | 135523: ````` <0xE2><0x9D> `````, 104: ````` <0xA3> `````                        |
|        461 | ````` ¿🇯? `````          | 0.000176631 | 169789: ````` 🇯 `````                                                            |
|        269 | ````` ¿ℹ? `````          | 0.000176657 | 27829: ````` <0xE2><0x84> `````, 125: ````` <0xB9> `````                         |
|        314 | ````` ¿☘? `````          | 0.000176742 | 34133: ````` <0xE2><0x98> `````, 254: ````` <0x98> `````                         |
|        472 | ````` ¿🇺? `````          | 0.000176762 | 9554: ````` 🇺 `````                                                              |
|        490 | ````` ¿🈺? `````         | 0.00017683  | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 126: ````` <0xBA> ````` |
|        285 | ````` ¿⏬? `````         | 0.00017686  | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 113: ````` <0xAC> `````        |
|        361 | ````` ¿⚪? `````         | 0.000176882 | 175142: ````` <0xE2><0x9A> `````, 111: ````` <0xAA> `````                        |
|        338 | ````` ¿♒? `````         | 0.000176976 | 45687: ````` <0xE2><0x99> `````, 248: ````` <0x92> `````                         |
|        385 | ````` ¿⛹? `````          | 0.000177062 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 125: ````` <0xB9> `````        |
|        540 | ````` ¿🌱? `````         | 0.000177099 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 117: ````` <0xB1> ````` |
|        471 | ````` ¿🇹? `````          | 0.000177101 | 10591: ````` 🇹 `````                                                             |
|        292 | ````` ¿⏳? `````         | 0.000177233 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 119: ````` <0xB3> `````        |
|        304 | ````` ¿◾? `````         | 0.00017738  | 37357: ````` <0xE2><0x97> `````, 130: ````` <0xBE> `````                         |
|        384 | ````` ¿⛸? `````          | 0.000177411 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 124: ````` <0xB8> `````        |
|        510 | ````` ¿🌑? `````         | 0.000177415 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 247: ````` <0x91> ````` |
|        358 | ````` ¿⚠? `````          | 0.000177499 | 175142: ````` <0xE2><0x9A> `````, 262: ````` <0xA0> `````                        |
|        538 | ````` ¿🌯? `````         | 0.000177585 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 115: ````` <0xAF> ````` |
|        480 | ````` ¿🈚? `````         | 0.000177619 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 256: ````` <0x9A> ````` |
|        354 | ````` ¿⚗? `````          | 0.000177696 | 175142: ````` <0xE2><0x9A> `````, 253: ````` <0x97> `````                        |
|        464 | ````` ¿🇲? `````          | 0.000177844 | 62579: ````` 🇲 `````                                                             |
|        501 | ````` ¿🌈? `````         | 0.00017796  | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 238: ````` <0x88> ````` |
|        335 | ````` ¿♏? `````         | 0.000178007 | 45687: ````` <0xE2><0x99> `````, 245: ````` <0x8F> `````                         |
|        392 | ````` ¿✊? `````         | 0.00017809  | 70336: ````` <0xE2><0x9C> `````, 240: ````` <0x8A> `````                         |
|        324 | ````` ¿☹? `````          | 0.000178093 | 34133: ````` <0xE2><0x98> `````, 125: ````` <0xB9> `````                         |
|        299 | ````` ¿▶? `````          | 0.000178102 | 29034: ````` <0xE2><0x96> `````, 122: ````` <0xB6> `````                         |
|        455 | ````` ¿🇩? `````          | 0.000178135 | 66360: ````` 🇩 `````                                                             |
|        287 | ````` ¿⏮? `````          | 0.000178136 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 114: ````` <0xAE> `````        |
|        498 | ````` ¿🌅? `````         | 0.000178273 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 235: ````` <0x85> ````` |
|        488 | ````` ¿🈸? `````         | 0.000178405 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 124: ````` <0xB8> ````` |
|        369 | ````` ¿⛈? `````          | 0.000178409 | 166: ````` <0xE2> `````, 32197: ````` <0x9B><0x88> `````                         |
|        343 | ````` ¿♥? `````          | 0.000178414 | 171540: ````` ♥ `````                                                            |
|        377 | ````` ¿⛰? `````          | 0.000178472 | 166: ````` <0xE2> `````, 71996: ````` <0x9B><0xB0> `````                         |
|        421 | ````` ¿⤴? `````          | 0.000178802 | 166: ````` <0xE2> `````, 105: ````` <0xA4> `````, 120: ````` <0xB4> `````        |
|        278 | ````` ¿⌚? `````         | 0.000178853 | 166: ````` <0xE2> `````, 242: ````` <0x8C> `````, 256: ````` <0x9A> `````        |
|        487 | ````` ¿🈷? `````         | 0.000178853 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 123: ````` <0xB7> ````` |
|        276 | ````` ¿↩? `````          | 0.000178873 | 76876: ````` <0xE2><0x86> `````, 110: ````` <0xA9> `````                         |
|        470 | ````` ¿🇸? `````          | 0.00017892  | 6705: ````` 🇸 `````                                                              |
|        551 | ````` ¿🌼? `````         | 0.000179172 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 128: ````` <0xBC> ````` |
|        310 | ````` ¿☎? `````          | 0.000179209 | 34133: ````` <0xE2><0x98> `````, 244: ````` <0x8E> `````                         |
|        359 | ````` ¿⚡? `````         | 0.000179235 | 175142: ````` <0xE2><0x9A> `````, 102: ````` <0xA1> `````                        |
|        360 | ````` ¿⚧? `````          | 0.000179264 | 175142: ````` <0xE2><0x9A> `````, 108: ````` <0xA7> `````                        |
|        379 | ````` ¿⛲? `````         | 0.000179305 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 118: ````` <0xB2> `````        |
|        452 | ````` ¿🇦? `````          | 0.0001794   | 21170: ````` 🇦 `````                                                             |
|        302 | ````` ¿◼? `````          | 0.0001794   | 37357: ````` <0xE2><0x97> `````, 128: ````` <0xBC> `````                         |
|        531 | ````` ¿🌨? `````          | 0.00017941  | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 109: ````` <0xA8> ````` |
|        512 | ````` ¿🌓? `````         | 0.000179531 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 249: ````` <0x93> ````` |
|        539 | ````` ¿🌰? `````         | 0.000179628 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 116: ````` <0xB0> ````` |
|        267 | ````` ¿⃣? `````           | 0.000179681 | 166: ````` <0xE2> `````, 233: ````` <0x83> `````, 104: ````` <0xA3> `````        |
|        331 | ````` ¿♋? `````         | 0.000179876 | 45687: ````` <0xE2><0x99> `````, 241: ````` <0x8B> `````                         |
|        273 | ````` ¿↗? `````          | 0.000179899 | 76876: ````` <0xE2><0x86> `````, 253: ````` <0x97> `````                         |
|        297 | ````` ¿▪? `````          | 0.000180027 | 237072: ````` ▪ `````                                                            |
|        404 | ````` ¿✴? `````          | 0.000180063 | 70336: ````` <0xE2><0x9C> `````, 120: ````` <0xB4> `````                         |
|        277 | ````` ¿↪? `````          | 0.00018013  | 76876: ````` <0xE2><0x86> `````, 111: ````` <0xAA> `````                         |
|        282 | ````` ¿⏩? `````         | 0.000180136 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 110: ````` <0xA9> `````        |
|        390 | ````` ¿✈? `````          | 0.000180251 | 70336: ````` <0xE2><0x9C> `````, 238: ````` <0x88> `````                         |
|        408 | ````` ¿❎? `````         | 0.000180281 | 135523: ````` <0xE2><0x9D> `````, 244: ````` <0x8E> `````                        |
|        348 | ````` ¿♿? `````         | 0.00018031  | 45687: ````` <0xE2><0x99> `````, 131: ````` <0xBF> `````                         |
|        440 | ````` ¿🅿? `````          | 0.000180384 | 2226: ````` <0xF0><0x9F> `````, 235: ````` <0x85> `````, 131: ````` <0xBF> ````` |
|        544 | ````` ¿🌵? `````         | 0.000180402 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 121: ````` <0xB5> ````` |
|        394 | ````` ¿✌? `````          | 0.000180511 | 70336: ````` <0xE2><0x9C> `````, 242: ````` <0x8C> `````                         |
|        264 | ````` ¿\u200d? `````     | 0.00018053  | 35927: ````` \u200d `````                                                        |
|        577 | ````` ¿🍖? `````         | 0.000180566 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 252: ````` <0x96> ````` |
|        410 | ````` ¿❔? `````         | 0.000180594 | 135523: ````` <0xE2><0x9D> `````, 250: ````` <0x94> `````                        |
|        387 | ````` ¿⛽? `````         | 0.000180615 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 129: ````` <0xBD> `````        |
|        400 | ````` ¿✝? `````          | 0.00018069  | 70336: ````` <0xE2><0x9C> `````, 259: ````` <0x9D> `````                         |
|        447 | ````` ¿🆖? `````         | 0.000180796 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 252: ````` <0x96> ````` |
|        449 | ````` ¿🆘? `````         | 0.000180842 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 254: ````` <0x98> ````` |
|        391 | ````` ¿✉? `````          | 0.000180916 | 70336: ````` <0xE2><0x9C> `````, 239: ````` <0x89> `````                         |
|        473 | ````` ¿🇻? `````          | 0.000180963 | 99202: ````` 🇻 `````                                                             |
|        303 | ````` ¿◽? `````         | 0.000180974 | 37357: ````` <0xE2><0x97> `````, 129: ````` <0xBD> `````                         |
|        329 | ````` ¿♉? `````         | 0.000181073 | 45687: ````` <0xE2><0x99> `````, 239: ````` <0x89> `````                         |
|        337 | ````` ¿♑? `````         | 0.000181134 | 45687: ````` <0xE2><0x99> `````, 247: ````` <0x91> `````                         |
|        371 | ````` ¿⛏? `````          | 0.000181194 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 245: ````` <0x8F> `````        |
|        280 | ````` ¿⌨? `````          | 0.000181249 | 166: ````` <0xE2> `````, 242: ````` <0x8C> `````, 109: ````` <0xA8> `````        |
|        454 | ````` ¿🇨? `````          | 0.000181277 | 62600: ````` 🇨 `````                                                             |
|        345 | ````` ¿♨? `````          | 0.000181466 | 45687: ````` <0xE2><0x99> `````, 109: ````` <0xA8> `````                         |
|        367 | ````` ¿⛄? `````         | 0.000181512 | 166: ````` <0xE2> `````, 7840: ````` <0x9B><0x84> `````                          |
|        271 | ````` ¿↕? `````          | 0.000181542 | 76876: ````` <0xE2><0x86> `````, 251: ````` <0x95> `````                         |
|        429 | ````` ¿⭕? `````         | 0.000181622 | 166: ````` <0xE2> `````, 263: ````` <0xAD> `````, 251: ````` <0x95> `````        |
|        323 | ````` ¿☸? `````          | 0.000181738 | 34133: ````` <0xE2><0x98> `````, 124: ````` <0xB8> `````                         |
|        431 | ````` ¿〽? `````         | 0.000181741 | 1800: ````` <0xE3><0x80> `````, 129: ````` <0xBD> `````                          |
|        615 | ````` ¿🍼? `````         | 0.000181752 | 2226: ````` <0xF0><0x9F> `````, 22059: ````` <0x8D><0xBC> `````                  |
|        362 | ````` ¿⚫? `````         | 0.00018181  | 175142: ````` <0xE2><0x9A> `````, 112: ````` <0xAB> `````                        |
|        321 | ````` ¿☮? `````          | 0.000181865 | 34133: ````` <0xE2><0x98> `````, 114: ````` <0xAE> `````                         |
|        448 | ````` ¿🆗? `````         | 0.00018193  | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 253: ````` <0x97> ````` |
|        467 | ````` ¿🇵? `````          | 0.000182267 | 137446: ````` 🇵 `````                                                            |
|        296 | ````` ¿Ⓜ? `````          | 0.000182334 | 166: ````` <0xE2> `````, 249: ````` <0x93> `````, 232: ````` <0x82> `````        |
|        281 | ````` ¿⏏? `````          | 0.000182466 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 245: ````` <0x8F> `````        |
|        355 | ````` ¿⚙? `````          | 0.000182564 | 175142: ````` <0xE2><0x9A> `````, 255: ````` <0x99> `````                        |
|        416 | ````` ¿➖? `````         | 0.000182625 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 252: ````` <0x96> `````        |
|        489 | ````` ¿🈹? `````         | 0.000182661 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 125: ````` <0xB9> ````` |
|        325 | ````` ¿☺? `````          | 0.000182718 | 34133: ````` <0xE2><0x98> `````, 126: ````` <0xBA> `````                         |
|        428 | ````` ¿⭐? `````         | 0.000182773 | 137546: ````` ⭐ `````                                                           |
|        407 | ````` ¿❌? `````         | 0.000182961 | 135523: ````` <0xE2><0x9D> `````, 242: ````` <0x8C> `````                        |
|        533 | ````` ¿🌪? `````          | 0.000182981 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 111: ````` <0xAA> ````` |
|        527 | ````` ¿🌤? `````          | 0.000182991 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 105: ````` <0xA4> ````` |
|        530 | ````` ¿🌧? `````          | 0.000183059 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 108: ````` <0xA7> ````` |
|        356 | ````` ¿⚛? `````          | 0.000183085 | 175142: ````` <0xE2><0x9A> `````, 257: ````` <0x9B> `````                        |
|        265 | ````` ¿‼? `````          | 0.000183185 | 1773: ````` <0xE2><0x80> `````, 128: ````` <0xBC> `````                          |
|        710 | ````` ¿🏠? `````         | 0.000183243 | 216125: ````` <0xF0><0x9F><0x8F> `````, 262: ````` <0xA0> `````                  |
|        350 | ````` ¿⚓? `````         | 0.000183443 | 175142: ````` <0xE2><0x9A> `````, 249: ````` <0x93> `````                        |
|        723 | ````` ¿🏭? `````         | 0.000183499 | 216125: ````` <0xF0><0x9F><0x8F> `````, 263: ````` <0xAD> `````                  |
|        617 | ````` ¿🍾? `````         | 0.000183573 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 130: ````` <0xBE> ````` |
|        479 | ````` ¿🈂? `````         | 0.000183789 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 232: ````` <0x82> ````` |
|        378 | ````` ¿⛱? `````          | 0.000183808 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 117: ````` <0xB1> `````        |
|        650 | ````` ¿🎤? `````         | 0.000183817 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 105: ````` <0xA4> ````` |
|        672 | ````` ¿🎺? `````         | 0.000183909 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 126: ````` <0xBA> ````` |
|        536 | ````` ¿🌭? `````         | 0.000184112 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 263: ````` <0xAD> ````` |
|        668 | ````` ¿🎶? `````         | 0.000184121 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 122: ````` <0xB6> ````` |
|        376 | ````` ¿⛪? `````         | 0.000184209 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 111: ````` <0xAA> `````        |
|        589 | ````` ¿🍢? `````         | 0.00018426  | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 103: ````` <0xA2> ````` |
|        374 | ````` ¿⛔? `````         | 0.0001845   | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 250: ````` <0x94> `````        |
|        456 | ````` ¿🇪? `````          | 0.000184509 | 8548: ````` 🇪 `````                                                              |
|        629 | ````` ¿🎊? `````         | 0.000184572 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 240: ````` <0x8A> ````` |
|        322 | ````` ¿☯? `````          | 0.000184637 | 34133: ````` <0xE2><0x98> `````, 115: ````` <0xAF> `````                         |
|        434 | ````` ¿️? `````           | 0.000184668 | 57462: ````` ️ `````                                                              |
|        611 | ````` ¿🍸? `````         | 0.000184709 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 124: ````` <0xB8> ````` |
|        726 | ````` ¿🏰? `````         | 0.000185043 | 216125: ````` <0xF0><0x9F><0x8F> `````, 116: ````` <0xB0> `````                  |
|        457 | ````` ¿🇫? `````          | 0.0001851   | 106104: ````` 🇫 `````                                                            |
|        605 | ````` ¿🍲? `````         | 0.000185139 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 118: ````` <0xB2> ````` |
|        353 | ````` ¿⚖? `````          | 0.000185324 | 175142: ````` <0xE2><0x9A> `````, 252: ````` <0x96> `````                        |
|        634 | ````` ¿🎏? `````         | 0.000185443 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 245: ````` <0x8F> ````` |
|        482 | ````` ¿🈲? `````         | 0.000185476 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 118: ````` <0xB2> ````` |
|        657 | ````` ¿🎫? `````         | 0.000185525 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 112: ````` <0xAB> ````` |
|        393 | ````` ¿✋? `````         | 0.00018555  | 70336: ````` <0xE2><0x9C> `````, 241: ````` <0x8B> `````                         |
|        610 | ````` ¿🍷? `````         | 0.000185599 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 123: ````` <0xB7> ````` |
|        382 | ````` ¿⛵? `````         | 0.00018566  | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 121: ````` <0xB5> `````        |
|        658 | ````` ¿🎬? `````         | 0.00018569  | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 113: ````` <0xAC> ````` |
|        537 | ````` ¿🌮? `````         | 0.000185704 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 114: ````` <0xAE> ````` |
|        732 | ````` ¿🏹? `````         | 0.000185738 | 216125: ````` <0xF0><0x9F><0x8F> `````, 125: ````` <0xB9> `````                  |
|        500 | ````` ¿🌇? `````         | 0.000185746 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 237: ````` <0x87> ````` |
|        712 | ````` ¿🏢? `````         | 0.000185847 | 216125: ````` <0xF0><0x9F><0x8F> `````, 103: ````` <0xA2> `````                  |
|        648 | ````` ¿🎢? `````         | 0.000185923 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 103: ````` <0xA2> ````` |
|        630 | ````` ¿🎋? `````         | 0.000186013 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 241: ````` <0x8B> ````` |
|        718 | ````` ¿🏨? `````         | 0.000186144 | 216125: ````` <0xF0><0x9F><0x8F> `````, 109: ````` <0xA8> `````                  |
|        441 | ````` ¿🆎? `````         | 0.000186194 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 244: ````` <0x8E> ````` |
|        654 | ````` ¿🎨? `````         | 0.000186197 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 109: ````` <0xA8> ````` |
|        735 | ````` ¿🏼? `````           | 0.000186227 | 216125: ````` <0xF0><0x9F><0x8F> `````, 128: ````` <0xBC> `````                  |
|        596 | ````` ¿🍩? `````         | 0.000186418 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 110: ````` <0xA9> ````` |
|        504 | ````` ¿🌋? `````         | 0.000186567 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 241: ````` <0x8B> ````` |
|        731 | ````` ¿🏸? `````         | 0.000186626 | 216125: ````` <0xF0><0x9F><0x8F> `````, 124: ````` <0xB8> `````                  |
|        561 | ````` ¿🍆? `````         | 0.000186669 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 236: ````` <0x86> ````` |
|        555 | ````` ¿🍀? `````         | 0.00018674  | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 230: ````` <0x80> ````` |
|        642 | ````` ¿🎚? `````          | 0.000186784 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 256: ````` <0x9A> ````` |
|        515 | ````` ¿🌖? `````         | 0.000186816 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 252: ````` <0x96> ````` |
|        675 | ````` ¿🎽? `````         | 0.000186825 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 129: ````` <0xBD> ````` |
|        708 | ````` ¿🏞? `````          | 0.000186984 | 216125: ````` <0xF0><0x9F><0x8F> `````, 260: ````` <0x9E> `````                  |
|        724 | ````` ¿🏮? `````         | 0.000186989 | 216125: ````` <0xF0><0x9F><0x8F> `````, 114: ````` <0xAE> `````                  |
|        678 | ````` ¿🏀? `````         | 0.000187039 | 216125: ````` <0xF0><0x9F><0x8F> `````, 230: ````` <0x80> `````                  |
|        643 | ````` ¿🎛? `````          | 0.000187339 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 257: ````` <0x9B> ````` |
|        595 | ````` ¿🍨? `````         | 0.000187402 | 2226: ````` <0xF0><0x9F> `````, 49252: ````` <0x8D><0xA8> `````                  |
|        509 | ````` ¿🌐? `````         | 0.000187429 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 246: ````` <0x90> ````` |
|        604 | ````` ¿🍱? `````         | 0.000187466 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 117: ````` <0xB1> ````` |
|        529 | ````` ¿🌦? `````          | 0.0001875   | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 107: ````` <0xA6> ````` |
|        573 | ````` ¿🍒? `````         | 0.000187516 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 248: ````` <0x92> ````` |
|        684 | ````` ¿🏆? `````         | 0.000187579 | 216125: ````` <0xF0><0x9F><0x8F> `````, 236: ````` <0x86> `````                  |
|        688 | ````` ¿🏊? `````         | 0.000187581 | 216125: ````` <0xF0><0x9F><0x8F> `````, 240: ````` <0x8A> `````                  |
|        635 | ````` ¿🎐? `````         | 0.000187702 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 246: ````` <0x90> ````` |
|        705 | ````` ¿🏛? `````          | 0.000187715 | 216125: ````` <0xF0><0x9F><0x8F> `````, 257: ````` <0x9B> `````                  |
|        702 | ````` ¿🏘? `````          | 0.000187784 | 216125: ````` <0xF0><0x9F><0x8F> `````, 254: ````` <0x98> `````                  |
|        674 | ````` ¿🎼? `````         | 0.000188168 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 128: ````` <0xBC> ````` |
|        730 | ````` ¿🏷? `````          | 0.000188385 | 216125: ````` <0xF0><0x9F><0x8F> `````, 123: ````` <0xB7> `````                  |
|        663 | ````` ¿🎱? `````         | 0.000188459 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 117: ````` <0xB1> ````` |
|        598 | ````` ¿🍫? `````         | 0.000188486 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 112: ````` <0xAB> ````` |
|        680 | ````` ¿🏂? `````         | 0.000188495 | 216125: ````` <0xF0><0x9F><0x8F> `````, 232: ````` <0x82> `````                  |
|        687 | ````` ¿🏉? `````         | 0.000188564 | 216125: ````` <0xF0><0x9F><0x8F> `````, 239: ````` <0x89> `````                  |
|        412 | ````` ¿❗? `````         | 0.000188689 | 135523: ````` <0xE2><0x9D> `````, 253: ````` <0x97> `````                        |
|        599 | ````` ¿🍬? `````         | 0.000188699 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 113: ````` <0xAC> ````` |
|        666 | ````` ¿🎴? `````         | 0.000188716 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 120: ````` <0xB4> ````` |
|        628 | ````` ¿🎉? `````         | 0.000188766 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 239: ````` <0x89> ````` |
|        649 | ````` ¿🎣? `````         | 0.000188767 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 104: ````` <0xA3> ````` |
|        554 | ````` ¿🌿? `````         | 0.000188797 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 131: ````` <0xBF> ````` |
|        720 | ````` ¿🏪? `````         | 0.000188885 | 216125: ````` <0xF0><0x9F><0x8F> `````, 111: ````` <0xAA> `````                  |
|        682 | ````` ¿🏄? `````         | 0.000188959 | 216125: ````` <0xF0><0x9F><0x8F> `````, 234: ````` <0x84> `````                  |
|        558 | ````` ¿🍃? `````         | 0.0001892   | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 233: ````` <0x83> ````` |
|        694 | ````` ¿🏐? `````         | 0.000189338 | 216125: ````` <0xF0><0x9F><0x8F> `````, 246: ````` <0x90> `````                  |
|        565 | ````` ¿🍊? `````         | 0.000189359 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 240: ````` <0x8A> ````` |
|        608 | ````` ¿🍵? `````         | 0.000189361 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 121: ````` <0xB5> ````` |
|        716 | ````` ¿🏦? `````         | 0.000189375 | 216125: ````` <0xF0><0x9F><0x8F> `````, 107: ````` <0xA6> `````                  |
|        719 | ````` ¿🏩? `````         | 0.000189599 | 216125: ````` <0xF0><0x9F><0x8F> `````, 110: ````` <0xA9> `````                  |
|        477 | ````` ¿🇿? `````          | 0.000189711 | 42240: ````` 🇿 `````                                                             |
|        572 | ````` ¿🍑? `````         | 0.0001898   | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 247: ````` <0x91> ````` |
|        686 | ````` ¿🏈? `````         | 0.000189871 | 216125: ````` <0xF0><0x9F><0x8F> `````, 238: ````` <0x88> `````                  |
|        609 | ````` ¿🍶? `````         | 0.000189967 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 122: ````` <0xB6> ````` |
|        698 | ````` ¿🏔? `````          | 0.000190073 | 216125: ````` <0xF0><0x9F><0x8F> `````, 250: ````` <0x94> `````                  |
|        651 | ````` ¿🎥? `````         | 0.000190351 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 106: ````` <0xA5> ````` |
|        614 | ````` ¿🍻? `````         | 0.000190412 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 127: ````` <0xBB> ````` |
|        632 | ````` ¿🎍? `````         | 0.00019048  | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 243: ````` <0x8D> ````` |
|        559 | ````` ¿🍄? `````         | 0.000190581 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 234: ````` <0x84> ````` |
|        562 | ````` ¿🍇? `````         | 0.000190601 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 237: ````` <0x87> ````` |
|        563 | ````` ¿🍈? `````         | 0.000190641 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 238: ````` <0x88> ````` |
|        677 | ````` ¿🎿? `````         | 0.000190716 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 131: ````` <0xBF> ````` |
|        568 | ````` ¿🍍? `````         | 0.000190876 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 243: ````` <0x8D> ````` |
|        633 | ````` ¿🎎? `````         | 0.000191298 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 244: ````` <0x8E> ````` |
|        553 | ````` ¿🌾? `````         | 0.000191612 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 130: ````` <0xBE> ````` |
|        722 | ````` ¿🏬? `````         | 0.00019164  | 216125: ````` <0xF0><0x9F><0x8F> `````, 113: ````` <0xAC> `````                  |
|        644 | ````` ¿🎞? `````          | 0.000191716 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 260: ````` <0x9E> ````` |
|        728 | ````` ¿🏴? `````         | 0.000191936 | 148987: ````` 🏴 `````                                                           |
|        695 | ````` ¿🏑? `````         | 0.00019205  | 216125: ````` <0xF0><0x9F><0x8F> `````, 247: ````` <0x91> `````                  |
|        661 | ````` ¿🎯? `````         | 0.00019235  | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 115: ````` <0xAF> ````` |
|        665 | ````` ¿🎳? `````         | 0.000192352 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 119: ````` <0xB3> ````` |
|        655 | ````` ¿🎩? `````         | 0.000192518 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 110: ````` <0xA9> ````` |
|        636 | ````` ¿🎑? `````         | 0.000192535 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 247: ````` <0x91> ````` |
|        734 | ````` ¿🏻? `````           | 0.000192658 | 216125: ````` <0xF0><0x9F><0x8F> `````, 127: ````` <0xBB> `````                  |
|        624 | ````` ¿🎅? `````         | 0.000192777 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 235: ````` <0x85> ````` |
|        656 | ````` ¿🎪? `````         | 0.000192781 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 111: ````` <0xAA> ````` |
|        580 | ````` ¿🍙? `````         | 0.00019287  | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 255: ````` <0x99> ````` |
|        592 | ````` ¿🍥? `````         | 0.000192891 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 106: ````` <0xA5> ````` |
|        584 | ````` ¿🍝? `````         | 0.000193071 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 259: ````` <0x9D> ````` |
|        606 | ````` ¿🍳? `````         | 0.000193336 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 119: ````` <0xB3> ````` |
|        581 | ````` ¿🍚? `````         | 0.000193416 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 256: ````` <0x9A> ````` |
|        653 | ````` ¿🎧? `````         | 0.000193427 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 108: ````` <0xA7> ````` |
|        639 | ````` ¿🎖? `````          | 0.000193477 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 252: ````` <0x96> ````` |
|        566 | ````` ¿🍋? `````         | 0.000193697 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 241: ````` <0x8B> ````` |
|        693 | ````` ¿🏏? `````         | 0.000193717 | 216125: ````` <0xF0><0x9F><0x8F> `````, 245: ````` <0x8F> `````                  |
|        662 | ````` ¿🎰? `````         | 0.000193795 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 116: ````` <0xB0> ````` |
|        714 | ````` ¿🏤? `````         | 0.000193855 | 216125: ````` <0xF0><0x9F><0x8F> `````, 105: ````` <0xA4> `````                  |
|        721 | ````` ¿🏫? `````         | 0.000193878 | 216125: ````` <0xF0><0x9F><0x8F> `````, 112: ````` <0xAB> `````                  |
|        641 | ````` ¿🎙? `````          | 0.000194206 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 255: ````` <0x99> ````` |
|        640 | ````` ¿🎗? `````          | 0.000194362 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 253: ````` <0x97> ````` |
|        597 | ````` ¿🍪? `````         | 0.0001944   | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 111: ````` <0xAA> ````` |
|        621 | ````` ¿🎂? `````         | 0.00019455  | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 232: ````` <0x82> ````` |
|        591 | ````` ¿🍤? `````         | 0.000194722 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 105: ````` <0xA4> ````` |
|        557 | ````` ¿🍂? `````         | 0.000194794 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 232: ````` <0x82> ````` |
|        625 | ````` ¿🎆? `````         | 0.000194954 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 236: ````` <0x86> ````` |
|        727 | ````` ¿🏳? `````          | 0.000194982 | 216125: ````` <0xF0><0x9F><0x8F> `````, 119: ````` <0xB3> `````                  |
|        575 | ````` ¿🍔? `````         | 0.000195274 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 250: ````` <0x94> ````` |
|        709 | ````` ¿🏟? `````          | 0.000195315 | 216125: ````` <0xF0><0x9F><0x8F> `````, 261: ````` <0x9F> `````                  |
|        690 | ````` ¿🏌? `````          | 0.000195378 | 216125: ````` <0xF0><0x9F><0x8F> `````, 242: ````` <0x8C> `````                  |
|        579 | ````` ¿🍘? `````         | 0.000195589 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 254: ````` <0x98> ````` |
|       1494 | ````` ¿🦵? `````         | 0.000195599 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 121: ````` <0xB5> ````` |
|        585 | ````` ¿🍞? `````         | 0.000195608 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 260: ````` <0x9E> ````` |
|        699 | ````` ¿🏕? `````          | 0.000195859 | 216125: ````` <0xF0><0x9F><0x8F> `````, 251: ````` <0x95> `````                  |
|        627 | ````` ¿🎈? `````         | 0.000195958 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 238: ````` <0x88> ````` |
|        685 | ````` ¿🏇? `````         | 0.000195973 | 216125: ````` <0xF0><0x9F><0x8F> `````, 237: ````` <0x87> `````                  |
|        717 | ````` ¿🏧? `````         | 0.000196053 | 216125: ````` <0xF0><0x9F><0x8F> `````, 108: ````` <0xA7> `````                  |
|        711 | ````` ¿🏡? `````         | 0.000196149 | 216125: ````` <0xF0><0x9F><0x8F> `````, 102: ````` <0xA1> `````                  |
|        571 | ````` ¿🍐? `````         | 0.00019628  | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 246: ````` <0x90> ````` |
|        586 | ````` ¿🍟? `````         | 0.000196324 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 261: ````` <0x9F> ````` |
|        681 | ````` ¿🏃? `````         | 0.000196329 | 216125: ````` <0xF0><0x9F><0x8F> `````, 233: ````` <0x83> `````                  |
|        574 | ````` ¿🍓? `````         | 0.000196423 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 249: ````` <0x93> ````` |
|        659 | ````` ¿🎭? `````         | 0.000196509 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 263: ````` <0xAD> ````` |
|       1500 | ````` ¿🦻? `````         | 0.000196514 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 127: ````` <0xBB> ````` |
|        590 | ````` ¿🍣? `````         | 0.000196567 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 104: ````` <0xA3> ````` |
|        582 | ````` ¿🍛? `````         | 0.000196573 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 257: ````` <0x9B> ````` |
|        676 | ````` ¿🎾? `````         | 0.000196597 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 130: ````` <0xBE> ````` |
|        733 | ````` ¿🏺? `````         | 0.00019669  | 216125: ````` <0xF0><0x9F><0x8F> `````, 126: ````` <0xBA> `````                  |
|        683 | ````` ¿🏅? `````         | 0.000196707 | 216125: ````` <0xF0><0x9F><0x8F> `````, 235: ````` <0x85> `````                  |
|        673 | ````` ¿🎻? `````         | 0.000196739 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 127: ````` <0xBB> ````` |
|        602 | ````` ¿🍯? `````         | 0.00019676  | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 115: ````` <0xAF> ````` |
|        593 | ````` ¿🍦? `````         | 0.000196829 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 107: ````` <0xA6> ````` |
|        715 | ````` ¿🏥? `````         | 0.000196881 | 216125: ````` <0xF0><0x9F><0x8F> `````, 106: ````` <0xA5> `````                  |
|        622 | ````` ¿🎃? `````         | 0.000196893 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 233: ````` <0x83> ````` |
|        689 | ````` ¿🏋? `````          | 0.000197001 | 216125: ````` <0xF0><0x9F><0x8F> `````, 241: ````` <0x8B> `````                  |
|        713 | ````` ¿🏣? `````         | 0.000197025 | 216125: ````` <0xF0><0x9F><0x8F> `````, 104: ````` <0xA3> `````                  |
|        679 | ````` ¿🏁? `````         | 0.000197064 | 216125: ````` <0xF0><0x9F><0x8F> `````, 231: ````` <0x81> `````                  |
|        564 | ````` ¿🍉? `````         | 0.000197131 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 239: ````` <0x89> ````` |
|        706 | ````` ¿🏜? `````          | 0.000197202 | 216125: ````` <0xF0><0x9F><0x8F> `````, 258: ````` <0x9C> `````                  |
|        567 | ````` ¿🍌? `````         | 0.000197421 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 242: ````` <0x8C> ````` |
|        664 | ````` ¿🎲? `````         | 0.000197496 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 118: ````` <0xB2> ````` |
|        619 | ````` ¿🎀? `````         | 0.000197553 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 230: ````` <0x80> ````` |
|        620 | ````` ¿🎁? `````         | 0.000197648 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 231: ````` <0x81> ````` |
|        696 | ````` ¿🏒? `````         | 0.000197719 | 216125: ````` <0xF0><0x9F><0x8F> `````, 248: ````` <0x92> `````                  |
|        707 | ````` ¿🏝? `````          | 0.000197726 | 216125: ````` <0xF0><0x9F><0x8F> `````, 259: ````` <0x9D> `````                  |
|        588 | ````` ¿🍡? `````         | 0.000197796 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 102: ````` <0xA1> ````` |
|        703 | ````` ¿🏙? `````          | 0.000198046 | 216125: ````` <0xF0><0x9F><0x8F> `````, 255: ````` <0x99> `````                  |
|        638 | ````` ¿🎓? `````         | 0.00019811  | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 249: ````` <0x93> ````` |
|        645 | ````` ¿🎟? `````          | 0.000198124 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 261: ````` <0x9F> ````` |
|        692 | ````` ¿🏎? `````          | 0.000198147 | 216125: ````` <0xF0><0x9F><0x8F> `````, 244: ````` <0x8E> `````                  |
|        652 | ````` ¿🎦? `````         | 0.000198154 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 107: ````` <0xA6> ````` |
|       1527 | ````` ¿🧖? `````         | 0.000198202 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 252: ````` <0x96> ````` |
|        631 | ````` ¿🎌? `````         | 0.000198264 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 242: ````` <0x8C> ````` |
|        670 | ````` ¿🎸? `````         | 0.000198273 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 124: ````` <0xB8> ````` |
|        691 | ````` ¿🏍? `````          | 0.000198389 | 216125: ````` <0xF0><0x9F><0x8F> `````, 243: ````` <0x8D> `````                  |
|        647 | ````` ¿🎡? `````         | 0.000198483 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 102: ````` <0xA1> ````` |
|        607 | ````` ¿🍴? `````         | 0.000198578 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 120: ````` <0xB4> ````` |
|        576 | ````` ¿🍕? `````         | 0.000198638 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 251: ````` <0x95> ````` |
|        697 | ````` ¿🏓? `````         | 0.000198731 | 216125: ````` <0xF0><0x9F><0x8F> `````, 249: ````` <0x93> `````                  |
|        578 | ````` ¿🍗? `````         | 0.000198792 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 253: ````` <0x97> ````` |
|        671 | ````` ¿🎹? `````         | 0.000198836 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 125: ````` <0xB9> ````` |
|        660 | ````` ¿🎮? `````         | 0.000198966 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 114: ````` <0xAE> ````` |
|        646 | ````` ¿🎠? `````         | 0.000199038 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 262: ````` <0xA0> ````` |
|        637 | ````` ¿🎒? `````         | 0.000199141 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 248: ````` <0x92> ````` |
|        603 | ````` ¿🍰? `````         | 0.000199155 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 116: ````` <0xB0> ````` |
|        594 | ````` ¿🍧? `````         | 0.000199182 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 108: ````` <0xA7> ````` |
|        729 | ````` ¿🏵? `````          | 0.000199185 | 216125: ````` <0xF0><0x9F><0x8F> `````, 121: ````` <0xB5> `````                  |
|        587 | ````` ¿🍠? `````         | 0.000199205 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 262: ````` <0xA0> ````` |
|       1513 | ````` ¿🧈? `````         | 0.000199575 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 238: ````` <0x88> ````` |
|       1489 | ````` ¿🦰? `````         | 0.000199606 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 116: ````` <0xB0> ````` |
|        618 | ````` ¿🍿? `````         | 0.000199685 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 131: ````` <0xBF> ````` |
|        616 | ````` ¿🍽? `````          | 0.000199862 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 129: ````` <0xBD> ````` |
|        583 | ````` ¿🍜? `````         | 0.000199998 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 258: ````` <0x9C> ````` |
|        725 | ````` ¿🏯? `````         | 0.000200122 | 216125: ````` <0xF0><0x9F><0x8F> `````, 115: ````` <0xAF> `````                  |
|        569 | ````` ¿🍎? `````         | 0.000200201 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 244: ````` <0x8E> ````` |
|       1594 | ````` ¿🪘? `````         | 0.000200327 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 254: ````` <0x98> ````` |
|        700 | ````` ¿🏖? `````          | 0.000200356 | 216125: ````` <0xF0><0x9F><0x8F> `````, 252: ````` <0x96> `````                  |
|        552 | ````` ¿🌽? `````         | 0.000200374 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 129: ````` <0xBD> ````` |
|        626 | ````` ¿🎇? `````         | 0.000200576 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 237: ````` <0x87> ````` |
|       1491 | ````` ¿🦲? `````         | 0.000200635 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 118: ````` <0xB2> ````` |
|        600 | ````` ¿🍭? `````         | 0.000200911 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 263: ````` <0xAD> ````` |
|        623 | ````` ¿🎄? `````         | 0.000201192 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 234: ````` <0x84> ````` |
|        613 | ````` ¿🍺? `````         | 0.000201331 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 126: ````` <0xBA> ````` |
|       1542 | ````` ¿🧥? `````         | 0.000201368 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 106: ````` <0xA5> ````` |
|       1512 | ````` ¿🧇? `````         | 0.000201375 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 237: ````` <0x87> ````` |
|        701 | ````` ¿🏗? `````          | 0.000201395 | 216125: ````` <0xF0><0x9F><0x8F> `````, 253: ````` <0x97> `````                  |
|        612 | ````` ¿🍹? `````         | 0.000201501 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 125: ````` <0xB9> ````` |
|        669 | ````` ¿🎷? `````         | 0.000201602 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 123: ````` <0xB7> ````` |
|       1558 | ````` ¿🧵? `````         | 0.000201623 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 121: ````` <0xB5> ````` |
|        704 | ````` ¿🏚? `````          | 0.000201626 | 216125: ````` <0xF0><0x9F><0x8F> `````, 256: ````` <0x9A> `````                  |
|        667 | ````` ¿🎵? `````         | 0.000201757 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 121: ````` <0xB5> ````` |
|        570 | ````` ¿🍏? `````         | 0.000202097 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 245: ````` <0x8F> ````` |
|        601 | ````` ¿🍮? `````         | 0.000202114 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 114: ````` <0xAE> ````` |
|        556 | ````` ¿🍁? `````         | 0.00020263  | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 231: ````` <0x81> ````` |
|       1520 | ````` ¿🧏? `````         | 0.000202897 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 245: ````` <0x8F> ````` |
|       1566 | ````` ¿🧽? `````         | 0.00020295  | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 129: ````` <0xBD> ````` |
|       1576 | ````` ¿🩺? `````         | 0.000203347 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 126: ````` <0xBA> ````` |
|       1546 | ````` ¿🧩? `````         | 0.000204144 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 110: ````` <0xA9> ````` |
|       1478 | ````` ¿🦥? `````         | 0.000204499 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 106: ````` <0xA5> ````` |
|        560 | ````` ¿🍅? `````         | 0.000204772 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 235: ````` <0x85> ````` |
|       1487 | ````` ¿🦮? `````         | 0.000205091 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 114: ````` <0xAE> ````` |
|       1547 | ````` ¿🧪? `````         | 0.000205836 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 111: ````` <0xAA> ````` |
|       1587 | ````` ¿🪑? `````         | 0.00020604  | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 247: ````` <0x91> ````` |
|       1474 | ````` ¿🦡? `````         | 0.000206566 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 102: ````` <0xA1> ````` |
|       1631 | ````` ¿\U0001fac5? ````` | 0.000206808 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 235: ````` <0x85> ````` |
|       1480 | ````` ¿🦧? `````         | 0.000206824 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 108: ````` <0xA7> ````` |
|       1554 | ````` ¿🧱? `````         | 0.000207107 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 117: ````` <0xB1> ````` |
|       1568 | ````` ¿🧿? `````         | 0.000207219 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 131: ````` <0xBF> ````` |
|        844 | ````` ¿👩? `````         | 0.000207459 | 154565: ````` <0xF0><0x9F><0x91> `````, 110: ````` <0xA9> `````                  |
|       1574 | ````` ¿🩸? `````         | 0.000207487 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 124: ````` <0xB8> ````` |
|       1657 | ````` ¿\U000e0062? ````` | 0.000207921 | 3330: ````` <0xF3><0xA0><0x81> `````, 103: ````` <0xA2> `````                    |
|       1486 | ````` ¿🦭? `````         | 0.000208076 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 263: ````` <0xAD> ````` |
|       1557 | ````` ¿🧴? `````         | 0.00020835  | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 120: ````` <0xB4> ````` |
|       1636 | ````` ¿🫔? `````         | 0.000208471 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 250: ````` <0x94> ````` |
|       1654 | ````` ¿\U0001faf4? ````` | 0.000208622 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 120: ````` <0xB4> ````` |
|       1534 | ````` ¿🧝? `````         | 0.000208683 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 259: ````` <0x9D> ````` |
|       1597 | ````` ¿🪛? `````         | 0.000208747 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 257: ````` <0x9B> ````` |
|       1638 | ````` ¿🫖? `````         | 0.000208954 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 252: ````` <0x96> ````` |
|       1506 | ````` ¿🧁? `````         | 0.00020914  | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 231: ````` <0x81> ````` |
|        766 | ````` ¿🐛? `````         | 0.000209147 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 257: ````` <0x9B> ````` |
|       1565 | ````` ¿🧼? `````         | 0.000209232 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 128: ````` <0xBC> ````` |
|       1639 | ````` ¿\U0001fad7? ````` | 0.000209251 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 253: ````` <0x97> ````` |
|       1476 | ````` ¿🦣? `````         | 0.000209327 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 104: ````` <0xA3> ````` |
|       1519 | ````` ¿🧎? `````         | 0.000209535 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 244: ````` <0x8E> ````` |
|       1504 | ````` ¿🦿? `````         | 0.000209545 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 131: ````` <0xBF> ````` |
|       1540 | ````` ¿🧣? `````         | 0.000209711 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 104: ````` <0xA3> ````` |
|       1661 | ````` ¿\U000e006c? ````` | 0.000209774 | 69092: ````` \U000e006c `````                                                    |
|       1538 | ````` ¿🧡? `````         | 0.000210111 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 102: ````` <0xA1> ````` |
|       1629 | ````` ¿\U0001fac3? ````` | 0.000210184 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 233: ````` <0x83> ````` |
|       1570 | ````` ¿🩱? `````         | 0.000210331 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 117: ````` <0xB1> ````` |
|       1611 | ````` ¿\U0001faa9? ````` | 0.000210562 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 110: ````` <0xA9> ````` |
|        761 | ````` ¿🐖? `````         | 0.000210588 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 252: ````` <0x96> ````` |
|       1592 | ````` ¿🪖? `````         | 0.000210624 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 252: ````` <0x96> ````` |
|       1559 | ````` ¿🧶? `````         | 0.000210792 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 122: ````` <0xB6> ````` |
|       1475 | ````` ¿🦢? `````         | 0.00021105  | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 103: ````` <0xA2> ````` |
|       1635 | ````` ¿🫓? `````         | 0.000211089 | 2226: ````` <0xF0><0x9F> `````, 171080: ````` <0xAB><0x93> `````                 |
|       1621 | ````` ¿🪶? `````         | 0.000211108 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 122: ````` <0xB6> ````` |
|       1510 | ````` ¿🧅? `````         | 0.000211209 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 235: ````` <0x85> ````` |
|       1575 | ````` ¿🩹? `````         | 0.000211266 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 125: ````` <0xB9> ````` |
|       1653 | ````` ¿\U0001faf3? ````` | 0.000211412 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 119: ````` <0xB3> ````` |
|       1593 | ````` ¿🪗? `````         | 0.000211578 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 253: ````` <0x97> ````` |
|       1615 | ````` ¿🪰? `````         | 0.000211642 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 116: ````` <0xB0> ````` |
|       1509 | ````` ¿🧄? `````         | 0.000211715 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 234: ````` <0x84> ````` |
|        747 | ````` ¿🐈? `````         | 0.000211747 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 238: ````` <0x88> ````` |
|       1511 | ````` ¿🧆? `````         | 0.000211767 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 236: ````` <0x86> ````` |
|       1533 | ````` ¿🧜? `````         | 0.000211772 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 258: ````` <0x9C> ````` |
|       1516 | ````` ¿🧋? `````         | 0.000211819 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 241: ````` <0x8B> ````` |
|       1528 | ````` ¿🧗? `````         | 0.000211831 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 253: ````` <0x97> ````` |
|       1502 | ````` ¿🦽? `````         | 0.000211839 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 129: ````` <0xBD> ````` |
|       1501 | ````` ¿🦼? `````         | 0.000211843 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 128: ````` <0xBC> ````` |
|       1591 | ````` ¿🪕? `````         | 0.000211867 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 251: ````` <0x95> ````` |
|        816 | ````` ¿👍? `````         | 0.000211888 | 154565: ````` <0xF0><0x9F><0x91> `````, 243: ````` <0x8D> `````                  |
|       1490 | ````` ¿🦱? `````         | 0.000211916 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 117: ````` <0xB1> ````` |
|       1588 | ````` ¿🪒? `````         | 0.000211927 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 248: ````` <0x92> ````` |
|       1479 | ````` ¿🦦? `````         | 0.000211995 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 107: ````` <0xA6> ````` |
|       1624 | ````` ¿\U0001fab9? ````` | 0.000212034 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 125: ````` <0xB9> ````` |
|        823 | ````` ¿👔? `````         | 0.000212041 | 154565: ````` <0xF0><0x9F><0x91> `````, 250: ````` <0x94> `````                  |
|       1600 | ````` ¿🪞? `````         | 0.000212042 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 260: ````` <0x9E> ````` |
|       1620 | ````` ¿🪵? `````         | 0.000212069 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 121: ````` <0xB5> ````` |
|       1525 | ````` ¿🧔? `````         | 0.000212103 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 250: ````` <0x94> ````` |
|       1656 | ````` ¿\U0001faf6? ````` | 0.000212161 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 122: ````` <0xB6> ````` |
|       1649 | ````` ¿\U0001fae7? ````` | 0.000212194 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 108: ````` <0xA7> ````` |
|       1580 | ````` ¿🪁? `````         | 0.00021227  | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 231: ````` <0x81> ````` |
|       1508 | ````` ¿🧃? `````         | 0.00021241  | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 233: ````` <0x83> ````` |
|       1543 | ````` ¿🧦? `````         | 0.000212557 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 107: ````` <0xA6> ````` |
|       1603 | ````` ¿🪡? `````         | 0.000212702 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 102: ````` <0xA1> ````` |
|       1503 | ````` ¿🦾? `````         | 0.00021271  | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 130: ````` <0xBE> ````` |
|        890 | ````` ¿💗? `````         | 0.000212767 | 106024: ````` <0xF0><0x9F><0x92> `````, 253: ````` <0x97> `````                  |
|       1562 | ````` ¿🧹? `````         | 0.000212803 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 125: ````` <0xB9> ````` |
|       1614 | ````` ¿\U0001faac? ````` | 0.000212826 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 113: ````` <0xAC> ````` |
|        856 | ````` ¿👵? `````         | 0.000212832 | 154565: ````` <0xF0><0x9F><0x91> `````, 121: ````` <0xB5> `````                  |
|       1627 | ````` ¿🫁? `````         | 0.000212845 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 231: ````` <0x81> ````` |
|       1618 | ````` ¿🪳? `````         | 0.000212851 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 119: ````` <0xB3> ````` |
|       1642 | ````` ¿\U0001fae0? ````` | 0.000212872 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 262: ````` <0xA0> ````` |
|        846 | ````` ¿👫? `````         | 0.000213    | 154565: ````` <0xF0><0x9F><0x91> `````, 112: ````` <0xAB> `````                  |
|       1586 | ````` ¿🪐? `````         | 0.000213014 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 246: ````` <0x90> ````` |
|       1596 | ````` ¿🪚? `````         | 0.000213111 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 256: ````` <0x9A> ````` |
|       1622 | ````` ¿\U0001fab7? ````` | 0.000213166 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 123: ````` <0xB7> ````` |
|        757 | ````` ¿🐒? `````         | 0.000213258 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 248: ````` <0x92> ````` |
|       1537 | ````` ¿🧠? `````         | 0.000213275 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 262: ````` <0xA0> ````` |
|        741 | ````` ¿🐂? `````         | 0.000213293 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 232: ````` <0x82> ````` |
|        829 | ````` ¿👚? `````         | 0.000213306 | 154565: ````` <0xF0><0x9F><0x91> `````, 256: ````` <0x9A> `````                  |
|        863 | ````` ¿👼? `````         | 0.000213342 | 154565: ````` <0xF0><0x9F><0x91> `````, 128: ````` <0xBC> `````                  |
|       1539 | ````` ¿🧢? `````         | 0.000213591 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 103: ````` <0xA2> ````` |
|       1522 | ````` ¿🧑? `````         | 0.000213597 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 247: ````` <0x91> ````` |
|       1564 | ````` ¿🧻? `````         | 0.000213603 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 127: ````` <0xBB> ````` |
|        865 | ````` ¿👾? `````         | 0.00021375  | 154565: ````` <0xF0><0x9F><0x91> `````, 130: ````` <0xBE> `````                  |
|        742 | ````` ¿🐃? `````         | 0.000213825 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 233: ````` <0x83> ````` |
|       1599 | ````` ¿🪝? `````         | 0.000213898 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 259: ````` <0x9D> ````` |
|        803 | ````` ¿👀? `````         | 0.000213905 | 154565: ````` <0xF0><0x9F><0x91> `````, 230: ````` <0x80> `````                  |
|       1619 | ````` ¿🪴? `````         | 0.000213949 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 120: ````` <0xB4> ````` |
|       1573 | ````` ¿🩴? `````         | 0.000214007 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 120: ````` <0xB4> ````` |
|        894 | ````` ¿💛? `````         | 0.000214095 | 106024: ````` <0xF0><0x9F><0x92> `````, 257: ````` <0x9B> `````                  |
|        753 | ````` ¿🐎? `````         | 0.00021418  | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 244: ````` <0x8E> ````` |
|        882 | ````` ¿💏? `````         | 0.000214265 | 106024: ````` <0xF0><0x9F><0x92> `````, 245: ````` <0x8F> `````                  |
|        998 | ````` ¿🔄? `````         | 0.000214524 | 205860: ````` <0xF0><0x9F><0x94> `````, 234: ````` <0x84> `````                  |
|        907 | ````` ¿💨? `````         | 0.000214608 | 106024: ````` <0xF0><0x9F><0x92> `````, 109: ````` <0xA8> `````                  |
|       1488 | ````` ¿🦯? `````         | 0.000214641 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 115: ````` <0xAF> ````` |
|       1563 | ````` ¿🧺? `````         | 0.000214656 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 126: ````` <0xBA> ````` |
|        855 | ````` ¿👴? `````         | 0.000214696 | 154565: ````` <0xF0><0x9F><0x91> `````, 120: ````` <0xB4> `````                  |
|        842 | ````` ¿👧? `````         | 0.000214729 | 154565: ````` <0xF0><0x9F><0x91> `````, 108: ````` <0xA7> `````                  |
|       1492 | ````` ¿🦳? `````         | 0.000214767 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 119: ````` <0xB3> ````` |
|        810 | ````` ¿👇? `````         | 0.000214771 | 154565: ````` <0xF0><0x9F><0x91> `````, 237: ````` <0x87> `````                  |
|       1530 | ````` ¿🧙? `````         | 0.000214815 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 255: ````` <0x99> ````` |
|       1589 | ````` ¿🪓? `````         | 0.000214853 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 249: ````` <0x93> ````` |
|       1536 | ````` ¿🧟? `````         | 0.000214907 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 261: ````` <0x9F> ````` |
|       1532 | ````` ¿🧛? `````         | 0.000214932 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 257: ````` <0x9B> ````` |
|        743 | ````` ¿🐄? `````         | 0.000215036 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 234: ````` <0x84> ````` |
|        774 | ````` ¿🐣? `````         | 0.000215077 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 104: ````` <0xA3> ````` |
|       1541 | ````` ¿🧤? `````         | 0.000215084 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 105: ````` <0xA4> ````` |
|       1583 | ````` ¿🪄? `````         | 0.000215213 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 234: ````` <0x84> ````` |
|        783 | ````` ¿🐬? `````         | 0.000215214 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 113: ````` <0xAC> ````` |
|       1484 | ````` ¿🦫? `````         | 0.000215318 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 112: ````` <0xAB> ````` |
|       1605 | ````` ¿🪣? `````         | 0.000215414 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 104: ````` <0xA3> ````` |
|       1659 | ````` ¿\U000e0065? ````` | 0.000215423 | 3330: ````` <0xF3><0xA0><0x81> `````, 106: ````` <0xA5> `````                    |
|        862 | ````` ¿👻? `````         | 0.000215427 | 154565: ````` <0xF0><0x9F><0x91> `````, 127: ````` <0xBB> `````                  |
|        839 | ````` ¿👤? `````         | 0.000215435 | 154565: ````` <0xF0><0x9F><0x91> `````, 105: ````` <0xA4> `````                  |
|        794 | ````` ¿🐷? `````         | 0.000215441 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 123: ````` <0xB7> ````` |
|        875 | ````` ¿💈? `````         | 0.000215542 | 106024: ````` <0xF0><0x9F><0x92> `````, 238: ````` <0x88> `````                  |
|       1526 | ````` ¿🧕? `````         | 0.00021566  | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 251: ````` <0x95> ````` |
|        841 | ````` ¿👦? `````         | 0.000215671 | 154565: ````` <0xF0><0x9F><0x91> `````, 107: ````` <0xA6> `````                  |
|       1660 | ````` ¿\U000e0067? ````` | 0.000215681 | 3330: ````` <0xF3><0xA0><0x81> `````, 108: ````` <0xA7> `````                    |
|        754 | ````` ¿🐏? `````         | 0.000215683 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 245: ````` <0x8F> ````` |
|       1493 | ````` ¿🦴? `````         | 0.000215827 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 120: ````` <0xB4> ````` |
|        904 | ````` ¿💥? `````         | 0.000215936 | 106024: ````` <0xF0><0x9F><0x92> `````, 106: ````` <0xA5> `````                  |
|       1521 | ````` ¿🧐? `````         | 0.000215956 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 246: ````` <0x90> ````` |
|        878 | ````` ¿💋? `````         | 0.00021606  | 106024: ````` <0xF0><0x9F><0x92> `````, 241: ````` <0x8B> `````                  |
|       1485 | ````` ¿🦬? `````         | 0.000216084 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 113: ````` <0xAC> ````` |
|        820 | ````` ¿👑? `````         | 0.000216148 | 154565: ````` <0xF0><0x9F><0x91> `````, 247: ````` <0x91> `````                  |
|        830 | ````` ¿👛? `````         | 0.000216199 | 154565: ````` <0xF0><0x9F><0x91> `````, 257: ````` <0x9B> `````                  |
|       1473 | ````` ¿🦠? `````         | 0.000216278 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 262: ````` <0xA0> ````` |
|        788 | ````` ¿🐱? `````         | 0.000216329 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 117: ````` <0xB1> ````` |
|       1524 | ````` ¿🧓? `````         | 0.000216343 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 249: ````` <0x93> ````` |
|        752 | ````` ¿🐍? `````         | 0.00021638  | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 243: ````` <0x8D> ````` |
|        898 | ````` ¿💟? `````         | 0.00021642  | 106024: ````` <0xF0><0x9F><0x92> `````, 261: ````` <0x9F> `````                  |
|        845 | ````` ¿👪? `````         | 0.000216454 | 154565: ````` <0xF0><0x9F><0x91> `````, 111: ````` <0xAA> `````                  |
|        848 | ````` ¿👭? `````         | 0.000216499 | 154565: ````` <0xF0><0x9F><0x91> `````, 263: ````` <0xAD> `````                  |
|        821 | ````` ¿👒? `````         | 0.000216512 | 154565: ````` <0xF0><0x9F><0x91> `````, 248: ````` <0x92> `````                  |
|        887 | ````` ¿💔? `````         | 0.000216556 | 106024: ````` <0xF0><0x9F><0x92> `````, 250: ````` <0x94> `````                  |
|        806 | ````` ¿👃? `````         | 0.000216589 | 154565: ````` <0xF0><0x9F><0x91> `````, 233: ````` <0x83> `````                  |
|        861 | ````` ¿👺? `````         | 0.000216593 | 154565: ````` <0xF0><0x9F><0x91> `````, 126: ````` <0xBA> `````                  |
|        800 | ````` ¿🐽? `````         | 0.000216635 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 129: ````` <0xBD> ````` |
|       1482 | ````` ¿🦩? `````         | 0.000216678 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 110: ````` <0xA9> ````` |
|        854 | ````` ¿👳? `````         | 0.000216707 | 154565: ````` <0xF0><0x9F><0x91> `````, 119: ````` <0xB3> `````                  |
|        763 | ````` ¿🐘? `````         | 0.000216707 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 254: ````` <0x98> ````` |
|        802 | ````` ¿🐿? `````          | 0.000216711 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 131: ````` <0xBF> ````` |
|       1651 | ````` ¿\U0001faf1? ````` | 0.000216745 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 117: ````` <0xB1> ````` |
|        871 | ````` ¿💄? `````         | 0.000216899 | 106024: ````` <0xF0><0x9F><0x92> `````, 234: ````` <0x84> `````                  |
|       1590 | ````` ¿🪔? `````         | 0.000217068 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 250: ````` <0x94> ````` |
|        880 | ````` ¿💍? `````         | 0.000217158 | 106024: ````` <0xF0><0x9F><0x92> `````, 243: ````` <0x8D> `````                  |
|       1514 | ````` ¿🧉? `````         | 0.000217237 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 239: ````` <0x89> ````` |
|        910 | ````` ¿💫? `````         | 0.00021742  | 106024: ````` <0xF0><0x9F><0x92> `````, 112: ````` <0xAB> `````                  |
|        903 | ````` ¿💤? `````         | 0.00021751  | 106024: ````` <0xF0><0x9F><0x92> `````, 105: ````` <0xA4> `````                  |
|       1655 | ````` ¿\U0001faf5? ````` | 0.000217577 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 121: ````` <0xB5> ````` |
|        789 | ````` ¿🐲? `````         | 0.000217635 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 118: ````` <0xB2> ````` |
|       1607 | ````` ¿🪥? `````         | 0.000217696 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 106: ````` <0xA5> ````` |
|        790 | ````` ¿🐳? `````         | 0.000217837 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 119: ````` <0xB3> ````` |
|        808 | ````` ¿👅? `````         | 0.000217864 | 154565: ````` <0xF0><0x9F><0x91> `````, 235: ````` <0x85> `````                  |
|        852 | ````` ¿👱? `````         | 0.00021789  | 154565: ````` <0xF0><0x9F><0x91> `````, 117: ````` <0xB1> `````                  |
|       1644 | ````` ¿\U0001fae2? ````` | 0.000217932 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 103: ````` <0xA2> ````` |
|        883 | ````` ¿💐? `````         | 0.000217933 | 106024: ````` <0xF0><0x9F><0x92> `````, 246: ````` <0x90> `````                  |
|        815 | ````` ¿👌? `````         | 0.000217941 | 154565: ````` <0xF0><0x9F><0x91> `````, 242: ````` <0x8C> `````                  |
|        805 | ````` ¿👂? `````         | 0.000218275 | 154565: ````` <0xF0><0x9F><0x91> `````, 232: ````` <0x82> `````                  |
|        899 | ````` ¿💠? `````         | 0.000218289 | 106024: ````` <0xF0><0x9F><0x92> `````, 262: ````` <0xA0> `````                  |
|        828 | ````` ¿👙? `````         | 0.000218395 | 154565: ````` <0xF0><0x9F><0x91> `````, 255: ````` <0x99> `````                  |
|        778 | ````` ¿🐧? `````         | 0.000218427 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 108: ````` <0xA7> ````` |
|       1634 | ````` ¿🫒? `````         | 0.000218487 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 248: ````` <0x92> ````` |
|        776 | ````` ¿🐥? `````         | 0.000218535 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 106: ````` <0xA5> ````` |
|       1632 | ````` ¿🫐? `````         | 0.000218552 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 246: ````` <0x90> ````` |
|       1652 | ````` ¿\U0001faf2? ````` | 0.000218552 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 118: ````` <0xB2> ````` |
|        737 | ````` ¿🏾? `````           | 0.000218596 | 216125: ````` <0xF0><0x9F><0x8F> `````, 130: ````` <0xBE> `````                  |
|        834 | ````` ¿👟? `````         | 0.000218644 | 154565: ````` <0xF0><0x9F><0x91> `````, 261: ````` <0x9F> `````                  |
|       1626 | ````` ¿🫀? `````         | 0.000218647 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 230: ````` <0x80> ````` |
|        876 | ````` ¿💉? `````         | 0.000218662 | 106024: ````` <0xF0><0x9F><0x92> `````, 239: ````` <0x89> `````                  |
|        771 | ````` ¿🐠? `````         | 0.00021871  | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 262: ````` <0xA0> ````` |
|        886 | ````` ¿💓? `````         | 0.000218725 | 106024: ````` <0xF0><0x9F><0x92> `````, 249: ````` <0x93> `````                  |
|        756 | ````` ¿🐑? `````         | 0.000218779 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 247: ````` <0x91> ````` |
|        891 | ````` ¿💘? `````         | 0.000218844 | 106024: ````` <0xF0><0x9F><0x92> `````, 254: ````` <0x98> `````                  |
|       1560 | ````` ¿🧷? `````         | 0.000218849 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 123: ````` <0xB7> ````` |
|        759 | ````` ¿🐔? `````         | 0.000218939 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 250: ````` <0x94> ````` |
|        793 | ````` ¿🐶? `````         | 0.000218976 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 122: ````` <0xB6> ````` |
|       1641 | ````` ¿\U0001fad9? ````` | 0.000219077 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 255: ````` <0x99> ````` |
|        762 | ````` ¿🐗? `````         | 0.000219113 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 253: ````` <0x97> ````` |
|       1647 | ````` ¿\U0001fae5? ````` | 0.000219113 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 106: ````` <0xA5> ````` |
|       1646 | ````` ¿\U0001fae4? ````` | 0.000219134 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 105: ````` <0xA4> ````` |
|       1551 | ````` ¿🧮? `````         | 0.000219324 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 114: ````` <0xAE> ````` |
|        769 | ````` ¿🐞? `````         | 0.000219333 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 260: ````` <0x9E> ````` |
|        930 | ````` ¿💿? `````         | 0.000219373 | 106024: ````` <0xF0><0x9F><0x92> `````, 131: ````` <0xBF> `````                  |
|        885 | ````` ¿💒? `````         | 0.000219414 | 106024: ````` <0xF0><0x9F><0x92> `````, 248: ````` <0x92> `````                  |
|        911 | ````` ¿💬? `````         | 0.000219435 | 106024: ````` <0xF0><0x9F><0x92> `````, 113: ````` <0xAC> `````                  |
|        832 | ````` ¿👝? `````         | 0.000219476 | 154565: ````` <0xF0><0x9F><0x91> `````, 259: ````` <0x9D> `````                  |
|        906 | ````` ¿💧? `````         | 0.000219478 | 106024: ````` <0xF0><0x9F><0x92> `````, 108: ````` <0xA7> `````                  |
|       1098 | ````` ¿🖋? `````          | 0.000219503 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 241: ````` <0x8B> ````` |
|        912 | ````` ¿💭? `````         | 0.000219586 | 106024: ````` <0xF0><0x9F><0x92> `````, 263: ````` <0xAD> `````                  |
|       1606 | ````` ¿🪤? `````         | 0.000219604 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 105: ````` <0xA4> ````` |
|       1567 | ````` ¿🧾? `````         | 0.00021973  | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 130: ````` <0xBE> ````` |
|       1633 | ````` ¿🫑? `````         | 0.000219749 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 247: ````` <0x91> ````` |
|        918 | ````` ¿💳? `````         | 0.00021977  | 106024: ````` <0xF0><0x9F><0x92> `````, 119: ````` <0xB3> `````                  |
|        999 | ````` ¿🔅? `````         | 0.000219837 | 205860: ````` <0xF0><0x9F><0x94> `````, 235: ````` <0x85> `````                  |
|       1577 | ````` ¿\U0001fa7b? ````` | 0.000219854 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 127: ````` <0xBB> ````` |
|        833 | ````` ¿👞? `````         | 0.000219855 | 154565: ````` <0xF0><0x9F><0x91> `````, 260: ````` <0x9E> `````                  |
|        909 | ````` ¿💪? `````         | 0.000219863 | 106024: ````` <0xF0><0x9F><0x92> `````, 111: ````` <0xAA> `````                  |
|       1609 | ````` ¿🪧? `````         | 0.000219885 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 108: ````` <0xA7> ````` |
|       1556 | ````` ¿🧳? `````         | 0.000220028 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 119: ````` <0xB3> ````` |
|        974 | ````` ¿📫? `````         | 0.000220105 | 185981: ````` <0xF0><0x9F><0x93> `````, 112: ````` <0xAB> `````                  |
|       1616 | ````` ¿🪱? `````         | 0.000220137 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 117: ````` <0xB1> ````` |
|        868 | ````` ¿💁? `````         | 0.000220187 | 106024: ````` <0xF0><0x9F><0x92> `````, 231: ````` <0x81> `````                  |
|       1628 | ````` ¿🫂? `````         | 0.000220192 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 232: ````` <0x82> ````` |
|        915 | ````` ¿💰? `````         | 0.000220198 | 106024: ````` <0xF0><0x9F><0x92> `````, 116: ````` <0xB0> `````                  |
|        895 | ````` ¿💜? `````         | 0.000220207 | 106024: ````` <0xF0><0x9F><0x92> `````, 258: ````` <0x9C> `````                  |
|        867 | ````` ¿💀? `````         | 0.000220223 | 106024: ````` <0xF0><0x9F><0x92> `````, 230: ````` <0x80> `````                  |
|       1548 | ````` ¿🧫? `````         | 0.000220235 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 112: ````` <0xAB> ````` |
|        781 | ````` ¿🐪? `````         | 0.000220265 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 111: ````` <0xAA> ````` |
|        914 | ````` ¿💯? `````         | 0.000220276 | 106024: ````` <0xF0><0x9F><0x92> `````, 115: ````` <0xAF> `````                  |
|        949 | ````` ¿📒? `````         | 0.000220342 | 185981: ````` <0xF0><0x9F><0x93> `````, 248: ````` <0x92> `````                  |
|       1578 | ````` ¿\U0001fa7c? ````` | 0.000220346 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 128: ````` <0xBC> ````` |
|        960 | ````` ¿📝? `````         | 0.000220356 | 185981: ````` <0xF0><0x9F><0x93> `````, 259: ````` <0x9D> `````                  |
|       1040 | ````` ¿🔮? `````         | 0.00022039  | 205860: ````` <0xF0><0x9F><0x94> `````, 114: ````` <0xAE> `````                  |
|       1076 | ````` ¿🕞? `````         | 0.000220394 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 260: ````` <0x9E> ````` |
|       1544 | ````` ¿🧧? `````         | 0.000220418 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 108: ````` <0xA7> ````` |
|        931 | ````` ¿📀? `````         | 0.000220432 | 185981: ````` <0xF0><0x9F><0x93> `````, 230: ````` <0x80> `````                  |
|       1068 | ````` ¿🕖? `````         | 0.000220507 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 252: ````` <0x96> ````` |
|        925 | ````` ¿💺? `````         | 0.0002207   | 106024: ````` <0xF0><0x9F><0x92> `````, 126: ````` <0xBA> `````                  |
|        749 | ````` ¿🐊? `````         | 0.00022072  | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 240: ````` <0x8A> ````` |
|       1529 | ````` ¿🧘? `````         | 0.000220729 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 254: ````` <0x98> ````` |
|        864 | ````` ¿👽? `````         | 0.000220731 | 154565: ````` <0xF0><0x9F><0x91> `````, 129: ````` <0xBD> `````                  |
|        935 | ````` ¿📄? `````         | 0.000220739 | 185981: ````` <0xF0><0x9F><0x93> `````, 234: ````` <0x84> `````                  |
|        962 | ````` ¿📟? `````         | 0.000220762 | 185981: ````` <0xF0><0x9F><0x93> `````, 261: ````` <0x9F> `````                  |
|        978 | ````` ¿📯? `````         | 0.000220766 | 185981: ````` <0xF0><0x9F><0x93> `````, 115: ````` <0xAF> `````                  |
|        838 | ````` ¿👣? `````         | 0.00022084  | 154565: ````` <0xF0><0x9F><0x91> `````, 104: ````` <0xA3> `````                  |
|       1637 | ````` ¿🫕? `````         | 0.000220846 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 251: ````` <0x95> ````` |
|       1047 | ````` ¿🔵? `````         | 0.000220903 | 205860: ````` <0xF0><0x9F><0x94> `````, 121: ````` <0xB5> `````                  |
|        857 | ````` ¿👶? `````         | 0.000221014 | 154565: ````` <0xF0><0x9F><0x91> `````, 122: ````` <0xB6> `````                  |
|        872 | ````` ¿💅? `````         | 0.000221024 | 106024: ````` <0xF0><0x9F><0x92> `````, 235: ````` <0x85> `````                  |
|       1073 | ````` ¿🕛? `````         | 0.000221026 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 257: ````` <0x9B> ````` |
|       1648 | ````` ¿\U0001fae6? ````` | 0.00022109  | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 107: ````` <0xA6> ````` |
|        917 | ````` ¿💲? `````         | 0.000221092 | 106024: ````` <0xF0><0x9F><0x92> `````, 118: ````` <0xB2> `````                  |
|       1617 | ````` ¿🪲? `````         | 0.000221225 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 118: ````` <0xB2> ````` |
|       1610 | ````` ¿🪨? `````         | 0.000221225 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 109: ````` <0xA8> ````` |
|        840 | ````` ¿👥? `````         | 0.000221255 | 154565: ````` <0xF0><0x9F><0x91> `````, 106: ````` <0xA5> `````                  |
|        787 | ````` ¿🐰? `````         | 0.000221314 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 116: ````` <0xB0> ````` |
|       1472 | ````` ¿🦟? `````         | 0.000221319 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 261: ````` <0x9F> ````` |
|       1595 | ````` ¿🪙? `````         | 0.00022135  | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 255: ````` <0x99> ````` |
|        836 | ````` ¿👡? `````         | 0.000221403 | 154565: ````` <0xF0><0x9F><0x91> `````, 102: ````` <0xA1> `````                  |
|       1477 | ````` ¿🦤? `````         | 0.00022144  | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 105: ````` <0xA4> ````` |
|       1531 | ````` ¿🧚? `````         | 0.00022144  | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 256: ````` <0x9A> ````` |
|       1026 | ````` ¿🔠? `````         | 0.000221447 | 205860: ````` <0xF0><0x9F><0x94> `````, 262: ````` <0xA0> `````                  |
|       1579 | ````` ¿🪀? `````         | 0.000221458 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 230: ````` <0x80> ````` |
|       1060 | ````` ¿🕍? `````         | 0.000221482 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 243: ````` <0x8D> ````` |
|       1550 | ````` ¿🧭? `````         | 0.000221482 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 263: ````` <0xAD> ````` |
|        881 | ````` ¿💎? `````         | 0.000221592 | 106024: ````` <0xF0><0x9F><0x92> `````, 244: ````` <0x8E> `````                  |
|       1650 | ````` ¿\U0001faf0? ````` | 0.000221617 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 116: ````` <0xB0> ````` |
|       1549 | ````` ¿🧬? `````         | 0.000221706 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 113: ````` <0xAC> ````` |
|        751 | ````` ¿🐌? `````         | 0.000221756 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 242: ````` <0x8C> ````` |
|       1640 | ````` ¿\U0001fad8? ````` | 0.000221831 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 254: ````` <0x98> ````` |
|       1598 | ````` ¿🪜? `````         | 0.00022186  | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 258: ````` <0x9C> ````` |
|        825 | ````` ¿👖? `````         | 0.000221898 | 154565: ````` <0xF0><0x9F><0x91> `````, 252: ````` <0x96> `````                  |
|       1100 | ````` ¿🖍? `````          | 0.000221951 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 243: ````` <0x8D> ````` |
|        916 | ````` ¿💱? `````         | 0.000221966 | 106024: ````` <0xF0><0x9F><0x92> `````, 117: ````` <0xB1> `````                  |
|       1497 | ````` ¿🦸? `````         | 0.00022197  | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 124: ````` <0xB8> ````` |
|        893 | ````` ¿💚? `````         | 0.000222005 | 106024: ````` <0xF0><0x9F><0x92> `````, 256: ````` <0x9A> `````                  |
|       1612 | ````` ¿\U0001faaa? ````` | 0.000222033 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 111: ````` <0xAA> ````` |
|        888 | ````` ¿💕? `````         | 0.000222082 | 106024: ````` <0xF0><0x9F><0x92> `````, 251: ````` <0x95> `````                  |
|       1625 | ````` ¿\U0001faba? ````` | 0.000222085 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 126: ````` <0xBA> ````` |
|        786 | ````` ¿🐯? `````         | 0.000222091 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 115: ````` <0xAF> ````` |
|       1555 | ````` ¿🧲? `````         | 0.000222101 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 118: ````` <0xB2> ````` |
|        954 | ````` ¿📗? `````         | 0.000222106 | 185981: ````` <0xF0><0x9F><0x93> `````, 253: ````` <0x97> `````                  |
|        807 | ````` ¿👄? `````         | 0.000222107 | 154565: ````` <0xF0><0x9F><0x91> `````, 234: ````` <0x84> `````                  |
|        822 | ````` ¿👓? `````         | 0.000222107 | 154565: ````` <0xF0><0x9F><0x91> `````, 249: ````` <0x93> `````                  |
|       1561 | ````` ¿🧸? `````         | 0.000222109 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 124: ````` <0xB8> ````` |
|        748 | ````` ¿🐉? `````         | 0.00022214  | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 239: ````` <0x89> ````` |
|       1602 | ````` ¿🪠? `````         | 0.000222151 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 262: ````` <0xA0> ````` |
|       1623 | ````` ¿\U0001fab8? ````` | 0.000222178 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 124: ````` <0xB8> ````` |
|       1000 | ````` ¿🔆? `````         | 0.000222208 | 205860: ````` <0xF0><0x9F><0x94> `````, 236: ````` <0x86> `````                  |
|        870 | ````` ¿💃? `````         | 0.000222208 | 106024: ````` <0xF0><0x9F><0x92> `````, 233: ````` <0x83> `````                  |
|       1505 | ````` ¿🧀? `````         | 0.00022221  | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 230: ````` <0x80> ````` |
|        785 | ````` ¿🐮? `````         | 0.000222234 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 114: ````` <0xAE> ````` |
|       1518 | ````` ¿🧍? `````         | 0.000222263 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 243: ````` <0x8D> ````` |
|        919 | ````` ¿💴? `````         | 0.000222294 | 106024: ````` <0xF0><0x9F><0x92> `````, 120: ````` <0xB4> `````                  |
|        920 | ````` ¿💵? `````         | 0.000222325 | 106024: ````` <0xF0><0x9F><0x92> `````, 121: ````` <0xB5> `````                  |
|       1495 | ````` ¿🦶? `````         | 0.000222401 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 122: ````` <0xB6> ````` |
|        792 | ````` ¿🐵? `````         | 0.000222403 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 121: ````` <0xB5> ````` |
|       1085 | ````` ¿🕧? `````         | 0.000222423 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 108: ````` <0xA7> ````` |
|        859 | ````` ¿👸? `````         | 0.000222444 | 2226: ````` <0xF0><0x9F> `````, 44125: ````` <0x91><0xB8> `````                  |
|        835 | ````` ¿👠? `````         | 0.000222469 | 154565: ````` <0xF0><0x9F><0x91> `````, 262: ````` <0xA0> `````                  |
|        760 | ````` ¿🐕? `````         | 0.000222622 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 251: ````` <0x95> ````` |
|        963 | ````` ¿📠? `````         | 0.000222636 | 185981: ````` <0xF0><0x9F><0x93> `````, 262: ````` <0xA0> `````                  |
|        813 | ````` ¿👊? `````         | 0.000222664 | 154565: ````` <0xF0><0x9F><0x91> `````, 240: ````` <0x8A> `````                  |
|        985 | ````` ¿📶? `````         | 0.000222678 | 185981: ````` <0xF0><0x9F><0x93> `````, 122: ````` <0xB6> `````                  |
|        736 | ````` ¿🏽? `````           | 0.000222704 | 216125: ````` <0xF0><0x9F><0x8F> `````, 129: ````` <0xBD> `````                  |
|       1601 | ````` ¿🪟? `````         | 0.000222747 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 261: ````` <0x9F> ````` |
|        869 | ````` ¿💂? `````         | 0.000222823 | 106024: ````` <0xF0><0x9F><0x92> `````, 232: ````` <0x82> `````                  |
|        900 | ````` ¿💡? `````         | 0.000222844 | 106024: ````` <0xF0><0x9F><0x92> `````, 102: ````` <0xA1> `````                  |
|        799 | ````` ¿🐼? `````         | 0.000222894 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 128: ````` <0xBC> ````` |
|        768 | ````` ¿🐝? `````         | 0.000222925 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 259: ````` <0x9D> ````` |
|        901 | ````` ¿💢? `````         | 0.000223071 | 106024: ````` <0xF0><0x9F><0x92> `````, 103: ````` <0xA2> `````                  |
|        777 | ````` ¿🐦? `````         | 0.00022308  | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 107: ````` <0xA6> ````` |
|        819 | ````` ¿👐? `````         | 0.000223156 | 2226: ````` <0xF0><0x9F> `````, 11948: ````` <0x91><0x90> `````                  |
|        746 | ````` ¿🐇? `````         | 0.000223213 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 237: ````` <0x87> ````` |
|        858 | ````` ¿👷? `````         | 0.000223244 | 154565: ````` <0xF0><0x9F><0x91> `````, 123: ````` <0xB7> `````                  |
|       1517 | ````` ¿\U0001f9cc? ````` | 0.000223269 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 242: ````` <0x8C> ````` |
|        811 | ````` ¿👈? `````         | 0.000223339 | 154565: ````` <0xF0><0x9F><0x91> `````, 238: ````` <0x88> `````                  |
|        897 | ````` ¿💞? `````         | 0.000223396 | 106024: ````` <0xF0><0x9F><0x92> `````, 260: ````` <0x9E> `````                  |
|       1585 | ````` ¿🪆? `````         | 0.000223432 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 236: ````` <0x86> ````` |
|        892 | ````` ¿💙? `````         | 0.000223517 | 106024: ````` <0xF0><0x9F><0x92> `````, 255: ````` <0x99> `````                  |
|       1496 | ````` ¿🦷? `````         | 0.000223543 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 123: ````` <0xB7> ````` |
|       1613 | ````` ¿\U0001faab? ````` | 0.000223687 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 112: ````` <0xAB> ````` |
|        849 | ````` ¿👮? `````         | 0.000223696 | 154565: ````` <0xF0><0x9F><0x91> `````, 114: ````` <0xAE> `````                  |
|        866 | ````` ¿👿? `````         | 0.000223712 | 154565: ````` <0xF0><0x9F><0x91> `````, 131: ````` <0xBF> `````                  |
|        843 | ````` ¿👨? `````         | 0.000223715 | 154565: ````` <0xF0><0x9F><0x91> `````, 109: ````` <0xA8> `````                  |
|        824 | ````` ¿👕? `````         | 0.000223726 | 154565: ````` <0xF0><0x9F><0x91> `````, 251: ````` <0x95> `````                  |
|        851 | ````` ¿👰? `````         | 0.000223728 | 154565: ````` <0xF0><0x9F><0x91> `````, 116: ````` <0xB0> `````                  |
|        809 | ````` ¿👆? `````         | 0.00022378  | 154565: ````` <0xF0><0x9F><0x91> `````, 236: ````` <0x86> `````                  |
|        818 | ````` ¿👏? `````         | 0.000223791 | 154565: ````` <0xF0><0x9F><0x91> `````, 245: ````` <0x8F> `````                  |
|        795 | ````` ¿🐸? `````         | 0.000223837 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 124: ````` <0xB8> ````` |
|       1007 | ````` ¿🔍? `````         | 0.000223846 | 205860: ````` <0xF0><0x9F><0x94> `````, 243: ````` <0x8D> `````                  |
|       1604 | ````` ¿🪢? `````         | 0.000223856 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 103: ````` <0xA2> ````` |
|       1645 | ````` ¿\U0001fae3? ````` | 0.000223938 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 104: ````` <0xA3> ````` |
|       1608 | ````` ¿🪦? `````         | 0.000223979 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 107: ````` <0xA6> ````` |
|        745 | ````` ¿🐆? `````         | 0.000223987 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 236: ````` <0x86> ````` |
|        936 | ````` ¿📅? `````         | 0.00022408  | 185981: ````` <0xF0><0x9F><0x93> `````, 235: ````` <0x85> `````                  |
|       1481 | ````` ¿🦨? `````         | 0.000224177 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 109: ````` <0xA8> ````` |
|        992 | ````` ¿📽? `````          | 0.000224248 | 185981: ````` <0xF0><0x9F><0x93> `````, 129: ````` <0xBD> `````                  |
|        775 | ````` ¿🐤? `````         | 0.000224274 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 105: ````` <0xA4> ````` |
|        951 | ````` ¿📔? `````         | 0.000224276 | 185981: ````` <0xF0><0x9F><0x93> `````, 250: ````` <0x94> `````                  |
|        905 | ````` ¿💦? `````         | 0.000224288 | 106024: ````` <0xF0><0x9F><0x92> `````, 107: ````` <0xA6> `````                  |
|       1006 | ````` ¿🔌? `````         | 0.000224367 | 205860: ````` <0xF0><0x9F><0x94> `````, 242: ````` <0x8C> `````                  |
|       1074 | ````` ¿🕜? `````         | 0.000224484 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 258: ````` <0x9C> ````` |
|       1483 | ````` ¿🦪? `````         | 0.00022454  | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 111: ````` <0xAA> ````` |
|        767 | ````` ¿🐜? `````         | 0.00022454  | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 258: ````` <0x9C> ````` |
|       1515 | ````` ¿🧊? `````         | 0.000224615 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 240: ````` <0x8A> ````` |
|        784 | ````` ¿🐭? `````         | 0.000224636 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 263: ````` <0xAD> ````` |
|        928 | ````` ¿💽? `````         | 0.000224648 | 106024: ````` <0xF0><0x9F><0x92> `````, 129: ````` <0xBD> `````                  |
|        782 | ````` ¿🐫? `````         | 0.000224674 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 112: ````` <0xAB> ````` |
|       1021 | ````` ¿🔛? `````         | 0.00022469  | 205860: ````` <0xF0><0x9F><0x94> `````, 257: ````` <0x9B> `````                  |
|        937 | ````` ¿📆? `````         | 0.000224701 | 185981: ````` <0xF0><0x9F><0x93> `````, 236: ````` <0x86> `````                  |
|       1643 | ````` ¿\U0001fae1? ````` | 0.000224814 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 102: ````` <0xA1> ````` |
|        961 | ````` ¿📞? `````         | 0.000224818 | 185981: ````` <0xF0><0x9F><0x93> `````, 260: ````` <0x9E> `````                  |
|        853 | ````` ¿👲? `````         | 0.000224855 | 154565: ````` <0xF0><0x9F><0x91> `````, 118: ````` <0xB2> `````                  |
|        770 | ````` ¿🐟? `````         | 0.000224933 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 261: ````` <0x9F> ````` |
|        772 | ````` ¿🐡? `````         | 0.000224972 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 102: ````` <0xA1> ````` |
|        814 | ````` ¿👋? `````         | 0.00022498  | 154565: ````` <0xF0><0x9F><0x91> `````, 241: ````` <0x8B> `````                  |
|       1029 | ````` ¿🔣? `````         | 0.000225074 | 205860: ````` <0xF0><0x9F><0x94> `````, 104: ````` <0xA3> `````                  |
|        943 | ````` ¿📌? `````         | 0.00022508  | 185981: ````` <0xF0><0x9F><0x93> `````, 242: ````` <0x8C> `````                  |
|        927 | ````` ¿💼? `````         | 0.000225147 | 106024: ````` <0xF0><0x9F><0x92> `````, 128: ````` <0xBC> `````                  |
|        804 | ````` ¿👁? `````          | 0.000225148 | 154565: ````` <0xF0><0x9F><0x91> `````, 231: ````` <0x81> `````                  |
|       1087 | ````` ¿🕰? `````          | 0.000225312 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 116: ````` <0xB0> ````` |
|       1499 | ````` ¿🦺? `````         | 0.000225326 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 126: ````` <0xBA> ````` |
|        765 | ````` ¿🐚? `````         | 0.000225493 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 256: ````` <0x9A> ````` |
|        740 | ````` ¿🐁? `````         | 0.000225529 | 2226: ````` <0xF0><0x9F> `````, 245332: ````` <0x90><0x81> `````                 |
|        896 | ````` ¿💝? `````         | 0.000225603 | 106024: ````` <0xF0><0x9F><0x92> `````, 259: ````` <0x9D> `````                  |
|        994 | ````` ¿🔀? `````         | 0.00022565  | 205860: ````` <0xF0><0x9F><0x94> `````, 230: ````` <0x80> `````                  |
|       1016 | ````` ¿🔖? `````         | 0.000225664 | 205860: ````` <0xF0><0x9F><0x94> `````, 252: ````` <0x96> `````                  |
|        877 | ````` ¿💊? `````         | 0.000225687 | 106024: ````` <0xF0><0x9F><0x92> `````, 240: ````` <0x8A> `````                  |
|        938 | ````` ¿📇? `````         | 0.000225687 | 185981: ````` <0xF0><0x9F><0x93> `````, 237: ````` <0x87> `````                  |
|       1663 | ````` ¿\U000e0073? ````` | 0.000225715 | 69089: ````` \U000e0073 `````                                                    |
|       1044 | ````` ¿🔲? `````         | 0.000225827 | 205860: ````` <0xF0><0x9F><0x94> `````, 118: ````` <0xB2> `````                  |
|        797 | ````` ¿🐺? `````         | 0.000225832 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 126: ````` <0xBA> ````` |
|       1581 | ````` ¿🪂? `````         | 0.000225876 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 232: ````` <0x82> ````` |
|        773 | ````` ¿🐢? `````         | 0.000225968 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 103: ````` <0xA2> ````` |
|        874 | ````` ¿💇? `````         | 0.000226081 | 106024: ````` <0xF0><0x9F><0x92> `````, 237: ````` <0x87> `````                  |
|        796 | ````` ¿🐹? `````         | 0.000226126 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 125: ````` <0xB9> ````` |
|        764 | ````` ¿🐙? `````         | 0.000226151 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 255: ````` <0x99> ````` |
|       1099 | ````` ¿🖌? `````          | 0.000226176 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 242: ````` <0x8C> ````` |
|        750 | ````` ¿🐋? `````         | 0.0002262   | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 241: ````` <0x8B> ````` |
|        889 | ````` ¿💖? `````         | 0.000226209 | 106024: ````` <0xF0><0x9F><0x92> `````, 252: ````` <0x96> `````                  |
|        988 | ````` ¿📹? `````         | 0.000226294 | 185981: ````` <0xF0><0x9F><0x93> `````, 125: ````` <0xB9> `````                  |
|        860 | ````` ¿👹? `````         | 0.000226396 | 154565: ````` <0xF0><0x9F><0x91> `````, 125: ````` <0xB9> `````                  |
|        812 | ````` ¿👉? `````         | 0.000226439 | 154565: ````` <0xF0><0x9F><0x91> `````, 239: ````` <0x89> `````                  |
|        879 | ````` ¿💌? `````         | 0.000226463 | 106024: ````` <0xF0><0x9F><0x92> `````, 242: ````` <0x8C> `````                  |
|        975 | ````` ¿📬? `````         | 0.000226477 | 185981: ````` <0xF0><0x9F><0x93> `````, 113: ````` <0xAC> `````                  |
|        831 | ````` ¿👜? `````         | 0.000226483 | 2226: ````` <0xF0><0x9F> `````, 11524: ````` <0x91><0x9C> `````                  |
|        744 | ````` ¿🐅? `````         | 0.000226494 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 235: ````` <0x85> ````` |
|        913 | ````` ¿💮? `````         | 0.000226624 | 106024: ````` <0xF0><0x9F><0x92> `````, 114: ````` <0xAE> `````                  |
|       1553 | ````` ¿🧰? `````         | 0.000226634 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 116: ````` <0xB0> ````` |
|        827 | ````` ¿👘? `````         | 0.000226771 | 154565: ````` <0xF0><0x9F><0x91> `````, 254: ````` <0x98> `````                  |
|        984 | ````` ¿📵? `````         | 0.000226804 | 185981: ````` <0xF0><0x9F><0x93> `````, 121: ````` <0xB5> `````                  |
|       1083 | ````` ¿🕥? `````         | 0.00022686  | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 106: ````` <0xA5> ````` |
|        993 | ````` ¿📿? `````         | 0.000226885 | 185981: ````` <0xF0><0x9F><0x93> `````, 131: ````` <0xBF> `````                  |
|        826 | ````` ¿👗? `````         | 0.000226897 | 154565: ````` <0xF0><0x9F><0x91> `````, 253: ````` <0x97> `````                  |
|        755 | ````` ¿🐐? `````         | 0.000226967 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 246: ````` <0x90> ````` |
|        739 | ````` ¿🐀? `````         | 0.000227022 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 230: ````` <0x80> ````` |
|        801 | ````` ¿🐾? `````         | 0.000227112 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 130: ````` <0xBE> ````` |
|       1545 | ````` ¿🧨? `````         | 0.000227157 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 109: ````` <0xA8> ````` |
|        738 | ````` ¿🏿? `````           | 0.000227219 | 216125: ````` <0xF0><0x9F><0x8F> `````, 131: ````` <0xBF> `````                  |
|       1066 | ````` ¿🕔? `````         | 0.00022731  | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 250: ````` <0x94> ````` |
|        902 | ````` ¿💣? `````         | 0.000227311 | 106024: ````` <0xF0><0x9F><0x92> `````, 104: ````` <0xA3> `````                  |
|        922 | ````` ¿💷? `````         | 0.000227363 | 106024: ````` <0xF0><0x9F><0x92> `````, 123: ````` <0xB7> `````                  |
|        926 | ````` ¿💻? `````         | 0.000227415 | 251116: ````` 💻 `````                                                           |
|        837 | ````` ¿👢? `````         | 0.000227479 | 154565: ````` <0xF0><0x9F><0x91> `````, 103: ````` <0xA2> `````                  |
|        791 | ````` ¿🐴? `````         | 0.000227585 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 120: ````` <0xB4> ````` |
|        958 | ````` ¿📛? `````         | 0.000227652 | 185981: ````` <0xF0><0x9F><0x93> `````, 257: ````` <0x9B> `````                  |
|       1523 | ````` ¿🧒? `````         | 0.000227683 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 248: ````` <0x92> ````` |
|       1020 | ````` ¿🔚? `````         | 0.0002278   | 205860: ````` <0xF0><0x9F><0x94> `````, 256: ````` <0x9A> `````                  |
|       1054 | ````` ¿🔼? `````         | 0.000227837 | 205860: ````` <0xF0><0x9F><0x94> `````, 128: ````` <0xBC> `````                  |
|        983 | ````` ¿📴? `````         | 0.000227849 | 185981: ````` <0xF0><0x9F><0x93> `````, 120: ````` <0xB4> `````                  |
|        758 | ````` ¿🐓? `````         | 0.000227984 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 249: ````` <0x93> ````` |
|       1067 | ````` ¿🕕? `````         | 0.000228104 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 251: ````` <0x95> ````` |
|        873 | ````` ¿💆? `````         | 0.000228125 | 106024: ````` <0xF0><0x9F><0x92> `````, 236: ````` <0x86> `````                  |
|        817 | ````` ¿👎? `````         | 0.00022817  | 154565: ````` <0xF0><0x9F><0x91> `````, 244: ````` <0x8E> `````                  |
|       1052 | ````` ¿🔺? `````         | 0.000228225 | 205860: ````` <0xF0><0x9F><0x94> `````, 126: ````` <0xBA> `````                  |
|        939 | ````` ¿📈? `````         | 0.000228348 | 185981: ````` <0xF0><0x9F><0x93> `````, 238: ````` <0x88> `````                  |
|        997 | ````` ¿🔃? `````         | 0.000228428 | 205860: ````` <0xF0><0x9F><0x94> `````, 233: ````` <0x83> `````                  |
|        980 | ````` ¿📱? `````         | 0.000228451 | 185981: ````` <0xF0><0x9F><0x93> `````, 117: ````` <0xB1> `````                  |
|       1064 | ````` ¿🕒? `````         | 0.000228607 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 248: ````` <0x92> ````` |
|        990 | ````` ¿📻? `````         | 0.000228613 | 185981: ````` <0xF0><0x9F><0x93> `````, 127: ````` <0xBB> `````                  |
|        780 | ````` ¿🐩? `````         | 0.000228619 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 110: ````` <0xA9> ````` |
|        987 | ````` ¿📸? `````         | 0.000228636 | 185981: ````` <0xF0><0x9F><0x93> `````, 124: ````` <0xB8> `````                  |
|       1057 | ````` ¿🕊? `````          | 0.000228643 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 240: ````` <0x8A> ````` |
|        940 | ````` ¿📉? `````         | 0.000228668 | 185981: ````` <0xF0><0x9F><0x93> `````, 239: ````` <0x89> `````                  |
|       1048 | ````` ¿🔶? `````         | 0.000228684 | 205860: ````` <0xF0><0x9F><0x94> `````, 122: ````` <0xB6> `````                  |
|       1070 | ````` ¿🕘? `````         | 0.00022869  | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 254: ````` <0x98> ````` |
|       1069 | ````` ¿🕗? `````         | 0.000228705 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 253: ````` <0x97> ````` |
|       1036 | ````` ¿🔪? `````         | 0.000228709 | 205860: ````` <0xF0><0x9F><0x94> `````, 111: ````` <0xAA> `````                  |
|       1010 | ````` ¿🔐? `````         | 0.000228731 | 205860: ````` <0xF0><0x9F><0x94> `````, 246: ````` <0x90> `````                  |
|       1101 | ````` ¿🖐? `````          | 0.000228738 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 246: ````` <0x90> ````` |
|        779 | ````` ¿🐨? `````         | 0.000228754 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 109: ````` <0xA8> ````` |
|        982 | ````` ¿📳? `````         | 0.000228835 | 185981: ````` <0xF0><0x9F><0x93> `````, 119: ````` <0xB3> `````                  |
|       1053 | ````` ¿🔻? `````         | 0.000228839 | 205860: ````` <0xF0><0x9F><0x94> `````, 127: ````` <0xBB> `````                  |
|        968 | ````` ¿📥? `````         | 0.00022886  | 185981: ````` <0xF0><0x9F><0x93> `````, 106: ````` <0xA5> `````                  |
|       1072 | ````` ¿🕚? `````         | 0.000228899 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 256: ````` <0x9A> ````` |
|        986 | ````` ¿📷? `````         | 0.000228904 | 185981: ````` <0xF0><0x9F><0x93> `````, 123: ````` <0xB7> `````                  |
|       1004 | ````` ¿🔊? `````         | 0.000229028 | 205860: ````` <0xF0><0x9F><0x94> `````, 240: ````` <0x8A> `````                  |
|        942 | ````` ¿📋? `````         | 0.000229126 | 185981: ````` <0xF0><0x9F><0x93> `````, 241: ````` <0x8B> `````                  |
|       1061 | ````` ¿🕎? `````         | 0.000229127 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 244: ````` <0x8E> ````` |
|        850 | ````` ¿👯? `````         | 0.000229132 | 154565: ````` <0xF0><0x9F><0x91> `````, 115: ````` <0xAF> `````                  |
|        847 | ````` ¿👬? `````         | 0.000229159 | 154565: ````` <0xF0><0x9F><0x91> `````, 113: ````` <0xAC> `````                  |
|       1102 | ````` ¿🖕? `````         | 0.000229248 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 251: ````` <0x95> ````` |
|        953 | ````` ¿📖? `````         | 0.000229327 | 185981: ````` <0xF0><0x9F><0x93> `````, 252: ````` <0x96> `````                  |
|        798 | ````` ¿🐻? `````         | 0.000229345 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 127: ````` <0xBB> ````` |
|       1037 | ````` ¿🔫? `````         | 0.000229354 | 205860: ````` <0xF0><0x9F><0x94> `````, 112: ````` <0xAB> `````                  |
|       1022 | ````` ¿🔜? `````         | 0.000229376 | 205860: ````` <0xF0><0x9F><0x94> `````, 258: ````` <0x9C> `````                  |
|        973 | ````` ¿📪? `````         | 0.000229398 | 185981: ````` <0xF0><0x9F><0x93> `````, 111: ````` <0xAA> `````                  |
|        991 | ````` ¿📼? `````         | 0.000229425 | 185981: ````` <0xF0><0x9F><0x93> `````, 128: ````` <0xBC> `````                  |
|       1507 | ````` ¿🧂? `````         | 0.000229455 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 232: ````` <0x82> ````` |
|       1031 | ````` ¿🔥? `````         | 0.00022946  | 205860: ````` <0xF0><0x9F><0x94> `````, 106: ````` <0xA5> `````                  |
|       1009 | ````` ¿🔏? `````         | 0.00022955  | 205860: ````` <0xF0><0x9F><0x94> `````, 245: ````` <0x8F> `````                  |
|       1002 | ````` ¿🔈? `````         | 0.000229608 | 205860: ````` <0xF0><0x9F><0x94> `````, 238: ````` <0x88> `````                  |
|       1075 | ````` ¿🕝? `````         | 0.00022961  | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 259: ````` <0x9D> ````` |
|        932 | ````` ¿📁? `````         | 0.00022968  | 185981: ````` <0xF0><0x9F><0x93> `````, 231: ````` <0x81> `````                  |
|        933 | ````` ¿📂? `````         | 0.000229684 | 185981: ````` <0xF0><0x9F><0x93> `````, 232: ````` <0x82> `````                  |
|       1086 | ````` ¿🕯? `````          | 0.00022972  | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 115: ````` <0xAF> ````` |
|       1030 | ````` ¿🔤? `````         | 0.000229725 | 205860: ````` <0xF0><0x9F><0x94> `````, 105: ````` <0xA4> `````                  |
|       1038 | ````` ¿🔬? `````         | 0.000229796 | 205860: ````` <0xF0><0x9F><0x94> `````, 113: ````` <0xAC> `````                  |
|        934 | ````` ¿📃? `````         | 0.000229801 | 185981: ````` <0xF0><0x9F><0x93> `````, 233: ````` <0x83> `````                  |
|       1080 | ````` ¿🕢? `````         | 0.000229874 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 103: ````` <0xA2> ````` |
|        908 | ````` ¿💩? `````         | 0.000229898 | 106024: ````` <0xF0><0x9F><0x92> `````, 110: ````` <0xA9> `````                  |
|       1024 | ````` ¿🔞? `````         | 0.00022993  | 205860: ````` <0xF0><0x9F><0x94> `````, 260: ````` <0x9E> `````                  |
|       1045 | ````` ¿🔳? `````         | 0.000229945 | 205860: ````` <0xF0><0x9F><0x94> `````, 119: ````` <0xB3> `````                  |
|        941 | ````` ¿📊? `````         | 0.000229997 | 185981: ````` <0xF0><0x9F><0x93> `````, 240: ````` <0x8A> `````                  |
|       1092 | ````` ¿🕷? `````          | 0.000230089 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 123: ````` <0xB7> ````` |
|       1032 | ````` ¿🔦? `````         | 0.000230175 | 205860: ````` <0xF0><0x9F><0x94> `````, 107: ````` <0xA6> `````                  |
|        965 | ````` ¿📢? `````         | 0.000230291 | 185981: ````` <0xF0><0x9F><0x93> `````, 103: ````` <0xA2> `````                  |
|       1012 | ````` ¿🔒? `````         | 0.000230342 | 205860: ````` <0xF0><0x9F><0x94> `````, 248: ````` <0x92> `````                  |
|        981 | ````` ¿📲? `````         | 0.00023036  | 185981: ````` <0xF0><0x9F><0x93> `````, 118: ````` <0xB2> `````                  |
|       1013 | ````` ¿🔓? `````         | 0.00023039  | 205860: ````` <0xF0><0x9F><0x94> `````, 249: ````` <0x93> `````                  |
|        971 | ````` ¿📨? `````         | 0.000230491 | 2226: ````` <0xF0><0x9F> `````, 65064: ````` <0x93><0xA8> `````                  |
|       1046 | ````` ¿🔴? `````         | 0.000230509 | 205860: ````` <0xF0><0x9F><0x94> `````, 120: ````` <0xB4> `````                  |
|        956 | ````` ¿📙? `````         | 0.000230633 | 185981: ````` <0xF0><0x9F><0x93> `````, 255: ````` <0x99> `````                  |
|       1082 | ````` ¿🕤? `````         | 0.000230687 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 105: ````` <0xA4> ````` |
|        884 | ````` ¿💑? `````         | 0.000230778 | 106024: ````` <0xF0><0x9F><0x92> `````, 247: ````` <0x91> `````                  |
|        950 | ````` ¿📓? `````         | 0.000230964 | 185981: ````` <0xF0><0x9F><0x93> `````, 249: ````` <0x93> `````                  |
|       1065 | ````` ¿🕓? `````         | 0.000231106 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 249: ````` <0x93> ````` |
|       1043 | ````` ¿🔱? `````         | 0.00023135  | 205860: ````` <0xF0><0x9F><0x94> `````, 117: ````` <0xB1> `````                  |
|        944 | ````` ¿📍? `````         | 0.000231356 | 185981: ````` <0xF0><0x9F><0x93> `````, 243: ````` <0x8D> `````                  |
|        955 | ````` ¿📘? `````         | 0.000231374 | 185981: ````` <0xF0><0x9F><0x93> `````, 254: ````` <0x98> `````                  |
|       1017 | ````` ¿🔗? `````         | 0.000231393 | 205860: ````` <0xF0><0x9F><0x94> `````, 253: ````` <0x97> `````                  |
|        947 | ````` ¿📐? `````         | 0.00023146  | 185981: ````` <0xF0><0x9F><0x93> `````, 246: ````` <0x90> `````                  |
|        989 | ````` ¿📺? `````         | 0.000231558 | 185981: ````` <0xF0><0x9F><0x93> `````, 126: ````` <0xBA> `````                  |
|        948 | ````` ¿📑? `````         | 0.000231596 | 185981: ````` <0xF0><0x9F><0x93> `````, 247: ````` <0x91> `````                  |
|        995 | ````` ¿🔁? `````         | 0.000231602 | 205860: ````` <0xF0><0x9F><0x94> `````, 231: ````` <0x81> `````                  |
|        970 | ````` ¿📧? `````         | 0.000231831 | 185981: ````` <0xF0><0x9F><0x93> `````, 108: ````` <0xA7> `````                  |
|        972 | ````` ¿📩? `````         | 0.000231878 | 185981: ````` <0xF0><0x9F><0x93> `````, 110: ````` <0xA9> `````                  |
|       1051 | ````` ¿🔹? `````         | 0.000231898 | 205860: ````` <0xF0><0x9F><0x94> `````, 125: ````` <0xB9> `````                  |
|        952 | ````` ¿📕? `````         | 0.000231952 | 185981: ````` <0xF0><0x9F><0x93> `````, 251: ````` <0x95> `````                  |
|       1003 | ````` ¿🔉? `````         | 0.000231963 | 205860: ````` <0xF0><0x9F><0x94> `````, 239: ````` <0x89> `````                  |
|        977 | ````` ¿📮? `````         | 0.000231993 | 185981: ````` <0xF0><0x9F><0x93> `````, 114: ````` <0xAE> `````                  |
|       1027 | ````` ¿🔡? `````         | 0.00023215  | 205860: ````` <0xF0><0x9F><0x94> `````, 102: ````` <0xA1> `````                  |
|       1050 | ````` ¿🔸? `````         | 0.00023216  | 205860: ````` <0xF0><0x9F><0x94> `````, 124: ````` <0xB8> `````                  |
|       1091 | ````` ¿🕶? `````          | 0.000232206 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 122: ````` <0xB6> ````` |
|       1028 | ````` ¿🔢? `````         | 0.000232224 | 205860: ````` <0xF0><0x9F><0x94> `````, 103: ````` <0xA2> `````                  |
|       1014 | ````` ¿🔔? `````         | 0.00023223  | 2226: ````` <0xF0><0x9F> `````, 10121: ````` <0x94><0x94> `````                  |
|        921 | ````` ¿💶? `````         | 0.000232244 | 106024: ````` <0xF0><0x9F><0x92> `````, 122: ````` <0xB6> `````                  |
|        945 | ````` ¿📎? `````         | 0.000232308 | 185981: ````` <0xF0><0x9F><0x93> `````, 244: ````` <0x8E> `````                  |
|       1025 | ````` ¿🔟? `````         | 0.000232323 | 205860: ````` <0xF0><0x9F><0x94> `````, 261: ````` <0x9F> `````                  |
|       1095 | ````` ¿🕺? `````         | 0.000232414 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 126: ````` <0xBA> ````` |
|       1097 | ````` ¿🖊? `````          | 0.000232664 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 240: ````` <0x8A> ````` |
|        959 | ````` ¿📜? `````         | 0.000232672 | 185981: ````` <0xF0><0x9F><0x93> `````, 258: ````` <0x9C> `````                  |
|       1011 | ````` ¿🔑? `````         | 0.000232906 | 205860: ````` <0xF0><0x9F><0x94> `````, 247: ````` <0x91> `````                  |
|        967 | ````` ¿📤? `````         | 0.000232958 | 185981: ````` <0xF0><0x9F><0x93> `````, 105: ````` <0xA4> `````                  |
|       1079 | ````` ¿🕡? `````         | 0.000233031 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 102: ````` <0xA1> ````` |
|       1034 | ````` ¿🔨? `````         | 0.000233136 | 205860: ````` <0xF0><0x9F><0x94> `````, 109: ````` <0xA8> `````                  |
|       1081 | ````` ¿🕣? `````         | 0.000233156 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 104: ````` <0xA3> ````` |
|        969 | ````` ¿📦? `````         | 0.000233351 | 185981: ````` <0xF0><0x9F><0x93> `````, 107: ````` <0xA6> `````                  |
|        957 | ````` ¿📚? `````         | 0.00023343  | 185981: ````` <0xF0><0x9F><0x93> `````, 256: ````` <0x9A> `````                  |
|       1005 | ````` ¿🔋? `````         | 0.000233447 | 205860: ````` <0xF0><0x9F><0x94> `````, 241: ````` <0x8B> `````                  |
|        979 | ````` ¿📰? `````         | 0.000233553 | 2226: ````` <0xF0><0x9F> `````, 22231: ````` <0x93><0xB0> `````                  |
|        946 | ````` ¿📏? `````         | 0.000233721 | 185981: ````` <0xF0><0x9F><0x93> `````, 245: ````` <0x8F> `````                  |
|       1001 | ````` ¿🔇? `````         | 0.000233794 | 205860: ````` <0xF0><0x9F><0x94> `````, 237: ````` <0x87> `````                  |
|        966 | ````` ¿📣? `````         | 0.000233844 | 185981: ````` <0xF0><0x9F><0x93> `````, 104: ````` <0xA3> `````                  |
|       1023 | ````` ¿🔝? `````         | 0.000233859 | 205860: ````` <0xF0><0x9F><0x94> `````, 259: ````` <0x9D> `````                  |
|       1535 | ````` ¿🧞? `````         | 0.000234019 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 260: ````` <0x9E> ````` |
|       1096 | ````` ¿🖇? `````          | 0.000234058 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 237: ````` <0x87> ````` |
|       1035 | ````` ¿🔩? `````         | 0.000234105 | 205860: ````` <0xF0><0x9F><0x94> `````, 110: ````` <0xA9> `````                  |
|        964 | ````` ¿📡? `````         | 0.000234346 | 185981: ````` <0xF0><0x9F><0x93> `````, 102: ````` <0xA1> `````                  |
|       1018 | ````` ¿🔘? `````         | 0.000234948 | 205860: ````` <0xF0><0x9F><0x94> `````, 254: ````` <0x98> `````                  |
|       1033 | ````` ¿🔧? `````         | 0.000234959 | 205860: ````` <0xF0><0x9F><0x94> `````, 108: ````` <0xA7> `````                  |
|       1015 | ````` ¿🔕? `````         | 0.00023513  | 205860: ````` <0xF0><0x9F><0x94> `````, 251: ````` <0x95> `````                  |
|       1063 | ````` ¿🕑? `````         | 0.000235403 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 247: ````` <0x91> ````` |
|       1055 | ````` ¿🔽? `````         | 0.000235532 | 205860: ````` <0xF0><0x9F><0x94> `````, 129: ````` <0xBD> `````                  |
|       1078 | ````` ¿🕠? `````         | 0.000235819 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 262: ````` <0xA0> ````` |
|       1008 | ````` ¿🔎? `````         | 0.000235932 | 205860: ````` <0xF0><0x9F><0x94> `````, 244: ````` <0x8E> `````                  |
|       1058 | ````` ¿🕋? `````         | 0.000236333 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 241: ````` <0x8B> ````` |
|       1019 | ````` ¿🔙? `````         | 0.000236367 | 205860: ````` <0xF0><0x9F><0x94> `````, 255: ````` <0x99> `````                  |
|       1077 | ````` ¿🕟? `````         | 0.000236693 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 261: ````` <0x9F> ````` |
|       1059 | ````` ¿🕌? `````         | 0.000236894 | 2226: ````` <0xF0><0x9F> `````, 12443: ````` <0x95><0x8C> `````                  |
|       1039 | ````` ¿🔭? `````         | 0.000237721 | 205860: ````` <0xF0><0x9F><0x94> `````, 263: ````` <0xAD> `````                  |
|       1094 | ````` ¿🕹? `````          | 0.000237925 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 125: ````` <0xB9> ````` |
|        976 | ````` ¿📭? `````         | 0.000238096 | 185981: ````` <0xF0><0x9F><0x93> `````, 263: ````` <0xAD> `````                  |
|       1088 | ````` ¿🕳? `````          | 0.000238117 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 119: ````` <0xB3> ````` |
|       1103 | ````` ¿🖖? `````         | 0.000238131 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 252: ````` <0x96> ````` |
|        924 | ````` ¿💹? `````         | 0.000238528 | 106024: ````` <0xF0><0x9F><0x92> `````, 125: ````` <0xB9> `````                  |
|       1049 | ````` ¿🔷? `````         | 0.00023858  | 205860: ````` <0xF0><0x9F><0x94> `````, 123: ````` <0xB7> `````                  |
|        996 | ````` ¿🔂? `````         | 0.000238917 | 205860: ````` <0xF0><0x9F><0x94> `````, 232: ````` <0x82> `````                  |
|       1664 | ````` ¿\U000e0074? ````` | 0.000239119 | 202195: ````` \U000e0074 `````                                                   |
|       1084 | ````` ¿🕦? `````         | 0.000239132 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 107: ````` <0xA6> ````` |
|       1056 | ````` ¿🕉? `````          | 0.000239168 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 239: ````` <0x89> ````` |
|       1093 | ````` ¿🕸? `````          | 0.000239977 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 124: ````` <0xB8> ````` |
|       1090 | ````` ¿🕵? `````          | 0.000240198 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 121: ````` <0xB5> ````` |
|        923 | ````` ¿💸? `````         | 0.00024038  | 106024: ````` <0xF0><0x9F><0x92> `````, 124: ````` <0xB8> `````                  |
|       1071 | ````` ¿🕙? `````         | 0.00024059  | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 255: ````` <0x99> ````` |
|       1089 | ````` ¿🕴? `````          | 0.000240673 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 120: ````` <0xB4> ````` |
|       1041 | ````` ¿🔯? `````         | 0.000240981 | 205860: ````` <0xF0><0x9F><0x94> `````, 115: ````` <0xAF> `````                  |
|       1120 | ````` ¿🗣? `````          | 0.000241283 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 104: ````` <0xA3> ````` |
|       1174 | ````` ¿😬? `````         | 0.00024139  | 188568: ````` <0xF0><0x9F><0x98> `````, 113: ````` <0xAC> `````                  |
|       1105 | ````` ¿🖥? `````          | 0.000241495 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 106: ````` <0xA5> ````` |
|       1062 | ````` ¿🕐? `````         | 0.000241617 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 246: ````` <0x90> ````` |
|       1582 | ````` ¿🪃? `````         | 0.000241655 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 233: ````` <0x83> ````` |
|       1125 | ````` ¿🗻? `````         | 0.000241912 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 127: ````` <0xBB> ````` |
|       1202 | ````` ¿🙈? `````         | 0.000241984 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 238: ````` <0x88> ````` |
|       1658 | ````` ¿\U000e0063? ````` | 0.000242148 | 202213: ````` \U000e0063 `````                                                   |
|        929 | ````` ¿💾? `````         | 0.000242342 | 106024: ````` <0xF0><0x9F><0x92> `````, 130: ````` <0xBE> `````                  |
|       1405 | ````` ¿🥜? `````         | 0.000242942 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 258: ````` <0x9C> ````` |
|       1149 | ````` ¿😓? `````         | 0.000243056 | 188568: ````` <0xF0><0x9F><0x98> `````, 249: ````` <0x93> `````                  |
|       1498 | ````` ¿🦹? `````         | 0.000243418 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 125: ````` <0xB9> ````` |
|       1662 | ````` ¿\U000e006e? ````` | 0.000243491 | 9738: ````` \U000e006e `````                                                     |
|       1439 | ````` ¿🥾? `````         | 0.000243659 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 130: ````` <0xBE> ````` |
|       1571 | ````` ¿🩲? `````         | 0.000243822 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 118: ````` <0xB2> ````` |
|       1170 | ````` ¿😨? `````         | 0.000243902 | 188568: ````` <0xF0><0x9F><0x98> `````, 109: ````` <0xA8> `````                  |
|       1666 | ````` ¿\U000e007f? ````` | 0.000243984 | 60446: ````` \U000e007f `````                                                    |
|       1171 | ````` ¿😩? `````         | 0.000244425 | 188568: ````` <0xF0><0x9F><0x98> `````, 110: ````` <0xA9> `````                  |
|       1042 | ````` ¿🔰? `````         | 0.000244584 | 205860: ````` <0xF0><0x9F><0x94> `````, 116: ````` <0xB0> `````                  |
|       1107 | ````` ¿🖱? `````          | 0.000244709 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 117: ````` <0xB1> ````` |
|       1172 | ````` ¿😪? `````         | 0.000245164 | 188568: ````` <0xF0><0x9F><0x98> `````, 111: ````` <0xAA> `````                  |
|       1195 | ````` ¿🙁? `````         | 0.000245202 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 231: ````` <0x81> ````` |
|       1665 | ````` ¿\U000e0077? ````` | 0.000245419 | 3330: ````` <0xF3><0xA0><0x81> `````, 123: ````` <0xB7> `````                    |
|       1201 | ````` ¿🙇? `````         | 0.000245672 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 237: ````` <0x87> ````` |
|       1150 | ````` ¿😔? `````         | 0.000246104 | 188568: ````` <0xF0><0x9F><0x98> `````, 250: ````` <0x94> `````                  |
|       1552 | ````` ¿🧯? `````         | 0.00024612  | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 115: ````` <0xAF> ````` |
|       1381 | ````` ¿🥃? `````         | 0.000246157 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 233: ````` <0x83> ````` |
|       1211 | ````` ¿🚁? `````         | 0.000246183 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 231: ````` <0x81> ````` |
|       1291 | ````` ¿\U0001f6dd? ````` | 0.000246426 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 259: ````` <0x9D> ````` |
|       1409 | ````` ¿🥠? `````         | 0.000246764 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 262: ````` <0xA0> ````` |
|       1410 | ````` ¿🥡? `````         | 0.000247273 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 102: ````` <0xA1> ````` |
|       1569 | ````` ¿🩰? `````         | 0.000247333 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 116: ````` <0xB0> ````` |
|       1204 | ````` ¿🙊? `````         | 0.000247405 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 240: ````` <0x8A> ````` |
|       1156 | ````` ¿😚? `````         | 0.000247584 | 188568: ````` <0xF0><0x9F><0x98> `````, 256: ````` <0x9A> `````                  |
|       1630 | ````` ¿\U0001fac4? ````` | 0.000247861 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 234: ````` <0x84> ````` |
|       1297 | ````` ¿🛣? `````          | 0.000247926 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 104: ````` <0xA3> ````` |
|       1347 | ````` ¿🤠? `````         | 0.000248151 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 262: ````` <0xA0> ````` |
|       1433 | ````` ¿🥸? `````         | 0.000249107 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 124: ````` <0xB8> ````` |
|       1184 | ````` ¿😶? `````         | 0.000249144 | 188568: ````` <0xF0><0x9F><0x98> `````, 122: ````` <0xB6> `````                  |
|       1378 | ````` ¿🥀? `````         | 0.000249427 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 230: ````` <0x80> ````` |
|       1384 | ````` ¿🥇? `````         | 0.000249904 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 237: ````` <0x87> ````` |
|       1382 | ````` ¿🥄? `````         | 0.000250118 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 234: ````` <0x84> ````` |
|       1392 | ````` ¿🥏? `````         | 0.000251096 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 245: ````` <0x8F> ````` |
|       1310 | ````` ¿🛹? `````         | 0.00025138  | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 125: ````` <0xB9> ````` |
|       1584 | ````` ¿🪅? `````         | 0.000251488 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 235: ````` <0x85> ````` |
|       1344 | ````` ¿🤝? `````         | 0.000251539 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 259: ````` <0x9D> ````` |
|       1572 | ````` ¿🩳? `````         | 0.000251809 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 119: ````` <0xB3> ````` |
|       1452 | ````` ¿🦋? `````         | 0.000252353 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 241: ````` <0x8B> ````` |
|       1395 | ````` ¿🥒? `````         | 0.000252395 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 248: ````` <0x92> ````` |
|       1305 | ````` ¿🛴? `````         | 0.000253197 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 120: ````` <0xB4> ````` |
|       1413 | ````` ¿🥤? `````         | 0.00025324  | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 105: ````` <0xA4> ````` |
|       1407 | ````` ¿🥞? `````         | 0.00025327  | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 260: ````` <0x9E> ````` |
|       1414 | ````` ¿🥥? `````         | 0.000253303 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 106: ````` <0xA5> ````` |
|       1362 | ````` ¿🤯? `````         | 0.000253346 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 115: ````` <0xAF> ````` |
|       1417 | ````` ¿🥨? `````         | 0.000253375 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 109: ````` <0xA8> ````` |
|       1457 | ````` ¿🦐? `````         | 0.00025355  | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 246: ````` <0x90> ````` |
|       1336 | ````` ¿🤕? `````         | 0.000253558 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 251: ````` <0x95> ````` |
|       1348 | ````` ¿🤡? `````         | 0.000253601 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 102: ````` <0xA1> ````` |
|       1380 | ````` ¿🥂? `````         | 0.00025375  | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 232: ````` <0x82> ````` |
|       1375 | ````` ¿🤽? `````         | 0.000253928 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 129: ````` <0xBD> ````` |
|       1363 | ````` ¿🤰? `````         | 0.000254189 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 116: ````` <0xB0> ````` |
|       1373 | ````` ¿🤺? `````         | 0.000254203 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 126: ````` <0xBA> ````` |
|       1401 | ````` ¿🥘? `````         | 0.000254496 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 254: ````` <0x98> ````` |
|       1337 | ````` ¿🤖? `````         | 0.000254496 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 252: ````` <0x96> ````` |
|       1341 | ````` ¿🤚? `````         | 0.000254862 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 256: ````` <0x9A> ````` |
|       1331 | ````` ¿🤐? `````         | 0.000254896 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 246: ````` <0x90> ````` |
|       1306 | ````` ¿🛵? `````         | 0.000255029 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 121: ````` <0xB5> ````` |
|       1290 | ````` ¿🛗? `````         | 0.000255374 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 253: ````` <0x97> ````` |
|       1354 | ````` ¿🤧? `````         | 0.000255583 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 108: ````` <0xA7> ````` |
|       1295 | ````` ¿🛡? `````          | 0.000255729 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 102: ````` <0xA1> ````` |
|       1359 | ````` ¿🤬? `````         | 0.000256114 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 113: ````` <0xAC> ````` |
|       1332 | ````` ¿🤑? `````         | 0.000256165 | 2226: ````` <0xF0><0x9F> `````, 6605: ````` <0xA4><0x91> `````                   |
|       1385 | ````` ¿🥈? `````         | 0.000256255 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 238: ````` <0x88> ````` |
|       1459 | ````` ¿🦒? `````         | 0.000256281 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 248: ````` <0x92> ````` |
|       1322 | ````` ¿🟨? `````         | 0.000256734 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 109: ````` <0xA8> ````` |
|       1466 | ````` ¿🦙? `````         | 0.000257044 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 255: ````` <0x99> ````` |
|       1365 | ````` ¿🤲? `````         | 0.000257046 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 118: ````` <0xB2> ````` |
|       1376 | ````` ¿🤾? `````         | 0.000257112 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 130: ````` <0xBE> ````` |
|       1352 | ````` ¿🤥? `````         | 0.000257139 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 106: ````` <0xA5> ````` |
|       1301 | ````` ¿🛫? `````         | 0.000257262 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 112: ````` <0xAB> ````` |
|       1324 | ````` ¿🟪? `````         | 0.000257866 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 111: ````` <0xAA> ````` |
|       1308 | ````` ¿🛷? `````         | 0.000258101 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 123: ````` <0xB7> ````` |
|       1349 | ````` ¿🤢? `````         | 0.000258155 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 103: ````` <0xA2> ````` |
|       1393 | ````` ¿🥐? `````         | 0.000258467 | 2226: ````` <0xF0><0x9F> `````, 61365: ````` <0xA5><0x90> `````                  |
|       1356 | ````` ¿🤩? `````         | 0.000259688 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 110: ````` <0xA9> ````` |
|       1247 | ````` ¿🚥? `````         | 0.000261265 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 106: ````` <0xA5> ````` |
|       1276 | ````` ¿🛂? `````         | 0.000262368 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 232: ````` <0x82> ````` |
|       1470 | ````` ¿🦝? `````         | 0.00026477  | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 259: ````` <0x9D> ````` |
|       1423 | ````` ¿🥮? `````         | 0.000266057 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 114: ````` <0xAE> ````` |
|       1432 | ````` ¿🥷? `````         | 0.000266066 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 123: ````` <0xB7> ````` |
|       1268 | ````` ¿🚺? `````         | 0.000266237 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 126: ````` <0xBA> ````` |
|       1134 | ````` ¿😄? `````         | 0.000266938 | 188568: ````` <0xF0><0x9F><0x98> `````, 234: ````` <0x84> `````                  |
|       1420 | ````` ¿🥫? `````         | 0.0002672   | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 112: ````` <0xAB> ````` |
|       1257 | ````` ¿🚯? `````         | 0.000267469 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 115: ````` <0xAF> ````` |
|       1388 | ````` ¿🥋? `````         | 0.000267526 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 241: ````` <0x8B> ````` |
|       1135 | ````` ¿😅? `````         | 0.00026773  | 188568: ````` <0xF0><0x9F><0x98> `````, 235: ````` <0x85> `````                  |
|       1205 | ````` ¿🙋? `````         | 0.000267913 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 241: ````` <0x8B> ````` |
|       1304 | ````` ¿🛳? `````          | 0.000268262 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 119: ````` <0xB3> ````` |
|       1178 | ````` ¿😰? `````         | 0.000268297 | 188568: ````` <0xF0><0x9F><0x98> `````, 116: ````` <0xB0> `````                  |
|       1158 | ````` ¿😜? `````         | 0.00026838  | 188568: ````` <0xF0><0x9F><0x98> `````, 258: ````` <0x9C> `````                  |
|       1424 | ````` ¿🥯? `````         | 0.000268381 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 115: ````` <0xAF> ````` |
|       1263 | ````` ¿🚵? `````         | 0.000268404 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 121: ````` <0xB5> ````` |
|       1242 | ````` ¿🚠? `````         | 0.000268539 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 262: ````` <0xA0> ````` |
|       1371 | ````` ¿🤸? `````         | 0.000268589 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 124: ````` <0xB8> ````` |
|       1110 | ````` ¿🗂? `````          | 0.000268682 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 232: ````` <0x82> ````` |
|       1240 | ````` ¿🚞? `````         | 0.000268798 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 260: ````` <0x9E> ````` |
|       1275 | ````` ¿🛁? `````         | 0.000268824 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 231: ````` <0x81> ````` |
|       1200 | ````` ¿🙆? `````         | 0.000268863 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 236: ````` <0x86> ````` |
|       1168 | ````` ¿😦? `````         | 0.000268944 | 188568: ````` <0xF0><0x9F><0x98> `````, 107: ````` <0xA6> `````                  |
|       1254 | ````` ¿🚬? `````         | 0.000269107 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 113: ````` <0xAC> ````` |
|       1317 | ````` ¿🟣? `````         | 0.000269146 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 104: ````` <0xA3> ````` |
|       1114 | ````` ¿🗒? `````          | 0.000269213 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 248: ````` <0x92> ````` |
|       1286 | ````` ¿🛑? `````         | 0.00026946  | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 247: ````` <0x91> ````` |
|       1173 | ````` ¿😫? `````         | 0.000269583 | 188568: ````` <0xF0><0x9F><0x98> `````, 112: ````` <0xAB> `````                  |
|       1203 | ````` ¿🙉? `````         | 0.000269597 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 239: ````` <0x89> ````` |
|       1148 | ````` ¿😒? `````         | 0.000269661 | 188568: ````` <0xF0><0x9F><0x98> `````, 248: ````` <0x92> `````                  |
|       1273 | ````` ¿🚿? `````         | 0.000269667 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 131: ````` <0xBF> ````` |
|       1357 | ````` ¿🤪? `````         | 0.000269683 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 111: ````` <0xAA> ````` |
|       1355 | ````` ¿🤨? `````         | 0.00026969  | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 109: ````` <0xA8> ````` |
|       1251 | ````` ¿🚩? `````         | 0.000269706 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 110: ````` <0xA9> ````` |
|       1146 | ````` ¿😐? `````         | 0.000269749 | 2226: ````` <0xF0><0x9F> `````, 15468: ````` <0x98><0x90> `````                  |
|       1265 | ````` ¿🚷? `````         | 0.000269762 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 123: ````` <0xB7> ````` |
|       1261 | ````` ¿🚳? `````         | 0.000269771 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 119: ````` <0xB3> ````` |
|       1128 | ````` ¿🗾? `````         | 0.000269783 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 130: ````` <0xBE> ````` |
|       1213 | ````` ¿🚃? `````         | 0.000269892 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 233: ````` <0x83> ````` |
|       1227 | ````` ¿🚑? `````         | 0.000269917 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 247: ````` <0x91> ````` |
|       1208 | ````` ¿🙎? `````         | 0.000269962 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 244: ````` <0x8E> ````` |
|       1228 | ````` ¿🚒? `````         | 0.000269986 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 248: ````` <0x92> ````` |
|       1139 | ````` ¿😉? `````         | 0.000270054 | 188568: ````` <0xF0><0x9F><0x98> `````, 239: ````` <0x89> `````                  |
|       1230 | ````` ¿🚔? `````         | 0.000270266 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 250: ````` <0x94> ````` |
|       1122 | ````` ¿🗯? `````          | 0.000270266 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 115: ````` <0xAF> ````` |
|       1157 | ````` ¿😛? `````         | 0.000270362 | 188568: ````` <0xF0><0x9F><0x98> `````, 257: ````` <0x9B> `````                  |
|       1226 | ````` ¿🚐? `````         | 0.000270444 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 246: ````` <0x90> ````` |
|       1262 | ````` ¿🚴? `````         | 0.000270533 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 120: ````` <0xB4> ````` |
|       1113 | ````` ¿🗑? `````          | 0.000270537 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 247: ````` <0x91> ````` |
|       1118 | ````` ¿🗞? `````          | 0.000270546 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 260: ````` <0x9E> ````` |
|       1264 | ````` ¿🚶? `````         | 0.000270557 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 122: ````` <0xB6> ````` |
|       1175 | ````` ¿😭? `````         | 0.000270626 | 188568: ````` <0xF0><0x9F><0x98> `````, 263: ````` <0xAD> `````                  |
|       1186 | ````` ¿😸? `````         | 0.000270664 | 188568: ````` <0xF0><0x9F><0x98> `````, 124: ````` <0xB8> `````                  |
|       1141 | ````` ¿😋? `````         | 0.00027069  | 188568: ````` <0xF0><0x9F><0x98> `````, 241: ````` <0x8B> `````                  |
|       1225 | ````` ¿🚏? `````         | 0.000270693 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 245: ````` <0x8F> ````` |
|       1180 | ````` ¿😲? `````         | 0.000270716 | 188568: ````` <0xF0><0x9F><0x98> `````, 118: ````` <0xB2> `````                  |
|       1456 | ````` ¿🦏? `````         | 0.000270728 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 245: ````` <0x8F> ````` |
|       1121 | ````` ¿🗨? `````          | 0.000270795 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 109: ````` <0xA8> ````` |
|       1131 | ````` ¿😁? `````         | 0.000270869 | 188568: ````` <0xF0><0x9F><0x98> `````, 231: ````` <0x81> `````                  |
|       1116 | ````` ¿🗜? `````          | 0.000270894 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 258: ````` <0x9C> ````` |
|       1234 | ````` ¿🚘? `````         | 0.000270906 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 254: ````` <0x98> ````` |
|       1269 | ````` ¿🚻? `````         | 0.000270935 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 127: ````` <0xBB> ````` |
|       1220 | ````` ¿🚊? `````         | 0.000270978 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 240: ````` <0x8A> ````` |
|       1258 | ````` ¿🚰? `````         | 0.000271007 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 116: ````` <0xB0> ````` |
|       1232 | ````` ¿🚖? `````         | 0.000271008 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 252: ````` <0x96> ````` |
|       1267 | ````` ¿🚹? `````         | 0.000271112 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 125: ````` <0xB9> ````` |
|       1419 | ````` ¿🥪? `````         | 0.000271131 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 111: ````` <0xAA> ````` |
|       1217 | ````` ¿🚇? `````         | 0.000271135 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 237: ````` <0x87> ````` |
|       1250 | ````` ¿🚨? `````         | 0.000271137 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 109: ````` <0xA8> ````` |
|       1210 | ````` ¿🚀? `````         | 0.000271138 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 230: ````` <0x80> ````` |
|       1252 | ````` ¿🚪? `````         | 0.000271145 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 111: ````` <0xAA> ````` |
|       1108 | ````` ¿🖲? `````          | 0.000271158 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 118: ````` <0xB2> ````` |
|       1278 | ````` ¿🛄? `````         | 0.000271168 | 2226: ````` <0xF0><0x9F> `````, 7840: ````` <0x9B><0x84> `````                   |
|       1159 | ````` ¿😝? `````         | 0.000271209 | 188568: ````` <0xF0><0x9F><0x98> `````, 259: ````` <0x9D> `````                  |
|       1206 | ````` ¿🙌? `````         | 0.000271246 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 242: ````` <0x8C> ````` |
|       1283 | ````` ¿🛎? `````          | 0.00027131  | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 244: ````` <0x8E> ````` |
|       1165 | ````` ¿😣? `````         | 0.00027134  | 188568: ````` <0xF0><0x9F><0x98> `````, 104: ````` <0xA3> `````                  |
|       1212 | ````` ¿🚂? `````         | 0.000271353 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 232: ````` <0x82> ````` |
|       1162 | ````` ¿😠? `````         | 0.000271357 | 188568: ````` <0xF0><0x9F><0x98> `````, 262: ````` <0xA0> `````                  |
|       1167 | ````` ¿😥? `````         | 0.000271372 | 188568: ````` <0xF0><0x9F><0x98> `````, 106: ````` <0xA5> `````                  |
|       1284 | ````` ¿🛏? `````          | 0.000271434 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 245: ````` <0x8F> ````` |
|       1282 | ````` ¿🛍? `````          | 0.000271462 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 243: ````` <0x8D> ````` |
|       1244 | ````` ¿🚢? `````         | 0.000271526 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 103: ````` <0xA2> ````` |
|       1239 | ````` ¿🚝? `````         | 0.000271555 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 259: ````` <0x9D> ````` |
|       1272 | ````` ¿🚾? `````         | 0.000271601 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 130: ````` <0xBE> ````` |
|       1143 | ````` ¿😍? `````         | 0.000271695 | 188568: ````` <0xF0><0x9F><0x98> `````, 243: ````` <0x8D> `````                  |
|       1191 | ````` ¿😽? `````         | 0.00027172  | 188568: ````` <0xF0><0x9F><0x98> `````, 129: ````` <0xBD> `````                  |
|       1270 | ````` ¿🚼? `````         | 0.000271728 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 128: ````` <0xBC> ````` |
|       1462 | ````` ¿🦕? `````         | 0.000271728 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 251: ````` <0x95> ````` |
|       1192 | ````` ¿😾? `````         | 0.000271862 | 188568: ````` <0xF0><0x9F><0x98> `````, 130: ````` <0xBE> `````                  |
|       1260 | ````` ¿🚲? `````         | 0.000271867 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 118: ````` <0xB2> ````` |
|       1285 | ````` ¿🛐? `````         | 0.000271875 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 246: ````` <0x90> ````` |
|       1130 | ````` ¿😀? `````         | 0.000271946 | 188568: ````` <0xF0><0x9F><0x98> `````, 230: ````` <0x80> `````                  |
|       1245 | ````` ¿🚣? `````         | 0.00027199  | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 104: ````` <0xA3> ````` |
|       1281 | ````` ¿🛌? `````         | 0.000272    | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 242: ````` <0x8C> ````` |
|       1123 | ````` ¿🗳? `````          | 0.000272002 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 119: ````` <0xB3> ````` |
|       1219 | ````` ¿🚉? `````         | 0.000272007 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 239: ````` <0x89> ````` |
|       1196 | ````` ¿🙂? `````         | 0.000272032 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 232: ````` <0x82> ````` |
|       1182 | ````` ¿😴? `````         | 0.000272049 | 188568: ````` <0xF0><0x9F><0x98> `````, 120: ````` <0xB4> `````                  |
|       1259 | ````` ¿🚱? `````         | 0.000272067 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 117: ````` <0xB1> ````` |
|       1152 | ````` ¿😖? `````         | 0.000272106 | 188568: ````` <0xF0><0x9F><0x98> `````, 252: ````` <0x96> `````                  |
|       1279 | ````` ¿🛅? `````         | 0.000272124 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 235: ````` <0x85> ````` |
|       1136 | ````` ¿😆? `````         | 0.000272343 | 188568: ````` <0xF0><0x9F><0x98> `````, 236: ````` <0x86> `````                  |
|       1426 | ````` ¿🥱? `````         | 0.000272408 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 117: ````` <0xB1> ````` |
|       1274 | ````` ¿🛀? `````         | 0.000272427 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 230: ````` <0x80> ````` |
|       1190 | ````` ¿😼? `````         | 0.000272432 | 188568: ````` <0xF0><0x9F><0x98> `````, 128: ````` <0xBC> `````                  |
|       1109 | ````` ¿🖼? `````          | 0.000272472 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 128: ````` <0xBC> ````` |
|       1147 | ````` ¿😑? `````         | 0.000272475 | 188568: ````` <0xF0><0x9F><0x98> `````, 247: ````` <0x91> `````                  |
|       1198 | ````` ¿🙄? `````         | 0.000272548 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 234: ````` <0x84> ````` |
|       1124 | ````` ¿🗺? `````          | 0.000272566 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 126: ````` <0xBA> ````` |
|       1216 | ````` ¿🚆? `````         | 0.000272568 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 236: ````` <0x86> ````` |
|       1142 | ````` ¿😌? `````         | 0.000272571 | 188568: ````` <0xF0><0x9F><0x98> `````, 242: ````` <0x8C> `````                  |
|       1222 | ````` ¿🚌? `````         | 0.000272591 | 2226: ````` <0xF0><0x9F> `````, 6617: ````` <0x9A><0x8C> `````                   |
|       1161 | ````` ¿😟? `````         | 0.000272598 | 188568: ````` <0xF0><0x9F><0x98> `````, 261: ````` <0x9F> `````                  |
|       1153 | ````` ¿😗? `````         | 0.000272846 | 188568: ````` <0xF0><0x9F><0x98> `````, 253: ````` <0x97> `````                  |
|       1366 | ````` ¿🤳? `````         | 0.00027287  | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 119: ````` <0xB3> ````` |
|       1236 | ````` ¿🚚? `````         | 0.00027291  | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 256: ````` <0x9A> ````` |
|       1458 | ````` ¿🦑? `````         | 0.000272963 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 247: ````` <0x91> ````` |
|       1145 | ````` ¿😏? `````         | 0.000272977 | 188568: ````` <0xF0><0x9F><0x98> `````, 245: ````` <0x8F> `````                  |
|       1447 | ````` ¿🦆? `````         | 0.000273006 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 236: ````` <0x86> ````` |
|       1137 | ````` ¿😇? `````         | 0.000273114 | 188568: ````` <0xF0><0x9F><0x98> `````, 237: ````` <0x87> `````                  |
|       1112 | ````` ¿🗄? `````          | 0.000273123 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 234: ````` <0x84> ````` |
|       1422 | ````` ¿🥭? `````         | 0.000273232 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 263: ````` <0xAD> ````` |
|       1214 | ````` ¿🚄? `````         | 0.000273238 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 234: ````` <0x84> ````` |
|       1179 | ````` ¿😱? `````         | 0.00027326  | 188568: ````` <0xF0><0x9F><0x98> `````, 117: ````` <0xB1> `````                  |
|       1443 | ````` ¿🦂? `````         | 0.000273276 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 232: ````` <0x82> ````` |
|       1253 | ````` ¿🚫? `````         | 0.0002733   | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 112: ````` <0xAB> ````` |
|       1221 | ````` ¿🚋? `````         | 0.000273313 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 241: ````` <0x8B> ````` |
|       1129 | ````` ¿🗿? `````         | 0.000273346 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 131: ````` <0xBF> ````` |
|       1231 | ````` ¿🚕? `````         | 0.000273356 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 251: ````` <0x95> ````` |
|       1241 | ````` ¿🚟? `````         | 0.000273481 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 261: ````` <0x9F> ````` |
|       1115 | ````` ¿🗓? `````          | 0.000273523 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 249: ````` <0x93> ````` |
|       1138 | ````` ¿😈? `````         | 0.000273547 | 188568: ````` <0xF0><0x9F><0x98> `````, 238: ````` <0x88> `````                  |
|       1316 | ````` ¿🟢? `````         | 0.000273554 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 103: ````` <0xA2> ````` |
|       1224 | ````` ¿🚎? `````         | 0.00027356  | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 244: ````` <0x8E> ````` |
|       1187 | ````` ¿😹? `````         | 0.000273648 | 188568: ````` <0xF0><0x9F><0x98> `````, 125: ````` <0xB9> `````                  |
|       1235 | ````` ¿🚙? `````         | 0.000273759 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 255: ````` <0x99> ````` |
|       1133 | ````` ¿😃? `````         | 0.000273767 | 188568: ````` <0xF0><0x9F><0x98> `````, 233: ````` <0x83> `````                  |
|       1248 | ````` ¿🚦? `````         | 0.000273787 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 107: ````` <0xA6> ````` |
|       1166 | ````` ¿😤? `````         | 0.000273808 | 188568: ````` <0xF0><0x9F><0x98> `````, 105: ````` <0xA4> `````                  |
|       1280 | ````` ¿🛋? `````          | 0.000273845 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 241: ````` <0x8B> ````` |
|       1342 | ````` ¿🤛? `````         | 0.000273927 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 257: ````` <0x9B> ````` |
|       1207 | ````` ¿🙍? `````         | 0.000273968 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 243: ````` <0x8D> ````` |
|       1160 | ````` ¿😞? `````         | 0.000273972 | 188568: ````` <0xF0><0x9F><0x98> `````, 260: ````` <0x9E> `````                  |
|       1169 | ````` ¿😧? `````         | 0.000274004 | 188568: ````` <0xF0><0x9F><0x98> `````, 108: ````` <0xA7> `````                  |
|       1199 | ````` ¿🙅? `````         | 0.000274006 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 235: ````` <0x85> ````` |
|       1246 | ````` ¿🚤? `````         | 0.000274029 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 105: ````` <0xA4> ````` |
|       1243 | ````` ¿🚡? `````         | 0.000274041 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 102: ````` <0xA1> ````` |
|       1111 | ````` ¿🗃? `````          | 0.000274047 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 233: ````` <0x83> ````` |
|       1163 | ````` ¿😡? `````         | 0.000274114 | 188568: ````` <0xF0><0x9F><0x98> `````, 102: ````` <0xA1> `````                  |
|       1155 | ````` ¿😙? `````         | 0.000274161 | 188568: ````` <0xF0><0x9F><0x98> `````, 255: ````` <0x99> `````                  |
|       1238 | ````` ¿🚜? `````         | 0.000274167 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 258: ````` <0x9C> ````` |
|       1189 | ````` ¿😻? `````         | 0.000274186 | 188568: ````` <0xF0><0x9F><0x98> `````, 127: ````` <0xBB> `````                  |
|       1181 | ````` ¿😳? `````         | 0.0002742   | 188568: ````` <0xF0><0x9F><0x98> `````, 119: ````` <0xB3> `````                  |
|       1425 | ````` ¿🥰? `````         | 0.000274261 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 116: ````` <0xB0> ````` |
|       1390 | ````` ¿🥍? `````         | 0.0002743   | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 243: ````` <0x8D> ````` |
|       1127 | ````` ¿🗽? `````         | 0.000274401 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 129: ````` <0xBD> ````` |
|       1223 | ````` ¿🚍? `````         | 0.000274434 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 243: ````` <0x8D> ````` |
|       1464 | ````` ¿🦗? `````         | 0.000274449 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 253: ````` <0x97> ````` |
|       1266 | ````` ¿🚸? `````         | 0.000274536 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 124: ````` <0xB8> ````` |
|       1277 | ````` ¿🛃? `````         | 0.000274545 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 233: ````` <0x83> ````` |
|       1193 | ````` ¿😿? `````         | 0.000274549 | 188568: ````` <0xF0><0x9F><0x98> `````, 131: ````` <0xBF> `````                  |
|       1237 | ````` ¿🚛? `````         | 0.000274599 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 257: ````` <0x9B> ````` |
|       1144 | ````` ¿😎? `````         | 0.00027461  | 188568: ````` <0xF0><0x9F><0x98> `````, 244: ````` <0x8E> `````                  |
|       1151 | ````` ¿😕? `````         | 0.00027466  | 188568: ````` <0xF0><0x9F><0x98> `````, 251: ````` <0x95> `````                  |
|       1315 | ````` ¿🟡? `````         | 0.000274709 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 102: ````` <0xA1> ````` |
|       1194 | ````` ¿🙀? `````         | 0.000274731 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 230: ````` <0x80> ````` |
|       1367 | ````` ¿🤴? `````         | 0.000274739 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 120: ````` <0xB4> ````` |
|       1176 | ````` ¿😮? `````         | 0.000274749 | 188568: ````` <0xF0><0x9F><0x98> `````, 114: ````` <0xAE> `````                  |
|       1294 | ````` ¿🛠? `````          | 0.000274752 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 262: ````` <0xA0> ````` |
|       1104 | ````` ¿🖤? `````         | 0.00027478  | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 105: ````` <0xA4> ````` |
|       1106 | ````` ¿🖨? `````          | 0.000274829 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 109: ````` <0xA8> ````` |
|       1271 | ````` ¿🚽? `````         | 0.000274895 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 129: ````` <0xBD> ````` |
|       1364 | ````` ¿🤱? `````         | 0.000274918 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 117: ````` <0xB1> ````` |
|       1126 | ````` ¿🗼? `````         | 0.000274969 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 128: ````` <0xBC> ````` |
|       1183 | ````` ¿😵? `````         | 0.000275015 | 188568: ````` <0xF0><0x9F><0x98> `````, 121: ````` <0xB5> `````                  |
|       1256 | ````` ¿🚮? `````         | 0.000275024 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 114: ````` <0xAE> ````` |
|       1132 | ````` ¿😂? `````         | 0.00027504  | 188568: ````` <0xF0><0x9F><0x98> `````, 232: ````` <0x82> `````                  |
|       1429 | ````` ¿🥴? `````         | 0.000275042 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 120: ````` <0xB4> ````` |
|       1400 | ````` ¿🥗? `````         | 0.000275092 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 253: ````` <0x97> ````` |
|       1453 | ````` ¿🦌? `````         | 0.000275107 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 242: ````` <0x8C> ````` |
|       1320 | ````` ¿🟦? `````         | 0.000275131 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 107: ````` <0xA6> ````` |
|       1296 | ````` ¿🛢? `````          | 0.000275265 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 103: ````` <0xA2> ````` |
|       1471 | ````` ¿🦞? `````         | 0.000275301 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 260: ````` <0x9E> ````` |
|       1329 | ````` ¿🤎? `````         | 0.000275316 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 244: ````` <0x8E> ````` |
|       1437 | ````` ¿🥼? `````         | 0.000275464 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 128: ````` <0xBC> ````` |
|       1455 | ````` ¿🦎? `````         | 0.000275498 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 244: ````` <0x8E> ````` |
|       1441 | ````` ¿🦀? `````         | 0.000275512 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 230: ````` <0x80> ````` |
|       1229 | ````` ¿🚓? `````         | 0.000275518 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 249: ````` <0x93> ````` |
|       1338 | ````` ¿🤗? `````         | 0.000275775 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 253: ````` <0x97> ````` |
|       1399 | ````` ¿🥖? `````         | 0.000275988 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 252: ````` <0x96> ````` |
|       1411 | ````` ¿🥢? `````         | 0.000276094 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 103: ````` <0xA2> ````` |
|       1140 | ````` ¿😊? `````         | 0.000276159 | 188568: ````` <0xF0><0x9F><0x98> `````, 240: ````` <0x8A> `````                  |
|       1233 | ````` ¿🚗? `````         | 0.000276205 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 253: ````` <0x97> ````` |
|       1351 | ````` ¿🤤? `````         | 0.000276229 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 105: ````` <0xA4> ````` |
|       1412 | ````` ¿🥣? `````         | 0.000276252 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 104: ````` <0xA3> ````` |
|       1369 | ````` ¿🤶? `````         | 0.000276254 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 122: ````` <0xB6> ````` |
|       1188 | ````` ¿😺? `````         | 0.000276309 | 188568: ````` <0xF0><0x9F><0x98> `````, 126: ````` <0xBA> `````                  |
|       1249 | ````` ¿🚧? `````         | 0.000276384 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 108: ````` <0xA7> ````` |
|       1469 | ````` ¿🦜? `````         | 0.000276402 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 258: ````` <0x9C> ````` |
|       1440 | ````` ¿🥿? `````         | 0.000276514 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 131: ````` <0xBF> ````` |
|       1289 | ````` ¿🛖? `````         | 0.000276528 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 252: ````` <0x96> ````` |
|       1321 | ````` ¿🟧? `````         | 0.000276597 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 108: ````` <0xA7> ````` |
|       1299 | ````` ¿🛥? `````          | 0.000276611 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 106: ````` <0xA5> ````` |
|       1312 | ````` ¿🛻? `````         | 0.000276645 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 127: ````` <0xBB> ````` |
|       1177 | ````` ¿😯? `````         | 0.000276659 | 188568: ````` <0xF0><0x9F><0x98> `````, 115: ````` <0xAF> `````                  |
|       1403 | ````` ¿🥚? `````         | 0.000276683 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 256: ````` <0x9A> ````` |
|       1119 | ````` ¿🗡? `````          | 0.000276729 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 102: ````` <0xA1> ````` |
|       1463 | ````` ¿🦖? `````         | 0.000276797 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 252: ````` <0x96> ````` |
|       1445 | ````` ¿🦄? `````         | 0.000276798 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 234: ````` <0x84> ````` |
|       1379 | ````` ¿🥁? `````         | 0.000276832 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 231: ````` <0x81> ````` |
|       1346 | ````` ¿🤟? `````         | 0.000276901 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 261: ````` <0x9F> ````` |
|       1396 | ````` ¿🥓? `````         | 0.000276998 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 249: ````` <0x93> ````` |
|       1467 | ````` ¿🦚? `````         | 0.000277068 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 256: ````` <0x9A> ````` |
|       1326 | ````` ¿\U0001f7f0? ````` | 0.0002771   | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 116: ````` <0xB0> ````` |
|       1454 | ````` ¿🦍? `````         | 0.000277127 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 243: ````` <0x8D> ````` |
|       1333 | ````` ¿🤒? `````         | 0.000277174 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 248: ````` <0x92> ````` |
|       1164 | ````` ¿😢? `````         | 0.00027731  | 188568: ````` <0xF0><0x9F><0x98> `````, 103: ````` <0xA2> `````                  |
|       1313 | ````` ¿🛼? `````         | 0.00027732  | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 128: ````` <0xBC> ````` |
|       1327 | ````` ¿🤌? `````         | 0.000277348 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 242: ````` <0x8C> ````` |
|       1397 | ````` ¿🥔? `````         | 0.00027736  | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 250: ````` <0x94> ````` |
|       1372 | ````` ¿🤹? `````         | 0.000277515 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 125: ````` <0xB9> ````` |
|       1339 | ````` ¿🤘? `````         | 0.00027755  | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 254: ````` <0x98> ````` |
|       1255 | ````` ¿🚭? `````         | 0.000277722 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 263: ````` <0xAD> ````` |
|       1398 | ````` ¿🥕? `````         | 0.000277883 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 251: ````` <0x95> ````` |
|       1154 | ````` ¿😘? `````         | 0.000278194 | 188568: ````` <0xF0><0x9F><0x98> `````, 254: ````` <0x98> `````                  |
|       1218 | ````` ¿🚈? `````         | 0.000278339 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 238: ````` <0x88> ````` |
|       1387 | ````` ¿🥊? `````         | 0.000278369 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 240: ````` <0x8A> ````` |
|       1215 | ````` ¿🚅? `````         | 0.000278386 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 235: ````` <0x85> ````` |
|       1418 | ````` ¿🥩? `````         | 0.000278751 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 110: ````` <0xA9> ````` |
|       1353 | ````` ¿🤦? `````         | 0.000278816 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 107: ````` <0xA6> ````` |
|       1343 | ````` ¿🤜? `````         | 0.000278817 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 258: ````` <0x9C> ````` |
|       1416 | ````` ¿🥧? `````         | 0.000279254 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 108: ````` <0xA7> ````` |
|       1406 | ````` ¿🥝? `````         | 0.00027943  | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 259: ````` <0x9D> ````` |
|       1117 | ````` ¿🗝? `````          | 0.000279622 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 259: ````` <0x9D> ````` |
|       1374 | ````` ¿🤼? `````         | 0.000279634 | 2226: ````` <0xF0><0x9F> `````, 139814: ````` <0xA4><0xBC> `````                 |
|       1368 | ````` ¿🤵? `````         | 0.000279756 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 121: ````` <0xB5> ````` |
|       1302 | ````` ¿🛬? `````         | 0.000279816 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 113: ````` <0xAC> ````` |
|       1319 | ````` ¿🟥? `````         | 0.000279964 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 106: ````` <0xA5> ````` |
|       1287 | ````` ¿🛒? `````         | 0.00027997  | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 248: ````` <0x92> ````` |
|       1197 | ````` ¿🙃? `````         | 0.000280029 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 233: ````` <0x83> ````` |
|       1451 | ````` ¿🦊? `````         | 0.000280159 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 240: ````` <0x8A> ````` |
|       1185 | ````` ¿😷? `````         | 0.000280363 | 188568: ````` <0xF0><0x9F><0x98> `````, 123: ````` <0xB7> `````                  |
|       1300 | ````` ¿🛩? `````          | 0.000280477 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 110: ````` <0xA9> ````` |
|       1421 | ````` ¿🥬? `````         | 0.000280677 | 2226: ````` <0xF0><0x9F> `````, 178448: ````` <0xA5><0xAC> `````                 |
|       1209 | ````` ¿🙏? `````         | 0.000281005 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 245: ````` <0x8F> ````` |
|       1435 | ````` ¿🥺? `````         | 0.000281089 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 126: ````` <0xBA> ````` |
|       1303 | ````` ¿🛰? `````          | 0.000281157 | 2226: ````` <0xF0><0x9F> `````, 71996: ````` <0x9B><0xB0> `````                  |
|       1448 | ````` ¿🦇? `````         | 0.000281327 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 237: ````` <0x87> ````` |
|       1328 | ````` ¿🤍? `````         | 0.000281368 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 243: ````` <0x8D> ````` |
|       1361 | ````` ¿🤮? `````         | 0.000281389 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 114: ````` <0xAE> ````` |
|       1386 | ````` ¿🥉? `````         | 0.000281424 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 239: ````` <0x89> ````` |
|       1428 | ````` ¿🥳? `````         | 0.000281625 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 119: ````` <0xB3> ````` |
|       1340 | ````` ¿🤙? `````         | 0.000281644 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 255: ````` <0x99> ````` |
|       1334 | ````` ¿🤓? `````         | 0.000281797 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 249: ````` <0x93> ````` |
|       1436 | ````` ¿🥻? `````         | 0.00028194  | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 127: ````` <0xBB> ````` |
|       1391 | ````` ¿🥎? `````         | 0.000281977 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 244: ````` <0x8E> ````` |
|       1307 | ````` ¿🛶? `````         | 0.000282062 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 122: ````` <0xB6> ````` |
|       1427 | ````` ¿🥲? `````         | 0.000282282 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 118: ````` <0xB2> ````` |
|       1325 | ````` ¿🟫? `````         | 0.000282337 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 112: ````` <0xAB> ````` |
|       1442 | ````` ¿🦁? `````         | 0.000282427 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 231: ````` <0x81> ````` |
|       1438 | ````` ¿🥽? `````         | 0.00028248  | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 129: ````` <0xBD> ````` |
|       1298 | ````` ¿🛤? `````          | 0.000282495 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 105: ````` <0xA4> ````` |
|       1394 | ````` ¿🥑? `````         | 0.000282531 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 247: ````` <0x91> ````` |
|       1360 | ````` ¿🤭? `````         | 0.000282727 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 263: ````` <0xAD> ````` |
|       1318 | ````` ¿🟤? `````         | 0.000282886 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 105: ````` <0xA4> ````` |
|       1314 | ````` ¿🟠? `````         | 0.000283132 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 262: ````` <0xA0> ````` |
|       1468 | ````` ¿🦛? `````         | 0.00028324  | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 257: ````` <0x9B> ````` |
|       1288 | ````` ¿🛕? `````         | 0.000283256 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 251: ````` <0x95> ````` |
|       1402 | ````` ¿🥙? `````         | 0.000283399 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 255: ````` <0x99> ````` |
|       1350 | ````` ¿🤣? `````         | 0.000283435 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 104: ````` <0xA3> ````` |
|       1311 | ````` ¿🛺? `````         | 0.000283509 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 126: ````` <0xBA> ````` |
|       1404 | ````` ¿🥛? `````         | 0.000283517 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 257: ````` <0x9B> ````` |
|       1446 | ````` ¿🦅? `````         | 0.00028355  | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 235: ````` <0x85> ````` |
|       1444 | ````` ¿🦃? `````         | 0.000283579 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 233: ````` <0x83> ````` |
|       1415 | ````` ¿🥦? `````         | 0.000283599 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 107: ````` <0xA6> ````` |
|       1330 | ````` ¿🤏? `````         | 0.000283638 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 245: ````` <0x8F> ````` |
|       1460 | ````` ¿🦓? `````         | 0.00028364  | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 249: ````` <0x93> ````` |
|       1377 | ````` ¿🤿? `````         | 0.000283683 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 131: ````` <0xBF> ````` |
|       1408 | ````` ¿🥟? `````         | 0.000283769 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 261: ````` <0x9F> ````` |
|       1434 | ````` ¿\U0001f979? ````` | 0.000283872 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 125: ````` <0xB9> ````` |
|       1449 | ````` ¿🦈? `````         | 0.000284154 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 238: ````` <0x88> ````` |
|       1431 | ````` ¿🥶? `````         | 0.000284492 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 122: ````` <0xB6> ````` |
|       1358 | ````` ¿🤫? `````         | 0.000284549 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 112: ````` <0xAB> ````` |
|       1383 | ````` ¿🥅? `````         | 0.000284618 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 235: ````` <0x85> ````` |
|       1389 | ````` ¿🥌? `````         | 0.000284667 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 242: ````` <0x8C> ````` |
|       1465 | ````` ¿🦘? `````         | 0.000284749 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 254: ````` <0x98> ````` |
|       1370 | ````` ¿🤷? `````         | 0.000284988 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 123: ````` <0xB7> ````` |
|       1323 | ````` ¿🟩? `````         | 0.000285164 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 110: ````` <0xA9> ````` |
|       1461 | ````` ¿🦔? `````         | 0.000285238 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 250: ````` <0x94> ````` |
|       1430 | ````` ¿🥵? `````         | 0.000285262 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 121: ````` <0xB5> ````` |
|       1335 | ````` ¿🤔? `````         | 0.000285272 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 250: ````` <0x94> ````` |
|       1293 | ````` ¿\U0001f6df? ````` | 0.000285306 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 261: ````` <0x9F> ````` |
|       1292 | ````` ¿\U0001f6de? ````` | 0.000285685 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 260: ````` <0x9E> ````` |
|       1309 | ````` ¿🛸? `````         | 0.000285856 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 124: ````` <0xB8> ````` |
|       1450 | ````` ¿🦉? `````         | 0.000285903 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 239: ````` <0x89> ````` |
|       1345 | ````` ¿🤞? `````         | 0.000286284 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 260: ````` <0x9E> ````` |
</details>

