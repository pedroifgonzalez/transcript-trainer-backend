import pytest

from app.services.loaders import YouTubeTranscriptionLoader


@pytest.mark.vcr
def test_fetch_transcription():
    ytt_loader = YouTubeTranscriptionLoader()
    transcript = ytt_loader.fetch(
        url="https://www.youtube.com/watch?v=XyiPDoCjO4s&t=89s"
    )
    assert transcript.startswith("I could not live without lying.")
    assert transcript.endswith("Thank you. (Applause)")
