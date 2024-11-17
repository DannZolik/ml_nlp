from deep_translator import GoogleTranslator

def translate(input, lang="en"):
    return GoogleTranslator(source='auto', target=lang).translate(input)


texts = ["Labdien! Kā jums klājas?","Es šodien lasīju interesantu grāmatu."]

for text in texts:
    print(f"Original Text: {text} \t Translated: {translate(text)}")
