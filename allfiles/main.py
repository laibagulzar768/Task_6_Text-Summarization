from preprocess import clean_text
from extractive import extractive_summary
from abstractive import abstractive_summary
from evaluate import evaluate_summary
from config import MAX_SENTENCES
import os
import requests


def get_user_input():
    """Get input text from user with multiple options"""
    print("\nChoose input method:")
    print("1. Enter text directly")
    print("2. Read from a text file")
    print("3. Enter a web URL")
  
    choice = input("Your choice (1-3): ").strip()

    if choice == "1":
        print("\nEnter/Paste your text (Ctrl+Z then Enter to submit):")
        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            lines.append(line)
        return "\n".join(lines)

    elif choice == "2":
        filepath = input("Enter file path: ").strip()
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found")
            return None

    elif choice == "3":
        return """Artificial intelligence (AI) is transforming industries..."""
    
    else:
        print("Invalid choice")
        return None

def summarize(article):
    cleaned = clean_text(article)
    return {
        "extractive": extractive_summary(cleaned, MAX_SENTENCES),
        "abstractive": abstractive_summary(cleaned)
    }

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Web & Text Summarization System ===")
        
        article = get_user_input()
        if article is None:
            continue
            
        results = summarize(article)
        
        print("\n=== Results ===")
        print("\nExtractive Summary:")
        print(results["extractive"])
        
        print("\nAbstractive Sumary:")
        print(results["abstractive"])
        
        if input("\nSummarize another? (y/n): ").lower() != 'y':
            break