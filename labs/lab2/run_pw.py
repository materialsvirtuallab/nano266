#!/usr/bin/env python

"""
This is a very simple python starter script to automate a series of PWSCF
calculations. If you don't know Python, get a quick primer from the official
Python documentation at https://docs.python.org/2.7/. The script is deliberately
simple so that only basic Python syntax is used and you can get comfortable with
making changes and writing programs.

Author: Shyue Ping Ong
"""

import os
import shutil

# Load the Si.pw.in.template file as a template.
with open("Si.pw.in.template") as f:
    template = f.read()

# Set default values for various parameters
k = 8 # k-point grid of 8x8x8
ecut = 50 # In Ry
alat = 10.26 # The lattice parameter for the cell in Bohr.
psp = "Si.pbe-n-kjpaw_psl.0.1.UPF"

# Loop through a series of values of ecut. Note that ecut is stipulated in Ry
# in PWSCF. Modify this accordingly to loop through either different values
# of alat, k, ecut, etc.
for ecut in [10, 20, 30, 40, 50]:
    # This generates a string from the template with the parameters replaced
    # by the specified values.
    s = template.format(alat=alat, k=k, ecut=ecut, pseudopotential=psp)

    # Let's define an easy jobname.
    jobname = "Si_%s_%s_%s" % (ecut, k, alat)

    # Write the actual input file for PWSCF.
    with open("%s.pw.in" % jobname, "w") as f:
        f.write(s)

    #Print some status messages.
    print("Running with ecut = %s, alat = %s, k = %s..." % (ecut, alat, k))
    # Run PWSCF. Modify the pw.x command accordingly if needed.
    os.system("pw.x < {jobname}.pw.in > {jobname}.out".format(jobname=jobname))

    print("Done. Output file is %s.out." % jobname)

# This just does cleanup. For this lab, we don't need the files that are
# dumped into the tmp directory.
shutil.rmtree("tmp")
