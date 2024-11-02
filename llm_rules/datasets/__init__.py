
from .animal_types import make_dataset as make_animal_types_dataset
from .english_vs_french import make_dataset as make_english_vs_french_dataset
from .male_vs_female import make_dataset as make_male_vs_female_dataset
from .uppercase_vs_lowercase import make_dataset as make_uppercase_vs_lowercase_dataset
from .starting_letter import make_dataset as make_starting_letter_dataset
from .numbers import make_multiples_dataset, make_square_numbers_dataset

__all__ = [
    # Semantic tasks
    "make_animal_types_dataset",
    "make_english_vs_french_dataset",
    "make_male_vs_female_dataset",
    # Syntactic tasks
    "make_uppercase_vs_lowercase_dataset",
    "make_starting_letter_dataset",
    # Numerical tasks
    "make_multiples_dataset",
    "make_square_numbers_dataset"
]