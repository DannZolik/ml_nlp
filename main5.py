import re

def clean_and_normalize_text(raw_text):
    text = re.sub(r"@\w+", "", raw_text)
    text = re.sub(r"http[s]?://\S+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = text.lower()
    text = " ".join(text.split())

    return text

raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"
cleaned_text = clean_and_normalize_text(raw_text)
print("Cleaned Text:", cleaned_text)
