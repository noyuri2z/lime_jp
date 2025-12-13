"""
Singleton tokenizer instances for Japanese processing.
Use Sudachi. The tokenizer is instantiated once at import for performance.

日本語データの処理のためのシングルトントークナイザー。
Sudachiを使用。パフォーマンス向上のため、インポート時に一度だけインスタンス化されます。

"""

try:
    # SudachiPy API (compatible with sudachi.rs python bindings)
    from sudachipy import tokenizer as _sudachi_tokenizer  # type: ignore
    from sudachipy import dictionary as _sudachi_dictionary  # type: ignore

    _SUDACHI_TOKENIZER = _sudachi_dictionary.Dictionary().create()
    _SUDACHI_MODE = _sudachi_tokenizer.Tokenizer.SplitMode.C
except Exception:
    _SUDACHI_TOKENIZER = None
    _SUDACHI_MODE = None


def has_sudachi():
    """
    Return True if the Sudachi tokenizer was successfully initialized.
    Sudachiのトークナイザーがインストールされているか確認する機能。
    """
    return _SUDACHI_TOKENIZER is not None


__all__ = ["_SUDACHI_TOKENIZER", "_SUDACHI_MODE", "has_sudachi"]
