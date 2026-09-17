import re
import unicodedata
from collections.abc import Iterator

# Політика токенізації:
# - Нормалізація: Застосовується NFC (Normalization Form C) для уніфікації символів з діакритичними знаками.
# - Згортання регістру: Використовується text.casefold() замість lower() для коректної роботи з різними мовами (включно з кирилицею).
# - Апострофи: Внутрішні апострофи (' та ’) зберігаються у складі слова (наприклад, "it's" або українські скорочення), використовуючи шаблон \w+(?:['’]\w+)*.
# - Дефіси: Розглядаються як розділювачі слів (наприклад, "state-of-the-art" розбивається на частини).
# - Цифри: Входять до складу токенів (наприклад, "v2" або "2026").

WORD_RE = re.compile(r"\w+(?:['’]\w+)*", re.UNICODE)


def tokenize(text: str) -> Iterator[str]:
    """Потокова токенізація текстів із поверненням ітератора токенів."""
    if not text:
        return

    normalized = unicodedata.normalize("NFC", text)
    folded = normalized.casefold()

    for match in WORD_RE.finditer(folded):
        yield match.group()
