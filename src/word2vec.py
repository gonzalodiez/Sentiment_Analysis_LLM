from typing import List

import numpy as np
from gensim.models.word2vec import Word2Vec


def vectorizer(
    corpus: List[List[str]], model: Word2Vec, num_features: int = 100
) -> np.ndarray:
    """
    This function takes a list of tokenized text documents (corpus) and a pre-trained
    Word2Vec model as input, and returns a matrix where each row represents the
    vectorized form of a document.

    palabra, vector
    hola, (0.2,0.5,1)

    Args:
        corpus : list
            A list of text documents that needs to be vectorized.

        model : Word2Vec
            A pre-trained Word2Vec model that will be used to vectorize the corpus.

        num_features : int
            The size of the vector representation of each word. Default is 100.

    Returns:
        corpus_vectors : numpy.ndarray
            A 2D numpy array where each row represents the vectorized form of a
            document in the corpus.
    """
    corpus_vectors = []
    for document in corpus:
        document_vector = np.zeros(num_features)
        document_length = len(document)
        word_count=0

        # Iterate over the corpus
        for word in document:
            if word in model.wv:
                document_vector += model.wv[word]
                word_count+=1
        
        # Normalize the vector
        if word_count>0:
            document_vector /= document_length

        # Append all the words in the corpus
        corpus_vectors.append(document_vector)
    return np.array(corpus_vectors)

def vectorizer_gensim(
    corpus: List[List[str]], model: Word2Vec, num_features: int = 100
) -> np.ndarray:
    """
    This function takes a list of tokenized text documents (corpus) and a pre-trained
    Word2Vec model as input, and returns a matrix where each row represents the
    vectorized form of a document.

    palabra, vector
    hola, (0.2,0.5,1)

    Args:
        corpus : list
            A list of text documents that needs to be vectorized.

        model : Word2Vec
            A pre-trained Word2Vec model that will be used to vectorize the corpus.

        num_features : int
            The size of the vector representation of each word. Default is 100.

    Returns:
        corpus_vectors : numpy.ndarray
            A 2D numpy array where each row represents the vectorized form of a
            document in the corpus.
    """
    corpus_vectors = []
    for document in corpus:
        document_vector = np.zeros(num_features)
        document_length = len(document)
        word_count=0

        # Iterate over the corpus
        for word in document:
            if word in model:
                document_vector += model[word]
                word_count+=1
        
        # Normalize the vector
        if word_count>0:
            document_vector /= document_length

        # Append all the words in the corpus
        corpus_vectors.append(document_vector)
    return np.array(corpus_vectors)
