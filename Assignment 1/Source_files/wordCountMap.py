#!/usr/bin/python
import sys

#--- get all lines from stdin ---
for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    line = line.strip()

    #--- split the line into words ---
    words = line.split()

    #--- output tuples [word, 1] in tab-delimited format---
    for word in words:
        # For each word in the line, output a key/value pair
        # with the word as the key, and "1" as the value.
        print '%s\t%s' % (word, 1)
