from colorama import Fore

from llm_rules.datasets.debug import make_case_dataset, make_word_count_dataset
from llm_rules.prompt import make_articulate_rules_prompt, make_icl_classification_prompt
from llm_rules.model import HuggingfaceModel
from llm_rules.evaluate import evaluate_icl_classification

a = make_case_dataset()
b = make_word_count_dataset()
model = HuggingfaceModel("EleutherAI/pythia-70m")





from llm_rules.datasets.exactly_k_words import make_dataset
from llm_rules.datasets.utils import train_test_split

k_words_dataset = make_dataset(3, 10)
print(k_words_dataset.data)
train_examples, val_examples = train_test_split(k_words_dataset.data, test_size=0.2)
result = evaluate_icl_classification(model, train_examples, val_examples)
print(result)

print(len(result))

import pandas as pd 


df = pd.DataFrame([
    {
        "prompt": d.prompt, 
        "response": d.response,
        "model_response": d.model_response,
        "is_correct": len(d.model_response) > 0 and d.model_response.contains(d.response)
    }
    for d in result
])
print(df)

# # Debugging
# cl_prompt, cl_response = make_icl_classification_prompt(a
# .data[0:3], a.data[3])
# model_response = model(cl_prompt)
# print(Fore.RESET + cl_prompt)
# print(Fore.GREEN + cl_response)
# print(Fore.BLUE + model_response)

# ar_prompt, ar_response = make_articulate_rules_prompt(a.data, a.rule, [b.rule])
# model_response = model(ar_prompt)

# print(Fore.RESET + ar_prompt)
# print(Fore.GREEN + ar_response)
# response = model(cl_prompt)
# print(Fore.BLUE + model_response)