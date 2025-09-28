"""
Preprocessing services.
"""

import re


def normalize_text(text: str) -> str:
    """Basic normalization: lowercase, remove punctuation, collapse spaces"""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    text = re.sub(r"\s+", " ", text)  # collapse multiple spaces
    return text.strip()
