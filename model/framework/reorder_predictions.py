import sys
import csv

infile_0 = sys.argv[0]
infile_1 = sys.argv[1]
outfile = sys.argv[2]

# descriptors file
with open(infile_0, "r") as f:
    reader = csv.reader(f)
    h = next(reader)
    for i, r in enumerate(reader):


# 
with open(infile_1, "r") as f:
    reader = csv.reader(f)
    h = next(reader)
