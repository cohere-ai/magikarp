# Report for `facebook/xglm-7.5B`

## Model info

* Model Info: 
  * Tied embeddings: True
  * LM head uses bias: False
  * Embeddings shape: [256008, 4096]
* Tokenizer Info: 
  * Vocab Size: 256008
  * Tokenizer Class: XGLMTokenizer
  * Tokenizer Type: Unigram
  * Token for verification prompt building: 习近平新时代中国特色社会主义思想
  * Token id for verification prompt building: 196096
* Indicator summary: 
  * Indicator for under-trained tokens: E_{out} Cosine Distance
  * Overall distribution: 0.950 +/- 0.039
* Detected Token Counts: 
  * Number of tested under-trained tokens: 5129, 5120 non-special, 11 below p = 0.01 threshold, 11 below soft indicator threshold
  * Number of single byte tokens: 94, of which 0 below indicator threshold
  * Number of special tokens: 20, of which 0 below indicator threshold
  * Number of non-single-byte unreachable tokens: 20, of which 0 below indicator threshold

## Under-trained token indicators plot
![Indicators scatter plots](../indicators_pairplot_byid/facebook_xglm_7_5B.png)

## Verification plot
![Verification plot](../verifications_scatterplot/facebook_xglm_7_5B.png)

## Under-trained token verification results
11 entries below threshold of 0.829

|   token_id | token                   |   indicator | max_prob                                                      | in_other_tokens                                                                                                                                                                                               |
|------------|-------------------------|-------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      48871 | ````` ▁अशी `````         |    0.808387 | <span style='border: 1px solid rgb(40, 167, 69);'>0.98</span> |                                                                                                                                                                                                               |
|      55230 | ````` ▁بررسي `````      |    0.8169   | <span style='border: 1px solid rgb(40, 167, 69);'>0.96</span> |                                                                                                                                                                                                               |
|     136633 | ````` ▁دروغ `````       |    0.822068 | <span style='border: 1px solid rgb(40, 167, 69);'>1</span>    |                                                                                                                                                                                                               |
|      88789 | ````` ▁навчальних ````` |    0.824703 | <span style='border: 1px solid rgb(40, 167, 69);'>0.94</span> |                                                                                                                                                                                                               |
|     241851 | ````` ▁सर्वसाधारण `````    |    0.824755 | <span style='border: 1px solid rgb(40, 167, 69);'>0.88</span> |                                                                                                                                                                                                               |
|      88004 | ````` ▁ادعا `````       |    0.825891 | <span style='border: 1px solid rgb(40, 167, 69);'>0.99</span> |                                                                                                                                                                                                               |
|     162015 | ````` ▁وضعيت `````      |    0.82625  | <span style='border: 1px solid rgb(40, 167, 69);'>1</span>    |                                                                                                                                                                                                               |
|      47578 | ````` າວ `````          |    0.826291 | <span style='border: 1px solid rgb(40, 167, 69);'>0.99</span> | <span style='border: 1px solid rgb(40, 167, 69);'>````` ຊາວ `````</span>, ````` ດັ່ງກ່າວ `````, <span style='border: 1px solid rgb(251, 189, 8);'>````` ▁ກ່າວ `````</span>, ````` ▁ຂ່າວ `````, ````` ້າວ `````, ... |
|      13785 | ````` ტი `````          |    0.827149 | <span style='border: 1px solid rgb(40, 167, 69);'>0.96</span> | ````` სტი `````, <span style='border: 1px solid rgb(40, 167, 69);'>````` ტის `````</span>, ````` ▁მეტი `````, ````` ანტი `````, ````` ▁ტი `````, ...                                                          |
|     121489 | ````` ▁خلاصه `````      |    0.827959 | <span style='border: 1px solid rgb(40, 167, 69);'>1</span>    |                                                                                                                                                                                                               |
|      52354 | ````` ▁عملیات `````     |    0.828597 | <span style='border: 1px solid rgb(40, 167, 69);'>1</span>    |                                                                                                                                                                                                               |


## Byte tokens
0 entries below threshold of 0.875




## Special tokens
9 entries below threshold of 0.875

|   token_id | token                     |   indicator | max_prob                                                         |
|------------|---------------------------|-------------|------------------------------------------------------------------|
|     256001 | ````` <madeupword0> ````` |    0.558459 | <span style='border: 1px solid rgb(251, 189, 8);'>0.05</span>    |
|     256002 | ````` <madeupword1> ````` |    0.558526 | <span style='border: 1px solid rgb(251, 189, 8);'>0.081</span>   |
|     256006 | ````` <madeupword5> ````` |    0.567849 | <span style='border: 1px solid rgb(251, 189, 8);'>0.018</span>   |
|          1 | ````` <pad> `````         |    0.567872 | <span style='border: 1px solid rgb(169, 68, 66);'>1.3e-07</span> |
|     256004 | ````` <madeupword3> ````` |    0.568816 | <span style='border: 1px solid rgb(251, 189, 8);'>0.066</span>   |
|     256003 | ````` <madeupword2> ````` |    0.590159 | <span style='border: 1px solid rgb(251, 189, 8);'>0.021</span>   |
|     256007 | ````` <madeupword6> ````` |    0.592199 | <span style='border: 1px solid rgb(251, 189, 8);'>0.034</span>   |
|     256005 | ````` <madeupword4> ````` |    0.609361 | <span style='border: 1px solid rgb(251, 189, 8);'>0.079</span>   |
|          0 | ````` <s> `````           |    0.86583  | <span style='border: 1px solid rgb(251, 189, 8);'>0.052</span>   |


## Unreachable tokens
0 entries below threshold of 0.875



