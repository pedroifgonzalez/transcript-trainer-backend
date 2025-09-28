from typing import List, Optional

from pydantic import BaseModel, Field

from app.services.comparison import Tag


class CompareTranscripts(BaseModel):
    original_transcript: str = Field(description="Original transcript")
    modified_transcript: str = Field(description="Modified transcript")


class Stats(BaseModel):
    accuracy: float = Field(description="Accuracy of the comparison")
    total_words: int = Field(
        description="Total number of words in the original transcript"
    )
    correct_words: int = Field(description="Number of correct words in the comparison")
    errors: int = Field(description="Number of errors in the comparison")


class DiffData(BaseModel):
    category: Tag = Field(description="Type of difference")
    text: Optional[str] = Field(None, description="Text of the difference")
    original: Optional[str] = Field(None, description="Original text")
    created: Optional[str] = Field(None, description="Created text")
    position: int = Field(description="Position of the difference")


class CompareTranscriptsDiff(BaseModel):
    similarity: float = Field(
        description="Similarity score between the two transcripts"
    )
    diff_data: List[DiffData] = Field(
        description="Differences between the two transcripts"
    )
    stats: Stats = Field(description="Statistics of the comparison")


class CompareTranscriptsResponse(BaseModel):
    message: str = Field(description="Message indicating the result of the comparison")
    data: CompareTranscriptsDiff = Field(description="Comparison results")
