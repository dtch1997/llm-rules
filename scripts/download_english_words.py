import nltk
from nltk.corpus import brown, names
from collections import defaultdict
import os
import pathlib

root_dir = pathlib.Path(__file__).parent.parent.resolve()

def download_nltk_data():
    """Download required NLTK data."""
    nltk.download('brown')
    nltk.download('names')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('universal_tagset')

def get_words_by_pos():
    """Extract words by part of speech from Brown corpus."""
    # Initialize defaultdict to store words by POS
    pos_words = defaultdict(set)
    
    # Get words and their POS tags from Brown corpus
    for word, pos in brown.tagged_words(tagset='universal'):
        # Convert to lowercase and check if it's alphabetic
        word = word.lower()
        if word.isalpha():
            if pos == 'NOUN':
                pos_words['nouns'].add(word)
            elif pos == 'ADJ':
                pos_words['adjectives'].add(word)
            elif pos == 'VERB':
                pos_words['verbs'].add(word)
    
    return pos_words

def get_names():
    """Extract male and female names from Names corpus."""
    name_dict = defaultdict(set)
    
    # Get male and female names
    male_names = set(name.title() for name in names.words('male.txt'))
    female_names = set(name.title() for name in names.words('female.txt'))
    
    # Some names appear in both lists, let's handle them separately
    ambiguous_names = male_names.intersection(female_names)
    unique_male_names = male_names - ambiguous_names
    unique_female_names = female_names - ambiguous_names
    
    name_dict['male_names'] = unique_male_names
    name_dict['female_names'] = unique_female_names
    name_dict['unisex_names'] = ambiguous_names
    
    return name_dict

def save_word_lists(pos_words, name_dict, output_dir='word_lists'):
    """Save word lists to files."""
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save each word list to a separate file
    for pos, words in pos_words.items():
        filename = f"{output_dir}/{pos}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            for word in sorted(words):
                f.write(f"{word}\n")
        print(f"Saved {len(words)} {pos} to {filename}")
    
    # Save name lists
    for name_type, names_set in name_dict.items():
        filename = f"{output_dir}/{name_type}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            for name in sorted(names_set):
                f.write(f"{name}\n")
        print(f"Saved {len(names_set)} {name_type} to {filename}")

def main():
    # Download required NLTK data
    print("Downloading NLTK data...")
    download_nltk_data()
    
    # Extract words by part of speech
    print("Extracting words from corpus...")
    pos_words = get_words_by_pos()
    
    print("Extracting names...")
    name_dict = get_names()
    
    # Save word lists and name lists
    print("Saving word lists and name lists...")
    save_word_lists(pos_words, name_dict, output_dir = root_dir / "assets" / "english_words")
    
    print("Done!")

if __name__ == "__main__":
    main()