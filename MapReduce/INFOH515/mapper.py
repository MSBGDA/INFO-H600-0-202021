#!/usr/local/anaconda3/bin/python
import sys

for line in sys.stdin:                              # The input data comes from STDIN (i.e: The standard input)
    line = line.strip()                             # Removal of leading and trailing whitespaces
    words = line.split()                            # Creation of a list containing all words by splitting the line in words
    # increase counters
    for word in words:                              # For each word in the list (i.e: words), do...
        print(word+"\t"+"1")
