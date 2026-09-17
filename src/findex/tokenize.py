import re
import unicodedata
from collections.abc import Iterator

WORD_RE = re.compile(r"\w+(?:['’]\w+)*", re.UNICODE)


def tokenize(text: str) -> Iterator[str]:
    """Потокова токенізація текстів із поверненням ітератора токенів."""
    if not text:
        return

    normalized = unicodedata.normalize("NFC", text)
    folded = normalized.casefold()

    for match in WORD_RE.finditer(folded):
        yield match.group()
