import os
import csv
import spacy

# Define directories
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
ORG_DIR = os.path.join(DATA_DIR, "organized_text")  # Input files
LEM_DIR = os.path.join(DATA_DIR, "lemmatized_text")  # Output folder

# Ensure the lemmatized_text folder exists
os.makedirs(LEM_DIR, exist_ok=True)

# Language models (ensure you have them installed)
NLP_MODELS = {
    "eng": spacy.load("en_core_web_sm"),
    "fr": spacy.load("fr_core_news_sm"),
    "sp": spacy.load("es_core_news_sm"),
    "rus": spacy.load("ru_core_news_sm")
}

# Define stopwords for each language
STOPWORDS = {
    "eng": NLP_MODELS["eng"].Defaults.stop_words,
    "fr": NLP_MODELS["fr"].Defaults.stop_words,
    "sp": NLP_MODELS["sp"].Defaults.stop_words,
    "rus": NLP_MODELS["rus"].Defaults.stop_words
}

def process_text(file_path, lang_code):
    """Lemmatize words and remove stopwords for the given language."""
    nlp = NLP_MODELS[lang_code]
    stopwords = STOPWORDS[lang_code]

    # Read words from file
    with open(file_path, 'r', encoding='utf-8') as file:
        words = [row[0] for row in csv.reader(file)]

    # Process words with spaCy
    lemmatized_words = []
    for word in words:
        doc = nlp(word)
        lemma = doc[0].lemma_  # Get lemma of the word
        if lemma not in stopwords:  # Remove stopwords
            lemmatized_words.append(lemma)

    return lemmatized_words

def lemmatize_files():
    """Process all CSV files in organized_text directory."""
    for filename in os.listdir(ORG_DIR):
        if filename.endswith(".csv"):
            file_path = os.path.join(ORG_DIR, filename)

            # Determine language from filename
            if "eng" in filename:
                lang_code = "eng"
            elif "fr" in filename:
                lang_code = "fr"
            elif "sp" in filename:
                lang_code = "sp"
            elif "rus" in filename:
                lang_code = "rus"
            else:
                print(f"Skipping {filename} (unknown language)")
                continue

            # Process file
            lemmatized_words = process_text(file_path, lang_code)

            # Save output
            output_filename = filename.replace(".csv", "_lemmatized.csv")
            output_path = os.path.join(LEM_DIR, output_filename)

            with open(output_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for word in lemmatized_words:
                    writer.writerow([word])

            print(f"Processed: {filename} → {output_filename}")

if __name__ == "__main__":
    lemmatize_files()
