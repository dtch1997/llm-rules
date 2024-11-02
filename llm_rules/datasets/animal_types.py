""" Script to make dataset to distinguish different types of animal """

import random 
from typing import Literal

from llm_rules.core import LLMRuleData, LLMRuleDataset
from llm_rules.utils import ASSETS_DIR
from llm_rules.datasets.utils import load_word_corpus

def make_dataset(
    pos_animal_type: Literal["mammal", "bird", "fish", "reptile"],
    neg_animal_type: Literal["mammal", "bird", "fish", "reptile"],
    n_samples: int,
    seed: int = 0
):
    
    assert pos_animal_type != neg_animal_type, "pos_animal_type and neg_animal_type must be different."
    rng = random.Random(seed)

    pos_animals = load_word_corpus(ASSETS_DIR / "english_words" / f"{pos_animal_type}.txt")
    neg_animals = load_word_corpus(ASSETS_DIR / "english_words" / f"{neg_animal_type}.txt")

    data = []
    # positive examples
    for i in range(n_samples // 2):
        text = rng.choice(pos_animals)
        data.append(LLMRuleData(text=text, label=1))

    # negative examples
    for i in range(n_samples // 2):
        text = rng.choice(neg_animals)
        data.append(LLMRuleData(text=text, label=0))

    rng.shuffle(data)
    return LLMRuleDataset(data=data, rule=f"The label is 1 if the word is a {pos_animal_type} and 0 if it is a {neg_animal_type}.")