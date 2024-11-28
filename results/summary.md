# Summary of under-trained token detection:

* 'Verified without s/b' refers to without special tokens or single byte tokens


| Model                    | reports                                                                                      | Embeddings   | Tokenizer          |   Vocab Size |   # bytes |   # unreachable |   # partial utf-8 |   # special | # verified   | # verified w/o s/b   | Longest token   | Examples                                                                                                                                                                                    |
|--------------------------|----------------------------------------------------------------------------------------------|--------------|--------------------|--------------|-----------|-----------------|-------------------|-------------|--------------|----------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| upstage/SOLAR-10.7B-v1.0 | [mini](reports_mini/upstage_SOLAR_10_7B_v1_0.md) [full](reports/upstage_SOLAR_10_7B_v1_0.md) | 32000 × 4096 | BPE, Byte Fallback |        32000 |       380 |               0 |                 0 |           3 | 58/638       | 51/523               | includegraphics | ````` ▁/**\r `````, ````` });\r `````, ````` };\r `````, ````` ▁});\r `````, ````` ▁//\r `````, ````` ';\r `````, ````` */\r `````, ````` ▁*/\r `````, ````` ]);\r `````, ````` ▁};\r ````` |

Processed 1 models, 1 succeeded