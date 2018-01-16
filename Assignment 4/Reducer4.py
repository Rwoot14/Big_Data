#!/usr/bin/python

# Reducer for session generation.
# Here we assemble user sessions

import sys
INPUT = sys.stdin
car = ['vin', 'condition', 'year', 'make', 'model', 'price', 'mileage']
car_dic={}
class_lis=['submitter', 'clicker', 'shower', 'visitor', 'other']
no_mo=['user_id','session']
def read_key_value(file):
    for line in file:
        # split the line into components, before and after the tab
        if not line.strip():
            continue
        else:
            yield line.strip().split('\t', 1)

def main():
    current_user_id = None
    event_list = []
    car_dic={}
    for user_id, event_string in read_key_value(INPUT):
        # eval() converts a data structure described on a string
        # into that internal data structure (for example, a dictionary).
        
        event = eval(event_string)

        # Assemble
        if user_id == current_user_id:
            
            dic={}
            
            if event['vin'] in car_dic:
                for i in car:
                    if i=='vin':
                        continue
                    else:
                        event.pop(i,None)
                event_list.append(event)
            else:
                for i in car:
                    if i=='vin':
                        continue
                    else:
                        dic[i]=(event[i])
                        event.pop(i,None)
                event_list.append(event)
                car_dic[event['vin']]=dic

            continue
        else:
            if current_user_id:
                class1='other'
                for i in event_list:
                    if class_lis.index(i['session'])<class_lis.index(class1):
                        class1=i['session']
                        for t in no_mo:
                            i.pop(t,None)
                    else:
                        for t in no_mo:
                            i.pop(t,None)
                        continue
                newlist = sorted(event_list, key=lambda k: k['timestamp']) 
                print '{}\t{}\t{}\t{}'.format(current_user_id,class1, newlist, car_dic)
            car_dic={}
            current_user_id = user_id
            event_list=[]
            
            dic={}
            
            for i in car:
                if i=='vin':
                    continue
                else:
                    dic[i]=(event[i])
                    event.pop(i,None)
            event_list.append(event)
            car_dic[event['vin']]=dic

    if user_id == current_user_id:
        if event['vin'] in car_dic:
            for i in car:
                if i=='vin':
                    continue
                else:
                    event.pop(i,None)
            event_list.append(event)
            
            
        else:
            for i in car:
                if i=='vin':
                    continue
                else:
                    dic[i]=(event[i])
                    event.pop(i,None)
            event_list.append(event)
            car_dic[event['vin']]=dic
            class1='other'
            
            
        for i in event_list:
            try:
                if class_lis.index(i['session'])<class_lis.index(class1):
                    class1=i['session']
                    for t in no_mo:
                        i.pop(t,None)
                else:
                    for t in no_mo:
                        i.pop(t,None)
                    continue
            except:
                KeyError
        newlist = sorted(event_list, key=lambda k: k['timestamp']) 

        print '{}\t{}\t{}\t{}'.format(current_user_id,class1, newlist, car_dic)

if __name__ == "__main__":
    main()

