from sentence_transformers import SentenceTransformer
import numpy as np
from deep_translator import GoogleTranslator

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def translate_array(array):
    res = []
    for el in array:
        res_el = GoogleTranslator(source='auto', target='en').translate(el)
        res.append(res_el)
    return res

def get_word_vectors(words, model):
    embeddings = {word: model.encode(word) for word in words}
    return embeddings

def calculate_similarity(vector1, vector2):
    similarity = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    return similarity

words = ["māja", "dzīvoklis", "jūra"]
words = translate_array(words)

word_vectors = get_word_vectors(words, model)

similarities = {}
for i, word1 in enumerate(words):
    for word2 in words[i + 1:]:
        similarity = calculate_similarity(word_vectors[word1], word_vectors[word2])
        similarities[(word1, word2)] = similarity

print("Word Vectors:")
for word, vector in word_vectors.items():
    print(f"{word}: {vector[:5]}... (truncated)")

print("\nWord Similarities:")
for word_pair, similarity in similarities.items():
    print(f"Similarity between {word_pair[0]} and {word_pair[1]}: {similarity:.4f}")