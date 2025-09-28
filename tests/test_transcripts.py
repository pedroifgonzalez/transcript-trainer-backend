import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app, base_url="http://localhost")


def test_compare_transcripts():
    original_transcript = "This is the original transcript."
    modified_transcript = "Thi is the modified transcrypt."
    response = client.post(
        "/transcripts/compare",
        json={
            "original_transcript": original_transcript,
            "modified_transcript": modified_transcript,
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Transcripts compared successfully",
        "data": {
            "similarity": 78.68852459016394,
            "diff_data": [
                {"category": "equal", "text": "Thi", "position": 0},
                {"category": "delete", "text": "s", "position": 3},
                {"category": "equal", "text": " is the ", "position": 4},
                {"category": "insert", "text": "m", "position": 12},
                {"category": "equal", "text": "o", "position": 12},
                {
                    "category": "replace",
                    "original": "r",
                    "created": "d",
                    "position": 13,
                },
                {"category": "equal", "text": "i", "position": 14},
                {
                    "category": "replace",
                    "original": "g",
                    "created": "f",
                    "position": 15,
                },
                {"category": "equal", "text": "i", "position": 16},
                {
                    "category": "replace",
                    "original": "nal",
                    "created": "ed",
                    "position": 17,
                },
                {"category": "equal", "text": " transcr", "position": 20},
                {
                    "category": "replace",
                    "original": "i",
                    "created": "y",
                    "position": 28,
                },
                {"category": "equal", "text": "pt.", "position": 29},
            ],
            "stats": {
                "accuracy": 78.7,
                "total_words": 5,
                "correct_words": 2,
                "errors": 3,
            },
        },
    }


@pytest.mark.vcr(ignore_localhost=True)
def test_compare_transcripts_with_url():
    response = client.post(
        "/transcripts/compare",
        json={
            "original_transcript_url": "https://www.youtube.com/watch?v=ry9SYnV3svc",
            "modified_transcript": """
            so whats new mark how is your new job going to be honest i cant
            complain i really love the company that i am working for my coworkers
            are all really friendly and helpful they really help me feel welcome
            its a really energetic and fun atmosphere my boss is hilarious and hes
            really flexible really how so he allows me to come in when i want and
            make my own hours i can also leave early if i start early there is no
            real dress code either i can wear jeans and a tshirt if i want i can
            even wear shorts in the summer wow it sounds really cool i cant stand
            wearing a suit every day which do you prefer working late or finishing
            early i prefer finishing early i really enjoy the morning i love getting
            up early and going for a run theres nothing like watching the sunrise
            while drinking my morning coffee really i am opposite i love sleeping
            in i am most alert in the evenings im a real night owl well you know
            what they say the early bird catches the worm you know you could be
            right maybe i will try to go to bed a little earlier tonight
            """,
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Transcripts compared successfully",
        "data": {
            "similarity": 100.0,
            "diff_data": [
                {
                    "category": "replace",
                    "original": "so what'",
                    "created": "\n            so what",
                    "position": 0,
                },
                {
                    "category": "equal",
                    "text": "s new mark how is your new job going to be honest i can",
                    "position": 8,
                },
                {
                    "category": "replace",
                    "original": "'t",
                    "created": "t\n           ",
                    "position": 63,
                },
                {
                    "category": "equal",
                    "text": " complain i really love the company that i am working for my co",
                    "position": 65,
                },
                {"category": "delete", "text": "-", "position": 128},
                {"category": "equal", "text": "workers ", "position": 129},
                {"category": "insert", "text": "            ", "position": 137},
                {
                    "category": "equal",
                    "text": "are all really friendly and helpful they really help me feel welcome ",
                    "position": 137,
                },
                {
                    "category": "replace",
                    "original": "it'",
                    "created": "            it",
                    "position": 206,
                },
                {
                    "category": "equal",
                    "text": "s a really energetic and fun atmosphere my boss is hilarious and he",
                    "position": 209,
                },
                {
                    "category": "replace",
                    "original": "'s",
                    "created": "s\n           ",
                    "position": 276,
                },
                {
                    "category": "equal",
                    "text": " really flexible really how so he allows me to come in when i want and ",
                    "position": 278,
                },
                {"category": "insert", "text": "            ", "position": 349},
                {
                    "category": "equal",
                    "text": "make my own hours i can also leave early if i start early there is no ",
                    "position": 349,
                },
                {"category": "insert", "text": "            ", "position": 419},
                {
                    "category": "equal",
                    "text": "real dress code either i can wear jeans and a t",
                    "position": 419,
                },
                {
                    "category": "replace",
                    "original": "-shirt if i want i can",
                    "created": "shirt if i want i can\n           ",
                    "position": 466,
                },
                {
                    "category": "equal",
                    "text": " even wear shorts in the summer wow it sounds really cool i can",
                    "position": 488,
                },
                {
                    "category": "replace",
                    "original": "'t stand",
                    "created": "t stand\n           ",
                    "position": 551,
                },
                {
                    "category": "equal",
                    "text": " wearing a suit every day which do you prefer working late or finishing ",
                    "position": 559,
                },
                {"category": "insert", "text": "            ", "position": 631},
                {
                    "category": "equal",
                    "text": "early i prefer finishing early i really enjoy the morning i love getting ",
                    "position": 631,
                },
                {"category": "insert", "text": "            ", "position": 704},
                {
                    "category": "equal",
                    "text": "up early and going for a run there",
                    "position": 704,
                },
                {"category": "delete", "text": "'", "position": 738},
                {
                    "category": "equal",
                    "text": "s nothing like watching the sunrise",
                    "position": 739,
                },
                {"category": "insert", "text": "\n           ", "position": 774},
                {
                    "category": "equal",
                    "text": " while drinking my morning coffee really i am opposite i love sleeping ",
                    "position": 774,
                },
                {"category": "insert", "text": "            ", "position": 845},
                {
                    "category": "equal",
                    "text": "in i am most alert in the evenings i",
                    "position": 845,
                },
                {"category": "delete", "text": "'", "position": 881},
                {
                    "category": "equal",
                    "text": "m a real night owl well you know ",
                    "position": 882,
                },
                {"category": "insert", "text": "            ", "position": 915},
                {
                    "category": "equal",
                    "text": "what they say the early bird catches the worm you know you could be ",
                    "position": 915,
                },
                {"category": "insert", "text": "            ", "position": 983},
                {
                    "category": "equal",
                    "text": "right maybe i will try to go to bed a little earlier tonight",
                    "position": 983,
                },
                {"category": "insert", "text": "\n            ", "position": 1043},
            ],
            "stats": {
                "accuracy": 100.0,
                "total_words": 208,
                "correct_words": 208,
                "errors": 0,
            },
        },
    }
