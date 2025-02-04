import os
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter
from math import log10

# Define paths
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
OUTPUTS_DIR = os.path.join(PROJECT_ROOT, "../output_analysis")

# Ensure language-specific output folders exist
languages = ['eng', 'fr', 'sp', 'rus']
for lang in languages:
    os.makedirs(os.path.join(OUTPUTS_DIR, lang), exist_ok=True)

def load_csv(file_path):
    """Loads a CSV file and returns a list of words."""
    df = pd.read_csv(file_path)
    words = df.iloc[:, 0].dropna().tolist()  # First column contains words
    return words

def process_frequency(words):
    """Processes the list of words and returns word frequency counts."""
    word_count = Counter(words)
    return word_count

def plot_frequency(word_count, lang):
    """Plots word frequency distribution and saves as a PNG file."""
    # Get top N words and their frequencies
    common_words = word_count.most_common(20)
    words, frequencies = zip(*common_words)

    # Plot bar chart for frequency distribution
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.title(f'Word Frequency Distribution ({lang})')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # Save the frequency bar chart as PNG
    plt.savefig(os.path.join(OUTPUTS_DIR, lang, 'frequency_graph.png'))
    plt.close()

def plot_log_frequency(word_count, lang):
    """Plots log-frequency distribution and saves as a PNG file."""
    # Calculate the log of frequencies
    words = list(word_count.keys())
    frequencies = list(word_count.values())
    log_frequencies = [log10(f) for f in frequencies]

    # Plot log-frequency distribution
    plt.figure(figsize=(10, 6))
    plt.plot(words, log_frequencies, marker='o', linestyle='-', color='orange')
    plt.title(f'Log Frequency Distribution ({lang})')
    plt.xlabel('Words')
    plt.ylabel('Log(Frequency)')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # Save the log-frequency graph as PNG
    plt.savefig(os.path.join(OUTPUTS_DIR, lang, 'log_frequency_graph.png'))
    plt.close()

def save_frequency_data(word_count, lang):
    """Saves word frequency data in a JSON format."""
    frequency_data = dict(word_count)
    with open(os.path.join(OUTPUTS_DIR, lang, 'frequency_data.json'), 'w', encoding='utf-8') as f:
        json.dump(frequency_data, f, ensure_ascii=False, indent=4)

def analyze_language(file_path, lang):
    """Analyzes word frequencies for a given language's file."""
    # Load the cleaned data (words list)
    words = load_csv(file_path)
    
    # Process word frequencies
    word_count = process_frequency(words)
    
    # Save frequency data to JSON
    save_frequency_data(word_count, lang)
    
    # Generate frequency and log-frequency plots
    plot_frequency(word_count, lang)
    plot_log_frequency(word_count, lang)

# Process each language's corresponding file
files = {
    'eng': '../data/lemmatized_text/clean_UDHR_eng_lemmatized.csv',
    'fr': '../data/lemmatized_text/clean_UDHR_fr_lemmatized.csv',
    'sp': '../data/lemmatized_text/clean_UDHR_sp_lemmatized.csv',
    'rus': '../data/lemmatized_text/clean_UDHR_rus_lemmatized.csv',
}

for lang, file_path in files.items():
    analyze_language(file_path, lang)

print("Frequency analysis and graph generation complete!")
