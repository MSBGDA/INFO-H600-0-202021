import sys
from itertools import groupby
from operator import itemgetter

def tokenize_input():
    """Split each line of standard input into a key and a value."""
    for line in sys.stdin:
        yield line.split('\t')

# produce key-value pairs of word lengths and counts separated by tabs
for word_length, group in groupby(tokenize_input(), itemgetter(0)):
    try:
        total = sum(int(count) for word_length, count in group)
        print(word_length + '\t' + str(total))
    except ValueError:
        pass # ignore word if its count was not an integer
