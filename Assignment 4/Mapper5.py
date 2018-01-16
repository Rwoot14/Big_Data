#!/usr/bin/python

# Mapper for session generation.
# Here we examine event log entries

import sys

INPUT = sys.stdin

field_name_list = ['user_id', 'event', 'timestamp', 'vin', 'condition', 'year', 'make', 'model', 'price', 'mileage' ]
action_target_list=['action','target']

def read_input(file):
    for line in file:
        # split the line into individual fields (fields are delimited by tab).
        yield line.strip().split('\t')

def digest_log_entry(field_value_list):
    field_value_dict = {}
    for i in range(len(field_name_list)):
        if field_name_list[i]=='event':
            action_target=field_value_list[i].split(' ',1)
            for item in range(len(action_target)):
                field_value_dict[action_target_list[item]]=action_target[item]
                if action_target_list[item]=='action':
                    class1=classifier(item,action_target)
                    field_value_dict['session']=class1
                if action_target_list[item]=='target' and action_target[item]=='contact form':
                    class1='submitter'
                    field_value_dict['session']=class1
                    
        else:
            field_value_dict[field_name_list[i]] = field_value_list[i]
    return field_value_dict

def classifier(item,action_target):
    if action_target[item]=='contact form':
        class_='submitter'
    elif action_target[item]=='click':
        class_='clicker'
    elif action_target[item]=='show' or action_target[item]=='display':
        class_='shower'
    elif action_target[item]=='visit':
        class_='visitor'
    else:
        class_='other'
    return class_
            
        

def main():
    # input comes from STDIN (standard input)
    # data is the generator that produces individual inputs
    data = read_input(INPUT)

    # For each log entry, digest all the fields,
    # output the user_id as the key,
    # output the digested log entry (a dictionary) as the value

    for log_entry in data:
        digested_log_entry = digest_log_entry(log_entry)
        print '%s\t%s'% ( digested_log_entry['user_id'], digested_log_entry)


if __name__ == "__main__":
    main()

