"""
Tests for Sudachi-backed Japanese tokenization.

These tests are skipped if `sudachipy` is not installed so CI can run
without the optional dependency.

SudachiPyを使用した日本語のトークン化に関するテストファイル。

sudachipyがインストールされていない場合、これらのテストはスキップされます。

"""
import pytest


def _is_installed(pkg):
    try:
        __import__(pkg)
        return True
    except Exception:
        return False

# Make sure sudachipy is used as the active backend
# sudachipyが使われているかどうかを確認
@pytest.mark.skipif(not _is_installed('sudachipy'), reason='sudachipy not installed')
def test_active_backend_is_sudachi():
    from lime.japanese import active_japanese_tokenizer
    assert active_japanese_tokenizer() == 'sudachi'


# Ensure sudachi tokenizer correctly works with simple example
# tokenizerが正しく動作するか確認
@pytest.mark.skipif(not _is_installed('sudachipy'), reason='sudachipy not installed')
def test_sudachi_splitter_returns_tokens():
    from lime.japanese import splitter
    s = "今日はいい天気です。"
    tokens = splitter(s)
    assert isinstance(tokens, list)
    assert all(isinstance(t, str) for t in tokens)
    assert len(tokens) >= 2
