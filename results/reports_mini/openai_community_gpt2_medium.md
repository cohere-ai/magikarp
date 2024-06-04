# Report for `openai-community/gpt2-medium`

## Model info

* Tied embeddings: yes
* LM head uses bias: no
* Indicator for under-trained tokens: E_{out} Cosine Distance
  * Overall distribution 0.489 +/- 0.053
  * Token used for verification prompt building: `BuyableInstoreAndOnline`
  * Verification threshold: 0.383
  * Threshold for showing candidate under-trained tokens: 0.041
  * Median verified threshold (for bytes, unreachable and special tokens): 0.005
* Embeddings shape: (50257, 1024)
* Vocabulary size: 50257
  * Number of single byte tokens: 256, of which 45 below indicator threshold
  * Number of special tokens: 1, of which 0 below indicator threshold
  * Number of non-single-byte UTF-fragment tokens: 216, 1 below soft indicator threshold
  * Number of tested under-trained tokens: 999, 967 non-special, 17 below p = 0.01 threshold, 11 below soft indicator threshold

## Under-trained token indicators plot
![Indicators scatter plots](../indicators_pairplot_byid/openai_community_gpt2_medium.png)

## Verification plot
![Verification plot](../verifications_scatterplot/openai_community_gpt2_medium.png)

## Under-trained token verification results
11 entries below threshold of 0.041

