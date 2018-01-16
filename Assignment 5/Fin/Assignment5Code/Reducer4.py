#!/usr/bin/python
import sys

def read_session(file):

    
    for line in file:
        # split the line into components: user_id:sessions_type, event_list, and dictionary
        # checks the mappers output to ignore blank lines
        if not line.strip():
            continue
        else:
            yield line.strip().split(' ')
            
def main():
    # initializes the current vin 
    current_vin=None
    # extracts the variables from the mapper
    for vin,session,click,contact,srp,vdp in read_session(sys.stdin):
        # converts strings to integers
        try:
            session=int(session)
            click=int(click)
            contact=int(contact)
            srp=int(srp)
            vdp=int(vdp)
        except:
            ValueError
        # aggregates counts for the current vin
        if current_vin==vin:
            session_count+=session
            click_count+=click
            contact_count+=contact
            srp_count+=srp
            vdp_count+=vdp
            current_vin==vin
        # Initializes/ resets counts when the reducer finds a new vin
        else:
            # prints the current vins final counts
            if current_vin:
                # does the left join by checking if vin had accured in the tab seperated doc.
                if session_count>0:
                    print current_vin,session_count,click_count,contact_count,srp_count,vdp_count
    
            session_count=0
            click_count=0
            contact_count=0
            srp_count=0
            vdp_count=0
            
            session_count+=session
            click_count+=click
            contact_count+=contact
            srp_count+=srp
            vdp_count+=vdp
            current_vin=vin
          
    # makes sure the last vin is printed
    if current_vin==vin:
        # does the left join by checking if vin had accured in the tab seperated doc.
        if session_count>0:
            print current_vin,session_count,click_count,contact_count,srp_count,vdp_count
        
        
if __name__ == "__main__":
    main()
    

