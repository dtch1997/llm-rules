""" Evaluate a GPTModel on the ICL classification task. """
import pandas as pd 

from llm_rules.datasets.contains_part_of_speech import make_dataset
from llm_rules.datasets.utils import train_test_split
from llm_rules.model import GPTModel
from llm_rules.evaluate import evaluate_icl_classification

dataset = make_dataset("noun", 10)
model = GPTModel("gpt-3.5-turbo")

# Train-test split
train_examples, val_examples = train_test_split(dataset.data, test_size=0.2)
result = evaluate_icl_classification(model, train_examples, val_examples)


df = pd.DataFrame([
    {
        "prompt": d.prompt, 
        "response": d.response,
        "model_response": d.model_response,
        "is_correct": len(d.model_response) > 0 and d.response in d.model_response # substring
    }
    for d in result
])

pd.set_option('display.max_colwidth', None)
df.head()