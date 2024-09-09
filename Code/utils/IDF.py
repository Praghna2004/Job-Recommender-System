import math
from collections import Counter

def tokenize(document):
    return document.split()

def calculate_idf(unique_words, corpus):
    idf_dict = {}
    N = len(corpus)

    # Count the number of documents containing each term
    document_frequency = Counter()
    for term in unique_words:
        document_frequency[term] = sum(1 for doc in corpus if term in tokenize(doc))

    # Calculate IDF for each term
    for term in unique_words:
        idf_dict[term] = math.log((N) / (document_frequency[term]))

    return idf_dict
