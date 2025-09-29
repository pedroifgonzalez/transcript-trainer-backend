import re

from nltk.corpus import stopwords


class ClozesGenerator:

    def __init__(self, language: str = "english"):
        self.stopwords = set(stopwords.words(language))

    def generate(self, snippet, freq_dict, max_clozes=2) -> str:
        """
        Generate clozes from a snippet of text
        """
        tokens = re.findall(
            r"[A-Za-z0-9]+(?:'[A-Za-z0-9]+)*|[^\w\s]", snippet, re.UNICODE
        )
        words = [t for t in tokens if re.match(r"[A-Za-z0-9]", t)]
        candidates = []
        for w in words:
            lw = w.lower()
            if lw in self.stopwords:
                continue
            freq = freq_dict.get(lw, 1)
            candidates.append((lw, freq))

        candidates.sort(key=lambda x: x[1])  # rarer first
        chosen = {w for w, _ in candidates[:max_clozes]}

        # Rebuild with clozes
        cloze_tokens = []
        counter = 1
        for t in tokens:
            if re.match(r"[A-Za-z0-9]", t) and t.lower() in chosen:
                cloze_tokens.append(f"{{{{c{counter}::{t}}}}}")
                counter += 1
            else:
                cloze_tokens.append(t)

        # Join with proper spacing
        result = ""
        for i, tok in enumerate(cloze_tokens):
            if i == 0:
                result += tok
            elif re.match(r"[,.!?;:)]", tok):
                result += tok  # no space before closing punctuation
            elif tok in ["'", "’"]:
                result += tok  # no space around apostrophes
            elif result.endswith("("):
                result += tok  # no space right after opening parenthesis
            else:
                result += " " + tok

        return result
