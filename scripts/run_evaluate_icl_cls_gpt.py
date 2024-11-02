""" Evaluate a GPTModel on ICL classification tasks. """
import pandas as pd 
import simple_parsing

from dataclasses import dataclass
from llm_rules.model import Model
from llm_rules.core import LLMRuleData
from llm_rules.datasets import build_dataset
from llm_rules.datasets.utils import train_test_split
from llm_rules.model import GPTModel
from llm_rules.evaluate import evaluate_icl_classification, convert_results_to_df
from llm_rules.utils import RESULTS_DIR

selected_datasets = [
    "reptile_vs_mammal",
    "english_vs_french",
    "male_vs_female",
    "a_vs_b",
    "upper_vs_lower",
    "multiple_of_2",
    "multiple_of_5",
    "square_numbers",
]

@dataclass
class ExperimentConfig:
    dataset: str
    model: str = "gpt-3.5-turbo"
    # Generic dataset args
    n_samples: int = 50
    test_size: float = 0.2
    # Evaluation args
    n_icl_examples: int = 3 # number of ICL examples to use for each query example
    seed: int = 0

def run_experiment(
    config: ExperimentConfig,
):
    model = GPTModel(config.model)
    dataset = build_dataset(config.dataset, n_samples = config.n_samples, seed=config.seed)
    train_examples, val_examples = train_test_split(dataset.data, test_size=config.test_size)
    result = evaluate_icl_classification(model, train_examples, val_examples, n_icl_examples=config.n_icl_examples)
    df = convert_results_to_df(result)

    # Print some info
    accuracy = df["is_correct"].mean()
    print(f"Accuracy: {accuracy:.2f}")

    # Save the results
    save_dir = RESULTS_DIR / f"icl_cls_{config.model}"
    save_dir.mkdir(exist_ok=True, parents=True)
    save_path = save_dir / f"{config.dataset}_{config.n_icl_examples}.parquet.gzip"
    df.to_parquet(save_path, compression="gzip")

if __name__ == "__main__":
    for dataset in selected_datasets:
        for n_icl_examples in [4, 10, 20]:
            config = ExperimentConfig(dataset=dataset, n_icl_examples=n_icl_examples)
            try: 
                run_experiment(config)
            except Exception as e:
                print(f"Error while running experiment with config: {config}")
                print(e)
                continue   