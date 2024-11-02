
from .animal_types import make_dataset as make_animal_types_dataset
from .english_vs_french import make_dataset as make_english_vs_french_dataset
from .male_vs_female import make_dataset as make_male_vs_female_dataset
from .uppercase_vs_lowercase import make_dataset as make_uppercase_vs_lowercase_dataset
from .starting_letter import make_dataset as make_starting_letter_dataset
from .numbers import make_multiples_dataset, make_square_numbers_dataset

from functools import partial

def _build_dataset_factories():
    dataset_factories = {}

    for pos_animal_type in ["mammal", "bird", "fish", "reptile"]:
        for neg_animal_type in ["mammal", "bird", "fish", "reptile"]:
            if pos_animal_type == neg_animal_type: continue
            dataset_factories[f"{pos_animal_type}_vs_{neg_animal_type}"] = partial(make_animal_types_dataset, pos_animal_type=pos_animal_type, neg_animal_type=neg_animal_type)

    for positive_language in ["english", "french"]:
        negative_language = "english" if positive_language == "french" else "french"
        dataset_factories[f"{positive_language}_vs_{negative_language}"] = partial(make_english_vs_french_dataset, positive_language=positive_language)

    for positive_gender in ["male", "female"]:
        negative_gender = "male" if positive_gender == "female" else "female"
        dataset_factories[f"{positive_gender}_vs_{negative_gender}"] = partial(make_male_vs_female_dataset, positive_gender=positive_gender)

    for positive_case in ["uppercase", "lowercase"]:
        dataset_factories[f"{positive_case}_vs_other"] = partial(make_uppercase_vs_lowercase_dataset, positive_case=positive_case)

    for positive_letter in "abcdefghijklmnopqrstuvwxyz":
        for negative_letter in "abcdefghijklmnopqrstuvwxyz":
            if positive_letter == negative_letter: continue
            dataset_factories[f"{positive_letter}_vs_{negative_letter}"] = partial(make_starting_letter_dataset, positive_letter=positive_letter, negative_letter=negative_letter)

    for positive_number in (2, 3, 5, 7):
        dataset_factories[f"multiples_of_{positive_number}"] = partial(make_multiples_dataset, multiple=positive_number)

    dataset_factories[f"square_numbers"] = make_square_numbers_dataset
    return dataset_factories

DATASET_FACTORIES = _build_dataset_factories()

def build_dataset(
    dataset_id, n_samples, seed=0
):
    return DATASET_FACTORIES[dataset_id](n_samples=n_samples, seed=seed)

def list_datasets():
    return list(DATASET_FACTORIES.keys())

__all__ = [
    "build_dataset",
    "list_datasets"
]