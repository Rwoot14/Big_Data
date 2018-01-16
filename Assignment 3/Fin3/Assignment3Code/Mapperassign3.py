#!/usr/bin/python
import sys
import re
# first replace the wierd occurance of space tab tab with just a space
# then split the email on tabs
def split_t(line):
    line=line.replace(' \t\t',' ')
    return line.split('\t')
# Find the email occurances we are looking for
def Finder(split_t_out):
    #append them to a list for further cleaning
    clean=[]
    for i in split_t_out:
        find=re.findall(r'To: [\w+.\w+@\w+,\- ]+.com',i) or re.findall(r'From: [\w+.\w+@\w+,\- ]+.com',i) or re.findall(r'Cc: [\w+.\w+@\w+.com,\- ]+',i) or re.findall(r'Bcc: [\w+.\w+@\w+.com,\- ]+',i) or re.findall(r'Message-ID: <\w+.\w+.\w+.\w+.\w+@\w+>',i)
        if find==[]:
            continue
        else:
            clean.append(find)
    return clean
# We need to assign To,Bcc,Cc,etc to emails which were in a list in those fields
def main_map(find_out):
    final=[]
    # loops through list created by Finder
    for i in find_out:
        # Loops through tab seperated fields in one email
        for t in i:
            # split on comma to seperate the emails from the field list
            split_comma=t.split(',')
            #loops through comma seperated emails
            for j in split_comma:
                # assigns a message id until a new one appears
                if 'Message-ID:' in j:
                    value=j
                    continue
                try:
                    # Appends Bcc,cc, To etc.. to the email
                    if j[0]==' ':
                        new_item=current_header.strip()+j
                        tupl=(new_item,value)
                        # creates a tuple of the identified email and the message id
                        final.append(tupl)
                    else:
                        # sets the current header
                        current_header=j[0:4]
                        tupl=(j,value)
                        final.append(tupl)
                except:
                    continue
    return final
# prints the field, message id pair
def final_out(fin_tup):
    for i,g in fin_tup:
        print '%s\t%s'%(i,g)

# puts it all together
def Mapper(line):
    line=line
    split_t_out=split_t(line)
    find_out=Finder(split_t_out)
    fin_tup=main_map(find_out)
    return final_out(fin_tup)

for line in sys.stdin:
    Mapper(line)

