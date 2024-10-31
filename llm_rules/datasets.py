""" Example datasets for the LLMRules package. """

from llm_rules.core import LLMRuleData, LLMRuleDataset

# TODO: improve the examples

def make_case_dataset() -> LLMRuleDataset:
    """ Generate a dataset where the label is 1 if the text is all uppercase and 0 if all lowercase. """
    # Create a list of LLMRuleData objects
    data = [
        LLMRuleData(text="HELLO", label=1),
        LLMRuleData(text="hello", label=0),
        LLMRuleData(text="WORLD", label=1),
        LLMRuleData(text="world", label=0),
    ]
    return LLMRuleDataset(data=data, rule="The label is 1 if the text is all uppercase and 0 if all lowercase.")

def make_word_count_dataset():
    """ Generate a dataset where the label is 1 if the text has more than 10 words and 0 otherwise. """
    data = [
        LLMRuleData(text="This is a short sentence.", label=0),
        LLMRuleData(text="This is a longer sentence with more than 10 words.", label=1),
    ]
    return LLMRuleDataset(data=data, rule="The label is 1 if the text has more than 10 words and 0 otherwise.")

