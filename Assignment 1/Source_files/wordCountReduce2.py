#!/usr/bin/python
import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # Count was not a number
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Output the count for current_word
            # Hadoop has sorted key/value pairs by key
            print '{}\t{}'.format(current_word, current_count)
        current_count = count
        current_word = word

# Output the last word, if needed
if current_word == word:
    print '{}\t{}'.format(current_word, current_count)
