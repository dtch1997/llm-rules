import random 

from dataclasses import dataclass
from llm_rules.model import Model
from llm_rules.datasets import LLMRuleDataset, LLMRuleData
from llm_rules.prompt import make_icl_classification_prompt, make_articulate_rules_prompt

@dataclass
class EvalResult:
    prompt: str
    response: str
    model_response: str

    @property 
    def is_correct(self) -> bool:
        return self.response[0] == self.model_response[0]    

def evaluate_icl_classification(
    model: Model,
    train_examples: list[LLMRuleData],
    val_examples: list[LLMRuleData],
    *,
    n_icl_examples: int = 3,
) -> list[EvalResult]:
    """ Evaluate the model's ability to classify new examples according to a simple classification rule. """

    seed = hash(train_examples[0].text)
    rng = random.Random(seed)

    data = [] 
    for query_example in val_examples:        
        icl_examples = rng.sample(train_examples, n_icl_examples)
        prompt, response = make_icl_classification_prompt(icl_examples, query_example)
        model_response = model(prompt)
        data.append(EvalResult(prompt=prompt, response=response, model_response=model_response))
    
    return data


def evaluate_icl_articulation(
    model: Model,
    train_examples: list[LLMRuleData],
    val_examples: list[LLMRuleData], 
    true_rule: str,
    distractor_rules: list[str],
    *,
    n_evaluations: int = 10,
    n_icl_examples: int = 3,
    n_incorrect_rules: int = 3,
) -> list[EvalResult]:
    """ Evaluate the model's ability to articulate the rule used to label a set of examples. """
    seed = hash(true_rule)
    rng = random.Random(seed)

    data = [] 
    for _ in range(n_evaluations):
        icl_examples = rng.sample(train_examples, n_icl_examples)
        incorrect_rules = rng.sample(distractor_rules, n_incorrect_rules)
        prompt, response = make_articulate_rules_prompt(icl_examples, true_rule, incorrect_rules)
        model_response = model(prompt)
        data.append(EvalResult(prompt=prompt, response=response, model_response=model_response))
    
    return data