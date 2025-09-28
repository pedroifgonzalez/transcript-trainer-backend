"""
Compare two transcripts and return the differences.
Statistics include accuracy, total words, correct words, and errors.
"""

import difflib
import enum
from typing import List, Optional, TypedDict

from rapidfuzz import fuzz

from app.services.loaders import YouTubeTranscriptionLoader
from app.services.preprocessing import normalize_text

loader = YouTubeTranscriptionLoader()


class Tag(str, enum.Enum):
    EQUAL = "equal"
    DELETE = "delete"
    INSERT = "insert"
    REPLACE = "replace"


class DiffDataDict(TypedDict, total=False):
    category: Tag
    text: str
    original: str
    created: str
    position: int


class StatsDict(TypedDict):
    accuracy: float
    total_words: int
    correct_words: int
    errors: int


class TranscriptDiffDict(TypedDict):
    similarity: float
    diff_data: List[DiffDataDict]
    stats: StatsDict


def process_transcript_diff(
    created: str,
    original: Optional[str] = None,
    original_transcript_url: Optional[str] = None,
) -> Optional[TranscriptDiffDict]:
    """
    Compare transcripts using normalized text for accuracy,
    but return diffs based on original text for highlighting.
    """

    # Get original transcript
    content = original
    if not content and original_transcript_url:
        content = loader.fetch(original_transcript_url)

    if not content:
        return None

    # Normalize for diff
    diff_content = content.replace("\n", " ").replace("\t", " ")
    diff_created = created.replace("\n", " ").replace("\t", " ")

    # Normalize for scoring
    norm_original = normalize_text(diff_content)
    norm_created = normalize_text(diff_created)

    # Get similarity score (normalized)
    similarity = fuzz.ratio(norm_original, norm_created)

    # Diff on *original* text for highlighting
    differ = difflib.SequenceMatcher(None, diff_content, diff_created)
    diff_data: List[DiffDataDict] = []

    for tag, i1, i2, j1, j2 in differ.get_opcodes():
        if tag == Tag.EQUAL:
            diff_data.append(
                {
                    "category": Tag.EQUAL,
                    "text": content[i1:i2],
                    "position": i1,
                }
            )
        elif tag == Tag.DELETE:
            diff_data.append(
                {
                    "category": Tag.DELETE,
                    "text": content[i1:i2],
                    "position": i1,
                }
            )
        elif tag == Tag.INSERT:
            diff_data.append(
                {
                    "category": Tag.INSERT,
                    "text": created[j1:j2],
                    "position": i1,
                }
            )
        elif tag == Tag.REPLACE:
            diff_data.append(
                {
                    "category": Tag.REPLACE,
                    "original": content[i1:i2],
                    "created": created[j1:j2],
                    "position": i1,
                }
            )

    original_words = norm_original.split()
    created_words = norm_created.split()

    word_errors = sum(
        1
        for i, word in enumerate(original_words)
        if i >= len(created_words) or word != created_words[i]
    )

    return {
        "similarity": similarity,
        "diff_data": diff_data,
        "stats": {
            "accuracy": round(similarity, 1),
            "total_words": len(original_words),
            "correct_words": len(original_words) - word_errors,
            "errors": word_errors,
        },
    }
