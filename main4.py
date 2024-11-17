from textblob import TextBlob
from deep_translator import GoogleTranslator

def analyze_sentiment(sentence):
    translation = GoogleTranslator(source='auto', target='en').translate(sentence)

    analysis = TextBlob(translation)
    polarity = analysis.sentiment.polarity

    if polarity > 0.5:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Input sentences
sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs.",
    "This product is amazing! I love using it."
]

print("Sentiment Analysis:")

for i in range(len(sentences)):
    sentiment = analyze_sentiment(sentences[i])
    print(f"Sentence {i}: {sentiment}")
