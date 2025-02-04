import os
import csv

# Define directories
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
CSV_DIR = os.path.join(DATA_DIR, "text_csv")  # Input files from previous step
ORG_DIR = os.path.join(DATA_DIR, "organized_text")  # Output folder for this step

# Ensure the organized_text folder exists
os.makedirs(ORG_DIR, exist_ok=True)

def organize_text():
    """Processes CSV files: transposes data, sorts words, converts to lowercase, and re-sorts."""
    for filename in os.listdir(CSV_DIR):
        if filename.endswith(".csv"):
            input_path = os.path.join(CSV_DIR, filename)
            output_filename = filename  # Keep the same filename
            output_path = os.path.join(ORG_DIR, output_filename)

            # Read CSV file (single row of words)
            with open(input_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                words = next(reader)  # Read first (and only) row

            # Sort alphabetically (first pass)
            words.sort()

            # Convert to lowercase
            words = [word.lower() for word in words]

            # Sort again after converting to lowercase
            words.sort()

            # Save transposed words (each word in a new row)
            with open(output_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for word in words:
                    writer.writerow([word])  # Each word in its own row

            print(f"Processed: {filename} → {output_filename}")

if __name__ == "__main__":
    organize_text()
