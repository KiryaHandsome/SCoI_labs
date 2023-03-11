import re
from constants import SENTENCE_PATTERN, NON_DECLARATIVE_SENTENCE_PATTERN, WORD_PATTERN, NUMBER_PATTERN, \
    ONE_WORD_ABBREVIATIONS, TWO_WORDS_ABBREVIATIONS


def count_sentences(text: str) -> int:
    lower_text = text.lower()
    amount = len(re.findall(SENTENCE_PATTERN, lower_text))

    for abbreviation in ONE_WORD_ABBREVIATIONS:
        amount -= lower_text.count(abbreviation)

    for abbreviation in TWO_WORDS_ABBREVIATIONS:
        amount -= lower_text.count(abbreviation) * 2

    return amount


def count_non_declarative_sentences(text: str) -> int:
    return len(re.findall(NON_DECLARATIVE_SENTENCE_PATTERN, text.lower()))

