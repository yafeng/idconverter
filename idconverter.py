import sys
import os
import getopt

################  Comand-line arguments ################
if len(sys.argv[1:])<=1:  ### Indicates that there are insufficient number of command-line arguments
    print "Warning! wrong command, please read the mannual in Readme.txt."
    print "Example: python idconverter.py --input input_filename --output output_filename --n 1"
else:
    options, remainder = getopt.getopt(sys.argv[1:],'', ['input=',
                                                         'n=',
                                                         'output='])
    for opt, arg in options:
        if opt == '--input': input_file=arg
        elif opt == '--n': n=int(arg)
        elif opt == '--output':output_file=arg
        else:
            print "Warning! Command-line argument: %s not recognized. Exiting..." % opt; sys.exit()

handle=open("proteinID_gene.txt",'r')
protein_gene={}

for line in handle:
    row=line.strip().split('\t')
    try:
        protein_gene[row[0]]=row[1]
    except IndexError:
        continue;

handle.close()

input=open(input_file,'r')
output=open(output_file,'w')

header=input.readline().strip().split('\t')
header.insert(n,'gene name')
output.write('\t'.join(header)+'\n')

for line in input:
    row=line.strip().split('\t')
    try:
        protein_list=row[n-1].split(";")
        genename=[]
        for protein in protein_list:
            genename.append(protein_gene.get(protein,'Not Found'))
        
        row.insert(n,";".join(genename))
    except IndexError:
        continue;
    output.write('\t'.join(row)+'\n')

input.close()
output.close()


