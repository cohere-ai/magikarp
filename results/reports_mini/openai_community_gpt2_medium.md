# Report for `openai-community/gpt2-medium`

## Model info

* Tied embeddings: yes
* LM head uses bias: no
* Indicator for under-trained tokens: E_{out} Cosine Distance w/o 1st PC
  * Overall distribution 0.999 +/- 0.045
  * Token used for verification prompt building: `BuyableInstoreAndOnline`
  * Verification threshold: 0.942
  * Threshold for showing candidate under-trained tokens: 0.155
  * Median verified threshold (for bytes, unreachable and special tokens): 0.039
* Embeddings shape: (50257, 1024)
* Vocabulary size: 50257
  * Number of single byte tokens: 256, of which 41 below indicator threshold
  * Number of special tokens: 1, of which 0 below indicator threshold
  * Number of non-single-byte UTF-fragment tokens: 216, 1 below soft indicator threshold
  * Number of tested under-trained tokens: 999, 965 non-special, 17 below p = 0.01 threshold, 11 below soft indicator threshold

## Under-trained token indicators plot
![Indicators scatter plots](../indicators_pairplot_byid/openai_community_gpt2_medium.png)

## Verification plot
![Verification plot](../verifications_scatterplot/openai_community_gpt2_medium.png)

## Under-trained token verification results
11 entries below threshold of 0.155

|   token_id | token                        |   indicator | max_prob                                                         | in_other_tokens                                                                                                                                                                                                                                                                          |
|------------|------------------------------|-------------|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      30897 | ````` reportprint `````      |   0.033295  | <span style='border: 1px solid rgb(169, 68, 66);'>3.9e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` embedreportprint `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` cloneembedreportprint `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` rawdownloadcloneembedreportprint `````</span> |
|      30212 | ````` ▁externalToEVA `````   |   0.0338109 | <span style='border: 1px solid rgb(169, 68, 66);'>3.3e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁externalToEVAOnly `````</span>                                                                                                                                                                                                  |
|      45544 | ````` ▁サーティ `````        |   0.0351641 | <span style='border: 1px solid rgb(169, 68, 66);'>2.7e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁サーティワン `````</span>                                                                                                                                                                                                       |
|      39752 | ````` quickShip `````        |   0.0366266 | <span style='border: 1px solid rgb(169, 68, 66);'>2.4e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` quickShipAvailable `````</span>                                                                                                                                                                                                  |
|      30905 | ````` rawdownload `````      |   0.0372465 | <span style='border: 1px solid rgb(169, 68, 66);'>3.3e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` rawdownloadcloneembedreportprint `````</span>                                                                                                                                                                                    |
|      36173 | ````` ▁RandomRedditor `````  |   0.0373348 | <span style='border: 1px solid rgb(169, 68, 66);'>2.7e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁RandomRedditorWithNo `````</span>                                                                                                                                                                                               |
|      40240 | ````` oreAndOnline `````     |   0.0375386 | <span style='border: 1px solid rgb(169, 68, 66);'>3e-07</span>   | <span style='border: 1px solid rgb(169, 68, 66);'>````` InstoreAndOnline `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` BuyableInstoreAndOnline `````</span>                                                                                                      |
|      40241 | ````` InstoreAndOnline ````` |   0.0382396 | <span style='border: 1px solid rgb(169, 68, 66);'>4.4e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` BuyableInstoreAndOnline `````</span>                                                                                                                                                                                             |
|      42089 | ````` ▁TheNitrome `````      |   0.0388501 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁TheNitromeFan `````</span>                                                                                                                                                                                                      |
|      30898 | ````` embedreportprint ````` |   0.0391257 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` cloneembedreportprint `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` rawdownloadcloneembedreportprint `````</span>                                                                                        |
|      30208 | ````` ▁externalTo `````      |   0.0953019 | <span style='border: 1px solid rgb(169, 68, 66);'>6.7e-06</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁externalToEVA `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁externalToEVAOnly `````</span>                                                                                                             |


## Tokens with partial UTF-8 sequences
1 entries below threshold of 0.155

|   token_id | token                      |   indicator | in_other_tokens                                                             |
|------------|----------------------------|-------------|-----------------------------------------------------------------------------|
|      39820 | ````` 龍<0xE5><0xA5> ````` |   0.0369992 | <span style='border: 1px solid rgb(40, 167, 69);'>````` 龍契士 `````</span> |


## Byte tokens
41 entries below threshold of 0.039

