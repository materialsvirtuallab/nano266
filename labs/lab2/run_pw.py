#!/usr/bin/env python

"""
This is a very simple python starter script to automate a series of PWSCF
calculations.

Author: Shyue Ping Ong
"""

import os
import shutil

# We use numpy, a numerical python package to help with some analyses. It comes
# with most modern Unix-based OSes, including Mac and Linux.
import numpy as np

# Load the Fe.pw.in.template file as a template.
with open("Si.pw.in.template") as f:
    template = f.read()

# Set the k-point grid
k = 8
ecut = 10 # In Ry
alat = 10 # The lattice parameter for the cell in Bohr.

# Loop through a series of values of ecut. Note that ecut is stipulated in Ry
# in PWSCF. Google for the meaning of the numpy.arange function (as well as any
# other python functions that are alien to you). When writing code to automate
# anything, you frequently need to consult documentation on the web. 
for ecut in np.arange(10, 50, 10):
    s = template.format(alat=alat, k=k, ecut=ecut)
    jobname = "Si_%s" % ecut
    
    # Write the actual input file for PWSCF.
    with open("%s.pw.in" % jobname, "w") as f:
        f.write(s)

    #Print some status messages.
    print("Running with ecut = %f, alat = %f, k = %f..." % (ecut, alat, k))
    # Run PWSCF. Modify the pw.x command accordingly if needed.
    os.system("pw.x.mac < {jobname}.pw.in > {jobname}.out".format(jobname=jobname))

    print("Done")

shutil.rmtree("tmp")
