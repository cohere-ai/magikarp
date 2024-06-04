# Report for `CohereForAI/c4ai-command-r-plus`

## Model info

* Tied embeddings: yes
* LM head uses bias: no
* Indicator for under-trained tokens: E_{out} Cosine Distance
  * Overall distribution 0.847 +/- 0.108
  * Token used for verification prompt building: `InvalidProtocolBufferException`
  * Verification threshold: 0.669
  * Threshold for showing candidate under-trained tokens: 0.051
  * Median verified threshold (for bytes, unreachable and special tokens): 0.017
* Embeddings shape: (256000, 12288)
* Vocabulary size: 255029
  * Number of single byte tokens: 256, of which 13 below indicator threshold
  * Number of special tokens: 37, of which 26 below indicator threshold
  * Number of non-single-byte unreachable tokens: 1403, of which 1403 below indicator threshold
  * Number of non-single-byte UTF-fragment tokens: 2956, 9 below soft indicator threshold
  * Number of tested under-trained tokens: 5012, 4962 non-special, 47 below p = 0.01 threshold, 35 below soft indicator threshold

## Under-trained token indicators plot
![Indicators scatter plots](../indicators_pairplot_byid/CohereForAI_c4ai_command_r_plus.png)

## Verification plot
![Verification plot](../verifications_scatterplot/CohereForAI_c4ai_command_r_plus.png)

## Under-trained token verification results
35 entries below threshold of 0.051

|   token_id | token                                                                                                                                |    indicator | max_prob                                                         | in_other_tokens                                                                                                                                                                                                                                                                 |
|------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     127300 | ````` tocguid `````                                                                                                                  | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |                                                                                                                                                                                                                                                                                 |
|     140485 | ````` 目前尚未由人工引 `````                                                                                                         | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` 目前尚未由人工引種栽培 `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` 目前尚未由人工引种栽培 `````</span>                                                                                        |
|      51386 | ````` ▁ARStdSong `````                                                                                                               | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |                                                                                                                                                                                                                                                                                 |
|     239520 | ````` ▁hbBiddersParams `````                                                                                                         | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |                                                                                                                                                                                                                                                                                 |
|      84176 | ````` recDocCases `````                                                                                                              |  0           | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |                                                                                                                                                                                                                                                                                 |
|      22188 | ````` ▁林肯近地小行星研究小 `````                                                                                                    |  0           | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁林肯近地小行星研究小組 `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁林肯近地小行星研究小组 `````</span>                                                                                      |
|     208149 | ````` AddLanguageSpecificText `````                                                                                                  |  0           | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` AddLanguageSpecificTextSet `````</span>                                                                                                                                                                                 |
|      15675 | ````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f ````` |  0.000192642 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> | ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f ````` |
|      71049 | ````` tocectory `````                                                                                                                |  0.000901222 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00014</span> |                                                                                                                                                                                                                                                                                 |
|     139462 | ````` 和人口皆未知 `````                                                                                                             |  0.00117636  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00014</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` 該地的面積和人口皆未知 `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` 该地的面积和人口皆未知 `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` 面积和人口皆未知 `````</span> |
|     208151 | ````` AddLanguageSpecificTextSet `````                                                                                               |  0.00149822  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00023</span> |                                                                                                                                                                                                                                                                                 |
|     224223 | ````` 面积和人口皆未知 `````                                                                                                         |  0.00159621  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00015</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` 该地的面积和人口皆未知 `````</span>                                                                                                                                                                                     |
|     145442 | ````` 》（）， `````                                                                                                                 |  0.00173283  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00013</span> |                                                                                                                                                                                                                                                                                 |
|     177875 | ````` tochassubtree `````                                                                                                            |  0.00259912  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00038</span> |                                                                                                                                                                                                                                                                                 |
|     141168 | ````` ephritidae `````                                                                                                               |  0.00267887  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00019</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Tephritidae `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` Tephritidae `````</span>                                                                                                             |
|      72754 | ````` ageryears `````                                                                                                                |  0.00279933  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00017</span> | ````` manageryears `````, ````` ▁manageryears `````                                                                                                                                                                                                                             |
|     177855 | ````` assubtree `````                                                                                                                |  0.00281382  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00039</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` tochassubtree `````</span>                                                                                                                                                                                              |
|     190228 | ````` ▁Hmelnî `````                                                                                                                  |  0.00304759  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00017</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁Hmelnîțkîi `````</span>                                                                                                                                                                                                |
|     141246 | ````` locatorSection `````                                                                                                           |  0.0049212   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00052</span> |                                                                                                                                                                                                                                                                                 |
|      94747 | ````` OnSearchSelect `````                                                                                                           |  0.0060094   | <span style='border: 1px solid rgb(169, 68, 66);'>0.00032</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` OnSearchSelectHide `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` OnSearchSelectShow `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` OnSearchSelectKey `````</span>        |
<details><summary>15 additional entries below threshold</summary>

|   token_id | token                                                |   indicator | max_prob                                                         | in_other_tokens                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------|------------------------------------------------------|-------------|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     190437 | ````` BiddersParams `````                            |  0.00673646 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00066</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁hbBiddersParams `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|       9741 | ````` \U000e0067\U000e0062\U000e0065\U000e006e ````` |  0.00779015 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00026</span> | ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` ▁🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span> |
|     149800 | ````` 年建立的教育 `````                             |  0.00792772 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00024</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` 年建立的教育机构 `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` 年建立的教育機構 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|      37757 | ````` （，）， `````                                 |  0.0173035  | <span style='border: 1px solid rgb(169, 68, 66);'>0.0005</span>  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|      51385 | ````` ▁ARStd `````                                   |  0.0184463  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0031</span>  | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁ARStdSong `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     100190 | ````` Desambigua `````                               |  0.0225713  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0023</span>  | <span style='border: 1px solid rgb(40, 167, 69);'>````` Desambiguações `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` Desambiguação `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|     223425 | ````` 而人口密度為 `````                             |  0.0249265  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00054</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` 而人口密度為每平方千米 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     127290 | ````` srguid `````                                   |  0.0263301  | <span style='border: 1px solid rgb(251, 189, 8);'>0.014</span>   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     223844 | ````` 該地的面積 `````                               |  0.0364665  | <span style='border: 1px solid rgb(169, 68, 66);'>0.00071</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` 該地的面積和人口皆未知 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|     119253 | ````` écosl `````                                    |  0.0443186  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0016</span>  | <span style='border: 1px solid rgb(40, 167, 69);'>````` écoslovaquie `````</span>, ````` ▁tchécoslova `````, ````` ▁Tchécoslovaquie `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` écoslova `````</span>                                                                                                                                                                                                                                                                                                                                                                                          |
|     144020 | ````` оспоживача `````                               |  0.0455816  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0068</span>  | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁особоспоживача `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|     172752 | ````` ablytyped `````                                |  0.0457996  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0053</span>  | <span style='border: 1px solid rgb(40, 167, 69);'>````` scalablytyped `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|     202267 | ````` \U000e0074\U000e007f `````                     |  0.0474659  | <span style='border: 1px solid rgb(251, 189, 8);'>0.02</span>    | ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````, ````` <0xB3>\U000e0063\U000e0074\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|      71714 | ````` 所属的省级 `````                               |  0.0495927  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0074</span>  | <span style='border: 1px solid rgb(40, 167, 69);'>````` 所属的省级选区为 `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|      63146 | ````` 》（） `````                                   |  0.0497289  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0091</span>  | <span style='border: 1px solid rgb(169, 68, 66);'>````` 》（）， `````</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
</details>


## Partial UTF-8 tokens
9 entries below threshold of 0.051

