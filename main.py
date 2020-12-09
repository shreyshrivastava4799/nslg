# Load the data and preprocess data and store corpus in raw_text
import nltk
import nltk.data
nltk.download('punkt')
from nltk.tokenize import word_tokenize

from word import Word
from state import State
from planner import Planner

import re
import numpy as np

LOG = True
embedding_size = 10

if __name__ == "__main__":

    raw_text = nltk.data.load('../corpus/Pride-and-Prejudice.txt', format='raw').decode('utf-8')
    raw_text = re.sub(r'[^\w\s]', '', raw_text)

    vocab = set()
    for sentences in re.split("\n", raw_text):
        curr_tokens = word_tokenize(sentences, language='english')
        vocab.update([token.lower() for token in curr_tokens if token.isalnum()]) 

    actions = []
    for word in vocab:
        actions.append(Word(word, np.random.randint(10)))

    # mostly start will be zero vector or application of sequence of words
    start =  np.random.randint(2, size=embedding_size)

    # still not sure how to decide end representation but helpful in deciding context
    end =  np.random.randint(2, size=embedding_size)

    planner = Planner(actions, LOG)
    print(planner.plan(start, end))

