#!/usr/bin/python

# Reducer for session generation.
# Here we assemble user sessions

import sys

def read_key_value(file):
    for line in file:
        # split the line into components, before and after the tab
        yield line.strip().split('\t', 1)

def main():
    current_user_id = None
    event_list = []

    for user_id, event_string in read_key_value(sys.stdin):
        # eval() converts a data structure described on a string
        # into that internal data structure (for example, a dictionary).
        event = eval(event_string)

        # Assemble
        if user_id == current_user_id:
            event_list.append(event)
            continue
        else:
            if current_user_id:
                print '{}\t{}'.format(current_user_id, event_list)
            current_user_id = user_id
            event_list = [event]

    if user_id == current_user_id:
        print '{}\t{}'.format(current_user_id, event_list)

if __name__ == "__main__":
    main()
