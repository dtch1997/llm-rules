import random 

from llm_rules.core import LLMRuleData, LLMRuleDataset
from llm_rules.utils import ASSETS_DIR
from llm_rules.datasets.utils import load_word_corpus

def make_dataset(
    k: int,
    n_samples: int,
    *,
    seed: int = 0
) -> LLMRuleDataset:
    """ Generate a dataset where the label is 1 if the text has exactly k words and 0 otherwise. """
    assert 1 <= k <= 9, "k must be between 1 and 9."
    incorrect_ks = set(range(1, 9)) - {k}
    incorrect_ks = list(incorrect_ks)

    rng = random.Random(seed)

    words = load_word_corpus(ASSETS_DIR / "english_words" / "nouns.txt")
    rng.shuffle(words)
    words = words[:1000]

    data = []

    # Positive examples
    for i in range(n_samples // 2):
        # Get k random words
        sample = rng.sample(words, k)
        text = " ".join(sample)
        data.append(LLMRuleData(text=text, label=1))        

    # Negative examples
    for i in range(n_samples // 2):
        # Get k random words
        incorrect_k = rng.sample(incorrect_ks, 1)[0]
        sample = rng.sample(words, incorrect_k)
        text = " ".join(sample)
        data.append(LLMRuleData(text=text, label=0))

    rng.shuffle(data)
    return LLMRuleDataset(data=data, rule=f"The label is 1 if the text has exactly {k} words and 0 otherwise.")