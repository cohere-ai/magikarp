# Report for `openai/gpt-oss-20b`

## Model info

* Model Info: 
  * Tied embeddings: False
  * LM head uses bias: False
  * Embeddings shape: [201088, 2880]
* Tokenizer Info: 
  * Vocab Size: 200019
  * Tokenizer Class: PreTrainedTokenizerFast
  * Tokenizer Type: BPE
  * Bytes handling: Byte Input
  * Token for verification prompt building: ABCDEFGHIJKLMNOPQRSTUVWXYZ
  * Token id for verification prompt building: 184150
* Indicator summary: 
  * Indicator for under-trained tokens: E_{in} L2 Norm
  * Overall distribution: 128.309 +/- 14.289
* Detected Token Counts: 
  * Number of tested under-trained tokens: 3969, 3966 non-special, 1346 below p = 0.01 threshold, 11 below soft indicator threshold
  * Number of single byte tokens: 256, of which 55 below indicator threshold
  * Number of special tokens: 21, of which 1 below indicator threshold
  * Number of non-single-byte unreachable tokens: 12, of which 0 below indicator threshold
  * Number of non-single-byte UTF-fragment tokens:  1434, of which 1 below soft indicator threshold

## Under-trained token indicators plot
![Indicators scatter plots](../indicators_pairplot_byid/openai_gpt_oss_20b.png)

## Verification plot
![Verification plot](../verifications_scatterplot/openai_gpt_oss_20b.png)

## Under-trained token verification results
11 entries below threshold of 96.582

|   token_id | token                 |   indicator | max_prob                                                        | in_other_tokens                                                                                                       |
|------------|-----------------------|-------------|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
|     193278 | ````` _REALTYPE ````` |     81.8549 | <span style='border: 1px solid rgb(251, 189, 8);'>0.023</span>  |                                                                                                                       |
|      15362 | ````` ▁Short `````    |     83.1738 | <span style='border: 1px solid rgb(255, 145, 0);'>0.0028</span> | ````` ▁Shorts `````, ````` ▁Shortly `````, ````` ▁Shortcut `````                                                      |
|     194425 | ````` /copyleft ````` |     92.8512 | <span style='border: 1px solid rgb(40, 167, 69);'>0.95</span>   |                                                                                                                       |
|     164424 | ````` /place `````    |     94.2154 | <span style='border: 1px solid rgb(40, 167, 69);'>0.4</span>    |                                                                                                                       |
|      66313 | ````` ѕ `````         |     94.2377 | <span style='border: 1px solid rgb(251, 189, 8);'>0.054</span>  |                                                                                                                       |
|     173853 | ````` .gstatic `````  |     95.2913 | <span style='border: 1px solid rgb(40, 167, 69);'>0.58</span>   |                                                                                                                       |
|     171423 | ````` ▁PMC `````      |     95.5809 | <span style='border: 1px solid rgb(40, 167, 69);'>0.26</span>   |                                                                                                                       |
|      33751 | ````` ấp `````        |     95.5988 | <span style='border: 1px solid rgb(40, 167, 69);'>0.86</span>   | ````` ▁cấp `````, ````` ▁hấp `````, ````` ▁thấp `````                                                                 |
|      51555 | ````` ắn `````        |     95.8954 | <span style='border: 1px solid rgb(40, 167, 69);'>0.11</span>   | ````` ▁hắn `````, ````` ắng `````, ````` ▁chắn `````, ````` ▁trắng `````, ````` ▁thắng `````                          |
|      24406 | ````` ối `````        |     95.9207 | <span style='border: 1px solid rgb(251, 189, 8);'>0.037</span>  | ````` ▁cuối `````, ````` ▁tối `````, ````` ▁nối `````, ````` ▁phối `````, ````` ▁đối `````                            |
|      43558 | ````` lever `````     |     96.0894 | <span style='border: 1px solid rgb(40, 167, 69);'>0.11</span>   | ````` ▁levering `````, ````` geleverd `````, ````` ▁leverancier `````, ````` ▁Clever `````, ````` ▁leveren `````, ... |


## Tokens with partial UTF-8 sequences
1 entries below threshold of 96.582

|   token_id | token                      |   indicator | in_other_tokens                                          |
|------------|----------------------------|-------------|----------------------------------------------------------|
|      20373 | ````` <0xBE><0xB3>门 ````` |     3.08234 | ````` 澳门 `````, ````` ▁澳门新 `````, ````` ▁澳门 ````` |


## Byte tokens
55 entries below threshold of 106.647

