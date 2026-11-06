# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Hongbin
# Date:2026/11/06
# Purpose: Create Sets.
# Usage: ./lab6a.py

# TO DO 1: Complete the functions below.

def buildtheSet(divisor):
    # Complete this function
    number = set()
    for i in range(1,101):
        if i % divisor == 0:
            number.add(i)
    return number

def main():

    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    s7 = buildtheSet(7)
    print("s7: ", s7)
    print("----------------------------------------")

    s11 = buildtheSet(11)
    print("s11: ", s11)

main()

# TO DO 2: Run the script. Take screenshot of only buildtheSet() function. No need to capture main() in the screenshot. 
