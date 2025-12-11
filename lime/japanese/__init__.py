"""Japanese-specific text processing utilities for LIME.

Export a small, stable API and keep implementation details in separate
modules. Users can import `lime.japanese` when they need Japanese-specific
functionality.
"""

from .splitters import mecab_unidic_split  # type: ignore
from .tokenizers import has_fugashi  # type: ignore

__all__ = ["mecab_unidic_split", "has_fugashi"]
