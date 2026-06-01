import nltk
from nltk.util import ngrams
from collections import defaultdict

# Step 1: Prepare the corpus (tokenize sentences)
corpus = [
    "The weather is beautiful today",
    "I am learning natural language processing",
    "I am studing ML",
    "Machine learning is fascinating",
    "Language models are powerful tools",
    "I love coding in C++",
    "I love programming in Python",
    "I love todays weather"
]

# Tokenize the corpus (split sentences into words)
tokenized_corpus = [
    nltk.word_tokenize(sentence.lower())
    for sentence in corpus
]

# Step 2: Train the bigram model
def train_bigram_model(corpus):
    model = defaultdict(lambda: defaultdict(int))  # Bigram model

    for sentence in corpus:
        # Generate bigrams for each sentence
        bigrams = ngrams(sentence, 2)

        for w1, w2 in bigrams:
            model[w1][w2] += 1  # Increment the count for each bigram

    return model


# Train the bigram model
bigram_model = train_bigram_model(tokenized_corpus)

# Step 3: Calculate word probabilities (bigram probabilities)
def calculate_word_probabilities(model):
    probabilities = defaultdict(lambda: defaultdict(float))

    for w1 in model:
        total_count = float(sum(model[w1].values()))

        for w2 in model[w1]:
            probabilities[w1][w2] = (
                model[w1][w2] / total_count
            )  # Probability of w2 after w1

    return probabilities


# Calculate word probabilities
word_probabilities = calculate_word_probabilities(bigram_model)

# Step 4: Predict the next word given a context (bigram prediction)
def predict_next_word(model, context):
    if context[-1] in model:
        next_word_probs = model[context[-1]]
        next_word = max(next_word_probs, key=next_word_probs.get)
        return next_word
    else:
        return None


# Take user input for context
user_input = input(
    "Enter a sentence or context (e.g., 'The bank'): "
)

# Process the user input (split into words)
context = user_input.lower().split()

# Predict the next word based on the user input
predicted_word = predict_next_word(
    bigram_model,
    context
)

# Print results
print(
    "\nPredicted next word given context '{}':".format(
        " ".join(context)
    ),
    predicted_word
)
