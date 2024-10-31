""" Make datasets where the label is 1 if the word is a {noun / adjective / verb} and 0 otherwise """
import random 
from typing import Literal

from llm_rules.core import LLMRuleData, LLMRuleDataset
from llm_rules.utils import ASSETS_DIR
from llm_rules.datasets.utils import load_word_corpus

def make_dataset(
    part_of_speech: Literal["noun", "adjective", "verb"],
    n_samples: int,
    seed: int = 0
):
    """ Generate a dataset where the label is 1 if the word is a {noun / adjective / verb} and 0 otherwise. """
    assert part_of_speech in ["noun", "adjective", "verb"], "part_of_speech must be 'noun', 'adjective', or 'verb'."
    rng = random.Random(seed)

    nouns = load_word_corpus(ASSETS_DIR / "english_words" / "nouns.txt")
    adjectives = load_word_corpus(ASSETS_DIR / "english_words" / "adjectives.txt")
    verbs = load_word_corpus(ASSETS_DIR / "english_words" / "verbs.txt")

    if part_of_speech == "noun":
        correct_words = nouns
        incorrect_words = adjectives + verbs
    elif part_of_speech == "adjective":
        correct_words = adjectives
        incorrect_words = nouns + verbs
    elif part_of_speech == "verb":
        correct_words = verbs
        incorrect_words = nouns + adjectives

    data = []
    # positive examples
    for i in range(n_samples // 2):
        text = rng.choice(correct_words)
        data.append(LLMRuleData(text=text, label=1))

    # negative examples
    for i in range(n_samples // 2):
        text = rng.choice(incorrect_words)
        data.append(LLMRuleData(text=text, label=0))

    rng.shuffle(data)
    return LLMRuleDataset(data=data, rule=f"The label is 1 if the word is a {part_of_speech} and 0 otherwise.")
    