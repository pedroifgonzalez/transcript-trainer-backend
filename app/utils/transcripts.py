def get_frequency_dict(transcript: str) -> dict[str, int]:
    """
    Get a dictionary with the number of ocurrences per word
    """
    words = transcript.split()
    return {word: words.count(word) for word in words}


def get_max_clozes(words: list[str]) -> int:
    """
    Get the maximum number of clozes to generate
    """
    return max(1, int(len(words) * 0.35))
