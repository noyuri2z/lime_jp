"""
Japanese-specific text processing utilities for LIME.

Export a small, stable API and keep implementation details in separate
modules. Users can import `lime.japanese` when they need Japanese-specific
functionality.

日本語でLIMEを使用する際にのみ必要な機能をまとめたファイル。

"""

from .splitters import split as splitter, active_japanese_tokenizer  # type: ignore

__all__ = [
    "splitter",
    "active_japanese_tokenizer",
]
