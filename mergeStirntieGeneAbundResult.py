#!/usr/bin/env python3.4
import sys
import getopt
def usage():
    print('''Useage: python script.py [option] [parameter] merge stringtie expression result, obtain expression FPKM table
    -l/--list               input the stirngtie gene Abund result list (absolute address)
    -o/--results             the  results
    -h/--help                show possible options''')
#######################
opts, args = getopt.getopt(sys.argv[1:], "hl:o:",["help","list=","results="])
for op, value in opts:
    if op == "-l" or op == "--list":
        list = value
    elif op == "-o" or op == "--results":
        results = value
    elif op == "-h" or op == "--help":
        usage()
        sys.exit(1)
if len(sys.argv) < 5:
    usage()
    sys.exit(1)
f1=open(list)
f2=open(results,'w')
total={}
title='GeneID\t'
tl=[]
for file in f1:
    file=file.strip()
    a=file.split('/')
    c=a[-1].split('.')
    tissue=c[0]
    tl.append(tissue)
    locals()[tissue]={}
    file=open(file)
    title=title+tissue+'\t'
    for i in file:
        i=i.strip('\n')
        i=i.split('\t')
        total[i[0]]=''
        locals()[tissue][i[0]]=i[7]
f2.write(title.strip('\t')+'\n')
f1.close()
for key,value in total.items():
    wy=''
    for tissue in tl:
        wy=wy+'\t'+locals()[tissue].get(key,'NA')
    f2.write(key+wy+'\n')
f2.close()
