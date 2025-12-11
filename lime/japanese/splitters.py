"""High-level splitter functions for Japanese text.

These functions use singleton tokenizer instances from tokenizers.py and
provide simple splitter APIs. They raise ImportError with clear instructions
if required libraries are missing.
"""
from .tokenizers import _SUDACHI_TOKENIZER, _SUDACHI_MODE, has_sudachi


def active_japanese_tokenizer():
    """Return which Japanese tokenizer backend is active: 'sudachi' or 'fallback'."""
    if has_sudachi():
        return 'sudachi'
    return 'fallback'


def mecab_unidic_split(text):
    """Split Japanese text using Sudachi when available, else a simple fallback.

    Note: despite the name, this now uses Sudachi for tokenization to avoid
    external dictionary management. The API remains the same.
    """
    if has_sudachi():
        # Sudachi returns morphemes; use surface() to get token strings
        return [m.surface() for m in _SUDACHI_TOKENIZER.tokenize(text, _SUDACHI_MODE)]

    # Simple fallback: return non-space characters as tokens.
    return [ch for ch in text if not ch.isspace()]


__all__ = ["mecab_unidic_split", "active_japanese_tokenizer"]
