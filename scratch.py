from colorama import Fore

from llm_rules.datasets import make_case_dataset, make_word_count_dataset
from llm_rules.prompt import make_articulate_rules_prompt, make_icl_classification_prompt
from llm_rules.model import HuggingfaceModel
from llm_rules.evaluate import evaluate_icl_classification

a = make_case_dataset()
b = make_word_count_dataset()
model = HuggingfaceModel("EleutherAI/pythia-70m")

cl_prompt, cl_response = make_icl_classification_prompt(a
.data[0:3], a.data[3])
model_response = model(cl_prompt)
print(Fore.RESET + cl_prompt)
print(Fore.GREEN + cl_response)
print(Fore.BLUE + model_response)

# Train-test split
train_examples = a.data[0:3]
val_examples = a.data[3:4]
result = evaluate_icl_classification(model, train_examples, val_examples)
print(result)

ar_prompt, ar_response = make_articulate_rules_prompt(a.data, a.rule, [b.rule])
model_response = model(ar_prompt)

print(Fore.RESET + ar_prompt)
print(Fore.GREEN + ar_response)
response = model(cl_prompt)
print(Fore.BLUE + model_response)