#!/usr/bin/env python

import re
import sys
import csv


# This defines the patterns for extracting relevant data from the output
# files.
patterns = {
    "energy": re.compile("total energy\s+=\s+([\d\.\-]+)\sRy"),
    "ecut": re.compile("kinetic\-energy cutoff\s+=\s+([\d\.\-]+)\s+Ry"),
    "alat": re.compile("celldm\(1\)=\s+([\d\.]+)\s"),
    "nkpts": re.compile("number of k points=\s+([\d]+)")
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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage is "python analyze.py filenames"')
        print('Wildcards can be used, e.g., "python analyze *.out"')
        sys.exit(0)
    fieldnames = ['filename', 'ecut', 'nkpts', 'alat', 'energy']
    with open('results.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for f in sys.argv[1:]:
            r = get_results(f)
            r["filename"] = f
            writer.writerow(r)
    print("Results written to results.csv!")