|   token_id | token              |   indicator |   ord | hex   | byte_type   |
|------------|--------------------|-------------|-------|-------|-------------|
|        183 | ````` <0xFB> ````` |     2.73783 |   251 | 0xFB  | unused_utf8 |
|        177 | ````` <0xF5> ````` |     2.86873 |   245 | 0xF5  | unused_utf8 |
|        125 | ````` <0xC1> ````` |     2.89802 |   193 | 0xC1  | unused_utf8 |
|        180 | ````` <0xF8> ````` |     3.03576 |   248 | 0xF8  | unused_utf8 |
|        124 | ````` <0xC0> ````` |     3.04319 |   192 | 0xC0  | unused_utf8 |
|        184 | ````` <0xFC> ````` |     3.17908 |   252 | 0xFC  | unused_utf8 |
|        181 | ````` <0xF9> ````` |     3.18167 |   249 | 0xF9  | unused_utf8 |
|        178 | ````` <0xF6> ````` |     3.19188 |   246 | 0xF6  | unused_utf8 |
|        185 | ````` <0xFD> ````` |     3.20594 |   253 | 0xFD  | unused_utf8 |
|        186 | ````` <0xFE> ````` |     3.27176 |   254 | 0xFE  | unused_utf8 |
|        179 | ````` <0xF7> ````` |     3.27246 |   247 | 0xF7  | unused_utf8 |
|        187 | ````` <0xFF> ````` |     3.34999 |   255 | 0xFF  | unused_utf8 |
|        182 | ````` <0xFA> ````` |     3.42075 |   250 | 0xFA  | unused_utf8 |
|        246 | ````` <0x98> ````` |    95.8309  |   152 | 0x98  | utf8        |
|        238 | ````` <0x90> ````` |    98.2937  |   144 | 0x90  | utf8        |
|        244 | ````` <0x96> ````` |    98.5914  |   150 | 0x96  | utf8        |
|        110 | ````` <0xB2> ````` |    98.6681  |   178 | 0xB2  | utf8        |
|        249 | ````` <0x9B> ````` |    99.2759  |   155 | 0x9B  | utf8        |
|        233 | ````` <0x8B> ````` |    99.508   |   139 | 0x8B  | utf8        |
|        109 | ````` <0xB1> ````` |    99.8037  |   177 | 0xB1  | utf8        |
<details><summary>35 additional entries below threshold</summary>

|   token_id | token              |   indicator |   ord | hex   | byte_type   |
|------------|--------------------|-------------|-------|-------|-------------|
|        236 | ````` <0x8E> ````` |     99.8598 |   142 | 0x8E  | utf8        |
|        248 | ````` <0x9A> ````` |    100.135  |   154 | 0x9A  | utf8        |
|        112 | ````` <0xB4> ````` |    100.441  |   180 | 0xB4  | utf8        |
|         94 | ````` <0xA1> ````` |    100.945  |   161 | 0xA1  | utf8        |
|        235 | ````` <0x8D> ````` |    101.118  |   141 | 0x8D  | utf8        |
|         97 | ````` <0xA4> ````` |    101.422  |   164 | 0xA4  | utf8        |
|         99 | ````` <0xA6> ````` |    101.739  |   166 | 0xA6  | utf8        |
|        237 | ````` <0x8F> ````` |    101.932  |   143 | 0x8F  | utf8        |
|        108 | ````` <0xB0> ````` |    102.074  |   176 | 0xB0  | utf8        |
|        119 | ````` <0xBB> ````` |    102.333  |   187 | 0xBB  | utf8        |
|        121 | ````` <0xBD> ````` |    102.431  |   189 | 0xBD  | utf8        |
|         95 | ````` <0xA2> ````` |    102.576  |   162 | 0xA2  | utf8        |
|        105 | ````` <0xAC> ````` |    102.69   |   172 | 0xAC  | utf8        |
|         98 | ````` <0xA5> ````` |    102.805  |   165 | 0xA5  | utf8        |
|        240 | ````` <0x92> ````` |    102.863  |   146 | 0x92  | utf8        |
|         96 | ````` <0xA3> ````` |    103.05   |   163 | 0xA3  | utf8        |
|        247 | ````` <0x99> ````` |    103.084  |   153 | 0x99  | utf8        |
|        111 | ````` <0xB3> ````` |    103.376  |   179 | 0xB3  | utf8        |
|        107 | ````` <0xAF> ````` |    103.556  |   175 | 0xAF  | utf8        |
|        252 | ````` <0x9E> ````` |    103.596  |   158 | 0x9E  | utf8        |
|        123 | ````` <0xBF> ````` |    103.66   |   191 | 0xBF  | utf8        |
|        115 | ````` <0xB7> ````` |    103.946  |   183 | 0xB7  | utf8        |
|        234 | ````` <0x8C> ````` |    104.144  |   140 | 0x8C  | utf8        |
|        100 | ````` <0xA7> ````` |    104.452  |   167 | 0xA7  | utf8        |
|        103 | ````` <0xAA> ````` |    105.035  |   170 | 0xAA  | utf8        |
|        116 | ````` <0xB8> ````` |    105.044  |   184 | 0xB8  | utf8        |
|        227 | ````` <0x85> ````` |    105.128  |   133 | 0x85  | utf8        |
|        122 | ````` <0xBE> ````` |    105.631  |   190 | 0xBE  | utf8        |
|        243 | ````` <0x95> ````` |    105.783  |   149 | 0x95  | utf8        |
|        215 | ````` \x1b `````   |    105.93   |    27 | 0x1B  | ascii       |
|        251 | ````` <0x9D> ````` |    105.961  |   157 | 0x9D  | utf8        |
|        241 | ````` <0x93> ````` |    106.044  |   147 | 0x93  | utf8        |
|        254 | ````` <0xA0> ````` |    106.048  |   160 | 0xA0  | utf8        |
|        229 | ````` <0x87> ````` |    106.162  |   135 | 0x87  | utf8        |
|        225 | ````` <0x83> ````` |    106.323  |   131 | 0x83  | utf8        |
</details>


## Special tokens
1 entries below threshold of 106.647

|   token_id | token                             |   indicator | max_prob                                                       |
|------------|-----------------------------------|-------------|----------------------------------------------------------------|
|     200010 | ````` <\|reserved_200010\|> ````` |     99.1692 | <span style='border: 1px solid rgb(251, 189, 8);'>0.022</span> |


## Unreachable tokens
0 entries below threshold of 106.647