|   token_id | token                                                 |    indicator | in_other_tokens                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------|-------------------------------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      97361 | ````` <0x95>시코 `````                                | -1.19209e-07 | ````` 멕시코 `````, ````` ▁멕시코 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|      70552 | ````` <0xB9><0x80><0xE0><0xB8> `````                  | -1.19209e-07 | ````` เ<0xE0><0xB8> `````, ````` ▁เ<0xE0><0xB8> `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|      57888 | ````` <0x89>글랜드 `````                              | -1.19209e-07 | ````` ▁잉글랜드 `````, ````` 잉글랜드 `````, ````` 잉글랜드의 `````, ````` ▁잉글랜드의 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|     113772 | ````` <0x98>리포니아 `````                            | -1.19209e-07 | ````` ▁캘리포니아 `````, ````` 캘리포니아 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|     202233 | ````` <0xB3>\U000e0063 `````                          |  0.00041014  | ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````, ````` <0xB3>\U000e0063\U000e0074\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|      62442 | ````` ▁🏴\U000e0067\U000e0062<0xF3><0xA0><0x81> ````` |  0.00253528  | ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|      69097 | ````` <0xB7>\U000e006c `````                          |  0.00378895  | ````` <0xB7>\U000e006c\U000e0073\U000e007f `````, ````` ▁🏴\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|       6132 | ````` <0xA7><0xF3><0xA0><0x81> `````                  |  0.0116265   | ````` ▁🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f `````, ````` 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, ````` \U000e0067<0xF3><0xA0><0x81> `````, <span style='border: 1px solid rgb(169, 68, 66);'>````` \U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````</span>, ````` ▁🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f `````, ... |
|      19460 | ````` ▁🇯<0xF0><0x9F><0x87> `````                      |  0.0177507   | ````` ▁🇯🇵 `````, ````` ▁🇯🇴 `````, ````` ▁🇯🇲 `````                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |


## Byte tokens
13 entries below threshold of 0.017

|   token_id | token              |    indicator |   ord | hex   | byte_type   |
|------------|--------------------|--------------|-------|-------|-------------|
|        189 | ````` <0xF9> ````` | -1.19209e-07 |   249 | 0xF9  | unused_utf8 |
|        195 | ````` <0xFF> ````` | -1.19209e-07 |   255 | 0xFF  | unused_utf8 |
|        132 | ````` <0xC0> ````` | -1.19209e-07 |   192 | 0xC0  | unused_utf8 |
|        188 | ````` <0xF8> ````` | -1.19209e-07 |   248 | 0xF8  | unused_utf8 |
|        133 | ````` <0xC1> ````` | -1.19209e-07 |   193 | 0xC1  | unused_utf8 |
|        194 | ````` <0xFE> ````` | -1.19209e-07 |   254 | 0xFE  | unused_utf8 |
|        187 | ````` <0xF7> ````` | -1.19209e-07 |   247 | 0xF7  | unused_utf8 |
|        190 | ````` <0xFA> ````` | -1.19209e-07 |   250 | 0xFA  | unused_utf8 |
|        193 | ````` <0xFD> ````` | -1.19209e-07 |   253 | 0xFD  | unused_utf8 |
|        186 | ````` <0xF6> ````` | -1.19209e-07 |   246 | 0xF6  | unused_utf8 |
|        191 | ````` <0xFB> ````` |  0           |   251 | 0xFB  | unused_utf8 |
|        192 | ````` <0xFC> ````` |  0           |   252 | 0xFC  | unused_utf8 |
|        185 | ````` <0xF5> ````` |  0           |   245 | 0xF5  | unused_utf8 |


## Special tokens
26 entries below threshold of 0.017

|   token_id | token                           |    indicator | max_prob                                                         |
|------------|---------------------------------|--------------|------------------------------------------------------------------|
|     255015 | ````` <\|USER_6_TOKEN\|> `````  | -2.38419e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255012 | ````` <\|USER_3_TOKEN\|> `````  | -2.38419e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255002 | ````` <\|YES_TOKEN\|> `````     | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255009 | ````` <\|USER_0_TOKEN\|> `````  | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255019 | ````` <\|EXTRA_0_TOKEN\|> ````` | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255011 | ````` <\|USER_2_TOKEN\|> `````  | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255023 | ````` <\|EXTRA_4_TOKEN\|> ````` | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255004 | ````` <\|GOOD_TOKEN\|> `````    | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255003 | ````` <\|NO_TOKEN\|> `````      | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255016 | ````` <\|USER_7_TOKEN\|> `````  | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255013 | ````` <\|USER_4_TOKEN\|> `````  | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255005 | ````` <\|BAD_TOKEN\|> `````     | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255021 | ````` <\|EXTRA_2_TOKEN\|> ````` | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255028 | ````` <\|EXTRA_9_TOKEN\|> ````` | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|          4 | ````` <MASK_TOKEN> `````        | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255020 | ````` <\|EXTRA_1_TOKEN\|> ````` | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255010 | ````` <\|USER_1_TOKEN\|> `````  | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255027 | ````` <\|EXTRA_8_TOKEN\|> ````` | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255022 | ````` <\|EXTRA_3_TOKEN\|> ````` | -1.19209e-07 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255025 | ````` <\|EXTRA_6_TOKEN\|> ````` |  0           | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
<details><summary>6 additional entries below threshold</summary>

|   token_id | token                           |   indicator | max_prob                                                         |
|------------|---------------------------------|-------------|------------------------------------------------------------------|
|     255018 | ````` <\|USER_9_TOKEN\|> `````  | 0           | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255026 | ````` <\|EXTRA_7_TOKEN\|> ````` | 0           | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255014 | ````` <\|USER_5_TOKEN\|> `````  | 0           | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255017 | ````` <\|USER_8_TOKEN\|> `````  | 0           | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|     255024 | ````` <\|EXTRA_5_TOKEN\|> ````` | 0           | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
|          7 | ````` <EOP_TOKEN> `````         | 2.86698e-05 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00012</span> |
</details>


## Unreachable tokens
1403 entries below threshold of 0.017

|   token_id | token            |    indicator | reencoded                                                                        |
|------------|------------------|--------------|----------------------------------------------------------------------------------|
|        612 | ````` ¿🍹? ````` | -3.57628e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 125: ````` <0xB9> ````` |
|        607 | ````` ¿🍴? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 120: ````` <0xB4> ````` |
|        584 | ````` ¿🍝? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 259: ````` <0x9D> ````` |
|       1086 | ````` ¿🕯? `````  | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 115: ````` <0xAF> ````` |
|        528 | ````` ¿🌥? `````  | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 106: ````` <0xA5> ````` |
|        620 | ````` ¿🎁? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 231: ````` <0x81> ````` |
|       1444 | ````` ¿🦃? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 233: ````` <0x83> ````` |
|       1489 | ````` ¿🦰? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 116: ````` <0xB0> ````` |
|        688 | ````` ¿🏊? ````` | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 240: ````` <0x8A> `````                  |
|       1115 | ````` ¿🗓? `````  | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 249: ````` <0x93> ````` |
|       1102 | ````` ¿🖕? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 251: ````` <0x95> ````` |
|        697 | ````` ¿🏓? ````` | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 249: ````` <0x93> `````                  |
|       1081 | ````` ¿🕣? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 104: ````` <0xA3> ````` |
|       1074 | ````` ¿🕜? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 258: ````` <0x9C> ````` |
|       1099 | ````` ¿🖌? `````  | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 242: ````` <0x8C> ````` |
|       1569 | ````` ¿🩰? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 116: ````` <0xB0> ````` |
|        604 | ````` ¿🍱? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 117: ````` <0xB1> ````` |
|        600 | ````` ¿🍭? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 263: ````` <0xAD> ````` |
|        683 | ````` ¿🏅? ````` | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 235: ````` <0x85> `````                  |
|       1415 | ````` ¿🥦? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 107: ````` <0xA6> ````` |
<details><summary>1383 additional entries below threshold</summary>

|   token_id | token                    |    indicator | reencoded                                                                        |
|------------|--------------------------|--------------|----------------------------------------------------------------------------------|
|       1069 | ````` ¿🕗? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 253: ````` <0x97> ````` |
|       1536 | ````` ¿🧟? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 261: ````` <0x9F> ````` |
|       1098 | ````` ¿🖋? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 241: ````` <0x8B> ````` |
|       1655 | ````` ¿\U0001faf5? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 121: ````` <0xB5> ````` |
|        551 | ````` ¿🌼? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 128: ````` <0xBC> ````` |
|       1105 | ````` ¿🖥? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 106: ````` <0xA5> ````` |
|       1050 | ````` ¿🔸? `````         | -2.38419e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 124: ````` <0xB8> `````                  |
|       1130 | ````` ¿😀? `````         | -2.38419e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 230: ````` <0x80> `````                  |
|        648 | ````` ¿🎢? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 103: ````` <0xA2> ````` |
|        665 | ````` ¿🎳? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 119: ````` <0xB3> ````` |
|       1228 | ````` ¿🚒? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 248: ````` <0x92> ````` |
|       1058 | ````` ¿🕋? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 241: ````` <0x8B> ````` |
|        562 | ````` ¿🍇? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 237: ````` <0x87> ````` |
|       1234 | ````` ¿🚘? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 254: ````` <0x98> ````` |
|        565 | ````` ¿🍊? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 240: ````` <0x8A> ````` |
|        581 | ````` ¿🍚? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 256: ````` <0x9A> ````` |
|       1097 | ````` ¿🖊? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 240: ````` <0x8A> ````` |
|        678 | ````` ¿🏀? `````         | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 230: ````` <0x80> `````                  |
|        684 | ````` ¿🏆? `````         | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 236: ````` <0x86> `````                  |
|       1038 | ````` ¿🔬? `````         | -2.38419e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 113: ````` <0xAC> `````                  |
|        605 | ````` ¿🍲? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 118: ````` <0xB2> ````` |
|        597 | ````` ¿🍪? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 111: ````` <0xAA> ````` |
|       1606 | ````` ¿🪤? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 105: ````` <0xA4> ````` |
|       1198 | ````` ¿🙄? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 234: ````` <0x84> ````` |
|       1204 | ````` ¿🙊? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 240: ````` <0x8A> ````` |
|       1568 | ````` ¿🧿? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 131: ````` <0xBF> ````` |
|        657 | ````` ¿🎫? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 112: ````` <0xAB> ````` |
|        569 | ````` ¿🍎? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 244: ````` <0x8E> ````` |
|        663 | ````` ¿🎱? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 117: ````` <0xB1> ````` |
|        670 | ````` ¿🎸? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 124: ````` <0xB8> ````` |
|       1230 | ````` ¿🚔? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 250: ````` <0x94> ````` |
|       1108 | ````` ¿🖲? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 118: ````` <0xB2> ````` |
|       1076 | ````` ¿🕞? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 260: ````` <0x9E> ````` |
|       1079 | ````` ¿🕡? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 102: ````` <0xA1> ````` |
|       1066 | ````` ¿🕔? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 250: ````` <0x94> ````` |
|       1143 | ````` ¿😍? `````         | -2.38419e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 243: ````` <0x8D> `````                  |
|        445 | ````` ¿🆔? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 250: ````` <0x94> ````` |
|       1641 | ````` ¿\U0001fad9? ````` | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 255: ````` <0x99> ````` |
|        502 | ````` ¿🌉? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 239: ````` <0x89> ````` |
|       1235 | ````` ¿🚙? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 255: ````` <0x99> ````` |
|       1100 | ````` ¿🖍? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 243: ````` <0x8D> ````` |
|        692 | ````` ¿🏎? `````          | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 244: ````` <0x8E> `````                  |
|        655 | ````` ¿🎩? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 110: ````` <0xA9> ````` |
|       1455 | ````` ¿🦎? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 244: ````` <0x8E> ````` |
|       1460 | ````` ¿🦓? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 249: ````` <0x93> ````` |
|        571 | ````` ¿🍐? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 246: ````` <0x90> ````` |
|        536 | ````` ¿🌭? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 263: ````` <0xAD> ````` |
|       1583 | ````` ¿🪄? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 234: ````` <0x84> ````` |
|        702 | ````` ¿🏘? `````          | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 254: ````` <0x98> `````                  |
|        533 | ````` ¿🌪? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 111: ````` <0xAA> ````` |
|        676 | ````` ¿🎾? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 130: ````` <0xBE> ````` |
|        598 | ````` ¿🍫? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 112: ````` <0xAB> ````` |
|       1072 | ````` ¿🕚? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 256: ````` <0x9A> ````` |
|        906 | ````` ¿💧? `````         | -2.38419e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 108: ````` <0xA7> `````                  |
|        852 | ````` ¿👱? `````         | -2.38419e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 117: ````` <0xB1> `````                  |
|        602 | ````` ¿🍯? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 115: ````` <0xAF> ````` |
|       1134 | ````` ¿😄? `````         | -2.38419e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 234: ````` <0x84> `````                  |
|        544 | ````` ¿🌵? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 121: ````` <0xB5> ````` |
|       1564 | ````` ¿🧻? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 127: ````` <0xBB> ````` |
|        693 | ````` ¿🏏? `````         | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 245: ````` <0x8F> `````                  |
|       1104 | ````` ¿🖤? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 105: ````` <0xA4> ````` |
|        711 | ````` ¿🏡? `````         | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 102: ````` <0xA1> `````                  |
|       1438 | ````` ¿🥽? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 129: ````` <0xBD> ````` |
|       1140 | ````` ¿😊? `````         | -2.38419e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 240: ````` <0x8A> `````                  |
|       1064 | ````` ¿🕒? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 248: ````` <0x92> ````` |
|        646 | ````` ¿🎠? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 262: ````` <0xA0> ````` |
|        695 | ````` ¿🏑? `````         | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 247: ````` <0x91> `````                  |
|       1131 | ````` ¿😁? `````         | -2.38419e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 231: ````` <0x81> `````                  |
|        556 | ````` ¿🍁? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 231: ````` <0x81> ````` |
|       1048 | ````` ¿🔶? `````         | -2.38419e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 122: ````` <0xB6> `````                  |
|        534 | ````` ¿🌫? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 112: ````` <0xAB> ````` |
|        504 | ````` ¿🌋? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 241: ````` <0x8B> ````` |
|       1562 | ````` ¿🧹? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 125: ````` <0xB9> ````` |
|       1073 | ````` ¿🕛? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 257: ````` <0x9B> ````` |
|       1113 | ````` ¿🗑? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 247: ````` <0x91> ````` |
|       1087 | ````` ¿🕰? `````          | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 116: ````` <0xB0> ````` |
|        627 | ````` ¿🎈? `````         | -2.38419e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 238: ````` <0x88> ````` |
|        700 | ````` ¿🏖? `````          | -2.38419e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 252: ````` <0x96> `````                  |
|       1158 | ````` ¿😜? `````         | -2.38419e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 258: ````` <0x9C> `````                  |
|        298 | ````` ¿▫? `````          | -1.19209e-07 | 29034: ````` <0xE2><0x96> `````, 112: ````` <0xAB> `````                         |
|       1372 | ````` ¿🤹? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 125: ````` <0xB9> ````` |
|       1481 | ````` ¿🦨? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 109: ````` <0xA8> ````` |
|        634 | ````` ¿🎏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 245: ````` <0x8F> ````` |
|        371 | ````` ¿⛏? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 245: ````` <0x8F> `````        |
|        713 | ````` ¿🏣? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 104: ````` <0xA3> `````                  |
|        494 | ````` ¿🌁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 231: ````` <0x81> ````` |
|        823 | ````` ¿👔? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 250: ````` <0x94> `````                  |
|        962 | ````` ¿📟? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 261: ````` <0x9F> `````                  |
|        719 | ````` ¿🏩? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 110: ````` <0xA9> `````                  |
|       1241 | ````` ¿🚟? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 261: ````` <0x9F> ````` |
|       1236 | ````` ¿🚚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 256: ````` <0x9A> ````` |
|       1203 | ````` ¿🙉? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 239: ````` <0x89> ````` |
|        967 | ````` ¿📤? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 105: ````` <0xA4> `````                  |
|        691 | ````` ¿🏍? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 243: ````` <0x8D> `````                  |
|       1207 | ````` ¿🙍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 243: ````` <0x8D> ````` |
|       1175 | ````` ¿😭? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 263: ````` <0xAD> `````                  |
|        498 | ````` ¿🌅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 235: ````` <0x85> ````` |
|       1112 | ````` ¿🗄? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 234: ````` <0x84> ````` |
|        642 | ````` ¿🎚? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 256: ````` <0x9A> ````` |
|       1020 | ````` ¿🔚? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 256: ````` <0x9A> `````                  |
|       1218 | ````` ¿🚈? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 238: ````` <0x88> ````` |
|        441 | ````` ¿🆎? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 244: ````` <0x8E> ````` |
|        380 | ````` ¿⛳? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 119: ````` <0xB3> `````        |
|        406 | ````` ¿❇? `````          | -1.19209e-07 | 135523: ````` <0xE2><0x9D> `````, 237: ````` <0x87> `````                        |
|       1013 | ````` ¿🔓? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 249: ````` <0x93> `````                  |
|       1521 | ````` ¿🧐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 246: ````` <0x90> ````` |
|       1469 | ````` ¿🦜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 258: ````` <0x9C> ````` |
|       1088 | ````` ¿🕳? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 119: ````` <0xB3> ````` |
|        934 | ````` ¿📃? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 233: ````` <0x83> `````                  |
|        366 | ````` ¿⚾? `````         | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 130: ````` <0xBE> `````                        |
|        894 | ````` ¿💛? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 257: ````` <0x9B> `````                  |
|       1445 | ````` ¿🦄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 234: ````` <0x84> ````` |
|       1245 | ````` ¿🚣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 104: ````` <0xA3> ````` |
|        947 | ````` ¿📐? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 246: ````` <0x90> `````                  |
|        877 | ````` ¿💊? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 240: ````` <0x8A> `````                  |
|        701 | ````` ¿🏗? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 253: ````` <0x97> `````                  |
|        342 | ````` ¿♣? `````          | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 104: ````` <0xA3> `````                         |
|       1332 | ````` ¿🤑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 6605: ````` <0xA4><0x91> `````                   |
|       1223 | ````` ¿🚍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 243: ````` <0x8D> ````` |
|       1534 | ````` ¿🧝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 259: ````` <0x9D> ````` |
|       1078 | ````` ¿🕠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 262: ````` <0xA0> ````` |
|        842 | ````` ¿👧? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 108: ````` <0xA7> `````                  |
|        640 | ````` ¿🎗? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 253: ````` <0x97> ````` |
|       1593 | ````` ¿🪗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 253: ````` <0x97> ````` |
|        867 | ````` ¿💀? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 230: ````` <0x80> `````                  |
|        714 | ````` ¿🏤? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 105: ````` <0xA4> `````                  |
|       1391 | ````` ¿🥎? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 244: ````` <0x8E> ````` |
|        566 | ````` ¿🍋? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 241: ````` <0x8B> ````` |
|        922 | ````` ¿💷? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 123: ````` <0xB7> `````                  |
|        935 | ````` ¿📄? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 234: ````` <0x84> `````                  |
|        548 | ````` ¿🌹? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 125: ````` <0xB9> ````` |
|       1580 | ````` ¿🪁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 231: ````` <0x81> ````` |
|       1239 | ````` ¿🚝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 259: ````` <0x9D> ````` |
|       1248 | ````` ¿🚦? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 107: ````` <0xA6> ````` |
|       1021 | ````` ¿🔛? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 257: ````` <0x9B> `````                  |
|        456 | ````` ¿🇪? `````          | -1.19209e-07 | 8548: ````` 🇪 `````                                                              |
|        358 | ````` ¿⚠? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 262: ````` <0xA0> `````                        |
|       1315 | ````` ¿🟡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 102: ````` <0xA1> ````` |
|       1139 | ````` ¿😉? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 239: ````` <0x89> `````                  |
|        671 | ````` ¿🎹? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 125: ````` <0xB9> ````` |
|        781 | ````` ¿🐪? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 111: ````` <0xAA> ````` |
|        944 | ````` ¿📍? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 243: ````` <0x8D> `````                  |
|       1368 | ````` ¿🤵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 121: ````` <0xB5> ````` |
|       1297 | ````` ¿🛣? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 104: ````` <0xA3> ````` |
|        878 | ````` ¿💋? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 241: ````` <0x8B> `````                  |
|        485 | ````` ¿🈵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 121: ````` <0xB5> ````` |
|        425 | ````` ¿⬇? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 113: ````` <0xAC> `````, 237: ````` <0x87> `````        |
|       1045 | ````` ¿🔳? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 119: ````` <0xB3> `````                  |
|        856 | ````` ¿👵? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 121: ````` <0xB5> `````                  |
|       1486 | ````` ¿🦭? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 263: ````` <0xAD> ````` |
|        909 | ````` ¿💪? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 111: ````` <0xAA> `````                  |
|        965 | ````` ¿📢? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 103: ````` <0xA2> `````                  |
|        950 | ````` ¿📓? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 249: ````` <0x93> `````                  |
|        428 | ````` ¿⭐? `````         | -1.19209e-07 | 137546: ````` ⭐ `````                                                           |
|        784 | ````` ¿🐭? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 263: ````` <0xAD> ````` |
|       1437 | ````` ¿🥼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 128: ````` <0xBC> ````` |
|       1053 | ````` ¿🔻? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 127: ````` <0xBB> `````                  |
|       1163 | ````` ¿😡? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 102: ````` <0xA1> `````                  |
|        529 | ````` ¿🌦? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 107: ````` <0xA6> ````` |
|       1329 | ````` ¿🤎? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 244: ````` <0x8E> ````` |
|        440 | ````` ¿🅿? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 235: ````` <0x85> `````, 131: ````` <0xBF> ````` |
|       1288 | ````` ¿🛕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 251: ````` <0x95> ````` |
|       1244 | ````` ¿🚢? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 103: ````` <0xA2> ````` |
|        540 | ````` ¿🌱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 117: ````` <0xB1> ````` |
|        690 | ````` ¿🏌? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 242: ````` <0x8C> `````                  |
|       1141 | ````` ¿😋? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 241: ````` <0x8B> `````                  |
|        327 | ````` ¿♂? `````          | -1.19209e-07 | 232883: ````` ♂ `````                                                            |
|        889 | ````` ¿💖? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 252: ````` <0x96> `````                  |
|       1552 | ````` ¿🧯? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 115: ````` <0xAF> ````` |
|        902 | ````` ¿💣? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 104: ````` <0xA3> `````                  |
|        827 | ````` ¿👘? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 254: ````` <0x98> `````                  |
|       1392 | ````` ¿🥏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 245: ````` <0x8F> ````` |
|       1303 | ````` ¿🛰? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 71996: ````` <0x9B><0xB0> `````                  |
|        338 | ````` ¿♒? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 248: ````` <0x92> `````                         |
|       1121 | ````` ¿🗨? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 109: ````` <0xA8> ````` |
|        707 | ````` ¿🏝? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 259: ````` <0x9D> `````                  |
|       1061 | ````` ¿🕎? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 244: ````` <0x8E> ````` |
|       1643 | ````` ¿\U0001fae1? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 102: ````` <0xA1> ````` |
|        978 | ````` ¿📯? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 115: ````` <0xAF> `````                  |
|        594 | ````` ¿🍧? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 108: ````` <0xA7> ````` |
|        512 | ````` ¿🌓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 249: ````` <0x93> ````` |
|        785 | ````` ¿🐮? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 114: ````` <0xAE> ````` |
|       1462 | ````` ¿🦕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 251: ````` <0x95> ````` |
|        493 | ````` ¿🌀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 3388: ````` <0x8C><0x80> `````                   |
|        929 | ````` ¿💾? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 130: ````` <0xBE> `````                  |
|       1119 | ````` ¿🗡? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 102: ````` <0xA1> ````` |
|        473 | ````` ¿🇻? `````          | -1.19209e-07 | 99202: ````` 🇻 `````                                                             |
|        681 | ````` ¿🏃? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 233: ````` <0x83> `````                  |
|       1144 | ````` ¿😎? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 244: ````` <0x8E> `````                  |
|       1461 | ````` ¿🦔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 250: ````` <0x94> ````` |
|        309 | ````` ¿☄? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 234: ````` <0x84> `````                         |
|       1292 | ````` ¿\U0001f6de? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 260: ````` <0x9E> ````` |
|        530 | ````` ¿🌧? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 108: ````` <0xA7> ````` |
|        431 | ````` ¿〽? `````         | -1.19209e-07 | 1800: ````` <0xE3><0x80> `````, 129: ````` <0xBD> `````                          |
|        946 | ````` ¿📏? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 245: ````` <0x8F> `````                  |
|       1261 | ````` ¿🚳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 119: ````` <0xB3> ````` |
|        403 | ````` ¿✳? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 119: ````` <0xB3> `````                         |
|        838 | ````` ¿👣? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 104: ````` <0xA3> `````                  |
|       1114 | ````` ¿🗒? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 248: ````` <0x92> ````` |
|        668 | ````` ¿🎶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 122: ````` <0xB6> ````` |
|        805 | ````` ¿👂? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 232: ````` <0x82> `````                  |
|       1588 | ````` ¿🪒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 248: ````` <0x92> ````` |
|        945 | ````` ¿📎? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 244: ````` <0x8E> `````                  |
|       1366 | ````` ¿🤳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 119: ````` <0xB3> ````` |
|       1238 | ````` ¿🚜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 258: ````` <0x9C> ````` |
|       1560 | ````` ¿🧷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 123: ````` <0xB7> ````` |
|        410 | ````` ¿❔? `````         | -1.19209e-07 | 135523: ````` <0xE2><0x9D> `````, 250: ````` <0x94> `````                        |
|        791 | ````` ¿🐴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 120: ````` <0xB4> ````` |
|       1289 | ````` ¿🛖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 252: ````` <0x96> ````` |
|        486 | ````` ¿🈶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 122: ````` <0xB6> ````` |
|       1028 | ````` ¿🔢? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 103: ````` <0xA2> `````                  |
|       1363 | ````` ¿🤰? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 116: ````` <0xB0> ````` |
|        900 | ````` ¿💡? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 102: ````` <0xA1> `````                  |
|        419 | ````` ¿➰? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 116: ````` <0xB0> `````        |
|       1491 | ````` ¿🦲? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 118: ````` <0xB2> ````` |
|       1127 | ````` ¿🗽? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 129: ````` <0xBD> ````` |
|       1060 | ````` ¿🕍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 243: ````` <0x8D> ````` |
|       1265 | ````` ¿🚷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 123: ````` <0xB7> ````` |
|        817 | ````` ¿👎? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 244: ````` <0x8E> `````                  |
|       1503 | ````` ¿🦾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 130: ````` <0xBE> ````` |
|        908 | ````` ¿💩? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 110: ````` <0xA9> `````                  |
|        518 | ````` ¿🌙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 255: ````` <0x99> ````` |
|       1386 | ````` ¿🥉? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 239: ````` <0x89> ````` |
|        669 | ````` ¿🎷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 123: ````` <0xB7> ````` |
|       1526 | ````` ¿🧕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 251: ````` <0x95> ````` |
|        830 | ````` ¿👛? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 257: ````` <0x9B> `````                  |
|       1524 | ````` ¿🧓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 249: ````` <0x93> ````` |
|       1360 | ````` ¿🤭? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 263: ````` <0xAD> ````` |
|       1540 | ````` ¿🧣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 104: ````` <0xA3> ````` |
|       1327 | ````` ¿🤌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 242: ````` <0x8C> ````` |
|        448 | ````` ¿🆗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 253: ````` <0x97> ````` |
|       1468 | ````` ¿🦛? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 257: ````` <0x9B> ````` |
|        395 | ````` ¿✍? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 243: ````` <0x8D> `````                         |
|       1546 | ````` ¿🧩? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 110: ````` <0xA9> ````` |
|        637 | ````` ¿🎒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 248: ````` <0x92> ````` |
|       1192 | ````` ¿😾? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 130: ````` <0xBE> `````                  |
|        837 | ````` ¿👢? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 103: ````` <0xA2> `````                  |
|       1120 | ````` ¿🗣? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 104: ````` <0xA3> ````` |
|       1549 | ````` ¿🧬? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 113: ````` <0xAC> ````` |
|        618 | ````` ¿🍿? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 131: ````` <0xBF> ````` |
|        334 | ````` ¿♎? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 244: ````` <0x8E> `````                         |
|       1423 | ````` ¿🥮? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 114: ````` <0xAE> ````` |
|       1414 | ````` ¿🥥? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 106: ````` <0xA5> ````` |
|        402 | ````` ¿✨? `````         | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 109: ````` <0xA8> `````                         |
|       1567 | ````` ¿🧾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 130: ````` <0xBE> ````` |
|       1153 | ````` ¿😗? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 253: ````` <0x97> `````                  |
|       1002 | ````` ¿🔈? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 238: ````` <0x88> `````                  |
|        647 | ````` ¿🎡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 102: ````` <0xA1> ````` |
|        396 | ````` ¿✏? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 245: ````` <0x8F> `````                         |
|        443 | ````` ¿🆒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 9519: ````` <0x86><0x92> `````                   |
|        632 | ````` ¿🎍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 243: ````` <0x8D> ````` |
|        844 | ````` ¿👩? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 110: ````` <0xA9> `````                  |
|        613 | ````` ¿🍺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 126: ````` <0xBA> ````` |
|       1135 | ````` ¿😅? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 235: ````` <0x85> `````                  |
|        351 | ````` ¿⚔? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 250: ````` <0x94> `````                        |
|       1173 | ````` ¿😫? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 112: ````` <0xAB> `````                  |
|        674 | ````` ¿🎼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 128: ````` <0xBC> ````` |
|       1335 | ````` ¿🤔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 250: ````` <0x94> ````` |
|        373 | ````` ¿⛓? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 249: ````` <0x93> `````        |
|        981 | ````` ¿📲? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 118: ````` <0xB2> `````                  |
|       1348 | ````` ¿🤡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 102: ````` <0xA1> ````` |
|        623 | ````` ¿🎄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 234: ````` <0x84> ````` |
|       1369 | ````` ¿🤶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 122: ````` <0xB6> ````` |
|       1501 | ````` ¿🦼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 128: ````` <0xBC> ````` |
|       1116 | ````` ¿🗜? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 258: ````` <0x9C> ````` |
|        348 | ````` ¿♿? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 131: ````` <0xBF> `````                         |
|        315 | ````` ¿☝? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 259: ````` <0x9D> `````                         |
|       1539 | ````` ¿🧢? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 103: ````` <0xA2> ````` |
|       1659 | ````` ¿\U000e0065? ````` | -1.19209e-07 | 3330: ````` <0xF3><0xA0><0x81> `````, 106: ````` <0xA5> `````                    |
|       1044 | ````` ¿🔲? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 118: ````` <0xB2> `````                  |
|        369 | ````` ¿⛈? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 32197: ````` <0x9B><0x88> `````                         |
|       1117 | ````` ¿🗝? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 259: ````` <0x9D> ````` |
|        362 | ````` ¿⚫? `````         | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 112: ````` <0xAB> `````                        |
|        905 | ````` ¿💦? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 107: ````` <0xA6> `````                  |
|       1613 | ````` ¿\U0001faab? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 112: ````` <0xAB> ````` |
|        611 | ````` ¿🍸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 124: ````` <0xB8> ````` |
|       1663 | ````` ¿\U000e0073? ````` | -1.19209e-07 | 69089: ````` \U000e0073 `````                                                    |
|        282 | ````` ¿⏩? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 110: ````` <0xA9> `````        |
|        272 | ````` ¿↖? `````          | -1.19209e-07 | 76876: ````` <0xE2><0x86> `````, 252: ````` <0x96> `````                         |
|       1216 | ````` ¿🚆? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 236: ````` <0x86> ````` |
|       1200 | ````` ¿🙆? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 236: ````` <0x86> ````` |
|       1551 | ````` ¿🧮? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 114: ````` <0xAE> ````` |
|       1012 | ````` ¿🔒? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 248: ````` <0x92> `````                  |
|        470 | ````` ¿🇸? `````          | -1.19209e-07 | 6705: ````` 🇸 `````                                                              |
|       1508 | ````` ¿🧃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 233: ````` <0x83> ````` |
|        488 | ````` ¿🈸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 124: ````` <0xB8> ````` |
|        330 | ````` ¿♊? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 240: ````` <0x8A> `````                         |
|       1664 | ````` ¿\U000e0074? ````` | -1.19209e-07 | 202195: ````` \U000e0074 `````                                                   |
|       1160 | ````` ¿😞? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 260: ````` <0x9E> `````                  |
|       1657 | ````` ¿\U000e0062? ````` | -1.19209e-07 | 3330: ````` <0xF3><0xA0><0x81> `````, 103: ````` <0xA2> `````                    |
|       1126 | ````` ¿🗼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 128: ````` <0xBC> ````` |
|       1256 | ````` ¿🚮? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 114: ````` <0xAE> ````` |
|        703 | ````` ¿🏙? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 255: ````` <0x99> `````                  |
|       1166 | ````` ¿😤? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 105: ````` <0xA4> `````                  |
|       1035 | ````` ¿🔩? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 110: ````` <0xA9> `````                  |
|        656 | ````` ¿🎪? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 111: ````` <0xAA> ````` |
|       1106 | ````` ¿🖨? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 109: ````` <0xA8> ````` |
|        725 | ````` ¿🏯? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 115: ````` <0xAF> `````                  |
|        299 | ````` ¿▶? `````          | -1.19209e-07 | 29034: ````` <0xE2><0x96> `````, 122: ````` <0xB6> `````                         |
|       1436 | ````` ¿🥻? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 127: ````` <0xBB> ````` |
|        818 | ````` ¿👏? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 245: ````` <0x8F> `````                  |
|       1213 | ````` ¿🚃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 233: ````` <0x83> ````` |
|        289 | ````` ¿⏰? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 116: ````` <0xB0> `````        |
|        447 | ````` ¿🆖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 252: ````` <0x96> ````` |
|        434 | ````` ¿️? `````           | -1.19209e-07 | 57462: ````` ️ `````                                                              |
|       1056 | ````` ¿🕉? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 239: ````` <0x89> ````` |
|       1591 | ````` ¿🪕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 251: ````` <0x95> ````` |
|        596 | ````` ¿🍩? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 110: ````` <0xA9> ````` |
|       1556 | ````` ¿🧳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 119: ````` <0xB3> ````` |
|        937 | ````` ¿📆? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 236: ````` <0x86> `````                  |
|        932 | ````` ¿📁? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 231: ````` <0x81> `````                  |
|        780 | ````` ¿🐩? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 110: ````` <0xA9> ````` |
|       1091 | ````` ¿🕶? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 122: ````` <0xB6> ````` |
|        868 | ````` ¿💁? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 231: ````` <0x81> `````                  |
|        383 | ````` ¿⛷? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 123: ````` <0xB7> `````        |
|       1502 | ````` ¿🦽? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 129: ````` <0xBD> ````` |
|       1566 | ````` ¿🧽? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 129: ````` <0xBD> ````` |
|       1284 | ````` ¿🛏? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 245: ````` <0x8F> ````` |
|        631 | ````` ¿🎌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 242: ````` <0x8C> ````` |
|        320 | ````` ¿☪? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 111: ````` <0xAA> `````                         |
|        915 | ````` ¿💰? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 116: ````` <0xB0> `````                  |
|        510 | ````` ¿🌑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 247: ````` <0x91> ````` |
|       1019 | ````` ¿🔙? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 255: ````` <0x99> `````                  |
|       1420 | ````` ¿🥫? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 112: ````` <0xAB> ````` |
|        558 | ````` ¿🍃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 233: ````` <0x83> ````` |
|        591 | ````` ¿🍤? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 105: ````` <0xA4> ````` |
|       1063 | ````` ¿🕑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 247: ````` <0x91> ````` |
|       1530 | ````` ¿🧙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 255: ````` <0x99> ````` |
|        778 | ````` ¿🐧? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 108: ````` <0xA7> ````` |
|        586 | ````` ¿🍟? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 261: ````` <0x9F> ````` |
|       1030 | ````` ¿🔤? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 105: ````` <0xA4> `````                  |
|       1522 | ````` ¿🧑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 247: ````` <0x91> ````` |
|       1037 | ````` ¿🔫? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 112: ````` <0xAB> `````                  |
|       1007 | ````` ¿🔍? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 243: ````` <0x8D> `````                  |
|       1605 | ````` ¿🪣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 104: ````` <0xA3> ````` |
|        367 | ````` ¿⛄? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 7840: ````` <0x9B><0x84> `````                          |
|       1071 | ````` ¿🕙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 255: ````` <0x99> ````` |
|       1454 | ````` ¿🦍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 243: ````` <0x8D> ````` |
|       1345 | ````` ¿🤞? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 260: ````` <0x9E> ````` |
|       1553 | ````` ¿🧰? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 116: ````` <0xB0> ````` |
|        860 | ````` ¿👹? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 125: ````` <0xB9> `````                  |
|        305 | ````` ¿☀? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 230: ````` <0x80> `````                         |
|       1440 | ````` ¿🥿? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 131: ````` <0xBF> ````` |
|        333 | ````` ¿♍? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 243: ````` <0x8D> `````                         |
|       1651 | ````` ¿\U0001faf1? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 117: ````` <0xB1> ````` |
|        483 | ````` ¿🈳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 119: ````` <0xB3> ````` |
|       1573 | ````` ¿🩴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 120: ````` <0xB4> ````` |
|       1233 | ````` ¿🚗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 253: ````` <0x97> ````` |
|        413 | ````` ¿❣? `````          | -1.19209e-07 | 135523: ````` <0xE2><0x9D> `````, 104: ````` <0xA3> `````                        |
|        649 | ````` ¿🎣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 104: ````` <0xA3> ````` |
|        919 | ````` ¿💴? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 120: ````` <0xB4> `````                  |
|       1184 | ````` ¿😶? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 122: ````` <0xB6> `````                  |
|        621 | ````` ¿🎂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 232: ````` <0x82> ````` |
|        281 | ````` ¿⏏? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 245: ````` <0x8F> `````        |
|        290 | ````` ¿⏱? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 117: ````` <0xB1> `````        |
|       1090 | ````` ¿🕵? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 121: ````` <0xB5> ````` |
|        829 | ````` ¿👚? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 256: ````` <0x9A> `````                  |
|       1132 | ````` ¿😂? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 232: ````` <0x82> `````                  |
|        850 | ````` ¿👯? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 115: ````` <0xAF> `````                  |
|        721 | ````` ¿🏫? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 112: ````` <0xAB> `````                  |
|       1476 | ````` ¿🦣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 104: ````` <0xA3> ````` |
|        863 | ````` ¿👼? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 128: ````` <0xBC> `````                  |
|        432 | ````` ¿㊗? `````         | -1.19209e-07 | 167: ````` <0xE3> `````, 240: ````` <0x8A> `````, 253: ````` <0x97> `````        |
|        723 | ````` ¿🏭? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 263: ````` <0xAD> `````                  |
|        895 | ````` ¿💜? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 258: ````` <0x9C> `````                  |
|        873 | ````` ¿💆? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 236: ````` <0x86> `````                  |
|       1624 | ````` ¿\U0001fab9? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 125: ````` <0xB9> ````` |
|       1406 | ````` ¿🥝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 259: ````` <0x9D> ````` |
|        994 | ````` ¿🔀? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 230: ````` <0x80> `````                  |
|       1250 | ````` ¿🚨? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 109: ````` <0xA8> ````` |
|        542 | ````` ¿🌳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 119: ````` <0xB3> ````` |
|       1417 | ````` ¿🥨? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 109: ````` <0xA8> ````` |
|        332 | ````` ¿♌? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 242: ````` <0x8C> `````                         |
|        474 | ````` ¿🇼? `````          | -1.19209e-07 | 108080: ````` 🇼 `````                                                            |
|        753 | ````` ¿🐎? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 244: ````` <0x8E> ````` |
|       1232 | ````` ¿🚖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 252: ````` <0x96> ````` |
|        513 | ````` ¿🌔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 250: ````` <0x94> ````` |
|        557 | ````` ¿🍂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 232: ````` <0x82> ````` |
|        651 | ````` ¿🎥? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 106: ````` <0xA5> ````` |
|       1178 | ````` ¿😰? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 116: ````` <0xB0> `````                  |
|       1123 | ````` ¿🗳? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 119: ````` <0xB3> ````` |
|       1047 | ````` ¿🔵? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 121: ````` <0xB5> `````                  |
|       1419 | ````` ¿🥪? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 111: ````` <0xAA> ````` |
|        522 | ````` ¿🌝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 259: ````` <0x9D> ````` |
|        864 | ````` ¿👽? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 129: ````` <0xBD> `````                  |
|       1559 | ````` ¿🧶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 122: ````` <0xB6> ````` |
|       1340 | ````` ¿🤙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 255: ````` <0x99> ````` |
|       1555 | ````` ¿🧲? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 118: ````` <0xB2> ````` |
|       1473 | ````` ¿🦠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 262: ````` <0xA0> ````` |
|       1268 | ````` ¿🚺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 126: ````` <0xBA> ````` |
|        626 | ````` ¿🎇? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 237: ````` <0x87> ````` |
|       1602 | ````` ¿🪠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 262: ````` <0xA0> ````` |
|       1111 | ````` ¿🗃? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 233: ````` <0x83> ````` |
|       1637 | ````` ¿🫕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 251: ````` <0x95> ````` |
|       1353 | ````` ¿🤦? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 107: ````` <0xA6> ````` |
|        553 | ````` ¿🌾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 130: ````` <0xBE> ````` |
|        487 | ````` ¿🈷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 123: ````` <0xB7> ````` |
|        849 | ````` ¿👮? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 114: ````` <0xAE> `````                  |
|       1662 | ````` ¿\U000e006e? ````` | -1.19209e-07 | 9738: ````` \U000e006e `````                                                     |
|        295 | ````` ¿⏺? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 126: ````` <0xBA> `````        |
|       1231 | ````` ¿🚕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 251: ````` <0x95> ````` |
|       1252 | ````` ¿🚪? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 111: ````` <0xAA> ````` |
|       1596 | ````` ¿🪚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 256: ````` <0x9A> ````` |
|       1544 | ````` ¿🧧? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 108: ````` <0xA7> ````` |
|        392 | ````` ¿✊? `````         | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 240: ````` <0x8A> `````                         |
|        733 | ````` ¿🏺? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 126: ````` <0xBA> `````                  |
|       1182 | ````` ¿😴? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 120: ````` <0xB4> `````                  |
|       1600 | ````` ¿🪞? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 260: ````` <0x9E> ````` |
|        343 | ````` ¿♥? `````          | -1.19209e-07 | 171540: ````` ♥ `````                                                            |
|       1209 | ````` ¿🙏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 245: ````` <0x8F> ````` |
|       1510 | ````` ¿🧅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 235: ````` <0x85> ````` |
|        987 | ````` ¿📸? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 124: ````` <0xB8> `````                  |
|       1008 | ````` ¿🔎? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 244: ````` <0x8E> `````                  |
|        869 | ````` ¿💂? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 232: ````` <0x82> `````                  |
|        940 | ````` ¿📉? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 239: ````` <0x89> `````                  |
|        476 | ````` ¿🇾? `````          | -1.19209e-07 | 100210: ````` 🇾 `````                                                            |
|        583 | ````` ¿🍜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 258: ````` <0x9C> ````` |
|       1054 | ````` ¿🔼? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 128: ````` <0xBC> `````                  |
|        727 | ````` ¿🏳? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 119: ````` <0xB3> `````                  |
|       1338 | ````` ¿🤗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 253: ````` <0x97> ````` |
|        593 | ````` ¿🍦? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 107: ````` <0xA6> ````` |
|       1162 | ````` ¿😠? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 262: ````` <0xA0> `````                  |
|       1222 | ````` ¿🚌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 6617: ````` <0x9A><0x8C> `````                   |
|        541 | ````` ¿🌲? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 118: ````` <0xB2> ````` |
|        851 | ````` ¿👰? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 116: ````` <0xB0> `````                  |
|        570 | ````` ¿🍏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 245: ````` <0x8F> ````` |
|        353 | ````` ¿⚖? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 252: ````` <0x96> `````                        |
|       1350 | ````` ¿🤣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 104: ````` <0xA3> ````` |
|        469 | ````` ¿🇷? `````          | -1.19209e-07 | 7534: ````` 🇷 `````                                                              |
|       1367 | ````` ¿🤴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 120: ````` <0xB4> ````` |
|        724 | ````` ¿🏮? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 114: ````` <0xAE> `````                  |
|       1033 | ````` ¿🔧? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 108: ````` <0xA7> `````                  |
|        411 | ````` ¿❕? `````         | -1.19209e-07 | 135523: ````` <0xE2><0x9D> `````, 251: ````` <0x95> `````                        |
|        625 | ````` ¿🎆? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 236: ````` <0x86> ````` |
|       1385 | ````` ¿🥈? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 238: ````` <0x88> ````` |
|        876 | ````` ¿💉? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 239: ````` <0x89> `````                  |
|       1253 | ````` ¿🚫? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 112: ````` <0xAB> ````` |
|       1255 | ````` ¿🚭? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 263: ````` <0xAD> ````` |
|        717 | ````` ¿🏧? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 108: ````` <0xA7> `````                  |
|       1649 | ````` ¿\U0001fae7? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 108: ````` <0xA7> ````` |
|       1278 | ````` ¿🛄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 7840: ````` <0x9B><0x84> `````                   |
|        810 | ````` ¿👇? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 237: ````` <0x87> `````                  |
|        599 | ````` ¿🍬? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 113: ````` <0xAC> ````` |
|       1587 | ````` ¿🪑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 247: ````` <0x91> ````` |
|        771 | ````` ¿🐠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 262: ````` <0xA0> ````` |
|        841 | ````` ¿👦? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 107: ````` <0xA6> `````                  |
|       1344 | ````` ¿🤝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 259: ````` <0x9D> ````` |
|        324 | ````` ¿☹? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 125: ````` <0xB9> `````                         |
|       1251 | ````` ¿🚩? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 110: ````` <0xA9> ````` |
|        964 | ````` ¿📡? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 102: ````` <0xA1> `````                  |
|        752 | ````` ¿🐍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 243: ````` <0x8D> ````` |
|        517 | ````` ¿🌘? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 254: ````` <0x98> ````` |
|        927 | ````` ¿💼? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 128: ````` <0xBC> `````                  |
|       1282 | ````` ¿🛍? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 243: ````` <0x8D> ````` |
|       1554 | ````` ¿🧱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 117: ````` <0xB1> ````` |
|        451 | ````` ¿🆚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 256: ````` <0x9A> ````` |
|       1427 | ````` ¿🥲? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 118: ````` <0xB2> ````` |
|       1650 | ````` ¿\U0001faf0? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 116: ````` <0xB0> ````` |
|       1003 | ````` ¿🔉? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 239: ````` <0x89> `````                  |
|       1046 | ````` ¿🔴? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 120: ````` <0xB4> `````                  |
|        991 | ````` ¿📼? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 128: ````` <0xBC> `````                  |
|        765 | ````` ¿🐚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 256: ````` <0x9A> ````` |
|       1505 | ````` ¿🧀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 230: ````` <0x80> ````` |
|       1156 | ````` ¿😚? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 256: ````` <0x9A> `````                  |
|        588 | ````` ¿🍡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 102: ````` <0xA1> ````` |
|        835 | ````` ¿👠? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 262: ````` <0xA0> `````                  |
|       1201 | ````` ¿🙇? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 237: ````` <0x87> ````` |
|       1010 | ````` ¿🔐? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 246: ````` <0x90> `````                  |
|        283 | ````` ¿⏪? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 111: ````` <0xAA> `````        |
|       1202 | ````` ¿🙈? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 238: ````` <0x88> ````` |
|       1592 | ````` ¿🪖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 252: ````` <0x96> ````` |
|        372 | ````` ¿⛑? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 247: ````` <0x91> `````        |
|       1654 | ````` ¿\U0001faf4? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 120: ````` <0xB4> ````` |
|       1597 | ````` ¿🪛? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 257: ````` <0x9B> ````` |
|       1475 | ````` ¿🦢? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 103: ````` <0xA2> ````` |
|       1242 | ````` ¿🚠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 262: ````` <0xA0> ````` |
|       1051 | ````` ¿🔹? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 125: ````` <0xB9> `````                  |
|        573 | ````` ¿🍒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 248: ````` <0x92> ````` |
|       1518 | ````` ¿🧍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 243: ````` <0x8D> ````` |
|       1656 | ````` ¿\U0001faf6? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 122: ````` <0xB6> ````` |
|        552 | ````` ¿🌽? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 129: ````` <0xBD> ````` |
|        576 | ````` ¿🍕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 251: ````` <0x95> ````` |
|       1149 | ````` ¿😓? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 249: ````` <0x93> `````                  |
|       1040 | ````` ¿🔮? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 114: ````` <0xAE> `````                  |
|       1371 | ````` ¿🤸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 124: ````` <0xB8> ````` |
|       1193 | ````` ¿😿? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 131: ````` <0xBF> `````                  |
|       1646 | ````` ¿\U0001fae4? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 105: ````` <0xA4> ````` |
|       1217 | ````` ¿🚇? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 237: ````` <0x87> ````` |
|        679 | ````` ¿🏁? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 231: ````` <0x81> `````                  |
|        880 | ````` ¿💍? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 243: ````` <0x8D> `````                  |
|        718 | ````` ¿🏨? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 109: ````` <0xA8> `````                  |
|        391 | ````` ¿✉? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 239: ````` <0x89> `````                         |
|       1459 | ````` ¿🦒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 248: ````` <0x92> ````` |
|        609 | ````` ¿🍶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 122: ````` <0xB6> ````` |
|       1579 | ````` ¿🪀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 230: ````` <0x80> ````` |
|       1059 | ````` ¿🕌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 12443: ````` <0x95><0x8C> `````                  |
|       1516 | ````` ¿🧋? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 241: ````` <0x8B> ````` |
|        899 | ````` ¿💠? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 262: ````` <0xA0> `````                  |
|        501 | ````` ¿🌈? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 238: ````` <0x88> ````` |
|       1170 | ````` ¿😨? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 109: ````` <0xA8> `````                  |
|        527 | ````` ¿🌤? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 105: ````` <0xA4> ````` |
|        744 | ````` ¿🐅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 235: ````` <0x85> ````` |
|        939 | ````` ¿📈? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 238: ````` <0x88> `````                  |
|       1389 | ````` ¿🥌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 242: ````` <0x8C> ````` |
|       1180 | ````` ¿😲? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 118: ````` <0xB2> `````                  |
|        360 | ````` ¿⚧? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 108: ````` <0xA7> `````                        |
|       1219 | ````` ¿🚉? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 239: ````` <0x89> ````` |
|       1194 | ````` ¿🙀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 230: ````` <0x80> ````` |
|        344 | ````` ¿♦? `````          | -1.19209e-07 | 238161: ````` ♦ `````                                                            |
|        595 | ````` ¿🍨? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 49252: ````` <0x8D><0xA8> `````                  |
|        957 | ````` ¿📚? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 256: ````` <0x9A> `````                  |
|        475 | ````` ¿🇽? `````          | -1.19209e-07 | 2244: ````` <0xF0><0x9F><0x87> `````, 129: ````` <0xBD> `````                    |
|       1594 | ````` ¿🪘? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 254: ````` <0x98> ````` |
|       1622 | ````` ¿\U0001fab7? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 123: ````` <0xB7> ````` |
|       1575 | ````` ¿🩹? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 125: ````` <0xB9> ````` |
|        836 | ````` ¿👡? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 102: ````` <0xA1> `````                  |
|        482 | ````` ¿🈲? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 118: ````` <0xB2> ````` |
|        535 | ````` ¿🌬? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 113: ````` <0xAC> ````` |
|       1164 | ````` ¿😢? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 103: ````` <0xA2> `````                  |
|       1317 | ````` ¿🟣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 104: ````` <0xA3> ````` |
|       1186 | ````` ¿😸? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 124: ````` <0xB8> `````                  |
|        291 | ````` ¿⏲? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 118: ````` <0xB2> `````        |
|       1084 | ````` ¿🕦? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 107: ````` <0xA6> ````` |
|        930 | ````` ¿💿? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 131: ````` <0xBF> `````                  |
|        730 | ````` ¿🏷? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 123: ````` <0xB7> `````                  |
|       1538 | ````` ¿🧡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 102: ````` <0xA1> ````` |
|        479 | ````` ¿🈂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 232: ````` <0x82> ````` |
|        942 | ````` ¿📋? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 241: ````` <0x8B> `````                  |
|        677 | ````` ¿🎿? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 131: ````` <0xBF> ````` |
|       1005 | ````` ¿🔋? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 241: ````` <0x8B> `````                  |
|        368 | ````` ¿⛅? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 235: ````` <0x85> `````        |
|       1494 | ````` ¿🦵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 121: ````` <0xB5> ````` |
|        757 | ````` ¿🐒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 248: ````` <0x92> ````` |
|       1429 | ````` ¿🥴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 120: ````` <0xB4> ````` |
|       1197 | ````` ¿🙃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 233: ````` <0x83> ````` |
|        931 | ````` ¿📀? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 230: ````` <0x80> `````                  |
|       1049 | ````` ¿🔷? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 123: ````` <0xB7> `````                  |
|       1273 | ````` ¿🚿? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 131: ````` <0xBF> ````` |
|       1023 | ````` ¿🔝? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 259: ````` <0x9D> `````                  |
|        606 | ````` ¿🍳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 119: ````` <0xB3> ````` |
|        722 | ````` ¿🏬? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 113: ````` <0xAC> `````                  |
|        901 | ````` ¿💢? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 103: ````` <0xA2> `````                  |
|        450 | ````` ¿🆙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 255: ````` <0x99> ````` |
|        862 | ````` ¿👻? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 127: ````` <0xBB> `````                  |
|        992 | ````` ¿📽? `````          | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 129: ````` <0xBD> `````                  |
|       1110 | ````` ¿🗂? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 232: ````` <0x82> ````` |
|        959 | ````` ¿📜? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 258: ````` <0x9C> `````                  |
|        304 | ````` ¿◾? `````         | -1.19209e-07 | 37357: ````` <0xE2><0x97> `````, 130: ````` <0xBE> `````                         |
|        854 | ````` ¿👳? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 119: ````` <0xB3> `````                  |
|        790 | ````` ¿🐳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 119: ````` <0xB3> ````` |
|       1157 | ````` ¿😛? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 257: ````` <0x9B> `````                  |
|        460 | ````` ¿🇮? `````          | -1.19209e-07 | 31122: ````` 🇮 `````                                                             |
|       1390 | ````` ¿🥍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 243: ````` <0x8D> ````` |
|        532 | ````` ¿🌩? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 110: ````` <0xA9> ````` |
|       1133 | ````` ¿😃? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 233: ````` <0x83> `````                  |
|       1259 | ````` ¿🚱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 117: ````` <0xB1> ````` |
|       1283 | ````` ¿🛎? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 244: ````` <0x8E> ````` |
|       1177 | ````` ¿😯? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 115: ````` <0xAF> `````                  |
|       1661 | ````` ¿\U000e006c? ````` | -1.19209e-07 | 69092: ````` \U000e006c `````                                                    |
|       1387 | ````` ¿🥊? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 240: ````` <0x8A> ````` |
|       1171 | ````` ¿😩? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 110: ````` <0xA9> `````                  |
|        307 | ````` ¿☂? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 232: ````` <0x82> `````                         |
|        579 | ````` ¿🍘? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 254: ````` <0x98> ````` |
|        756 | ````` ¿🐑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 247: ````` <0x91> ````` |
|       1576 | ````` ¿🩺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 126: ````` <0xBA> ````` |
|       1638 | ````` ¿🫖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 252: ````` <0x96> ````` |
|        699 | ````` ¿🏕? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 251: ````` <0x95> `````                  |
|       1630 | ````` ¿\U0001fac4? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 234: ````` <0x84> ````` |
|       1159 | ````` ¿😝? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 259: ````` <0x9D> `````                  |
|       1299 | ````` ¿🛥? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 106: ````` <0xA5> ````` |
|       1128 | ````` ¿🗾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 130: ````` <0xBE> ````` |
|       1148 | ````` ¿😒? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 248: ````` <0x92> `````                  |
|        798 | ````` ¿🐻? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 127: ````` <0xBB> ````` |
|        617 | ````` ¿🍾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 130: ````` <0xBE> ````` |
|        354 | ````` ¿⚗? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 253: ````` <0x97> `````                        |
|       1378 | ````` ¿🥀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 230: ````` <0x80> ````` |
|        375 | ````` ¿⛩? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 110: ````` <0xA9> `````        |
|        511 | ````` ¿🌒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 248: ````` <0x92> ````` |
|        865 | ````` ¿👾? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 130: ````` <0xBE> `````                  |
|       1146 | ````` ¿😐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 15468: ````` <0x98><0x90> `````                  |
|        630 | ````` ¿🎋? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 241: ````` <0x8B> ````` |
|        496 | ````` ¿🌃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 233: ````` <0x83> ````` |
|       1014 | ````` ¿🔔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 10121: ````` <0x94><0x94> `````                  |
|       1136 | ````` ¿😆? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 236: ````` <0x86> `````                  |
|        870 | ````` ¿💃? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 233: ````` <0x83> `````                  |
|        545 | ````` ¿🌶? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 122: ````` <0xB6> ````` |
|       1094 | ````` ¿🕹? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 125: ````` <0xB9> ````` |
|       1441 | ````` ¿🦀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 230: ````` <0x80> ````` |
|       1032 | ````` ¿🔦? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 107: ````` <0xA6> `````                  |
|       1018 | ````` ¿🔘? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 254: ````` <0x98> `````                  |
|        412 | ````` ¿❗? `````         | -1.19209e-07 | 135523: ````` <0xE2><0x9D> `````, 253: ````` <0x97> `````                        |
|       1001 | ````` ¿🔇? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 237: ````` <0x87> `````                  |
|        580 | ````` ¿🍙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 255: ````` <0x99> ````` |
|        712 | ````` ¿🏢? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 103: ````` <0xA2> `````                  |
|       1599 | ````` ¿🪝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 259: ````` <0x9D> ````` |
|       1004 | ````` ¿🔊? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 240: ````` <0x8A> `````                  |
|       1082 | ````` ¿🕤? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 105: ````` <0xA4> ````` |
|        658 | ````` ¿🎬? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 113: ````` <0xAC> ````` |
|        866 | ````` ¿👿? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 131: ````` <0xBF> `````                  |
|        846 | ````` ¿👫? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 112: ````` <0xAB> `````                  |
|        933 | ````` ¿📂? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 232: ````` <0x82> `````                  |
|        847 | ````` ¿👬? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 113: ````` <0xAC> `````                  |
|       1626 | ````` ¿🫀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 230: ````` <0x80> ````` |
|        828 | ````` ¿👙? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 255: ````` <0x99> `````                  |
|       1347 | ````` ¿🤠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 262: ````` <0xA0> ````` |
|        917 | ````` ¿💲? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 118: ````` <0xB2> `````                  |
|        382 | ````` ¿⛵? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 121: ````` <0xB5> `````        |
|       1274 | ````` ¿🛀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 230: ````` <0x80> ````` |
|       1254 | ````` ¿🚬? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 113: ````` <0xAC> ````` |
|        806 | ````` ¿👃? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 233: ````` <0x83> `````                  |
|       1196 | ````` ¿🙂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 232: ````` <0x82> ````` |
|        659 | ````` ¿🎭? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 263: ````` <0xAD> ````` |
|       1418 | ````` ¿🥩? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 110: ````` <0xA9> ````` |
|        633 | ````` ¿🎎? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 244: ````` <0x8E> ````` |
|        745 | ````` ¿🐆? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 236: ````` <0x86> ````` |
|       1247 | ````` ¿🚥? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 106: ````` <0xA5> ````` |
|       1224 | ````` ¿🚎? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 244: ````` <0x8E> ````` |
|       1666 | ````` ¿\U000e007f? ````` | -1.19209e-07 | 60446: ````` \U000e007f `````                                                    |
|       1525 | ````` ¿🧔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 250: ````` <0x94> ````` |
|        531 | ````` ¿🌨? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 109: ````` <0xA8> ````` |
|       1635 | ````` ¿🫓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 171080: ````` <0xAB><0x93> `````                 |
|        370 | ````` ¿⛎? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 244: ````` <0x8E> `````        |
|        822 | ````` ¿👓? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 249: ````` <0x93> `````                  |
|        340 | ````` ¿♟? `````          | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 261: ````` <0x9F> `````                         |
|        814 | ````` ¿👋? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 241: ````` <0x8B> `````                  |
|       1653 | ````` ¿\U0001faf3? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 119: ````` <0xB3> ````` |
|        986 | ````` ¿📷? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 123: ````` <0xB7> `````                  |
|       1633 | ````` ¿🫑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 247: ````` <0x91> ````` |
|       1279 | ````` ¿🛅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 235: ````` <0x85> ````` |
|       1220 | ````` ¿🚊? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 240: ````` <0x8A> ````` |
|        831 | ````` ¿👜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 11524: ````` <0x91><0x9C> `````                  |
|        622 | ````` ¿🎃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 233: ````` <0x83> ````` |
|        543 | ````` ¿🌴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 120: ````` <0xB4> ````` |
|        913 | ````` ¿💮? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 114: ````` <0xAE> `````                  |
|        325 | ````` ¿☺? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 126: ````` <0xBA> `````                         |
|        346 | ````` ¿♻? `````          | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 127: ````` <0xBB> `````                         |
|        574 | ````` ¿🍓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 249: ````` <0x93> ````` |
|        275 | ````` ¿↙? `````          | -1.19209e-07 | 76876: ````` <0xE2><0x86> `````, 255: ````` <0x99> `````                         |
|        974 | ````` ¿📫? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 112: ````` <0xAB> `````                  |
|        505 | ````` ¿🌌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 242: ````` <0x8C> ````` |
|       1517 | ````` ¿\U0001f9cc? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 242: ````` <0x8C> ````` |
|       1124 | ````` ¿🗺? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 126: ````` <0xBA> ````` |
|       1185 | ````` ¿😷? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 123: ````` <0xB7> `````                  |
|        661 | ````` ¿🎯? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 115: ````` <0xAF> ````` |
|        904 | ````` ¿💥? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 106: ````` <0xA5> `````                  |
|       1122 | ````` ¿🗯? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 115: ````` <0xAF> ````` |
|        652 | ````` ¿🎦? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 107: ````` <0xA6> ````` |
|       1446 | ````` ¿🦅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 235: ````` <0x85> ````` |
|        424 | ````` ¿⬆? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 113: ````` <0xAC> `````, 236: ````` <0x86> `````        |
|       1151 | ````` ¿😕? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 251: ````` <0x95> `````                  |
|       1382 | ````` ¿🥄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 234: ````` <0x84> ````` |
|       1373 | ````` ¿🤺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 126: ````` <0xBA> ````` |
|       1168 | ````` ¿😦? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 107: ````` <0xA6> `````                  |
|        477 | ````` ¿🇿? `````          | -1.19209e-07 | 42240: ````` 🇿 `````                                                             |
|       1343 | ````` ¿🤜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 258: ````` <0x9C> ````` |
|       1447 | ````` ¿🦆? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 236: ````` <0x86> ````` |
|       1351 | ````` ¿🤤? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 105: ````` <0xA4> ````` |
|       1150 | ````` ¿😔? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 250: ````` <0x94> `````                  |
|       1057 | ````` ¿🕊? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 240: ````` <0x8A> ````` |
|       1570 | ````` ¿🩱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 117: ````` <0xB1> ````` |
|        650 | ````` ¿🎤? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 105: ````` <0xA4> ````` |
|        710 | ````` ¿🏠? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 262: ````` <0xA0> `````                  |
|       1370 | ````` ¿🤷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 123: ````` <0xB7> ````` |
|        971 | ````` ¿📨? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 65064: ````` <0x93><0xA8> `````                  |
|       1075 | ````` ¿🕝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 259: ````` <0x9D> ````` |
|       1172 | ````` ¿😪? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 111: ````` <0xAA> `````                  |
|       1187 | ````` ¿😹? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 125: ````` <0xB9> `````                  |
|        912 | ````` ¿💭? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 263: ````` <0xAD> `````                  |
|        484 | ````` ¿🈴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 120: ````` <0xB4> ````` |
|        874 | ````` ¿💇? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 237: ````` <0x87> `````                  |
|       1077 | ````` ¿🕟? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 261: ````` <0x9F> ````` |
|       1466 | ````` ¿🦙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 255: ````` <0x99> ````` |
|        537 | ````` ¿🌮? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 114: ````` <0xAE> ````` |
|        590 | ````` ¿🍣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 104: ````` <0xA3> ````` |
|        672 | ````` ¿🎺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 126: ````` <0xBA> ````` |
|       1617 | ````` ¿🪲? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 118: ````` <0xB2> ````` |
|       1380 | ````` ¿🥂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 232: ````` <0x82> ````` |
|       1381 | ````` ¿🥃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 233: ````` <0x83> ````` |
|       1558 | ````` ¿🧵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 121: ````` <0xB5> ````` |
|        554 | ````` ¿🌿? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 131: ````` <0xBF> ````` |
|        641 | ````` ¿🎙? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 255: ````` <0x99> ````` |
|       1152 | ````` ¿😖? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 252: ````` <0x96> `````                  |
|        890 | ````` ¿💗? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 253: ````` <0x97> `````                  |
|        951 | ````` ¿📔? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 250: ````` <0x94> `````                  |
|        995 | ````` ¿🔁? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 231: ````` <0x81> `````                  |
|        801 | ````` ¿🐾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 130: ````` <0xBE> ````` |
|       1221 | ````` ¿🚋? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 241: ````` <0x8B> ````` |
|        644 | ````` ¿🎞? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 260: ````` <0x9E> ````` |
|       1174 | ````` ¿😬? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 113: ````` <0xAC> `````                  |
|       1070 | ````` ¿🕘? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 254: ````` <0x98> ````` |
|        355 | ````` ¿⚙? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 255: ````` <0x99> `````                        |
|        966 | ````` ¿📣? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 104: ````` <0xA3> `````                  |
|       1364 | ````` ¿🤱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 117: ````` <0xB1> ````` |
|        857 | ````` ¿👶? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 122: ````` <0xB6> `````                  |
|       1482 | ````` ¿🦩? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 110: ````` <0xA9> ````` |
|       1619 | ````` ¿🪴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 120: ````` <0xB4> ````` |
|       1465 | ````` ¿🦘? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 254: ````` <0x98> ````` |
|       1397 | ````` ¿🥔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 250: ````` <0x94> ````` |
|       1264 | ````` ¿🚶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 122: ````` <0xB6> ````` |
|        961 | ````` ¿📞? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 260: ````` <0x9E> `````                  |
|       1407 | ````` ¿🥞? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 260: ````` <0x9E> ````` |
|       1307 | ````` ¿🛶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 122: ````` <0xB6> ````` |
|       1227 | ````` ¿🚑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 247: ````` <0x91> ````` |
|        985 | ````` ¿📶? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 122: ````` <0xB6> `````                  |
|       1016 | ````` ¿🔖? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 252: ````` <0x96> `````                  |
|       1550 | ````` ¿🧭? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 263: ````` <0xAD> ````` |
|        840 | ````` ¿👥? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 106: ````` <0xA5> `````                  |
|        624 | ````` ¿🎅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 235: ````` <0x85> ````` |
|        673 | ````` ¿🎻? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 127: ````` <0xBB> ````` |
|        998 | ````` ¿🔄? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 234: ````` <0x84> `````                  |
|        288 | ````` ¿⏯? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 115: ````` <0xAF> `````        |
|       1431 | ````` ¿🥶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 122: ````` <0xB6> ````` |
|       1355 | ````` ¿🤨? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 109: ````` <0xA8> ````` |
|       1561 | ````` ¿🧸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 124: ````` <0xB8> ````` |
|        660 | ````` ¿🎮? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 114: ````` <0xAE> ````` |
|        687 | ````` ¿🏉? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 239: ````` <0x89> `````                  |
|       1499 | ````` ¿🦺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 126: ````` <0xBA> ````` |
|       1547 | ````` ¿🧪? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 111: ````` <0xAA> ````` |
|       1041 | ````` ¿🔯? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 115: ````` <0xAF> `````                  |
|       1085 | ````` ¿🕧? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 108: ````` <0xA7> ````` |
|        301 | ````` ¿◻? `````          | -1.19209e-07 | 37357: ````` <0xE2><0x97> `````, 127: ````` <0xBB> `````                         |
|       1026 | ````` ¿🔠? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 262: ````` <0xA0> `````                  |
|       1145 | ````` ¿😏? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 245: ````` <0x8F> `````                  |
|        387 | ````` ¿⛽? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 129: ````` <0xBD> `````        |
|       1634 | ````` ¿🫒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 248: ````` <0x92> ````` |
|       1208 | ````` ¿🙎? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 244: ````` <0x8E> ````` |
|        943 | ````` ¿📌? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 242: ````` <0x8C> `````                  |
|        514 | ````` ¿🌕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 251: ````` <0x95> ````` |
|       1374 | ````` ¿🤼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 139814: ````` <0xA4><0xBC> `````                 |
|       1533 | ````` ¿🧜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 258: ````` <0x9C> ````` |
|        564 | ````` ¿🍉? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 239: ````` <0x89> ````` |
|        920 | ````` ¿💵? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 121: ````` <0xB5> `````                  |
|        455 | ````` ¿🇩? `````          | -1.19209e-07 | 66360: ````` 🇩 `````                                                             |
|       1439 | ````` ¿🥾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 130: ````` <0xBE> ````` |
|       1609 | ````` ¿🪧? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 108: ````` <0xA7> ````` |
|        577 | ````` ¿🍖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 252: ````` <0x96> ````` |
|       1383 | ````` ¿🥅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 235: ````` <0x85> ````` |
|        903 | ````` ¿💤? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 105: ````` <0xA4> `````                  |
|        439 | ````` ¿🅾? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 235: ````` <0x85> `````, 130: ````` <0xBE> ````` |
|        603 | ````` ¿🍰? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 116: ````` <0xB0> ````` |
|        421 | ````` ¿⤴? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 105: ````` <0xA4> `````, 120: ````` <0xB4> `````        |
|       1107 | ````` ¿🖱? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 117: ````` <0xB1> ````` |
|        539 | ````` ¿🌰? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 116: ````` <0xB0> ````` |
|        461 | ````` ¿🇯? `````          | -1.19209e-07 | 169789: ````` 🇯 `````                                                            |
|       1055 | ````` ¿🔽? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 129: ````` <0xBD> `````                  |
|        560 | ````` ¿🍅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 235: ````` <0x85> ````` |
|        429 | ````` ¿⭕? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 263: ````` <0xAD> `````, 251: ````` <0x95> `````        |
|        973 | ````` ¿📪? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 111: ````` <0xAA> `````                  |
|       1572 | ````` ¿🩳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 119: ````` <0xB3> ````` |
|        645 | ````` ¿🎟? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 261: ````` <0x9F> ````` |
|        918 | ````` ¿💳? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 119: ````` <0xB3> `````                  |
|       1394 | ````` ¿🥑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 247: ````` <0x91> ````` |
|       1214 | ````` ¿🚄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 234: ````` <0x84> ````` |
|       1103 | ````` ¿🖖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 252: ````` <0x96> ````` |
|        381 | ````` ¿⛴? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 120: ````` <0xB4> `````        |
|       1612 | ````` ¿\U0001faaa? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 111: ````` <0xAA> ````` |
|        538 | ````` ¿🌯? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 115: ````` <0xAF> ````` |
|        589 | ````` ¿🍢? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 103: ````` <0xA2> ````` |
|       1006 | ````` ¿🔌? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 242: ````` <0x8C> `````                  |
|        893 | ````` ¿💚? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 256: ````` <0x9A> `````                  |
|        892 | ````` ¿💙? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 255: ````` <0x99> `````                  |
|        941 | ````` ¿📊? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 240: ````` <0x8A> `````                  |
|       1328 | ````` ¿🤍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 243: ````` <0x8D> ````` |
|        286 | ````` ¿⏭? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 263: ````` <0xAD> `````        |
|       1263 | ````` ¿🚵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 121: ````` <0xB5> ````` |
|        478 | ````` ¿🈁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 231: ````` <0x81> ````` |
|       1052 | ````` ¿🔺? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 126: ````` <0xBA> `````                  |
|       1342 | ````` ¿🤛? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 257: ````` <0x9B> ````` |
|       1031 | ````` ¿🔥? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 106: ````` <0xA5> `````                  |
|       1211 | ````` ¿🚁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 231: ````` <0x81> ````` |
|       1118 | ````` ¿🗞? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 260: ````` <0x9E> ````` |
|        389 | ````` ¿✅? `````         | -1.19209e-07 | 214871: ````` ✅ `````                                                           |
|        521 | ````` ¿🌜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 258: ````` <0x9C> ````` |
|        952 | ````` ¿📕? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 251: ````` <0x95> `````                  |
|        921 | ````` ¿💶? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 122: ````` <0xB6> `````                  |
|        490 | ````` ¿🈺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 126: ````` <0xBA> ````` |
|       1034 | ````` ¿🔨? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 109: ````` <0xA8> `````                  |
|        871 | ````` ¿💄? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 234: ````` <0x84> `````                  |
|       1527 | ````` ¿🧖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 252: ````` <0x96> ````` |
|       1409 | ````` ¿🥠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 262: ````` <0xA0> ````` |
|       1249 | ````` ¿🚧? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 108: ````` <0xA7> ````` |
|        462 | ````` ¿🇰? `````          | -1.19209e-07 | 30269: ````` 🇰 `````                                                             |
|        378 | ````` ¿⛱? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 117: ````` <0xB1> `````        |
|        897 | ````` ¿💞? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 260: ````` <0x9E> `````                  |
|       1330 | ````` ¿🤏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 245: ````` <0x8F> ````` |
|        377 | ````` ¿⛰? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 71996: ````` <0x9B><0xB0> `````                         |
|        887 | ````` ¿💔? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 250: ````` <0x94> `````                  |
|       1199 | ````` ¿🙅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 235: ````` <0x85> ````` |
|       1457 | ````` ¿🦐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 246: ````` <0x90> ````` |
|        336 | ````` ¿♐? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 246: ````` <0x90> `````                         |
|       1067 | ````` ¿🕕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 251: ````` <0x95> ````` |
|       1428 | ````` ¿🥳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 119: ````` <0xB3> ````` |
|       1616 | ````` ¿🪱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 117: ````` <0xB1> ````` |
|        546 | ````` ¿🌷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 123: ````` <0xB7> ````` |
|        515 | ````` ¿🌖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 252: ````` <0x96> ````` |
|        826 | ````` ¿👗? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 253: ````` <0x97> `````                  |
|        977 | ````` ¿📮? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 114: ````` <0xAE> `````                  |
|        643 | ````` ¿🎛? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 257: ````` <0x9B> ````` |
|        907 | ````` ¿💨? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 109: ````` <0xA8> `````                  |
|       1484 | ````` ¿🦫? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 112: ````` <0xAB> ````` |
|       1509 | ````` ¿🧄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 234: ````` <0x84> ````` |
|       1632 | ````` ¿🫐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 246: ````` <0x90> ````` |
|       1578 | ````` ¿\U0001fa7c? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 128: ````` <0xBC> ````` |
|        914 | ````` ¿💯? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 115: ````` <0xAF> `````                  |
|        563 | ````` ¿🍈? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 238: ````` <0x88> ````` |
|       1286 | ````` ¿🛑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 247: ````` <0x91> ````` |
|       1165 | ````` ¿😣? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 104: ````` <0xA3> `````                  |
|        398 | ````` ¿✔? `````          | -1.19209e-07 | 189894: ````` ✔ `````                                                            |
|        442 | ````` ¿🆑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 247: ````` <0x91> ````` |
|       1036 | ````` ¿🔪? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 111: ````` <0xAA> `````                  |
|       1611 | ````` ¿\U0001faa9? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 110: ````` <0xA9> ````` |
|       1024 | ````` ¿🔞? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 260: ````` <0x9E> `````                  |
|        549 | ````` ¿🌺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 126: ````` <0xBA> ````` |
|        911 | ````` ¿💬? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 113: ````` <0xAC> `````                  |
|        653 | ````` ¿🎧? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 108: ````` <0xA7> ````` |
|       1636 | ````` ¿🫔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 250: ````` <0x94> ````` |
|       1009 | ````` ¿🔏? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 245: ````` <0x8F> `````                  |
|        567 | ````` ¿🍌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 242: ````` <0x8C> ````` |
|        318 | ````` ¿☣? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 104: ````` <0xA3> `````                         |
|       1477 | ````` ¿🦤? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 105: ````` <0xA4> ````` |
|       1456 | ````` ¿🦏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 245: ````` <0x8F> ````` |
|        405 | ````` ¿❄? `````          | -1.19209e-07 | 135523: ````` <0xE2><0x9D> `````, 234: ````` <0x84> `````                        |
|        639 | ````` ¿🎖? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 252: ````` <0x96> ````` |
|        910 | ````` ¿💫? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 112: ````` <0xAB> `````                  |
|       1138 | ````` ¿😈? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 238: ````` <0x88> `````                  |
|        615 | ````` ¿🍼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 22059: ````` <0x8D><0xBC> `````                  |
|       1062 | ````` ¿🕐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 246: ````` <0x90> ````` |
|        582 | ````` ¿🍛? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 257: ````` <0x9B> ````` |
|       1500 | ````` ¿🦻? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 127: ````` <0xBB> ````` |
|        459 | ````` ¿🇭? `````          | -1.19209e-07 | 39476: ````` 🇭 `````                                                             |
|       1515 | ````` ¿🧊? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 240: ````` <0x8A> ````` |
|        480 | ````` ¿🈚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 256: ````` <0x9A> ````` |
|       1563 | ````` ¿🧺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 126: ````` <0xBA> ````` |
|       1400 | ````` ¿🥗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 253: ````` <0x97> ````` |
|        682 | ````` ¿🏄? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 234: ````` <0x84> `````                  |
|       1628 | ````` ¿🫂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 232: ````` <0x82> ````` |
|        859 | ````` ¿👸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 44125: ````` <0x91><0xB8> `````                  |
|        547 | ````` ¿🌸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 124: ````` <0xB8> ````` |
|       1648 | ````` ¿\U0001fae6? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 107: ````` <0xA6> ````` |
|       1404 | ````` ¿🥛? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 257: ````` <0x9B> ````` |
|       1529 | ````` ¿🧘? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 254: ````` <0x98> ````` |
|        271 | ````` ¿↕? `````          | -1.19209e-07 | 76876: ````` <0xE2><0x86> `````, 251: ````` <0x95> `````                         |
|        689 | ````` ¿🏋? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 241: ````` <0x8B> `````                  |
|       1167 | ````` ¿😥? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 106: ````` <0xA5> `````                  |
|       1402 | ````` ¿🥙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 255: ````` <0x99> ````` |
|        416 | ````` ¿➖? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 252: ````` <0x96> `````        |
|        799 | ````` ¿🐼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 128: ````` <0xBC> ````` |
|        393 | ````` ¿✋? `````         | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 241: ````` <0x8B> `````                         |
|       1652 | ````` ¿\U0001faf2? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 118: ````` <0xB2> ````` |
|        559 | ````` ¿🍄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 234: ````` <0x84> ````` |
|        379 | ````` ¿⛲? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 118: ````` <0xB2> `````        |
|       1450 | ````` ¿🦉? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 239: ````` <0x89> ````` |
|       1341 | ````` ¿🤚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 256: ````` <0x9A> ````` |
|        614 | ````` ¿🍻? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 127: ````` <0xBB> ````` |
|        875 | ````` ¿💈? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 238: ````` <0x88> `````                  |
|       1176 | ````` ¿😮? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 114: ````` <0xAE> `````                  |
|        926 | ````` ¿💻? `````         | -1.19209e-07 | 251116: ````` 💻 `````                                                           |
|       1096 | ````` ¿🖇? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 237: ````` <0x87> ````` |
|       1585 | ````` ¿🪆? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 236: ````` <0x86> ````` |
|        526 | ````` ¿🌡? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 102: ````` <0xA1> ````` |
|       1426 | ````` ¿🥱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 117: ````` <0xB1> ````` |
|        629 | ````` ¿🎊? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 240: ````` <0x8A> ````` |
|        284 | ````` ¿⏫? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 112: ````` <0xAB> `````        |
|        516 | ````` ¿🌗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 253: ````` <0x97> ````` |
|       1029 | ````` ¿🔣? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 104: ````` <0xA3> `````                  |
|        465 | ````` ¿🇳? `````          | -1.19209e-07 | 29878: ````` 🇳 `````                                                             |
|       1627 | ````` ¿🫁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 231: ````` <0x81> ````` |
|        825 | ````` ¿👖? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 252: ````` <0x96> `````                  |
|        662 | ````` ¿🎰? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 116: ````` <0xB0> ````` |
|       1601 | ````` ¿🪟? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 261: ````` <0x9F> ````` |
|       1068 | ````` ¿🕖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 252: ````` <0x96> ````` |
|        404 | ````` ¿✴? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 120: ````` <0xB4> `````                         |
|        872 | ````` ¿💅? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 235: ````` <0x85> `````                  |
|        608 | ````` ¿🍵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 121: ````` <0xB5> ````` |
|       1205 | ````` ¿🙋? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 241: ````` <0x8B> ````` |
|       1011 | ````` ¿🔑? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 247: ````` <0x91> `````                  |
|        963 | ````` ¿📠? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 262: ````` <0xA0> `````                  |
|        982 | ````` ¿📳? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 119: ````` <0xB3> `````                  |
|        390 | ````` ¿✈? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 238: ````` <0x88> `````                         |
|        578 | ````` ¿🍗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 253: ````` <0x97> ````` |
|       1101 | ````` ¿🖐? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 246: ````` <0x90> ````` |
|       1356 | ````` ¿🤩? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 110: ````` <0xA9> ````` |
|       1498 | ````` ¿🦹? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 125: ````` <0xB9> ````` |
|        969 | ````` ¿📦? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 107: ````` <0xA6> `````                  |
|       1129 | ````` ¿🗿? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 131: ````` <0xBF> ````` |
|       1331 | ````` ¿🤐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 246: ````` <0x90> ````` |
|        666 | ````` ¿🎴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 120: ````` <0xB4> ````` |
|        444 | ````` ¿🆓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 249: ````` <0x93> ````` |
|        928 | ````` ¿💽? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 129: ````` <0xBD> `````                  |
|        471 | ````` ¿🇹? `````          | -1.19209e-07 | 10591: ````` 🇹 `````                                                             |
|        720 | ````` ¿🏪? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 111: ````` <0xAA> `````                  |
|        949 | ````` ¿📒? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 248: ````` <0x92> `````                  |
|       1467 | ````` ¿🦚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 256: ````` <0x9A> ````` |
|        339 | ````` ¿♓? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 249: ````` <0x93> `````                         |
|       1483 | ````` ¿🦪? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 111: ````` <0xAA> ````` |
|        356 | ````` ¿⚛? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 257: ````` <0x9B> `````                        |
|       1321 | ````` ¿🟧? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 108: ````` <0xA7> ````` |
|       1422 | ````` ¿🥭? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 263: ````` <0xAD> ````` |
|        953 | ````` ¿📖? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 252: ````` <0x96> `````                  |
|       1270 | ````` ¿🚼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 128: ````` <0xBC> ````` |
|       1443 | ````` ¿🦂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 232: ````` <0x82> ````` |
|       1190 | ````` ¿😼? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 128: ````` <0xBC> `````                  |
|        680 | ````` ¿🏂? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 232: ````` <0x82> `````                  |
|        726 | ````` ¿🏰? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 116: ````` <0xB0> `````                  |
|        525 | ````` ¿🌠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 262: ````` <0xA0> ````` |
|        481 | ````` ¿🈯? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 115: ````` <0xAF> ````` |
|        980 | ````` ¿📱? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 117: ````` <0xB1> `````                  |
|       1430 | ````` ¿🥵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 121: ````` <0xB5> ````` |
|       1424 | ````` ¿🥯? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 115: ````` <0xAF> ````` |
|        855 | ````` ¿👴? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 120: ````` <0xB4> `````                  |
|        495 | ````` ¿🌂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 232: ````` <0x82> ````` |
|        329 | ````` ¿♉? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 239: ````` <0x89> `````                         |
|        509 | ````` ¿🌐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 246: ````` <0x90> ````` |
|       1425 | ````` ¿🥰? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 116: ````` <0xB0> ````` |
|        698 | ````` ¿🏔? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 250: ````` <0x94> `````                  |
|        489 | ````` ¿🈹? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 238: ````` <0x88> `````, 125: ````` <0xB9> ````` |
|       1542 | ````` ¿🧥? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 106: ````` <0xA5> ````` |
|       1631 | ````` ¿\U0001fac5? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 235: ````` <0x85> ````` |
|        735 | ````` ¿🏼? `````           | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 128: ````` <0xBC> `````                  |
|        555 | ````` ¿🍀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 230: ````` <0x80> ````` |
|        970 | ````` ¿📧? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 108: ````` <0xA7> `````                  |
|        819 | ````` ¿👐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 11948: ````` <0x91><0x90> `````                  |
|       1080 | ````` ¿🕢? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 103: ````` <0xA2> ````` |
|        385 | ````` ¿⛹? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 125: ````` <0xB9> `````        |
|        587 | ````` ¿🍠? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 262: ````` <0xA0> ````` |
|       1581 | ````` ¿🪂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 232: ````` <0x82> ````` |
|       1092 | ````` ¿🕷? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 123: ````` <0xB7> ````` |
|        708 | ````` ¿🏞? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 260: ````` <0x9E> `````                  |
|        524 | ````` ¿🌟? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 261: ````` <0x9F> ````` |
|        296 | ````` ¿Ⓜ? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 249: ````` <0x93> `````, 232: ````` <0x82> `````        |
|       1451 | ````` ¿🦊? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 240: ````` <0x8A> ````` |
|        858 | ````` ¿👷? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 123: ````` <0xB7> `````                  |
|       1608 | ````` ¿🪦? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 107: ````` <0xA6> ````` |
|        938 | ````` ¿📇? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 237: ````` <0x87> `````                  |
|       1532 | ````` ¿🧛? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 257: ````` <0x9B> ````` |
|       1458 | ````` ¿🦑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 247: ````` <0x91> ````` |
|       1154 | ````` ¿😘? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 254: ````` <0x98> `````                  |
|        523 | ````` ¿🌞? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 260: ````` <0x9E> ````` |
|        796 | ````` ¿🐹? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 125: ````` <0xB9> ````` |
|       1629 | ````` ¿\U0001fac3? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 233: ````` <0x83> ````` |
|        508 | ````` ¿🌏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 245: ````` <0x8F> ````` |
|       1411 | ````` ¿🥢? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 103: ````` <0xA2> ````` |
|       1541 | ````` ¿🧤? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 105: ````` <0xA4> ````` |
|        418 | ````` ¿➡? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 102: ````` <0xA1> `````        |
|        449 | ````` ¿🆘? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 254: ````` <0x98> ````` |
|       1095 | ````` ¿🕺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 126: ````` <0xBA> ````` |
|        754 | ````` ¿🐏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 245: ````` <0x8F> ````` |
|        438 | ````` ¿🅱? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 235: ````` <0x85> `````, 117: ````` <0xB1> ````` |
|       1212 | ````` ¿🚂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 232: ````` <0x82> ````` |
|       1590 | ````` ¿🪔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 250: ````` <0x94> ````` |
|        704 | ````` ¿🏚? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 256: ````` <0x9A> `````                  |
|       1137 | ````` ¿😇? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 237: ````` <0x87> `````                  |
|       1480 | ````` ¿🦧? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 108: ````` <0xA7> ````` |
|        958 | ````` ¿📛? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 257: ````` <0x9B> `````                  |
|        399 | ````` ¿✖? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 252: ````` <0x96> `````                         |
|        601 | ````` ¿🍮? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 114: ````` <0xAE> ````` |
|        853 | ````` ¿👲? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 118: ````` <0xB2> `````                  |
|       1359 | ````` ¿🤬? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 113: ````` <0xAC> ````` |
|       1025 | ````` ¿🔟? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 261: ````` <0x9F> `````                  |
|        454 | ````` ¿🇨? `````          | -1.19209e-07 | 62600: ````` 🇨 `````                                                             |
|       1658 | ````` ¿\U000e0063? ````` | -1.19209e-07 | 202213: ````` \U000e0063 `````                                                   |
|       1493 | ````` ¿🦴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 120: ````` <0xB4> ````` |
|       1377 | ````` ¿🤿? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 131: ````` <0xBF> ````` |
|        313 | ````` ¿☕? `````         | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 251: ````` <0x95> `````                         |
|        376 | ````` ¿⛪? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 111: ````` <0xAA> `````        |
|        388 | ````` ¿✂? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 232: ````` <0x82> `````                         |
|        414 | ````` ¿❤? `````          | -1.19209e-07 | 135523: ````` <0xE2><0x9D> `````, 105: ````` <0xA4> `````                        |
|        457 | ````` ¿🇫? `````          | -1.19209e-07 | 106104: ````` 🇫 `````                                                            |
|        675 | ````` ¿🎽? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 129: ````` <0xBD> ````` |
|       1334 | ````` ¿🤓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 249: ````` <0x93> ````` |
|        572 | ````` ¿🍑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 247: ````` <0x91> ````` |
|        975 | ````` ¿📬? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 113: ````` <0xAC> `````                  |
|       1504 | ````` ¿🦿? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 131: ````` <0xBF> ````` |
|        568 | ````` ¿🍍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 243: ````` <0x8D> ````` |
|       1229 | ````` ¿🚓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 249: ````` <0x93> ````` |
|        996 | ````` ¿🔂? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 232: ````` <0x82> `````                  |
|       1421 | ````` ¿🥬? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 178448: ````` <0xA5><0xAC> `````                 |
|        585 | ````` ¿🍞? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 260: ````` <0x9E> ````` |
|       1206 | ````` ¿🙌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 242: ````` <0x8C> ````` |
|        715 | ````` ¿🏥? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 106: ````` <0xA5> `````                  |
|        394 | ````` ¿✌? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 242: ````` <0x8C> `````                         |
|       1577 | ````` ¿\U0001fa7b? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 127: ````` <0xBB> ````` |
|       1155 | ````` ¿😙? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 255: ````` <0x99> `````                  |
|        550 | ````` ¿🌻? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 127: ````` <0xBB> ````` |
|       1266 | ````` ¿🚸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 124: ````` <0xB8> ````` |
|        499 | ````` ¿🌆? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 236: ````` <0x86> ````` |
|       1258 | ````` ¿🚰? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 116: ````` <0xB0> ````` |
|        758 | ````` ¿🐓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 249: ````` <0x93> ````` |
|        561 | ````` ¿🍆? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 236: ````` <0x86> ````` |
|        616 | ````` ¿🍽? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 129: ````` <0xBD> ````` |
|       1640 | ````` ¿\U0001fad8? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 254: ````` <0x98> ````` |
|        793 | ````` ¿🐶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 122: ````` <0xB6> ````` |
|       1571 | ````` ¿🩲? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 118: ````` <0xB2> ````` |
|        491 | ````` ¿🉐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 239: ````` <0x89> `````, 246: ````` <0x90> ````` |
|       1639 | ````` ¿\U0001fad7? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 253: ````` <0x97> ````` |
|       1479 | ````` ¿🦦? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 107: ````` <0xA6> ````` |
|        409 | ````` ¿❓? `````         | -1.19209e-07 | 135523: ````` <0xE2><0x9D> `````, 249: ````` <0x93> `````                        |
|       1393 | ````` ¿🥐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 61365: ````` <0xA5><0x90> `````                  |
|        463 | ````` ¿🇱? `````          | -1.19209e-07 | 24385: ````` 🇱 `````                                                             |
|       1528 | ````` ¿🧗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 253: ````` <0x97> ````` |
|       1089 | ````` ¿🕴? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 120: ````` <0xB4> ````` |
|       1017 | ````` ¿🔗? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 253: ````` <0x97> `````                  |
|        306 | ````` ¿☁? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 231: ````` <0x81> `````                         |
|        898 | ````` ¿💟? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 261: ````` <0x9F> `````                  |
|        993 | ````` ¿📿? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 131: ````` <0xBF> `````                  |
|       1271 | ````` ¿🚽? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 129: ````` <0xBD> ````` |
|       1318 | ````` ¿🟤? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 105: ````` <0xA4> ````` |
|       1240 | ````` ¿🚞? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 260: ````` <0x9E> ````` |
|        310 | ````` ¿☎? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 244: ````` <0x8E> `````                         |
|       1513 | ````` ¿🧈? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 238: ````` <0x88> ````` |
|       1472 | ````` ¿🦟? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 261: ````` <0x9F> ````` |
|        638 | ````` ¿🎓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 249: ````` <0x93> ````` |
|        401 | ````` ¿✡? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 102: ````` <0xA1> `````                         |
|       1410 | ````` ¿🥡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 102: ````` <0xA1> ````` |
|        881 | ````` ¿💎? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 244: ````` <0x8E> `````                  |
|       1275 | ````` ¿🛁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 231: ````` <0x81> ````` |
|        813 | ````` ¿👊? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 240: ````` <0x8A> `````                  |
|       1488 | ````` ¿🦯? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 115: ````` <0xAF> ````` |
|        716 | ````` ¿🏦? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 107: ````` <0xA6> `````                  |
|        452 | ````` ¿🇦? `````          | -1.19209e-07 | 21170: ````` 🇦 `````                                                             |
|        497 | ````` ¿🌄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 234: ````` <0x84> ````` |
|        845 | ````` ¿👪? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 111: ````` <0xAA> `````                  |
|       1260 | ````` ¿🚲? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 118: ````` <0xB2> ````` |
|       1506 | ````` ¿🧁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 231: ````` <0x81> ````` |
|        500 | ````` ¿🌇? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 237: ````` <0x87> ````` |
|       1039 | ````` ¿🔭? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 263: ````` <0xAD> `````                  |
|       1042 | ````` ¿🔰? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 116: ````` <0xB0> `````                  |
|        349 | ````` ¿⚒? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 248: ````` <0x92> `````                        |
|        269 | ````` ¿ℹ? `````          | -1.19209e-07 | 27829: ````` <0xE2><0x84> `````, 125: ````` <0xB9> `````                         |
|        635 | ````` ¿🎐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 246: ````` <0x90> ````` |
|        374 | ````` ¿⛔? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 250: ````` <0x94> `````        |
|        397 | ````` ¿✒? `````          | -1.19209e-07 | 70336: ````` <0xE2><0x9C> `````, 248: ````` <0x92> `````                         |
|        287 | ````` ¿⏮? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 114: ````` <0xAE> `````        |
|       1512 | ````` ¿🧇? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 237: ````` <0x87> ````` |
|       1557 | ````` ¿🧴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 120: ````` <0xB4> ````` |
|        365 | ````` ¿⚽? `````         | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 129: ````` <0xBD> `````                        |
|       1181 | ````` ¿😳? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 119: ````` <0xB3> `````                  |
|       1603 | ````` ¿🪡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 102: ````` <0xA1> ````` |
|       1595 | ````` ¿🪙? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 255: ````` <0x99> ````` |
|        302 | ````` ¿◼? `````          | -1.19209e-07 | 37357: ````` <0xE2><0x97> `````, 128: ````` <0xBC> `````                         |
|        696 | ````` ¿🏒? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 248: ````` <0x92> `````                  |
|        352 | ````` ¿⚕? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 251: ````` <0x95> `````                        |
|       1257 | ````` ¿🚯? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 115: ````` <0xAF> ````` |
|        427 | ````` ¿⬜? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 113: ````` <0xAC> `````, 258: ````` <0x9C> `````        |
|        809 | ````` ¿👆? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 236: ````` <0x86> `````                  |
|        575 | ````` ¿🍔? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 250: ````` <0x94> ````` |
|       1210 | ````` ¿🚀? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 230: ````` <0x80> ````` |
|       1276 | ````` ¿🛂? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 232: ````` <0x82> ````` |
|       1412 | ````` ¿🥣? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 104: ````` <0xA3> ````` |
|        705 | ````` ¿🏛? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 257: ````` <0x9B> `````                  |
|       1225 | ````` ¿🚏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 245: ````` <0x8F> ````` |
|        734 | ````` ¿🏻? `````           | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 127: ````` <0xBB> `````                  |
|       1125 | ````` ¿🗻? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 253: ````` <0x97> `````, 127: ````` <0xBB> ````` |
|       1647 | ````` ¿\U0001fae5? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 106: ````` <0xA5> ````` |
|        960 | ````` ¿📝? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 259: ````` <0x9D> `````                  |
|        709 | ````` ¿🏟? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 261: ````` <0x9F> `````                  |
|        503 | ````` ¿🌊? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 240: ````` <0x8A> ````` |
|       1495 | ````` ¿🦶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 122: ````` <0xB6> ````` |
|       1142 | ````` ¿😌? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 242: ````` <0x8C> `````                  |
|       1470 | ````` ¿🦝? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 259: ````` <0x9D> ````` |
|       1598 | ````` ¿🪜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 258: ````` <0x9C> ````` |
|       1464 | ````` ¿🦗? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 253: ````` <0x97> ````` |
|        923 | ````` ¿💸? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 124: ````` <0xB8> `````                  |
|       1660 | ````` ¿\U000e0067? ````` | -1.19209e-07 | 3330: ````` <0xF3><0xA0><0x81> `````, 108: ````` <0xA7> `````                    |
|       1083 | ````` ¿🕥? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 106: ````` <0xA5> ````` |
|        364 | ````` ¿⚱? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 117: ````` <0xB1> `````                        |
|        984 | ````` ¿📵? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 121: ````` <0xB5> `````                  |
|        997 | ````` ¿🔃? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 233: ````` <0x83> `````                  |
|        886 | ````` ¿💓? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 249: ````` <0x93> `````                  |
|       1463 | ````` ¿🦖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 252: ````` <0x96> ````` |
|       1434 | ````` ¿\U0001f979? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 125: ````` <0xB9> ````` |
|       1027 | ````` ¿🔡? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 102: ````` <0xA1> `````                  |
|       1442 | ````` ¿🦁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 231: ````` <0x81> ````` |
|       1449 | ````` ¿🦈? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 238: ````` <0x88> ````` |
|       1586 | ````` ¿🪐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 246: ````` <0x90> ````` |
|        924 | ````` ¿💹? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 125: ````` <0xB9> `````                  |
|       1432 | ````` ¿🥷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 123: ````` <0xB7> ````` |
|        293 | ````` ¿⏸? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 124: ````` <0xB8> `````        |
|       1285 | ````` ¿🛐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 246: ````` <0x90> ````` |
|       1452 | ````` ¿🦋? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 241: ````` <0x8B> ````` |
|        999 | ````` ¿🔅? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 235: ````` <0x85> `````                  |
|       1405 | ````` ¿🥜? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 258: ````` <0x9C> ````` |
|       1604 | ````` ¿🪢? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 103: ````` <0xA2> ````` |
|        816 | ````` ¿👍? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 243: ````` <0x8D> `````                  |
|        308 | ````` ¿☃? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 233: ````` <0x83> `````                         |
|       1295 | ````` ¿🛡? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 102: ````` <0xA1> ````` |
|        363 | ````` ¿⚰? `````          | -1.19209e-07 | 175142: ````` <0xE2><0x9A> `````, 116: ````` <0xB0> `````                        |
|       1548 | ````` ¿🧫? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 112: ````` <0xAB> ````` |
|       1277 | ````` ¿🛃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 233: ````` <0x83> ````` |
|        520 | ````` ¿🌛? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 257: ````` <0x9B> ````` |
|        694 | ````` ¿🏐? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 246: ````` <0x90> `````                  |
|        506 | ````` ¿🌍? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 243: ````` <0x8D> ````` |
|       1237 | ````` ¿🚛? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 257: ````` <0x9B> ````` |
|       1433 | ````` ¿🥸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 124: ````` <0xB8> ````` |
|        317 | ````` ¿☢? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 103: ````` <0xA2> `````                         |
|       1147 | ````` ¿😑? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 247: ````` <0x91> `````                  |
|        879 | ````` ¿💌? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 242: ````` <0x8C> `````                  |
|       1644 | ````` ¿\U0001fae2? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 103: ````` <0xA2> ````` |
|        896 | ````` ¿💝? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 259: ````` <0x9D> `````                  |
|        300 | ````` ¿◀? `````          | -1.19209e-07 | 37357: ````` <0xE2><0x97> `````, 230: ````` <0x80> `````                         |
|       1514 | ````` ¿🧉? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 239: ````` <0x89> ````` |
|        519 | ````` ¿🌚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 256: ````` <0x9A> ````` |
|        507 | ````` ¿🌎? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 242: ````` <0x8C> `````, 244: ````` <0x8E> ````` |
|       1246 | ````` ¿🚤? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 105: ````` <0xA4> ````` |
|        792 | ````` ¿🐵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 121: ````` <0xB5> ````` |
|        990 | ````` ¿📻? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 127: ````` <0xBB> `````                  |
|       1413 | ````` ¿🥤? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 105: ````` <0xA4> ````` |
|       1226 | ````` ¿🚐? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 246: ````` <0x90> ````` |
|       1520 | ````` ¿🧏? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 245: ````` <0x8F> ````` |
|        808 | ````` ¿👅? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 235: ````` <0x85> `````                  |
|       1620 | ````` ¿🪵? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 121: ````` <0xB5> ````` |
|       1287 | ````` ¿🛒? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 248: ````` <0x92> ````` |
|       1065 | ````` ¿🕓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 249: ````` <0x93> ````` |
|        685 | ````` ¿🏇? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 237: ````` <0x87> `````                  |
|        628 | ````` ¿🎉? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 239: ````` <0x89> ````` |
|       1511 | ````` ¿🧆? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 236: ````` <0x86> ````` |
|        314 | ````` ¿☘? `````          | -1.19209e-07 | 34133: ````` <0xE2><0x98> `````, 254: ````` <0x98> `````                         |
|        968 | ````` ¿📥? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 106: ````` <0xA5> `````                  |
|       1621 | ````` ¿🪶? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 122: ````` <0xB6> ````` |
|        925 | ````` ¿💺? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 126: ````` <0xBA> `````                  |
|        492 | ````` ¿🉑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 239: ````` <0x89> `````, 247: ````` <0x91> ````` |
|       1215 | ````` ¿🚅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 235: ````` <0x85> ````` |
|       1188 | ````` ¿😺? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 126: ````` <0xBA> `````                  |
|       1565 | ````` ¿🧼? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 128: ````` <0xBC> ````` |
|        803 | ````` ¿👀? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 230: ````` <0x80> `````                  |
|        423 | ````` ¿⬅? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 113: ````` <0xAC> `````, 235: ````` <0x85> `````        |
|        883 | ````` ¿💐? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 246: ````` <0x90> `````                  |
|        811 | ````` ¿👈? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 238: ````` <0x88> `````                  |
|       1262 | ````` ¿🚴? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 120: ````` <0xB4> ````` |
|       1043 | ````` ¿🔱? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 117: ````` <0xB1> `````                  |
|       1471 | ````` ¿🦞? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 260: ````` <0x9E> ````` |
|        453 | ````` ¿🇧? `````          | -1.19209e-07 | 90978: ````` 🇧 `````                                                             |
|       1453 | ````` ¿🦌? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 242: ````` <0x8C> ````` |
|       1183 | ````` ¿😵? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 121: ````` <0xB5> `````                  |
|       1022 | ````` ¿🔜? `````         | -1.19209e-07 | 205860: ````` <0xF0><0x9F><0x94> `````, 258: ````` <0x9C> `````                  |
|       1435 | ````` ¿🥺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 126: ````` <0xBA> ````` |
|        788 | ````` ¿🐱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 117: ````` <0xB1> ````` |
|        610 | ````` ¿🍷? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 123: ````` <0xB7> ````` |
|       1582 | ````` ¿🪃? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 233: ````` <0x83> ````` |
|       1376 | ````` ¿🤾? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 130: ````` <0xBE> ````` |
|        824 | ````` ¿👕? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 251: ````` <0x95> `````                  |
|        732 | ````` ¿🏹? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 125: ````` <0xB9> `````                  |
|       1625 | ````` ¿\U0001faba? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 126: ````` <0xBA> ````` |
|        772 | ````` ¿🐡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 102: ````` <0xA1> ````` |
|       1189 | ````` ¿😻? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 127: ````` <0xBB> `````                  |
|       1642 | ````` ¿\U0001fae0? ````` | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 262: ````` <0xA0> ````` |
|        592 | ````` ¿🍥? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 243: ````` <0x8D> `````, 106: ````` <0xA5> ````` |
|        804 | ````` ¿👁? `````          | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 231: ````` <0x81> `````                  |
|        955 | ````` ¿📘? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 254: ````` <0x98> `````                  |
|       1490 | ````` ¿🦱? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 117: ````` <0xB1> ````` |
|       1492 | ````` ¿🦳? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 119: ````` <0xB3> ````` |
|        433 | ````` ¿㊙? `````         | -1.19209e-07 | 167: ````` <0xE3> `````, 240: ````` <0x8A> `````, 255: ````` <0x99> `````        |
|        435 | ````` ¿🀄? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 230: ````` <0x80> `````, 234: ````` <0x84> ````` |
|        884 | ````` ¿💑? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 247: ````` <0x91> `````                  |
|       1093 | ````` ¿🕸? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 251: ````` <0x95> `````, 124: ````` <0xB8> ````` |
|        706 | ````` ¿🏜? `````          | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 258: ````` <0x9C> `````                  |
|       1243 | ````` ¿🚡? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 102: ````` <0xA1> ````` |
|        636 | ````` ¿🎑? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 247: ````` <0x91> ````` |
|        420 | ````` ¿➿? `````         | -1.19209e-07 | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 131: ````` <0xBF> `````        |
|       1607 | ````` ¿🪥? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 106: ````` <0xA5> ````` |
|       1497 | ````` ¿🦸? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 124: ````` <0xB8> ````` |
|       1109 | ````` ¿🖼? `````          | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 252: ````` <0x96> `````, 128: ````` <0xBC> ````` |
|        347 | ````` ¿♾? `````          | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 130: ````` <0xBE> `````                         |
|        654 | ````` ¿🎨? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 109: ````` <0xA8> ````` |
|        384 | ````` ¿⛸? `````          | -1.19209e-07 | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 124: ````` <0xB8> `````        |
|        936 | ````` ¿📅? `````         | -1.19209e-07 | 185981: ````` <0xF0><0x9F><0x93> `````, 235: ````` <0x85> `````                  |
|        446 | ````` ¿🆕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 236: ````` <0x86> `````, 251: ````` <0x95> ````` |
|        848 | ````` ¿👭? `````         | -1.19209e-07 | 154565: ````` <0xF0><0x9F><0x91> `````, 263: ````` <0xAD> `````                  |
|        731 | ````` ¿🏸? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 124: ````` <0xB8> `````                  |
|        686 | ````` ¿🏈? `````         | -1.19209e-07 | 216125: ````` <0xF0><0x9F><0x8F> `````, 238: ````` <0x88> `````                  |
|       1448 | ````` ¿🦇? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 237: ````` <0x87> ````` |
|       1191 | ````` ¿😽? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 129: ````` <0xBD> `````                  |
|        335 | ````` ¿♏? `````         | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 245: ````` <0x8F> `````                         |
|       1336 | ````` ¿🤕? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 251: ````` <0x95> ````` |
|       1337 | ````` ¿🤖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 252: ````` <0x96> ````` |
|       1399 | ````` ¿🥖? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 252: ````` <0x96> ````` |
|        882 | ````` ¿💏? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 245: ````` <0x8F> `````                  |
|       1161 | ````` ¿😟? `````         | -1.19209e-07 | 188568: ````` <0xF0><0x9F><0x98> `````, 261: ````` <0x9F> `````                  |
|        345 | ````` ¿♨? `````          | -1.19209e-07 | 45687: ````` <0xE2><0x99> `````, 109: ````` <0xA8> `````                         |
|        797 | ````` ¿🐺? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 126: ````` <0xBA> ````` |
|        916 | ````` ¿💱? `````         | -1.19209e-07 | 106024: ````` <0xF0><0x9F><0x92> `````, 117: ````` <0xB1> `````                  |
|       1584 | ````` ¿🪅? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 235: ````` <0x85> ````` |
|       1379 | ````` ¿🥁? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 231: ````` <0x81> ````` |
|       1531 | ````` ¿🧚? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 256: ````` <0x9A> ````` |
|       1396 | ````` ¿🥓? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 249: ````` <0x93> ````` |
|        750 | ````` ¿🐋? `````         | -1.19209e-07 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 241: ````` <0x8B> ````` |
|        436 | ````` ¿🃏? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 233: ````` <0x83> `````, 245: ````` <0x8F> ````` |
|        274 | ````` ¿↘? `````          |  0           | 76876: ````` <0xE2><0x86> `````, 254: ````` <0x98> `````                         |
|        285 | ````` ¿⏬? `````         |  0           | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 113: ````` <0xAC> `````        |
|       1614 | ````` ¿\U0001faac? ````` |  0           | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 113: ````` <0xAC> ````` |
|        956 | ````` ¿📙? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 255: ````` <0x99> `````                  |
|        276 | ````` ¿↩? `````          |  0           | 76876: ````` <0xE2><0x86> `````, 110: ````` <0xA9> `````                         |
|       1535 | ````` ¿🧞? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 260: ````` <0x9E> ````` |
|       1324 | ````` ¿🟪? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 111: ````` <0xAA> ````` |
|       1357 | ````` ¿🤪? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 111: ````` <0xAA> ````` |
|        979 | ````` ¿📰? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 22231: ````` <0x93><0xB0> `````                  |
|        458 | ````` ¿🇬? `````          |  0           | 42828: ````` 🇬 `````                                                             |
|       1169 | ````` ¿😧? `````         |  0           | 188568: ````` <0xF0><0x9F><0x98> `````, 108: ````` <0xA7> `````                  |
|        832 | ````` ¿👝? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 259: ````` <0x9D> `````                  |
|        761 | ````` ¿🐖? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 252: ````` <0x96> ````` |
|       1267 | ````` ¿🚹? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 125: ````` <0xB9> ````` |
|       1300 | ````` ¿🛩? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 110: ````` <0xA9> ````` |
|       1507 | ````` ¿🧂? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 232: ````` <0x82> ````` |
|       1487 | ````` ¿🦮? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 114: ````` <0xAE> ````` |
|       1610 | ````` ¿🪨? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 109: ````` <0xA8> ````` |
|       1496 | ````` ¿🦷? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 123: ````` <0xB7> ````` |
|        736 | ````` ¿🏽? `````           |  0           | 216125: ````` <0xF0><0x9F><0x8F> `````, 129: ````` <0xBD> `````                  |
|        749 | ````` ¿🐊? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 240: ````` <0x8A> ````` |
|        767 | ````` ¿🐜? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 258: ````` <0x9C> ````` |
|        861 | ````` ¿👺? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 126: ````` <0xBA> `````                  |
|        885 | ````` ¿💒? `````         |  0           | 106024: ````` <0xF0><0x9F><0x92> `````, 248: ````` <0x92> `````                  |
|        386 | ````` ¿⛺? `````         |  0           | 166: ````` <0xE2> `````, 257: ````` <0x9B> `````, 126: ````` <0xBA> `````        |
|        948 | ````` ¿📑? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 247: ````` <0x91> `````                  |
|       1325 | ````` ¿🟫? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 112: ````` <0xAB> ````` |
|        891 | ````` ¿💘? `````         |  0           | 106024: ````` <0xF0><0x9F><0x92> `````, 254: ````` <0x98> `````                  |
|        983 | ````` ¿📴? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 120: ````` <0xB4> `````                  |
|       1618 | ````` ¿🪳? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 119: ````` <0xB3> ````` |
|        779 | ````` ¿🐨? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 109: ````` <0xA8> ````` |
|        775 | ````` ¿🐤? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 105: ````` <0xA4> ````` |
|       1543 | ````` ¿🧦? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 107: ````` <0xA6> ````` |
|        331 | ````` ¿♋? `````         |  0           | 45687: ````` <0xE2><0x99> `````, 241: ````` <0x8B> `````                         |
|       1308 | ````` ¿🛷? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 123: ````` <0xB7> ````` |
|       1314 | ````` ¿🟠? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 262: ````` <0xA0> ````` |
|        297 | ````` ¿▪? `````          |  0           | 237072: ````` ▪ `````                                                            |
|        812 | ````` ¿👉? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 239: ````` <0x89> `````                  |
|        279 | ````` ¿⌛? `````         |  0           | 166: ````` <0xE2> `````, 242: ````` <0x8C> `````, 257: ````` <0x9B> `````        |
|       1290 | ````` ¿🛗? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 253: ````` <0x97> ````` |
|        739 | ````` ¿🐀? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 230: ````` <0x80> ````` |
|       1615 | ````` ¿🪰? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 116: ````` <0xB0> ````` |
|        786 | ````` ¿🐯? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 115: ````` <0xAF> ````` |
|       1416 | ````` ¿🥧? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 108: ````` <0xA7> ````` |
|       1395 | ````` ¿🥒? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 248: ````` <0x92> ````` |
|       1000 | ````` ¿🔆? `````         |  0           | 205860: ````` <0xF0><0x9F><0x94> `````, 236: ````` <0x86> `````                  |
|       1294 | ````` ¿🛠? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 262: ````` <0xA0> ````` |
|       1352 | ````` ¿🤥? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 106: ````` <0xA5> ````` |
|        737 | ````` ¿🏾? `````           |  0           | 216125: ````` <0xF0><0x9F><0x8F> `````, 130: ````` <0xBE> `````                  |
|        988 | ````` ¿📹? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 125: ````` <0xB9> `````                  |
|       1310 | ````` ¿🛹? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 125: ````` <0xB9> ````` |
|        361 | ````` ¿⚪? `````         |  0           | 175142: ````` <0xE2><0x9A> `````, 111: ````` <0xAA> `````                        |
|        807 | ````` ¿👄? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 234: ````` <0x84> `````                  |
|       1326 | ````` ¿\U0001f7f0? ````` |  0           | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 116: ````` <0xB0> ````` |
|       1304 | ````` ¿🛳? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 119: ````` <0xB3> ````` |
|       1179 | ````` ¿😱? `````         |  0           | 188568: ````` <0xF0><0x9F><0x98> `````, 117: ````` <0xB1> `````                  |
|        839 | ````` ¿👤? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 105: ````` <0xA4> `````                  |
|        746 | ````` ¿🐇? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 237: ````` <0x87> ````` |
|        316 | ````` ¿☠? `````          |  0           | 34133: ````` <0xE2><0x98> `````, 262: ````` <0xA0> `````                         |
|        972 | ````` ¿📩? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 110: ````` <0xA9> `````                  |
|       1485 | ````` ¿🦬? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 113: ````` <0xAC> ````` |
|       1015 | ````` ¿🔕? `````         |  0           | 205860: ````` <0xF0><0x9F><0x94> `````, 251: ````` <0x95> `````                  |
|       1320 | ````` ¿🟦? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 107: ````` <0xA6> ````` |
|       1316 | ````` ¿🟢? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 103: ````` <0xA2> ````` |
|       1645 | ````` ¿\U0001fae3? ````` |  0           | 2226: ````` <0xF0><0x9F> `````, 112: ````` <0xAB> `````, 104: ````` <0xA3> ````` |
|       1375 | ````` ¿🤽? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 129: ````` <0xBD> ````` |
|       1589 | ````` ¿🪓? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 249: ````` <0x93> ````` |
|        357 | ````` ¿⚜? `````          |  0           | 175142: ````` <0xE2><0x9A> `````, 258: ````` <0x9C> `````                        |
|        322 | ````` ¿☯? `````          |  0           | 34133: ````` <0xE2><0x98> `````, 115: ````` <0xAF> `````                         |
|        294 | ````` ¿⏹? `````          |  0           | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 125: ````` <0xB9> `````        |
|        764 | ````` ¿🐙? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 255: ````` <0x99> ````` |
|        323 | ````` ¿☸? `````          |  0           | 34133: ````` <0xE2><0x98> `````, 124: ````` <0xB8> `````                         |
|       1293 | ````` ¿\U0001f6df? ````` |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 261: ````` <0x9F> ````` |
|        783 | ````` ¿🐬? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 113: ````` <0xAC> ````` |
|        321 | ````` ¿☮? `````          |  0           | 34133: ````` <0xE2><0x98> `````, 114: ````` <0xAE> `````                         |
|       1269 | ````` ¿🚻? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 127: ````` <0xBB> ````` |
|       1474 | ````` ¿🦡? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 102: ````` <0xA1> ````` |
|        833 | ````` ¿👞? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 260: ````` <0x9E> `````                  |
|        888 | ````` ¿💕? `````         |  0           | 106024: ````` <0xF0><0x9F><0x92> `````, 251: ````` <0x95> `````                  |
|       1408 | ````` ¿🥟? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 261: ````` <0x9F> ````` |
|        303 | ````` ¿◽? `````         |  0           | 37357: ````` <0xE2><0x97> `````, 129: ````` <0xBD> `````                         |
|       1523 | ````` ¿🧒? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 248: ````` <0x92> ````` |
|        741 | ````` ¿🐂? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 232: ````` <0x82> ````` |
|        426 | ````` ¿⬛? `````         |  0           | 166: ````` <0xE2> `````, 113: ````` <0xAC> `````, 257: ````` <0x9B> `````        |
|       1362 | ````` ¿🤯? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 115: ````` <0xAF> ````` |
|        802 | ````` ¿🐿? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 131: ````` <0xBF> ````` |
|        400 | ````` ¿✝? `````          |  0           | 70336: ````` <0xE2><0x9C> `````, 259: ````` <0x9D> `````                         |
|        763 | ````` ¿🐘? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 254: ````` <0x98> ````` |
|        467 | ````` ¿🇵? `````          |  0           | 137446: ````` 🇵 `````                                                            |
|        350 | ````` ¿⚓? `````         |  0           | 175142: ````` <0xE2><0x9A> `````, 249: ````` <0x93> `````                        |
|       1280 | ````` ¿🛋? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 241: ````` <0x8B> ````` |
|        762 | ````` ¿🐗? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 253: ````` <0x97> ````` |
|       1519 | ````` ¿🧎? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 244: ````` <0x8E> ````` |
|        341 | ````` ¿♠? `````          |  0           | 45687: ````` <0xE2><0x99> `````, 262: ````` <0xA0> `````                         |
|        472 | ````` ¿🇺? `````          |  0           | 9554: ````` 🇺 `````                                                              |
|       1313 | ````` ¿🛼? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 128: ````` <0xBC> ````` |
|       1574 | ````` ¿🩸? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 110: ````` <0xA9> `````, 124: ````` <0xB8> ````` |
|        843 | ````` ¿👨? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 109: ````` <0xA8> `````                  |
|        266 | ````` ¿⁉? `````          |  0           | 36937: ````` <0xE2><0x81> `````, 239: ````` <0x89> `````                         |
|       1311 | ````` ¿🛺? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 126: ````` <0xBA> ````` |
|        742 | ````` ¿🐃? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 233: ````` <0x83> ````` |
|        437 | ````` ¿🅰? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 235: ````` <0x85> `````, 116: ````` <0xB0> ````` |
|       1478 | ````` ¿🦥? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 107: ````` <0xA6> `````, 106: ````` <0xA5> ````` |
|       1281 | ````` ¿🛌? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 242: ````` <0x8C> ````` |
|       1298 | ````` ¿🛤? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 105: ````` <0xA4> ````` |
|       1322 | ````` ¿🟨? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 109: ````` <0xA8> ````` |
|        328 | ````` ¿♈? `````         |  0           | 45687: ````` <0xE2><0x99> `````, 238: ````` <0x88> `````                         |
|       1301 | ````` ¿🛫? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 112: ````` <0xAB> ````` |
|       1323 | ````` ¿🟩? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 110: ````` <0xA9> ````` |
|        667 | ````` ¿🎵? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 121: ````` <0xB5> ````` |
|        770 | ````` ¿🐟? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 261: ````` <0x9F> ````` |
|        789 | ````` ¿🐲? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 118: ````` <0xB2> ````` |
|        468 | ````` ¿🇶? `````          |  0           | 144576: ````` 🇶 `````                                                            |
|        415 | ````` ¿➕? `````         |  0           | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 251: ````` <0x95> `````        |
|        619 | ````` ¿🎀? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 230: ````` <0x80> ````` |
|       1291 | ````` ¿\U0001f6dd? ````` |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 259: ````` <0x9D> ````` |
|       1349 | ````` ¿🤢? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 103: ````` <0xA2> ````` |
|        740 | ````` ¿🐁? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 245332: ````` <0x90><0x81> `````                 |
|        319 | ````` ¿☦? `````          |  0           | 34133: ````` <0xE2><0x98> `````, 107: ````` <0xA6> `````                         |
|        359 | ````` ¿⚡? `````         |  0           | 175142: ````` <0xE2><0x9A> `````, 102: ````` <0xA1> `````                        |
|        795 | ````` ¿🐸? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 124: ````` <0xB8> ````` |
|        738 | ````` ¿🏿? `````           |  0           | 216125: ````` <0xF0><0x9F><0x8F> `````, 131: ````` <0xBF> `````                  |
|        408 | ````` ¿❎? `````         |  0           | 135523: ````` <0xE2><0x9D> `````, 244: ````` <0x8E> `````                        |
|        278 | ````` ¿⌚? `````         |  0           | 166: ````` <0xE2> `````, 242: ````` <0x8C> `````, 256: ````` <0x9A> `````        |
|       1545 | ````` ¿🧨? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 109: ````` <0xA8> ````` |
|        787 | ````` ¿🐰? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 116: ````` <0xB0> ````` |
|        782 | ````` ¿🐫? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 112: ````` <0xAB> ````` |
|        292 | ````` ¿⏳? `````         |  0           | 166: ````` <0xE2> `````, 245: ````` <0x8F> `````, 119: ````` <0xB3> `````        |
|       1339 | ````` ¿🤘? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 254: ````` <0x98> ````` |
|        728 | ````` ¿🏴? `````         |  0           | 148987: ````` 🏴 `````                                                           |
|       1296 | ````` ¿🛢? `````          |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 103: ````` <0xA2> ````` |
|        270 | ````` ¿↔? `````          |  0           | 76876: ````` <0xE2><0x86> `````, 250: ````` <0x94> `````                         |
|        743 | ````` ¿🐄? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 234: ````` <0x84> ````` |
|        747 | ````` ¿🐈? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 238: ````` <0x88> ````` |
|        834 | ````` ¿👟? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 261: ````` <0x9F> `````                  |
|        417 | ````` ¿➗? `````         |  0           | 166: ````` <0xE2> `````, 260: ````` <0x9E> `````, 253: ````` <0x97> `````        |
|        989 | ````` ¿📺? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 126: ````` <0xBA> `````                  |
|        748 | ````` ¿🐉? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 239: ````` <0x89> ````` |
|       1537 | ````` ¿🧠? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 108: ````` <0xA7> `````, 262: ````` <0xA0> ````` |
|        820 | ````` ¿👑? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 247: ````` <0x91> `````                  |
|        794 | ````` ¿🐷? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 123: ````` <0xB7> ````` |
|        312 | ````` ¿☔? `````         |  0           | 34133: ````` <0xE2><0x98> `````, 250: ````` <0x94> `````                         |
|       1306 | ````` ¿🛵? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 121: ````` <0xB5> ````` |
|        751 | ````` ¿🐌? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 242: ````` <0x8C> ````` |
|       1403 | ````` ¿🥚? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 256: ````` <0x9A> ````` |
|        280 | ````` ¿⌨? `````          |  0           | 166: ````` <0xE2> `````, 242: ````` <0x8C> `````, 109: ````` <0xA8> `````        |
|       1272 | ````` ¿🚾? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 256: ````` <0x9A> `````, 130: ````` <0xBE> ````` |
|       1346 | ````` ¿🤟? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 261: ````` <0x9F> ````` |
|        729 | ````` ¿🏵? `````          |  0           | 216125: ````` <0xF0><0x9F><0x8F> `````, 121: ````` <0xB5> `````                  |
|        766 | ````` ¿🐛? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 257: ````` <0x9B> ````` |
|       1195 | ````` ¿🙁? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 255: ````` <0x99> `````, 231: ````` <0x81> ````` |
|       1665 | ````` ¿\U000e0077? ````` |  0           | 3330: ````` <0xF3><0xA0><0x81> `````, 123: ````` <0xB7> `````                    |
|        337 | ````` ¿♑? `````         |  0           | 45687: ````` <0xE2><0x99> `````, 247: ````` <0x91> `````                         |
|        777 | ````` ¿🐦? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 107: ````` <0xA6> ````` |
|        664 | ````` ¿🎲? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 244: ````` <0x8E> `````, 118: ````` <0xB2> ````` |
|       1398 | ````` ¿🥕? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 251: ````` <0x95> ````` |
|        466 | ````` ¿🇴? `````          |  0           | 40228: ````` 🇴 `````                                                             |
|        268 | ````` ¿™? `````          |  0           | 33572: ````` ™ `````                                                             |
|        976 | ````` ¿📭? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 263: ````` <0xAD> `````                  |
|        954 | ````` ¿📗? `````         |  0           | 185981: ````` <0xF0><0x9F><0x93> `````, 253: ````` <0x97> `````                  |
|       1319 | ````` ¿🟥? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 261: ````` <0x9F> `````, 106: ````` <0xA5> ````` |
|        273 | ````` ¿↗? `````          |  0           | 76876: ````` <0xE2><0x86> `````, 253: ````` <0x97> `````                         |
|        755 | ````` ¿🐐? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 246: ````` <0x90> ````` |
|       1388 | ````` ¿🥋? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 241: ````` <0x8B> ````` |
|        422 | ````` ¿⤵? `````          |  0           | 166: ````` <0xE2> `````, 105: ````` <0xA4> `````, 121: ````` <0xB5> `````        |
|       1361 | ````` ¿🤮? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 114: ````` <0xAE> ````` |
|       1401 | ````` ¿🥘? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 254: ````` <0x98> ````` |
|       1384 | ````` ¿🥇? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 106: ````` <0xA5> `````, 237: ````` <0x87> ````` |
|        815 | ````` ¿👌? `````         |  0           | 154565: ````` <0xF0><0x9F><0x91> `````, 242: ````` <0x8C> `````                  |
|        407 | ````` ¿❌? `````         |  0           | 135523: ````` <0xE2><0x9D> `````, 242: ````` <0x8C> `````                        |
|       1333 | ````` ¿🤒? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 248: ````` <0x92> ````` |
|       1358 | ````` ¿🤫? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 112: ````` <0xAB> ````` |
|        464 | ````` ¿🇲? `````          |  0           | 62579: ````` 🇲 `````                                                             |
|       1354 | ````` ¿🤧? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 108: ````` <0xA7> ````` |
|       1623 | ````` ¿\U0001fab8? ````` |  0           | 2226: ````` <0xF0><0x9F> `````, 111: ````` <0xAA> `````, 124: ````` <0xB8> ````` |
|        311 | ````` ¿☑? `````          |  0           | 34133: ````` <0xE2><0x98> `````, 247: ````` <0x91> `````                         |
|        800 | ````` ¿🐽? `````         |  0           | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 129: ````` <0xBD> ````` |
|        326 | ````` ¿♀? `````          |  5.96046e-08 | 45687: ````` <0xE2><0x99> `````, 230: ````` <0x80> `````                         |
|        776 | ````` ¿🐥? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 106: ````` <0xA5> ````` |
|        265 | ````` ¿‼? `````          |  5.96046e-08 | 1773: ````` <0xE2><0x80> `````, 128: ````` <0xBC> `````                          |
|       1365 | ````` ¿🤲? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 105: ````` <0xA4> `````, 118: ````` <0xB2> ````` |
|        821 | ````` ¿👒? `````         |  5.96046e-08 | 154565: ````` <0xF0><0x9F><0x91> `````, 248: ````` <0x92> `````                  |
|        759 | ````` ¿🐔? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 250: ````` <0x94> ````` |
|        264 | ````` ¿\u200d? `````     |  5.96046e-08 | 35927: ````` \u200d `````                                                        |
|        267 | ````` ¿⃣? `````           |  5.96046e-08 | 166: ````` <0xE2> `````, 233: ````` <0x83> `````, 104: ````` <0xA3> `````        |
|        760 | ````` ¿🐕? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 251: ````` <0x95> ````` |
|        769 | ````` ¿🐞? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 260: ````` <0x9E> ````` |
|        774 | ````` ¿🐣? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 104: ````` <0xA3> ````` |
|       1312 | ````` ¿🛻? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 127: ````` <0xBB> ````` |
|       1305 | ````` ¿🛴? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 120: ````` <0xB4> ````` |
|       1309 | ````` ¿🛸? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 124: ````` <0xB8> ````` |
|        430 | ````` ¿〰? `````         |  5.96046e-08 | 1800: ````` <0xE3><0x80> `````, 116: ````` <0xB0> `````                          |
|        277 | ````` ¿↪? `````          |  5.96046e-08 | 76876: ````` <0xE2><0x86> `````, 111: ````` <0xAA> `````                         |
|       1302 | ````` ¿🛬? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 257: ````` <0x9B> `````, 113: ````` <0xAC> ````` |
|        768 | ````` ¿🐝? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 259: ````` <0x9D> ````` |
|        773 | ````` ¿🐢? `````         |  5.96046e-08 | 2226: ````` <0xF0><0x9F> `````, 246: ````` <0x90> `````, 103: ````` <0xA2> ````` |
</details>

