
from .animal_types import make_dataset as make_animal_types_dataset
from .languages import make_dataset as make_english_vs_french_dataset
from .country_vs_not import make_dataset as make_country_vs_not_dataset
from .living_vs_nonliving import make_dataset as make_living_vs_nonliving_dataset
from .sentiment import make_dataset as make_sentiment_dataset

from .male_vs_female import make_dataset as make_male_vs_female_dataset
from .uppercase_vs_lowercase import make_dataset as make_uppercase_vs_lowercase_dataset
from .starting_letter import make_dataset as make_starting_letter_dataset
from .numbers import make_multiples_dataset, make_square_numbers_dataset

from functools import partial, lru_cache

def _build_dataset_factories():
    dataset_factories = {}

    for pos_animal_type in ["mammal", "bird", "fish", "reptile"]:
        for neg_animal_type in ["mammal", "bird", "fish", "reptile"]:
            if pos_animal_type == neg_animal_type: continue
            dataset_factories[f"{pos_animal_type}_vs_{neg_animal_type}"] = partial(make_animal_types_dataset, pos_animal_type=pos_animal_type, neg_animal_type=neg_animal_type)

    for positive_language in ["english", "french", "german", "malay"]:
        for negative_language in ["english", "french", "german", "malay"]:
            if positive_language == negative_language: continue
            dataset_factories[f"{positive_language}_vs_{negative_language}"] = partial(make_english_vs_french_dataset, positive_language=positive_language, negative_language=negative_language)

    dataset_factories[f"country_vs_not"] = make_country_vs_not_dataset
    dataset_factories[f"living_vs_nonliving"] = make_living_vs_nonliving_dataset
    dataset_factories[f"sentiment"] = make_sentiment_dataset

    for positive_gender in ["male", "female"]:
        negative_gender = "male" if positive_gender == "female" else "female"
        dataset_factories[f"{positive_gender}_vs_{negative_gender}"] = partial(make_male_vs_female_dataset, positive_gender=positive_gender)

    # syntactic tasks

    for positive_case in ["upper", "lower"]:
        negative_case = "upper" if positive_case == "lower" else "lower"
        dataset_factories[f"{positive_case}_vs_{negative_case}"] = partial(make_uppercase_vs_lowercase_dataset, positive_case=positive_case)

    for positive_letter in "abc":
        for negative_letter in "abc":
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

@lru_cache(maxsize=1)
def list_datasets():
    return list(DATASET_FACTORIES.keys())

@lru_cache(maxsize=1)
def build_distractor_rules():
    datasets = list_datasets()
    distractor_rules = set()
    for dataset_id in datasets:
        dataset = build_dataset(dataset_id, n_samples=100)
        distractor_rules.add(dataset.rule)
    return list(distractor_rules)

__all__ = [
    "build_dataset",
    "list_datasets"
]