# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Traverse dictionary.
# Usage: ./lab6e.py

my_dict = {"switzerland" : "Alps", "United States" : "Alska Range", "Armenia" : "Caucasus", "Argentina" : "Andes", "Karakoram" : "Pakistan"}
# TO DO 1: Create a for in loop as instructed in readme.md file. 
# TO DO 2: Run the script, and take the screenshot of code and output.

for key, value in my_dict.items():
    print(key, ':', value)