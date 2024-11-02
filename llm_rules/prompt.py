""" Prompt templates for evaluating LLMs. """

import random
from llm_rules.core import LLMRuleData

def get_unique_random_seed(strs: list[str]) -> int:
    """ Generate a unique random seed from a given list of strings. """
    return hash("".join(strs))

def make_icl_prompt(
    icl_examples: list[LLMRuleData],
    seed: int | None = None
) -> str:
    """ Prompt the model to classify a set of examples according to a simple classification rule. """
    prompt = "Here are some texts labelled according to a simple classification rule.\n\n"

    if seed is None:
        seed = get_unique_random_seed([data.text for data in icl_examples])

    rng = random.Random(seed)
    rng.shuffle(icl_examples)    
    for data in icl_examples:
        prompt += f"Text: {data.text}\n"
        prompt += f"Label: {data.label}\n\n"

    return prompt

def make_icl_classification_prompt(
    icl_examples: list[LLMRuleData],
    query_example: LLMRuleData,
) -> tuple[str, str]:
    """ Prompt the model to classify a new example according to the rule used to label a set of examples. """
    prompt = make_icl_prompt(icl_examples)    
    prompt += "Which label would you assign to the following text? Respond only with 0 or 1.\n\n"
    prompt += f"Text: {query_example.text}\n"
    prompt += f"Label: "

    response = f"{query_example.label}"
    return prompt, response

def make_mcq_articulation_prompt(
    icl_examples: list[LLMRuleData],
    true_rule: str,
    incorrect_rules: list[str],
    seed: int | None = None
) -> tuple[str, str]:
    """ Prompt the model to articulate the rule used to label a set of examples. """
    prompt = make_icl_prompt(icl_examples, seed)
    
    prompt += "Which of the following rules could have been used to label the texts? Choose from among the listed options. Respond only with the number corresponding to your choice.\n\n"
    rules = [true_rule] + incorrect_rules
    if seed is None:
        seed = get_unique_random_seed(rules)
    rng = random.Random(seed)

    # randomly order the rules 
    indices = list(range(len(rules)))
    rng.shuffle(indices)
    for i, idx in enumerate(indices):
        prompt += f"({i + 1}) {rules[idx]}\n"

    correct_idx = indices.index(0) + 1
    prompt += "\n Answer: ("
    response = f"{correct_idx}"

    return prompt, response
    
def make_freeform_articulation_prompt(
    icl_examples: list[LLMRuleData],
    true_rule: str,
    seed: int | None = None
) -> tuple[str, str]:
    """ Prompt the model to articulate the rule used to label a set of examples. """
    prompt = make_icl_prompt(icl_examples, seed)
    prompt += "What rule was used to label these texts?"

    response = true_rule
    return prompt, response

def make_judge_prompt(
    prompt: str, 
    response: str, 
    model_response: str
) -> str:
    """ Prompt a judge model to evaluate the model's response to a given prompt. """
    return f"Prompt: {prompt}\n\nTrue Response: {response}\n\nModel response: {model_response}\n\nWas the model response correct? Respond only with 'yes' or 'no'."