import pytest

from magikarp.fishing import UNUSED_TOKENS, TokenizerAnalyzer


TEST_MODELS = [m for m in UNUSED_TOKENS.keys()]


@pytest.mark.parametrize("model_id", TEST_MODELS)
def test_tokenizer(model_id):
    toka = TokenizerAnalyzer(model_id, trust_remote_code=True)

    phrases = ["test", " test", "", "a", "\x00"]
    for phrase in phrases:
        toks = toka.clean_encode(phrase)
        if any(t == toka.tokenizer.unk_token_id for t in toks):
            print(f"Skipping {model_id} for {phrase!r} -> {toks} because it has an unk token")
            continue
        vocabs = [toka.vocab_i2s[i] for i in toks]
        decoded = toka.clean_decode(toks)
        print(
            f"Testing {model_id=} with starting_space_mode = {toka.starting_space_mode} phrase {phrase!r} -> {toks} = {vocabs} -> {decoded!r}"
        )
        if phrase == "":
            assert toks == [], f"{model_id} tokenizer test failed: {phrase!r} -> {toks}"
        elif phrase[0] != " ":
            for sc in toka.SPACE_CHARS:
                assert not vocabs[0].startswith(
                    sc
                ), f"{model_id} tokenizer test failed: {phrase!r} -> {toks} starts with {sc!r}"

        assert decoded == phrase, f"{model_id} tokenizer test failed: {phrase!r} -> {toks} -> {decoded!r}"
