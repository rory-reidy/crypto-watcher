import os
import csv

with open('prices.csv.bak', 'rU') as infile, open('prices.csv', 'U') as outfile:
    for line in infile:
        outfile.write(line.replace('\r'))
os.remove('prices.csv.bak')