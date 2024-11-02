""" Script to make dataset to distinguish nonliving and living things """

import random 
from typing import Literal

from llm_rules.core import LLMRuleData, LLMRuleDataset
from llm_rules.utils import ASSETS_DIR
from llm_rules.datasets.utils import load_word_corpus

def load_nonliving_things():
    return (
        load_word_corpus(ASSETS_DIR / "english_words" / "musical_instruments.txt") 
        + load_word_corpus(ASSETS_DIR / "english_words" / "vehicles.txt")
        + load_word_corpus(ASSETS_DIR / "english_words" / "kitchen_utensils.txt")
        + load_word_corpus(ASSETS_DIR / "english_words" / "sports_equipment.txt")
        + load_word_corpus(ASSETS_DIR / "english_words" / "tools.txt")
    )

def load_living_things():
    return (
        load_word_corpus(ASSETS_DIR / "english_words" / "fish.txt")
        + load_word_corpus(ASSETS_DIR / "english_words" / "bird.txt")
        + load_word_corpus(ASSETS_DIR / "english_words" / "mammal.txt")
        + load_word_corpus(ASSETS_DIR / "english_words" / "reptile.txt") 
        + load_word_corpus(ASSETS_DIR / "english_words" / "plant.txt")
    )


def make_dataset(
    n_samples: int,
    seed: int = 0
):
    
    rng = random.Random(seed)

    nonliving_things = load_nonliving_things()
    living_things = load_living_things()

    data = []
    # positive examples
    for i in range(n_samples // 2):
        text = rng.choice(living_things)
        data.append(LLMRuleData(text=text, label=1))

    # negative examples
    for i in range(n_samples // 2):
        text = rng.choice(nonliving_things)
        data.append(LLMRuleData(text=text, label=0))

    rng.shuffle(data)
    return LLMRuleDataset(data=data, rule=f"The label is 1 if the word is a living thing and 0 if it is a nonliving thing.")