#!/usr/bin/python
import sys
#initialize the counts and opens up an empty dictionary
tot_count=0
tot_sq_count=0
word_dic={}
line_count=1
#starts the line loop
for line in sys.stdin:
    #strips the line of white space and splits the line into words by white space
    line=line.strip()
    
    words=line.split()
    #for each word in the line
    for word in words:
        #this count is for the total message word count
        tot_count+=1
        # This checks to see if the word is in the dictionary yet
        #if it is, add 1
        #if not put the word in the dictonary and start the count
        if word in word_dic.keys():
            word_dic[word]+=1
        else: 
            word_dic[word]=1
    # calls the keys in the dictonaries and prints out the count
    # and other operations of count
    for i in word_dic.keys():
        if i in line:
            print '%s %s %s %s %s' % (i,1, word_dic[i], (word_dic[i]*word_dic[i]),line_count)
            tot_sq_count+=(word_dic[i]*word_dic[i])
    # prints out message statistics
    print '%s %s %s %s %s' % ('MsgStat',1 ,tot_count,tot_count*tot_count,line_count)
    # resets the counts for every line(message) and resets the dictonary
    tot_count=0
    tot_sq_count=0
    line_count+=1
    word_dic={}

