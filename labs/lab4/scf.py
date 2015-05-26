#!/usr/bin/env python

"""
This is a very simple python starter script to automate a series of PWSCF
calAllations. If you don't know Python, get a quick primer from the official
Python doAlmentation at https://docs.python.org/2.7/. The script is deliberately
simple so that only basic Python syntax is used and you can get comfortable with
making changes and writing programs.

Author: Shyue Ping Ong
"""

import os
import shutil
import numpy as np

# Load the Si.pw.in.template file as a template.
with open("Al.100.bulk.pw.in.template") as f:
    template = f.read()

# Set default values for various parameters
k = 16 # k-point grid of 16x16x16
alat = 7.65 # The lattice parameter for the cell in Bohr.

# Loop through different k-points.
for alat in np.arange(7.55, 7.65, 0.01):
    # This generates a string from the template with the parameters replaced
    # by the specified values.
    s = template.format(k=k, alat=alat)

    # Let's define an easy jobname.
    jobname = "Al_100_bulk_%s" % (alat)

    # Write the actual input file for PWSCF.
    with open("%s.pw.in" % jobname, "w") as f:
        f.write(s)

    #Print some status messages.
    print("Running with alat = %s..." % (alat))
    # Run PWSCF. Modify the pw.x command accordingly if needed.
    os.system("pw.x -inp {jobname}.pw.in > {jobname}.out".format(jobname=jobname))

    print("Done. Output file is %s.out." % jobname)

# This just does cleanup. For this lab, we don't need the files that are
# dumped into the tmp directory.
shutil.rmtree("tmp")
