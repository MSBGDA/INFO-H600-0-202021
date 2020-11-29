import sys

def tokenize_input():
    """Split each line of standard input into a list of strings."""
    for line in sys.stdin:
        line = line.strip()
        yield line.split()[0]
        
# read each line in the the standard input and for every word
# produce a key-value pair containing the word, a tab and 1
for line in tokenize_input():
    print(line + '\t1')
