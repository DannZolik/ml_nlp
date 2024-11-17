from flair.data import Sentence
from flair.models import SequenceTagger

# Load the pre-trained NER model from Flair
ner_tagger = SequenceTagger.load('ner-multi')  # This model works for multiple languages, including Latvian

def extract_named_entities(text):
    # Create a Sentence object for Flair
    sentence = Sentence(text)

    # Predict named entities
    ner_tagger.predict(sentence)

    # Extract entities
    entities = {
        "PERSON": [],
        "ORG": []
    }

    for entity in sentence.get_spans('ner'):
        if entity.tag == "PER":
            entities["PERSON"].append(entity.text)
        elif entity.tag == "ORG":
            entities["ORG"].append(entity.text)

    return entities

# Input text
text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

# Extract named entities
named_entities = extract_named_entities(text)

# Print results
print("Named Entities:")
for entity_type, names in named_entities.items():
    print(f"{entity_type}: {', '.join(names)}")