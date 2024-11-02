""" Script to make dataset to distinguish capitalised and non-capitalised words """

import random 
from typing import Literal

from llm_rules.core import LLMRuleData, LLMRuleDataset
from llm_rules.utils import ASSETS_DIR
from llm_rules.datasets.utils import load_word_corpus

def make_dataset(
    positive_case: Literal["upper", "lower"],
    n_samples: int,
    seed: int = 0
):
    
    rng = random.Random(seed)

    negative_case = "upper" if positive_case == "lower" else "lower"
    words = load_word_corpus(ASSETS_DIR / "english_words" / f"english.txt")

    data = []
    # positive examples
    for i in range(n_samples // 2):
        text = rng.choice(words)
        if positive_case == "upper":
            text = text.upper()
        else:
            text = text.lower()
        data.append(LLMRuleData(text=text, label=1))

    # negative examples
    for i in range(n_samples // 2):
        text = rng.choice(words)
        if positive_case == "upper":
            text = text.lower()
        else:
            text = text.upper()
        data.append(LLMRuleData(text=text, label=0))

    rng.shuffle(data)
    return LLMRuleDataset(data=data, rule=f"The label is 1 if the word is {positive_case}-case and 0 if it is {negative_case}-case.")