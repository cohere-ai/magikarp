# Report for `deepseek-ai/deepseek-math-7b-base`

## Model info

* Tied embeddings: no
* LM head uses bias: no
* Indicator for under-trained tokens: E_{in} L2 Norm
  * Overall distribution 10.963 +/- 3.144
  * Token used for verification prompt building: `IllegalArgumentException`
  * Verification threshold: 3.014
  * Threshold for showing candidate under-trained tokens: 1.092
  * Median verified threshold (for bytes, unreachable and special tokens): 2.288
* Embeddings shape: (102400, 4096)
* Vocabulary size: 100002
  * Number of single byte tokens: 243, of which 0 below indicator threshold
  * Number of special tokens: 2, of which 0 below indicator threshold
  * Number of non-single-byte unreachable tokens: 12, of which 0 below indicator threshold
  * Number of non-single-byte UTF-fragment tokens: 438, 0 below soft indicator threshold
  * Number of tested under-trained tokens: 1989, 1989 non-special, 202 below p = 0.01 threshold, 13 below soft indicator threshold

## Under-trained token indicators plot
![Indicators scatter plots](../indicators_pairplot_byid/deepseek_ai_deepseek_math_7b_base.png)

## Verification plot
![Verification plot](../verifications_scatterplot/deepseek_ai_deepseek_math_7b_base.png)

## Under-trained token verification results
13 entries below threshold of 1.092

|   token_id | token                           |   indicator | max_prob                                                         | in_other_tokens                                                                                                                                                                      |
|------------|---------------------------------|-------------|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      63291 | ````` IconSuccessEncoded `````  |    0.439327 | <span style='border: 1px solid rgb(169, 68, 66);'>6.2e-05</span> |                                                                                                                                                                                      |
|      87662 | ````` 日内与新浪看点 `````      |    0.43966  | <span style='border: 1px solid rgb(169, 68, 66);'>4e-05</span>   | <span style='border: 1px solid rgb(169, 68, 66);'>````` 日内与新浪看点联系 `````</span>                                                                                              |
|      40482 | ````` IconErrorEncoded `````    |    0.510684 | <span style='border: 1px solid rgb(169, 68, 66);'>1.7e-09</span> |                                                                                                                                                                                      |
|      74777 | ````` orangehilldev `````       |    0.596192 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00026</span> |                                                                                                                                                                                      |
|      87661 | ````` 不代表新浪看点 `````      |    0.605036 | <span style='border: 1px solid rgb(169, 68, 66);'>3.6e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` 不代表新浪看点观点或立场 `````</span>                                                                                        |
|      98098 | ````` ="../../../../..">< ````` |    0.701254 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00013</span> |                                                                                                                                                                                      |
|      81096 | ````` ▁EDIPU `````              |    0.747061 | <span style='border: 1px solid rgb(169, 68, 66);'>2e-05</span>   | <span style='border: 1px solid rgb(255, 145, 0);'>````` ▁EDIPUCRS `````</span>                                                                                                       |
|      13009 | ````` lemanya `````             |    0.812841 | <span style='border: 1px solid rgb(169, 68, 66);'>0.00015</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` Alemanya `````</span>, <span style='border: 1px solid rgb(40, 167, 69);'>````` ▁alemanya `````</span>, ````` ▁Alemanya ````` |
|      60623 | ````` odeciclismo `````         |    0.892729 | <span style='border: 1px solid rgb(169, 68, 66);'>5.6e-05</span> | <span style='border: 1px solid rgb(169, 68, 66);'>````` iodeciclismo `````</span>, <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁sitiodeciclismo `````</span>             |
|      16238 | ````` кедония `````             |    0.929747 | <span style='border: 1px solid rgb(255, 145, 0);'>0.0063</span>  | ````` Македония `````, ````` ▁Македония `````                                                                                                                                        |
|      84405 | ````` RecordedVote `````        |    0.978604 | <span style='border: 1px solid rgb(40, 167, 69);'>0.51</span>    |                                                                                                                                                                                      |
|      97672 | ````` 基督教基督教基督教 `````  |    1.00834  | <span style='border: 1px solid rgb(255, 145, 0);'>0.001</span>   |                                                                                                                                                                                      |
|      86826 | ````` солство `````             |    1.07232  | <span style='border: 1px solid rgb(255, 145, 0);'>0.0016</span>  | <span style='border: 1px solid rgb(169, 68, 66);'>````` посолство `````</span>                                                                                                       |


## Partial UTF-8 tokens
0 entries below threshold of 1.092




## Byte tokens
0 entries below threshold of 2.288




## Special tokens
0 entries below threshold of 2.288




## Unreachable tokens
0 entries below threshold of 2.288



