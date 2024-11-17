from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

import nltk
nltk.download('stopwords')
nltk.download('punkt_tab')

def summarize_text(article):
    sentences = sent_tokenize(article)
    words = word_tokenize(article.lower())
    words = [word for word in words if word.isalnum() and word not in stopwords.words()]

    freq_dist = FreqDist(words)

    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_dist:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = freq_dist[word]
                else:
                    sentence_scores[sentence] += freq_dist[word]

    ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)

    summary = " ".join(ranked_sentences[:2])
    return summary

article = (
    "Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu "
    "vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, "
    "kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm."
)

summary = summarize_text(article)
print("Summary:", summary)