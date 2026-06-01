import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet

# Download required data (run once)
nltk.download('wordnet')
nltk.download('omw-1.4')


# Function for Word Sense Disambiguation (WSD)
def get_sense(sentence, ambiguous_word):
    words = sentence.split()
    sense = lesk(words, ambiguous_word)
    return sense


# Test sentences
sentences = [
    ("He deposited money in the bank", "bank"),
    ("The boat reached the bank of the river", "bank"),
    ("The bat flew in the night", "bat"),
    ("He hit the ball with a bat", "bat"),
    ("The crane is flying in the sky", "crane"),
    ("The crane lifted heavy loads", "crane")
]

# Run WSD
for sent, word in sentences:
    sense = get_sense(sent, word)

    print(f"Sentence: {sent}")
    print(f"Word: {word}")
    print(f"Predicted Sense: {sense}")
    print(
        f"Definition: {sense.definition() if sense else 'No sense found'}"
    )
    print("-" * 50)
