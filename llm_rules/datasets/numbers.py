""" Script to make dataset to distinguish different types of numbers """

import random 
from typing import Literal

from llm_rules.core import LLMRuleData, LLMRuleDataset
from llm_rules.utils import ASSETS_DIR

def make_multiples_dataset(
    multiple: int,
    n_samples: int,
    seed: int = 0
):
    """ Make a dataset to distinguish numbers that are multiples of a given number from those that are not. """
    assert multiple > 1, "The multiple must be greater than 1."
    rng = random.Random(seed)

    data = []
    # positive examples
    for i in range(n_samples // 2):
        num = multiple * rng.randint(1, 100)
        text = str(multiple * rng.randint(1, 100))
        data.append(LLMRuleData(text=text, label=1))

    # negative examples
    for i in range(n_samples // 2):
        num = multiple * rng.randint(1, 100) + 1
        text = str(rng.randint(1, 100))
        data.append(LLMRuleData(text=text, label=0))

    rng.shuffle(data)
    return LLMRuleDataset(data=data, rule=f"The label is 1 if the number is a multiple of {multiple} and 0 otherwise.")

def make_square_numbers_dataset(
    n_samples: int,
    seed: int = 0
):
    """ Make a dataset to distinguish square numbers from non-square numbers. """

    rng = random.Random(seed)

    data = []
    # positive examples
    for i in range(n_samples // 2):
        num = rng.randint(1, 25)
        text = str(num ** 2)
        data.append(LLMRuleData(text=text, label=1))

    # negative examples
    for i in range(n_samples // 2):
        num = rng.randint(1, 25)
        text = str(num * num + 1)
        data.append(LLMRuleData(text=text, label=0))

    rng.shuffle(data)
    return LLMRuleDataset(data=data, rule="The label is 1 if the number is a square number and 0 otherwise.")