from lingua import LanguageDetectorBuilder

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day.",
    "Сегодня солнечный день."
]

detector = LanguageDetectorBuilder.from_all_languages().with_preloaded_language_models().build()

for i in range(len(texts)):
    language = detector.detect_language_of(texts[i])
    print(f"Text {i+1}: {texts[i]} (Language: {language.name})")
