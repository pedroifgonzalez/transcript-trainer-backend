from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


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
