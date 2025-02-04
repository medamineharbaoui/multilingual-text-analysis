import os
import csv

# Define directories
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
CLEANED_DIR = os.path.join(DATA_DIR, "cleaned")
CSV_DIR = os.path.join(DATA_DIR, "text_csv")

# Ensure the CSV folder exists
os.makedirs(CSV_DIR, exist_ok=True)

def convert_txt_to_csv():
    """Converts cleaned text files into CSV format, splitting words into separate columns."""
    for filename in os.listdir(CLEANED_DIR):
        if filename.endswith(".txt"):
            input_path = os.path.join(CLEANED_DIR, filename)
            output_filename = filename.replace(".txt", ".csv")  # Change file extension
            output_path = os.path.join(CSV_DIR, output_filename)

            # Read text file
            with open(input_path, 'r', encoding='utf-8') as file:
                words = file.read().split()  # Split words by spaces

            # Write to CSV (each word in its own column)
            with open(output_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(words)  # Write words in a single row

            print(f"Converted: {filename} → {output_filename}")

if __name__ == "__main__":
    convert_txt_to_csv()
