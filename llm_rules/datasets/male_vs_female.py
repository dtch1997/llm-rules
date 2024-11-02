""" Script to make dataset to distinguish male and female names """

import random 
from typing import Literal

from llm_rules.core import LLMRuleData, LLMRuleDataset
from llm_rules.utils import ASSETS_DIR
from llm_rules.datasets.utils import load_word_corpus

def make_dataset(
    positive_gender: Literal["male", "female"],
    n_samples: int,
    seed: int = 0
):
    
    rng = random.Random(seed)

    pos_names = load_word_corpus(ASSETS_DIR / "english_words" / f"{positive_gender}.txt")
    negative_gender = "male" if positive_gender == "female" else "female"
    neg_names = load_word_corpus(ASSETS_DIR / "english_words" / f"{negative_gender}.txt")

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
    return LLMRuleDataset(data=data, rule=f"The label is 1 if the word is a {positive_gender} name and 0 if it is a {negative_gender} name.")