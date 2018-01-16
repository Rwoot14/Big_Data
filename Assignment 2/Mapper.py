#!/usr/bin/python
import sys

tot_count=0
tot_sq_count=0
word_dic={}
line_count=1
for line in sys.stdin:
    line=line.strip()
    
    words=line.split()
    for word in words:
        tot_count+=1
        if word in word_dic.keys():
            word_dic[word]+=1
        else: 
            word_dic[word]=1
    for i in word_dic.keys():
        if i in line:
            print '%s\t%s' % (i,1), word_dic[i], (word_dic[i]*word_dic[i]),line_count
            tot_sq_count+=(word_dic[i]*word_dic[i])
    print '%s\t%s' % ('MsgStat',1) ,tot_count,tot_count*tot_count,line_count
    tot_count=0
    tot_sq_count=0
    line_count+=1
    word_dic={}

