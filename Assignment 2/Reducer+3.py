#!/usr/bin/python
import sys
#initialize statistics and word tracking variables
current_word=None
total_msg_count=0
total_count=0
total_count_sq=0
word=None
max_=0
word={}
#start line loop
for line in sys.stdin:
    #gets rid of new line that mapper creates
    if not line.strip():
        continue
    else:
        line=line.strip()
        # gets the variables from the lines
        word,msg_count,tot_count,tot_count_sq,line_count=line.split(' ')
        #turns the variables into integers
        try:
            msg_count=float(msg_count)
            tot_count=float(tot_count)
            tot_count_sq=float(tot_count_sq) 
        except ValueError:
            continue
        # if the word is the same aggregate the counts
        if current_word==word:
            total_msg_count+=msg_count
            total_count+=tot_count
            total_count_sq+=tot_count_sq
            min_current=tot_count
            #continually update the max/min for each line
            if max_<tot_count:
                max_=tot_count
            else:
                continue
            if min_>min_current:
                min_=min_current
        # prints out final occurnce of the word and updates the new word
        else:
            if current_word:
                print current_word, total_msg_count,total_count,total_count_sq,round((total_count_sq-(total_count*total_count)/float(total_msg_count))/float(total_msg_count-1),2), round((float(total_count)/total_msg_count),2),min_,max_
            total_msg_count=msg_count
            total_count=tot_count
            total_count_sq=tot_count_sq
            current_word=word
            max_=0
            min_=tot_count    
#prints out the last word
if current_word==word:
    print current_word, total_msg_count,total_count,total_count_sq,round((total_count_sq-(total_count*total_count)/float(total_msg_count))/float(total_msg_count-1),2), round((float(total_count)/total_msg_count),2),min_,max_
  

