""" Prompt templates for evaluating LLMs. """

import random
from llm_rules.core import LLMRuleData

def get_unique_random_seed(rules: list[str]) -> int:
    """ Generate a unique random seed for a given list of rules. """
    seed = hash("".join(rules))
    random.seed(seed)
    return random.randint(0, 1000000)

def make_icl_classification_prompt(
    icl_examples: list[LLMRuleData],
    query_example: LLMRuleData,
) -> tuple[str, str]:
    """ Prompt the model to classify a new example according to the rule used to label a set of examples. """
    prompt = "Here are some texts labelled according to a simple classification rule.\n\n"

    # seed according to query example
    random.seed(hash(query_example.text))

    # randomly shuffle the data
    random.shuffle(icl_examples)
    for data in icl_examples:
        prompt += f"Text: {data.text}\n"
        prompt += f"Label: {data.label}\n\n"
    
    prompt += "Which label would you assign to the following text?\n\n"
    prompt += f"Text: {query_example.text}\n"
    prompt += f"Label: "

    response = f"{query_example.label}"
    return prompt, response

def make_articulate_rules_prompt(
    icl_examples: list[LLMRuleData],
    true_rule: str,
    incorrect_rules: list[str],
    seed: int | None = None
) -> tuple[str, str]:
    """ Prompt the model to articulate the rule used to label a set of examples. """
    prompt = "Here are some texts labelled according to a simple classification rule.\n\n"

    # seed according to true rule 
    random.seed(hash(true_rule))

    # randomly shuffle the data
    random.shuffle(icl_examples)
    for data in icl_examples:
        prompt += f"Text: {data.text}\n"
        prompt += f"Label: {data.label}\n\n"
    
    prompt += "Which of the following rules could have been used to label the texts?\n\n"
    rules = [true_rule] + incorrect_rules
    if seed is None:
        seed = get_unique_random_seed(rules)

    # randomly order the rules 
    indices = list(range(len(rules)))
    random.shuffle(indices)
    for i, idx in enumerate(indices):
        prompt += f"({i + 1}) {rules[idx]}\n"

    correct_idx = indices.index(0) + 1
    prompt += "\n Answer: ("
    response = f"{correct_idx}"

    return prompt, response
    