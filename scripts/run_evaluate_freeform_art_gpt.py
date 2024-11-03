""" Evaluate a GPTModel on ICL classification tasks. """

from dataclasses import dataclass
from llm_rules.datasets import build_dataset, build_distractor_rules
from llm_rules.datasets.utils import train_test_split
from llm_rules.model import GPTModel
from llm_rules.evaluate import evaluate_freeform_articulation, convert_judge_results_to_df
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

@dataclass
class ExperimentConfig:
    dataset: str
    model: str = "gpt-3.5-turbo"
    judge_model: str = "gpt-3.5-turbo"
    # Generic dataset args
    n_samples: int = 200
    test_size: float = 0.5
    # Evaluation args
    n_icl_examples: int = 3 # number of ICL examples to use for each query example
    n_evaluations: int = 100
    seed: int = 0

def run_experiment(
    config: ExperimentConfig,
):
    # Skip if the results already exist
    save_dir = RESULTS_DIR / f"freeform_art_{config.model}_{config.n_samples}_{config.test_size}_{config.n_evaluations}"
    save_dir.mkdir(exist_ok=True, parents=True)
    save_path = save_dir / f"{config.dataset}_{config.n_icl_examples}.parquet.gzip"
    if save_path.exists():
        print(f"Skipping experiment with config: {config}. Already exists.")
        return

    # Setup
    model = GPTModel(config.model)
    judge_model = GPTModel(config.judge_model)
    dataset = build_dataset(config.dataset, n_samples = config.n_samples, seed=config.seed)
    train_examples, _ = train_test_split(dataset.data, test_size=config.test_size)
    
    # Filter out the true rule
    distractor_rules = build_distractor_rules()
    distractor_rules = [r for r in distractor_rules if r != dataset.rule]


    # Run the experiment
    result = evaluate_freeform_articulation(
        model, 
        judge_model,
        train_examples, 
        true_rule = dataset.rule,
        n_icl_examples=config.n_icl_examples,
        n_evaluations=config.n_evaluations,
        description=f"Freeform articulation of {config.dataset} using {config.n_icl_examples} ICL examples.")
    df = convert_judge_results_to_df(result)

    # Print some info
    accuracy = df["is_correct"].mean()
    print(f"Accuracy: {accuracy:.2f}")

    # Save the results
    df.to_parquet(save_path, compression="gzip")

if __name__ == "__main__":
    for dataset in selected_datasets:
        for n_icl_examples in [20]:
            config = ExperimentConfig(dataset=dataset, n_icl_examples=n_icl_examples)
            try: 
                run_experiment(config)
            except Exception as e:
                print(f"Error while running experiment with config: {config}")
                print(e)
                continue