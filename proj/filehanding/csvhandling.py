import csv

# fh = open('data.csv')
# reader = csv.reader(fh)
# for line in reader:
#     print line
# fh.close()

# with open('data.csv') as fh:
#     for line in csv.reader(fh):
#         print line

with open('data.csv') as fh:
    for line in csv.reader(fh, delimiter='|'):
        print line