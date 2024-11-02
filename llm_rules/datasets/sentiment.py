""" Script to make dataset to distinguish positive and negative sentiment """

import random 
from typing import Literal

from llm_rules.core import LLMRuleData, LLMRuleDataset
from llm_rules.utils import ASSETS_DIR
from llm_rules.datasets.utils import load_word_corpus

def make_dataset(
    n_samples: int,
    seed: int = 0
):
    
    rng = random.Random(seed)

    positive_words = load_word_corpus(ASSETS_DIR / "english_words" / "positive.txt")
    negative_words = load_word_corpus(ASSETS_DIR / "english_words" / "negative.txt")

    data = []
    # positive examples
    for i in range(n_samples // 2):
        text = rng.choice(positive_words)
        data.append(LLMRuleData(text=text, label=1))

    # negative examples
    for i in range(n_samples // 2):
        text = rng.choice(negative_words)
        data.append(LLMRuleData(text=text, label=0))

    rng.shuffle(data)
    return LLMRuleDataset(data=data, rule=f"The label is 1 if the word is positive and 0 if it is negative.")