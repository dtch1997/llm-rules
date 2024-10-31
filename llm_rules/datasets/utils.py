import pathlib
import random 

def load_word_corpus(filepath: pathlib.Path | str) -> list[str]:
    """Load a word corpus from a file."""
    with open(filepath, "r") as f:
        return f.read().splitlines()
    
def train_test_split(data, test_size=0.2, random_state=0):
    """Split data into training and test sets."""
    rng = random.Random(random_state)
    rng.shuffle(data)
    split_idx = int(len(data) * (1 - test_size))
    return data[:split_idx], data[split_idx:]