|   token_id | token              |   indicator |   ord | hex   | byte_type   |
|------------|--------------------|-------------|-------|-------|-------------|
|        184 | ````` <0xFC> ````` |   0.0280493 |   252 | 0xFC  | unused_utf8 |
|        185 | ````` <0xFD> ````` |   0.0280969 |   253 | 0xFD  | unused_utf8 |
|        180 | ````` <0xF8> ````` |   0.0285165 |   248 | 0xF8  | unused_utf8 |
|        178 | ````` <0xF6> ````` |   0.0285981 |   246 | 0xF6  | unused_utf8 |
|        187 | ````` <0xFF> ````` |   0.0289848 |   255 | 0xFF  | unused_utf8 |
|        177 | ````` <0xF5> ````` |   0.0291439 |   245 | 0xF5  | unused_utf8 |
|        183 | ````` <0xFB> ````` |   0.0302289 |   251 | 0xFB  | unused_utf8 |
|        186 | ````` <0xFE> ````` |   0.0303413 |   254 | 0xFE  | unused_utf8 |
|        210 | ````` \x16 `````   |   0.0310303 |    22 | 0x16  | ascii       |
|        189 | ````` \x01 `````   |   0.0323922 |     1 | 0x01  | ascii       |
|        219 | ````` \x1f `````   |   0.032473  |    31 | 0x1F  | ascii       |
|        182 | ````` <0xFA> ````` |   0.0328182 |   250 | 0xFA  | unused_utf8 |
|        179 | ````` <0xF7> ````` |   0.0328272 |   247 | 0xF7  | unused_utf8 |
|        197 | ````` \t `````     |   0.0328517 |     9 | 0x09  | ascii       |
|        181 | ````` <0xF9> ````` |   0.0336775 |   249 | 0xF9  | unused_utf8 |
|        124 | ````` <0xC0> ````` |   0.0337997 |   192 | 0xC0  | unused_utf8 |
|        192 | ````` \x04 `````   |   0.0343153 |     4 | 0x04  | ascii       |
|        211 | ````` \x17 `````   |   0.0344452 |    23 | 0x17  | ascii       |
|        209 | ````` \x15 `````   |   0.0344477 |    21 | 0x15  | ascii       |
|        213 | ````` \x19 `````   |   0.0347515 |    25 | 0x19  | ascii       |
<details><summary>21 additional entries below threshold</summary>

|   token_id | token              |   indicator | hex   | byte_type   |   ord |
|------------|--------------------|-------------|-------|-------------|-------|
|        188 | ````` \x00 `````   |   0.0353258 | 0x00  | ascii       |       |
|        202 | ````` \x0e `````   |   0.035699  | 0x0E  | ascii       |    14 |
|        191 | ````` \x03 `````   |   0.0359075 | 0x03  | ascii       |     3 |
|        217 | ````` \x1d `````   |   0.0359418 | 0x1D  | ascii       |    29 |
|        205 | ````` \x11 `````   |   0.0359878 | 0x11  | ascii       |    17 |
|        207 | ````` \x13 `````   |   0.0363752 | 0x13  | ascii       |    19 |
|        221 | ````` \x7f `````   |   0.0367022 | 0x7F  | ascii       |   127 |
|        208 | ````` \x14 `````   |   0.0367163 | 0x14  | ascii       |    20 |
|        216 | ````` \x1c `````   |   0.0368353 | 0x1C  | ascii       |    28 |
|        212 | ````` \x18 `````   |   0.0369136 | 0x18  | ascii       |    24 |
|        218 | ````` \x1e `````   |   0.0371034 | 0x1E  | ascii       |    30 |
|        215 | ````` \x1b `````   |   0.0375644 | 0x1B  | ascii       |    27 |
|        196 | ````` \x08 `````   |   0.0376527 | 0x08  | ascii       |     8 |
|        206 | ````` \x12 `````   |   0.0377709 | 0x12  | ascii       |    18 |
|        125 | ````` <0xC1> ````` |   0.0379209 | 0xC1  | unused_utf8 |   193 |
|        199 | ````` \x0b `````   |   0.0379294 | 0x0B  | ascii       |    11 |
|        204 | ````` \x10 `````   |   0.038133  | 0x10  | ascii       |    16 |
|        200 | ````` \x0c `````   |   0.0381737 | 0x0C  | ascii       |    12 |
|        195 | ````` \x07 `````   |   0.0382445 | 0x07  | ascii       |     7 |
|        194 | ````` \x06 `````   |   0.0383338 | 0x06  | ascii       |     6 |
|        201 | ````` \r `````     |   0.0384327 | 0x0D  | ascii       |    13 |
</details>


## Special tokens
0 entries below threshold of 0.039



