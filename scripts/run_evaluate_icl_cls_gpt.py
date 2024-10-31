""" Evaluate a GPTModel on ICL classification tasks. """
import pandas as pd 
import simple_parsing

from dataclasses import dataclass
from llm_rules.model import Model
from llm_rules.core import LLMRuleData
from llm_rules.datasets.contains_part_of_speech import make_dataset
from llm_rules.datasets.utils import train_test_split
from llm_rules.model import GPTModel
from llm_rules.evaluate import evaluate_icl_classification, convert_results_to_df
from llm_rules.utils import RESULTS_DIR

@dataclass
class ExperimentConfig:
    model: str = "gpt-3.5-turbo"
    # Part of speech dataset config
    part_of_speech: str = "noun"
    # Generic dataset args
    n_samples: int = 10
    test_size: float = 0.5
    # Evaluation args
    n_icl_examples: int = 3 # number of ICL examples to use for each query example

def run_experiment(
    config: ExperimentConfig,
):
    model = GPTModel(config.model)
    dataset = make_dataset(config.part_of_speech, config.n_samples)
    train_examples, val_examples = train_test_split(dataset.data, test_size=0.5)
    result = evaluate_icl_classification(model, train_examples, val_examples, n_icl_examples=config.n_icl_examples)
    df = convert_results_to_df(result)

    # Print some info
    accuracy = df["is_correct"].mean()
    print(f"Accuracy: {accuracy:.2f}")

    # Save the results
    save_dir = RESULTS_DIR / f"icl_cls_{config.model}"
    save_dir.mkdir(exist_ok=True, parents=True)
    save_path = save_dir / f"{config.part_of_speech}_{config.n_samples}_{config.test_size}_{config.n_icl_examples}.parquet.gzip"
    df.to_parquet(save_path, compression="gzip")

if __name__ == "__main__":
    # for part_of_speech in ["noun", "adjective", "verb"]:
    #     config = ExperimentConfig(part_of_speech=part_of_speech)
    #     run_experiment(config)
    for n_icl_examples in [4, 10, 20]:
        config = ExperimentConfig(n_icl_examples=n_icl_examples)
        run_experiment(config)
        