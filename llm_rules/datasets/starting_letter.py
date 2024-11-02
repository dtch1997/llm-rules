""" Script to make dataset to distinguish words by their starting letter """

import random 
from typing import Literal

from llm_rules.core import LLMRuleData, LLMRuleDataset
from llm_rules.utils import ASSETS_DIR
from llm_rules.datasets.utils import load_word_corpus

def make_dataset(
    positive_letter: str,
    negative_letter: str,
    n_samples: int,
    seed: int = 0
):
    assert positive_letter != negative_letter, "positive_letter and negative_letter must be different."
    assert len(positive_letter) == 1, "positive_letter must be a single character."
    assert len(negative_letter) == 1, "negative_letter must be a single character."
    rng = random.Random(seed)

    words = load_word_corpus(ASSETS_DIR / "english_words" / f"nouns.txt")
    # Split words by starting letter
    pos_words = [word for word in words if word.startswith(positive_letter)]
    neg_words = [word for word in words if word.startswith(negative_letter)]

    data = []
    # positive examples
    for i in range(n_samples // 2):
        text = rng.choice(pos_words)
        data.append(LLMRuleData(text=text, label=1))

    # negative examples
    for i in range(n_samples // 2):
        text = rng.choice(neg_words)        
        data.append(LLMRuleData(text=text, label=0))

    rng.shuffle(data)
    return LLMRuleDataset(data=data, rule=f"The label is 1 if the word starts with '{positive_letter}' and 0 if it starts with '{negative_letter}'.")
