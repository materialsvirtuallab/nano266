#!/usr/bin/env python

import re
import sys

energy_pattern = re.compile("total energy\s+=\s+([\d\.\-]+)\sRy")

def get_energy(filename):
    energy = None
    with open(filename) as f:
        for l in f:
            m = energy_pattern.search(l)
            if m:
                energy = float(m.group(1))
    return energy


for f in sys.argv[1:]:
    print("%s: Final Energy = %f" % (f, get_energy(f)))
