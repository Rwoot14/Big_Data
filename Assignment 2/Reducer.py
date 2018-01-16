#!/usr/bin/python
import sys
current_word=None
total_msg_count=0
total_count=0
total_count_sq=0
word=None
max_=0
word={}

for line in sys.stdin:
    line=line.strip()
    word,msg_count,tot_count,tot_count_sq,line_count=line.split('\t',1)
    try:
        msg_count=int(msg_count)
        tot_count=int(tot_count)
        tot_count_sq=int(tot_count_sq) 
    except ValueError:
        continue
    if current_word==word:
        total_msg_count+=msg_count
        total_count+=tot_count
        total_count_sq+=tot_count_sq
        min_current=tot_count
        if max_<tot_count:
            max_=tot_count
        else:
            continue
        if min_>min_current:
            min_=min_current
    else:
        if current_word:
            print current_word, total_msg_count,total_count,total_count_sq,round((total_count_sq-(total_count*total_count)/float(total_msg_count))/float(total_msg_count-1),2), round((float(total_count)/total_msg_count),2),min_,max_
        total_msg_count=msg_count
        total_count=tot_count
        total_count_sq=tot_count_sq
        current_word=word
        max_=0
        min_=tot_count    

if current_word==word:
    print current_word, total_msg_count,total_count,total_count_sq,round((total_count_sq-((total_count*total_count)/total_msg_count))/float(total_msg_count-1),2), round((float(total_count)/total_msg_count),2),min_,max_
   

