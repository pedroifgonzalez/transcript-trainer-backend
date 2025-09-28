from typing import Optional

from youtube_transcript_api import YouTubeTranscriptApi


class YouTubeTranscriptionLoader:

    def __init__(self) -> None:
        self.ytt_api = YouTubeTranscriptApi()

    def fetch(self, url: str) -> Optional[str]:
        """
        Fetch the transcript from a YouTube video's url
        """
        query_params = url.split("?")[-1]
        key_value_pairs = query_params.split("&")
        video_id_pair = next(
            (pair for pair in key_value_pairs if pair.startswith("v=")), None
        )
        if not video_id_pair:
            return None
        video_id = video_id_pair.split("=")[1]
        fetched_transcript = self.ytt_api.fetch(video_id)
        return " ".join([snippet.text for snippet in fetched_transcript])
