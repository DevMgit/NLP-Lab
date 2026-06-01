import collections
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize


def get_ngrams(text, n):
    """Generate n-grams from the given text."""
    tokens = word_tokenize(text.lower())
    n_grams = ngrams(tokens, n)
    return list(n_grams)


# Example text
text1 = (
    "this is a sample text with several words this is another "
    "sample text with some different words"
)

text = "Sample list of words"

# Generate Uni-grams
print("List of Unigrams")
ngrams_list = get_ngrams(text, 1)

for ngram in ngrams_list:
    print(ngram)

# Generate Bi-grams
print("\nList of Bigrams")
ngrams_list = get_ngrams(text, 2)

for ngram in ngrams_list:
    print(ngram)

# Generate Tri-grams
print("\nList of Trigrams")
ngrams_list = get_ngrams(text, 3)

for ngram in ngrams_list:
    print(ngram)
