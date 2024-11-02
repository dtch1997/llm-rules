import random 
import pandas as pd
import tqdm

from dataclasses import dataclass
from llm_rules.model import Model
from llm_rules.datasets.debug import LLMRuleDataset, LLMRuleData
from llm_rules.prompt import make_icl_classification_prompt, make_articulate_rules_prompt

@dataclass
class EvalResult:
    prompt: str
    response: str
    model_response: str 

def get_balanced_icl_examples(
    train_examples: list[LLMRuleData],
    n_icl_examples: int,
    rng: random.Random,
):
    """ Get a balanced set of ICL examples, ensuring that there are an equal number of positive and negative examples. """
    positive_examples = [d for d in train_examples if d.label == 1]
    negative_examples = [d for d in train_examples if d.label == 0]
    n_positive = n_icl_examples // 2
    n_negative = n_icl_examples - n_positive

    positive_icl_examples = rng.sample(positive_examples, n_positive)
    negative_icl_examples = rng.sample(negative_examples, n_negative)
    all_examples = positive_icl_examples + negative_icl_examples
    rng.shuffle(all_examples)
    return all_examples

def evaluate_icl_classification(
    model: Model,
    train_examples: list[LLMRuleData],
    val_examples: list[LLMRuleData],
    *,
    n_icl_examples: int = 3,
    description: str = "Evaluating ICL classification",
    disable_tqdm: bool = False,
) -> list[EvalResult]:
    """ Evaluate the model's ability to classify new examples according to a simple classification rule. """

    seed = hash(train_examples[0].text)
    rng = random.Random(seed)

    data = [] 
    for query_example in tqdm.tqdm(val_examples, desc=description, disable=disable_tqdm):        
        icl_examples = get_balanced_icl_examples(train_examples, n_icl_examples, rng)
        prompt, response = make_icl_classification_prompt(icl_examples, query_example)
        model_response = model(prompt)
        data.append(EvalResult(prompt=prompt, response=response, model_response=model_response))
    
    return data

def convert_results_to_df(
    results: list[EvalResult]
) -> pd.DataFrame:
    """ Convert a list of evaluation results to a pandas DataFrame. """
    return pd.DataFrame([
        {
            "prompt": d.prompt, 
            "response": d.response,
            "model_response": d.model_response,
            # NOTE: Here, the 'correctness' is determined by whether the model's response is a substring of the true response
            # This is designed for the MCQ format where the response is a single number
            # For the freeform prompt template, this may need to be adjusted
            "is_correct": len(d.model_response) > 0 and d.response in d.model_response # substring
        }
        for d in results
    ])


def evaluate_icl_articulation(
    model: Model,
    train_examples: list[LLMRuleData],
    true_rule: str,
    distractor_rules: list[str],
    *,
    n_icl_examples: int = 3,
    n_evaluations: int = 10,
    n_incorrect_rules: int = 3,
    description: str = "Evaluating ICL articulation",
    disable_tqdm: bool = False,
) -> list[EvalResult]:
    """ Evaluate the model's ability to articulate the rule used to label a set of examples. """

    seed = hash(train_examples[0].text)
    rng = random.Random(seed)

    data = [] 
    for _ in tqdm.tqdm(range(n_evaluations), desc=description, disable=disable_tqdm):        
        icl_examples = get_balanced_icl_examples(train_examples, n_icl_examples, rng)
        incorrect_rules = rng.sample(distractor_rules, n_incorrect_rules)
        prompt, response = make_articulate_rules_prompt(icl_examples, true_rule, incorrect_rules)
        model_response = model(prompt)
        data.append(EvalResult(prompt=prompt, response=response, model_response=model_response))
    
    return data