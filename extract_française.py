#!/usr/bin/env python3
"""
Extract French phrases from Quebec Francisation Scale JSON files.
Writes phrases to a text file with blank lines between each phrase.
"""

import json
import sys
import os


def extract_française_phrases(json_file, output_file=None):
    """
    Extract French phrases from JSON file and write to text file.
    
    Args:
        json_file: Path to input JSON file
        output_file: Path to output text file (optional)
    """
    # If no output file specified, create one based on input filename
    if output_file is None:
        base_name = os.path.splitext(json_file)[0]
        output_file = f"{base_name}_french.txt"
    
    # Read the JSON file
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{json_file}': {e}")
        sys.exit(1)
    
    # Extract French phrases
    phrases = data.get('phrases', [])
    
    if not phrases:
        print(f"Warning: No phrases found in '{json_file}'")
        return
    
    # Append to output file (or create if doesn't exist) with blank lines between phrases
    try:
        # Check if file exists and has content to add proper spacing
        file_exists = os.path.exists(output_file) and os.path.getsize(output_file) > 0
        
        with open(output_file, 'a', encoding='utf-8') as f:
            # Add blank line before new content if appending to existing file
            if file_exists:
                f.write('\n')
            
            for i, phrase_obj in enumerate(phrases):
                french = phrase_obj.get('french', '')
                f.write(french + '\n')
                # Add blank line after each phrase except the last one
                if i < len(phrases) - 1:
                    f.write('\n')
        
        print(f"Successfully extracted {len(phrases)} French phrases")
        print(f"Output written to: {output_file}")
    
    except IOError as e:
        print(f"Error writing to '{output_file}': {e}")
        sys.exit(1)


def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python extract_française.py <input_json_file> [output_txt_file]")
        print("Example: python extract_française.py ecoute/niveau_01.json")
        print("Example: python extract_française.py ecoute/niveau_01.json phrases.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    extract_française_phrases(input_file, output_file)


if __name__ == "__main__":
    main()