""" Script to make dataset to distinguish English and French words """

import random 
from typing import Literal

from llm_rules.core import LLMRuleData, LLMRuleDataset
from llm_rules.utils import ASSETS_DIR
from llm_rules.datasets.utils import load_word_corpus

def make_dataset(
    positive_language: Literal["english", "french"],
    n_samples: int,
    seed: int = 0
):
    
    rng = random.Random(seed)

    pos_names = load_word_corpus(ASSETS_DIR / "english_words" / f"{positive_language}.txt")
    negative_language = "english" if positive_language == "french" else "english"
    neg_names = load_word_corpus(ASSETS_DIR / "english_words" / f"{negative_language}.txt")

    data = []
    # positive examples
    for i in range(n_samples // 2):
        text = rng.choice(pos_names)
        data.append(LLMRuleData(text=text, label=1))

    # negative examples
    for i in range(n_samples // 2):
        text = rng.choice(neg_names)
        data.append(LLMRuleData(text=text, label=0))

    rng.shuffle(data)
    return LLMRuleDataset(data=data, rule=f"The label is 1 if the word is {positive_language} and 0 if it is {negative_language}.")