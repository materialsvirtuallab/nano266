#!/usr/bin/env python

import re
import sys
import csv
import argparse


# This defines the patterns for extracting relevant data from the output
# files.
patterns = {
    "energy": re.compile("total energy\s+=\s+([\d\.\-]+)\sRy"),
    "ecut": re.compile("kinetic\-energy cutoff\s+=\s+([\d\.\-]+)\s+Ry"),
    "alat": re.compile("celldm\(1\)=\s+([\d\.]+)\s"),
    "nkpts": re.compile("number of k points=\s+([\d]+)"),
    "total_force": re.compile("Total force =\s+([\d\.]+)")
}


def get_results(filename):
    data = {}
    with open(filename) as f:
        for l in f:
            for k, p in patterns.items():
                m = p.search(l)
                if m:
                    data[k] = float(m.group(1))
                    continue
    return data


def analyze(filenames):
    fieldnames = ['filename', 'ecut', 'nkpts', 'alat', 'energy','total_force']
    with open('results.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for f in filenames:
            r = get_results(f)
            r["filename"] = f
            writer.writerow(r)
    print("Results written to results.csv!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='''Tool for analysis of PWSCF calculations.''')
    parser.add_argument(
        'filenames', metavar='filenames', type=str, nargs="+",
        help='Files to process. You may use wildcards, e.g., "python analyze.py *.out".')
    args = parser.parse_args()
    analyze(args.filenames)
