import os
import re
import string
import unidecode

# Define input and output directories
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
ORIGINALS_DIR = os.path.join(DATA_DIR, "originals")
CLEANED_DIR = os.path.join(DATA_DIR, "cleaned")

# Ensure the cleaned folder exists
os.makedirs(CLEANED_DIR, exist_ok=True)

# Patterns to remove headers (Article 1, Artículo 1, Статья 1, etc.)
HEADER_PATTERNS = [
    r'\bArticle\s\d+\b',  # English, French
    r'\bArtículo\s\d+\b',  # Spanish
    r'\bСтатья\s\d+\b'     # Russian
]

def clean_text(text):
    """Cleans the given text: removes headers, punctuation, normalizes accents, and formats spaces."""
    # Remove headers (for all languages)
    for pattern in HEADER_PATTERNS:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Normalize accents (e.g., é → e, à → a)
    text = unidecode.unidecode(text)

    # Replace newlines with spaces and remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def process_files():
    """Processes all text files in the originals folder and saves cleaned versions."""
    for filename in os.listdir(ORIGINALS_DIR):
        if filename.endswith(".txt"):
            input_path = os.path.join(ORIGINALS_DIR, filename)
            output_filename = f"clean_{filename}"  # Add prefix
            output_path = os.path.join(CLEANED_DIR, output_filename)

            # Read and clean the text
            with open(input_path, 'r', encoding='utf-8') as file:
                cleaned_text = clean_text(file.read())

            # Save the cleaned text
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_text)

            print(f"Processed: {filename} → {output_filename}")

if __name__ == "__main__":
    process_files()
