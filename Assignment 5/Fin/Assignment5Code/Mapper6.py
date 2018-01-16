#!/usr/bin/python
# Read session
import sys

def read_session(file):
    
    for line in file:
        # split the line into components: user_id:sessions_type, event_list, and dictionary
        yield line.strip().split('\t')
        
def main():
    for lis in read_session(sys.stdin):
        # if statment checks for length of the read_session generator to check if tab seperated or csv
        if len(lis)>1:
            # assign variable names and convert strings into data structures
            user_id_string, event_list_string, vin_dict_string=lis
            user_id, session_type = user_id_string.split(':')
            event_list = eval(event_list_string)
            vin_dict = eval(vin_dict_string)
            # iterates through the vin dictionary and checks the event list for information about the vin 
            for key, value in vin_dict.iteritems():
                click=0
                contact_form=0
                # checks for required information 
                for event in event_list:
                    if event['vin']==key:
                        if event['event_action']=='click':
                            click+=1
                        if event['event_target']=='contact form':
                            contact_form=1
                print key,1,click,contact_form,0,0

        # this section of code is for the csv file
        else:
            # read_session generates a list, so we have to iterate through it
            for i in lis:
                # seperates the list into its components 
                line=i.split(',')
                if line[1]=='SRP':
                    print line[0],0,0,0,line[2],0
                if line[1]=='VDP':
                    print line[0],0,0,0,0,line[2]
                
if __name__ == "__main__":
    main()
