"""Analyze a text file and provide statistics."""
import argparse
from collections import Counter
import re
import sys

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("filename", help="Path to the text file to analyze")
    parser.add_argument("--top", type=int, default=5, help="Number of top words to display")
    args = parser.parse_args()

    try:
        with open(args.filename, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{args.filename}' not found.", file=sys.stderr)
        sys.exit(1)

    lines = text.splitlines()
    words = re.findall(r'\b\w+\b', text.lower())
    chars = len(text)
    
    print(f"--- Text Analysis for {args.filename} ---")
    print(f"Lines: {len(lines)}")
    print(f"Words: {len(words)}")
    print(f"Characters: {chars}")
    
    if words:
        print(f"\nTop {args.top} most common words:")
        counter = Counter(words)
        for word, count in counter.most_common(args.top):
            print(f"  {word}: {count}")

if __name__ == "__main__":
    main()
