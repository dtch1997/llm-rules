""" Script to make dataset to distinguish names of countries from non-countries """

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

    countries = load_word_corpus(ASSETS_DIR / "english_words" / "countries.txt")
    non_countries = load_word_corpus(ASSETS_DIR / "english_words" / "nouns.txt")

    data = []
    # positive examples
    for i in range(n_samples // 2):
        text = rng.choice(countries)
        data.append(LLMRuleData(text=text, label=1))

    # negative examples
    for i in range(n_samples // 2):
        text = rng.choice(non_countries)
        data.append(LLMRuleData(text=text, label=0))

    rng.shuffle(data)
    return LLMRuleDataset(data=data, rule=f"The label is 1 if the word is a country and 0 if it is not.")