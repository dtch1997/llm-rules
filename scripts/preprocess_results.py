import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

from IPython.display import display, HTML
from llm_rules.utils import RESULTS_DIR

selected_datasets = [
    "reptile_vs_mammal",
    "mammal_vs_bird",
    "bird_vs_fish",
    "fish_vs_reptile",
    "english_vs_french",
    "french_vs_german",
    "german_vs_malay",
    "malay_vs_english",
    "country_vs_not",
    "living_vs_nonliving",
    "sentiment",
    "male_vs_female",
    # "a_vs_b",
    # "upper_vs_lower",
    # "multiples_of_2",
    # "multiples_of_5",
    # "square_numbers",
]

if __name__ == "__main__":

    # Preprocess the classification results
    rows = []
    for dataset in selected_datasets:
        for n_icl_examples in [4, 10, 20]:
            df = pd.read_parquet(RESULTS_DIR / f"icl_cls_gpt-3.5-turbo_200_0.5/{dataset}_{n_icl_examples}.parquet.gzip")
            accuracy = df["is_correct"].mean()
            print(f"{dataset} {n_icl_examples} ICL examples: {accuracy:.2f}")

            rows.append({
                "dataset": dataset,
                "n_icl_examples": n_icl_examples,
                "accuracy": accuracy
            })
    cls_df = pd.DataFrame(rows)
    cls_df.to_parquet(RESULTS_DIR / "icl_cls_gpt-3.5-turbo_200_0.5_summary.parquet.gzip")

    # Preprocess the articulation results
    rows = []
    for dataset in selected_datasets:
        for n_icl_examples in [4, 10, 20]:
            df = pd.read_parquet(RESULTS_DIR / f"mcq_art_gpt-3.5-turbo_200_0.5_100/{dataset}_{n_icl_examples}.parquet.gzip")
            accuracy = df["is_correct"].mean()
            print(f"{dataset} {n_icl_examples} ICL examples: {accuracy:.2f}")

            rows.append({
                "dataset": dataset,
                "n_icl_examples": n_icl_examples,
                "accuracy": accuracy
            })
    art_df = pd.DataFrame(rows)
    art_df.to_parquet(RESULTS_DIR / "mcq_art_gpt-3.5-turbo_200_0.5_100_summary.parquet.gzip")
    