|   token_id | token                        |   indicator | max_prob                                                         | in_other_tokens                                                                                                                                                                                                                                                                          |
|------------|------------------------------|-------------|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      30897 | ````` reportprint `````      |  0.00444567 | <span style='border: 1px solid rgb(169, 68, 66);'>3.9e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` embedreportprint `````</span>, <span style='border: 1px solid rgb(169, 68, 66);'>````` cloneembedreportprint `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` rawdownloadcloneembedreportprint `````</span> |
|      45544 | ````` ▁サーティ `````        |  0.00456727 | <span style='border: 1px solid rgb(169, 68, 66);'>2.7e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁サーティワン `````</span>                                                                                                                                                                                                       |
|      30212 | ````` ▁externalToEVA `````   |  0.00459385 | <span style='border: 1px solid rgb(169, 68, 66);'>3.3e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁externalToEVAOnly `````</span>                                                                                                                                                                                                  |
|      30905 | ````` rawdownload `````      |  0.00463021 | <span style='border: 1px solid rgb(169, 68, 66);'>3.3e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` rawdownloadcloneembedreportprint `````</span>                                                                                                                                                                                    |
|      39752 | ````` quickShip `````        |  0.00471389 | <span style='border: 1px solid rgb(169, 68, 66);'>2.4e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` quickShipAvailable `````</span>                                                                                                                                                                                                  |
|      36173 | ````` ▁RandomRedditor `````  |  0.00473255 | <span style='border: 1px solid rgb(169, 68, 66);'>2.7e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁RandomRedditorWithNo `````</span>                                                                                                                                                                                               |
|      42089 | ````` ▁TheNitrome `````      |  0.00477672 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁TheNitromeFan `````</span>                                                                                                                                                                                                      |
|      40241 | ````` InstoreAndOnline ````` |  0.00498092 | <span style='border: 1px solid rgb(169, 68, 66);'>4.4e-07</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` BuyableInstoreAndOnline `````</span>                                                                                                                                                                                             |
|      30898 | ````` embedreportprint ````` |  0.00511497 | <span style='border: 1px solid rgb(169, 68, 66);'>3.1e-07</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` cloneembedreportprint `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` rawdownloadcloneembedreportprint `````</span>                                                                                        |
|      40240 | ````` oreAndOnline `````     |  0.00512677 | <span style='border: 1px solid rgb(169, 68, 66);'>3e-07</span>   | <span style='border: 1px solid rgb(169, 68, 66);'>````` InstoreAndOnline `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` BuyableInstoreAndOnline `````</span>                                                                                                      |
|      30208 | ````` ▁externalTo `````      |  0.0234748  | <span style='border: 1px solid rgb(169, 68, 66);'>6.7e-06</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` ▁externalToEVA `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁externalToEVAOnly `````</span>                                                                                                             |


## Partial UTF-8 tokens
1 entries below threshold of 0.041

|   token_id | token                      |   indicator | in_other_tokens                                                             |
|------------|----------------------------|-------------|-----------------------------------------------------------------------------|
|      39820 | ````` 龍<0xE5><0xA5> ````` |  0.00473803 | <span style='border: 1px solid rgb(40, 167, 69);'>````` 龍契士 `````</span> |


## Byte tokens
45 entries below threshold of 0.005

|   token_id | token              |   indicator |   ord | hex   | byte_type   |
|------------|--------------------|-------------|-------|-------|-------------|
|        178 | ````` <0xF6> ````` |  0.00357658 |   246 | 0xF6  | unused_utf8 |
|        183 | ````` <0xFB> ````` |  0.00366396 |   251 | 0xFB  | unused_utf8 |
|        185 | ````` <0xFD> ````` |  0.00367862 |   253 | 0xFD  | unused_utf8 |
|        180 | ````` <0xF8> ````` |  0.0036788  |   248 | 0xF8  | unused_utf8 |
|        184 | ````` <0xFC> ````` |  0.00368083 |   252 | 0xFC  | unused_utf8 |
|        187 | ````` <0xFF> ````` |  0.00386095 |   255 | 0xFF  | unused_utf8 |
|        179 | ````` <0xF7> ````` |  0.00395703 |   247 | 0xF7  | unused_utf8 |
|        186 | ````` <0xFE> ````` |  0.00401849 |   254 | 0xFE  | unused_utf8 |
|        177 | ````` <0xF5> ````` |  0.00404406 |   245 | 0xF5  | unused_utf8 |
|        182 | ````` <0xFA> ````` |  0.00411302 |   250 | 0xFA  | unused_utf8 |
|        210 | ````` \x16 `````   |  0.00416565 |    22 | 0x16  | ascii       |
|        197 | ````` \t `````     |  0.00420243 |     9 | 0x09  | ascii       |
|        181 | ````` <0xF9> ````` |  0.00422907 |   249 | 0xF9  | unused_utf8 |
|        207 | ````` \x13 `````   |  0.00434786 |    19 | 0x13  | ascii       |
|        124 | ````` <0xC0> ````` |  0.00435007 |   192 | 0xC0  | unused_utf8 |
|        189 | ````` \x01 `````   |  0.00436115 |     1 | 0x01  | ascii       |
|        192 | ````` \x04 `````   |  0.00437033 |     4 | 0x04  | ascii       |
|        215 | ````` \x1b `````   |  0.00446457 |    27 | 0x1B  | ascii       |
|        217 | ````` \x1d `````   |  0.00447732 |    29 | 0x1D  | ascii       |
|        188 | ````` \x00 `````   |  0.00448298 |       | 0x00  | ascii       |
<details><summary>25 additional entries below threshold</summary>

|   token_id | token              |   indicator |   ord | hex   | byte_type   |
|------------|--------------------|-------------|-------|-------|-------------|
|        205 | ````` \x11 `````   |  0.00454181 |    17 | 0x11  | ascii       |
|        221 | ````` \x7f `````   |  0.0045619  |   127 | 0x7F  | ascii       |
|        196 | ````` \x08 `````   |  0.00457859 |     8 | 0x08  | ascii       |
|        191 | ````` \x03 `````   |  0.00458455 |     3 | 0x03  | ascii       |
|        211 | ````` \x17 `````   |  0.00458777 |    23 | 0x17  | ascii       |
|        209 | ````` \x15 `````   |  0.00459915 |    21 | 0x15  | ascii       |
|        218 | ````` \x1e `````   |  0.00462502 |    30 | 0x1E  | ascii       |
|        219 | ````` \x1f `````   |  0.00462788 |    31 | 0x1F  | ascii       |
|        201 | ````` \r `````     |  0.00464106 |    13 | 0x0D  | ascii       |
|        199 | ````` \x0b `````   |  0.00464898 |    11 | 0x0B  | ascii       |
|        125 | ````` <0xC1> ````` |  0.00469691 |   193 | 0xC1  | unused_utf8 |
|        213 | ````` \x19 `````   |  0.00470841 |    25 | 0x19  | ascii       |
|        214 | ````` \x1a `````   |  0.00472432 |    26 | 0x1A  | ascii       |
|        216 | ````` \x1c `````   |  0.00474203 |    28 | 0x1C  | ascii       |
|        204 | ````` \x10 `````   |  0.00481361 |    16 | 0x10  | ascii       |
|        195 | ````` \x07 `````   |  0.00482035 |     7 | 0x07  | ascii       |
|        208 | ````` \x14 `````   |  0.00483632 |    20 | 0x14  | ascii       |
|        202 | ````` \x0e `````   |  0.00483972 |    14 | 0x0E  | ascii       |
|        200 | ````` \x0c `````   |  0.0048672  |    12 | 0x0C  | ascii       |
|        193 | ````` \x05 `````   |  0.00487089 |     5 | 0x05  | ascii       |
|        206 | ````` \x12 `````   |  0.00490856 |    18 | 0x12  | ascii       |
|        190 | ````` \x02 `````   |  0.00498682 |     2 | 0x02  | ascii       |
|        194 | ````` \x06 `````   |  0.00503385 |     6 | 0x06  | ascii       |
|        212 | ````` \x18 `````   |  0.00508702 |    24 | 0x18  | ascii       |
|        203 | ````` \x0f `````   |  0.005108   |    15 | 0x0F  | ascii       |
</details>


## Special tokens
0 entries below threshold of 0.005



