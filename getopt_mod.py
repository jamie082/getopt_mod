#!/usr/bin/python3

import sys
import getopt

args=sys.argv[1:]
inputfile = ''
outputfile = ''

try:
    opts, args = getopt.getopt(args, "hi:o:",["infile=","outfile="])
except getopt.GetoptError:
    print ('test.py -i <inputfile> -o <outputfile>')
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print ('args.py -i <inputfile> -o <outputfile>')
        sys.exit()
    elif opt in ("-i", "--infile"):
        inputfile = arg
    elif opt in ("-o", "--outfile"):
        outputfile = arg

print ('Input file is "', inputfile)
print ('Outputfile is "', outputfile)
