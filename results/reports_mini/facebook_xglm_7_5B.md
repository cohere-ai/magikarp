# Report for `facebook/xglm-7.5B`

## Model info

* Tied embeddings: yes
* LM head uses bias: no
* Indicator for under-trained tokens: E_{out} L2 Distance
  * Overall distribution 2.111 +/- 0.636
  * Token used for verification prompt building: `习近平新时代中国特色社会主义思想`
  * Verification threshold: 1.052
  * Threshold for showing candidate under-trained tokens: 1.022
  * Median verified threshold (for bytes, unreachable and special tokens): 1.045
* Embeddings shape: (256008, 4096)
* Vocabulary size: 256008
  * Number of single byte tokens: 94, of which 0 below indicator threshold
  * Number of special tokens: 11, of which 9 below indicator threshold
  * Number of non-single-byte unreachable tokens: 20, of which 1 below indicator threshold
  * Number of tested under-trained tokens: 5129, 5120 non-special, 334 below p = 0.01 threshold, 11 below soft indicator threshold

## Under-trained token indicators plot
![Indicators scatter plots](../indicators_pairplot_byid/facebook_xglm_7_5B.png)

## Verification plot
![Verification plot](../verifications_scatterplot/facebook_xglm_7_5B.png)

## Under-trained token verification results
11 entries below threshold of 1.022

|   token_id | token                  |   indicator | max_prob                                                        | in_other_tokens          |
|------------|------------------------|-------------|-----------------------------------------------------------------|--------------------------|
|     164189 | ````` ▁nevladin `````  |     1.01397 | <span style='border: 1px solid rgb(251, 189, 8);'>0.048</span>  |                          |
|     211547 | ````` ▁следећи `````   |     1.01722 | <span style='border: 1px solid rgb(251, 189, 8);'>0.048</span>  |                          |
|      64286 | ````` વાનું `````         |     1.0174  | <span style='border: 1px solid rgb(251, 189, 8);'>0.076</span>  | ````` ▁કરવાનું `````        |
|      97859 | ````` ▁ерөнхий `````   |     1.01923 | <span style='border: 1px solid rgb(251, 189, 8);'>0.025</span>  | ````` ▁ерөнхийлөгч ````` |
|     179987 | ````` ▁tanteraka ````` |     1.01931 | <span style='border: 1px solid rgb(251, 189, 8);'>0.032</span>  |                          |
|      85701 | ````` ▁ಮುಂದೆ `````        |     1.02023 | <span style='border: 1px solid rgb(251, 189, 8);'>0.013</span>  |                          |
|     239258 | ````` ძიება `````      |     1.02039 | <span style='border: 1px solid rgb(40, 167, 69);'>0.14</span>   |                          |
|      64648 | ````` ▁පසුගිය `````      |     1.02113 | <span style='border: 1px solid rgb(251, 189, 8);'>0.039</span>  |                          |
|     157252 | ````` ▁prihvata `````  |     1.02116 | <span style='border: 1px solid rgb(251, 189, 8);'>0.022</span>  |                          |
|     240788 | ````` эдгээ `````      |     1.02143 | <span style='border: 1px solid rgb(255, 145, 0);'>0.0087</span> |                          |
|     167006 | ````` ▁өткізіл `````   |     1.02155 | <span style='border: 1px solid rgb(40, 167, 69);'>0.18</span>   |                          |


## Byte tokens
0 entries below threshold of 1.045




## Special tokens
9 entries below threshold of 1.045

|   token_id | token                     |   indicator | max_prob                                                         |
|------------|---------------------------|-------------|------------------------------------------------------------------|
|          1 | ````` <pad> `````         |    0.387592 | <span style='border: 1px solid rgb(169, 68, 66);'>1.3e-07</span> |
|     256006 | ````` <madeupword5> ````` |    0.90089  | <span style='border: 1px solid rgb(251, 189, 8);'>0.018</span>   |
|     256004 | ````` <madeupword3> ````` |    0.904612 | <span style='border: 1px solid rgb(251, 189, 8);'>0.066</span>   |
|     256003 | ````` <madeupword2> ````` |    0.912984 | <span style='border: 1px solid rgb(251, 189, 8);'>0.021</span>   |
|     256002 | ````` <madeupword1> ````` |    0.918276 | <span style='border: 1px solid rgb(251, 189, 8);'>0.081</span>   |
|     256007 | ````` <madeupword6> ````` |    0.921518 | <span style='border: 1px solid rgb(251, 189, 8);'>0.034</span>   |
|     256001 | ````` <madeupword0> ````` |    0.924558 | <span style='border: 1px solid rgb(251, 189, 8);'>0.05</span>    |
|     256005 | ````` <madeupword4> ````` |    0.929404 | <span style='border: 1px solid rgb(251, 189, 8);'>0.079</span>   |
|          0 | ````` <s> `````           |    1.03741  | <span style='border: 1px solid rgb(251, 189, 8);'>0.052</span>   |


## Unreachable tokens
1 entries below threshold of 1.045

|   token_id | token           |   indicator | reencoded                              |
|------------|-----------------|-------------|----------------------------------------|
|     107315 | ````` dei ````` |      1.0423 | 134: ````` de `````, 14: ````` i ````` |

