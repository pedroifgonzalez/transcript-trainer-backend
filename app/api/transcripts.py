from fastapi import APIRouter

from app.schemas.transcripts import (
    CompareTranscripts,
    CompareTranscriptsDiff,
    CompareTranscriptsResponse,
    DiffData,
    Stats,
)
from app.services.comparison import process_transcript_diff

router = APIRouter()


@router.post(
    "/compare",
    response_model=CompareTranscriptsResponse,
    response_model_exclude_none=True,
)
async def compare_transcripts(compare_transcripts: CompareTranscripts):
    diff_result = process_transcript_diff(
        created=compare_transcripts.modified_transcript,
        original=compare_transcripts.original_transcript,
        original_transcript_url=compare_transcripts.original_transcript_url,
    )
    if not diff_result:
        return CompareTranscriptsResponse(
            message="Transcripts comparison failed",
            data=None,
        )
    diff_data_models = [DiffData(**item) for item in diff_result["diff_data"]]
    stats_model = Stats(**diff_result["stats"])
    diff_model = CompareTranscriptsDiff(
        similarity=diff_result["similarity"],
        diff_data=diff_data_models,
        stats=stats_model,
    )
    return CompareTranscriptsResponse(
        message="Transcripts compared successfully",
        data=diff_model,
    )
