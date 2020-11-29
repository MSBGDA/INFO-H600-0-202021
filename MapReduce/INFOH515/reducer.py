#!/usr/local/anaconda3/bin/python
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:                              # The input data comes from STDIN (i.e: The standard input)
    line = line.strip()                             # Removal of leading and trailing whitespaces
    word, count = line.split('\t', 1)               # Parsing of the awaited key/value pair

    try:
        count = int(count)
    except ValueError:                              # In the case the value is not a number, we silently discard the line
        continue

    if current_word == word:                        # This IF only works because Hadoop sorts map output by key
        current_count += count                      # before it is passed to the reducer
    else:
        if current_word:
            print(current_word+"\t"+str(current_count))           # Output of the result to STDOUT
        current_count = count
        current_word = word

if current_word == word:                            # Output of the last word
    print(current_word+"\t"+str(current_count))
