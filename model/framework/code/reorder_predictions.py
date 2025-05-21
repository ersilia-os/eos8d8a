import sys
import csv

infile_0 = sys.argv[1]
infile_1 = sys.argv[2]
outfile = sys.argv[3]

# descriptors file
with open(infile_0, "r") as f:
    reader = csv.reader(f)
    h = next(reader)
    names = []
    for r in reader:
        names += [r[0]]

# predictions file
with open(infile_1, "r") as f:
    reader = csv.reader(f)
    h = next(reader)
    values = {}
    for r in reader:
        values[r[0]] = r[1]

# final file
with open(outfile, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["mycpermcheck_proba"])
    for n in names:
        writer.writerow([values[n]])
