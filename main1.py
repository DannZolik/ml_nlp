from collections import Counter
import string

def word_frequency_analysis(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    word_counts = Counter(words)
    return word_counts

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."
frequencies = word_frequency_analysis(text)

print("Word Frequencies:")
for word, count in frequencies.items():
    print(f"{word}: {count}")