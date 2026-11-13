# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Hongbin
# Date: 2026/11/06
# Purpose: Use Dictionary for Problem solving.
# Usage: ./lab5f.py

# TO DO 1: Create function histogram() as instructed in readme.md file. 
# TO DO 2: Create main() function and call histogram(). Call the main() function.
# TO DO 3: Run the script. Take screenshot of code showing the functions histogram() and main(). Also show output in the screenshot.

def histogram(sentence):
    letters = {}
    for ch in sentence:
        if ch!=" ":
            if ch in letters:
                letters[ch] = letters[ch]+1
            else:
                letters[ch] = 1

    for key, value in letters.items():
        print(key, '*'*value)

def main():
    histogram("hello amma")

main()