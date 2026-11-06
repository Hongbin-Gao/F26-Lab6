# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Hongbin
# Date:2026/11/06
# Purpose: Practice Set Operations.
# Usage: ./lab6b.py
# TO DO 1: Copy the code from lab6a.py and paste here.
# TO DO 2: Create the function s3ors5().
# TO DO 3: Run the script. Take screenshot of only s3ors5() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.

def buildtheSet(divisor):
    # Complete this function
    number = set()
    for i in range(1,101):
        if i % divisor == 0:
            number.add(i)
    return number

def s3_or_s5(s3,s5):
    only_s3 = s3.difference(s5)
    only_s5 = s5.difference(s3)
    common_set = s3.intersection(s5)
    result_set = (only_s3.union(only_s5)).difference(common_set)
    return result_set

def main():

    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    result = s3_or_s5(s3,s5)
    print("s3 or s5: ", result)
    print("----------------------------------------")

main()