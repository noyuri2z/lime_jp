"""
High-level splitter functions for Japanese text.

These functions use singleton tokenizer instances from tokenizers.py and
provide simple splitter APIs. They raise ImportError with clear instructions
if required libraries are missing.

日本語テキスト用の文章分割機能のファイル。

これらの関数は、tokenizers.pyからのシングルトントークナイザーインスタンスを使用し、
シンプルな分割APIを提供します。必要なライブラリが不足している場合は、ImportErrorを出力します。
"""
from .tokenizers import _SUDACHI_TOKENIZER, _SUDACHI_MODE, has_sudachi


def active_japanese_tokenizer():
    """
    Return which Japanese tokenizer backend is active: 'sudachi' or 'fallback'.
    使用中の日本語トークナイザーのバックエンドを返す機能：
    Sudachiを使う際は'sudachi' 、Sudachiがインストールされていない場合は 'fallback'と表示。
    """
    return 'sudachi' if has_sudachi() else 'fallback'


def split(text):
    """
    Split Japanese text using SudachiPy tokenizer when available; otherwise use a simple fallback.
    SudachiPyを使ってトークン化を行い、未インストール時は簡易フォールバックで分割します。
    """
    if not has_sudachi() or _SUDACHI_TOKENIZER is None or _SUDACHI_MODE is None:
        # Simple fallback: return non-space characters as tokens
        return [ch for ch in text if not ch.isspace()]

    # Sudachi returns morphemes; use surface() to get token strings
    return [m.surface() for m in _SUDACHI_TOKENIZER.tokenize(text, _SUDACHI_MODE)]


__all__ = ["split", "active_japanese_tokenizer"]
