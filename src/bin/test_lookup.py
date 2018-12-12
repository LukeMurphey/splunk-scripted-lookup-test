#!/usr/bin/env python

import csv
import sys

def main():
    if len(sys.argv) != 3:
        print "Usage: python external_lookup.py [host field] [ip field]"
        sys.exit(1)

    hostfield = sys.argv[1]
    ipfield = sys.argv[2]

    infile = sys.stdin
    outfile = sys.stdout

    r = csv.DictReader(infile)
    header = r.fieldnames

    w = csv.DictWriter(outfile, fieldnames=['clientip', 'clienthost', 'test'])
    w.writeheader()
    w.writerow({
        'clientip': 'clientip',
        'clienthost': 'clienthost',
        'test': 'test'
    })

main()

