#!/usr/bin/env python

"""
This is a very simple python starter script to automate a series of PWSCF
calculations.

Author: Shyue Ping Ong
"""

import os
import shutil

# Load the Fe.pw.in.template file as a template.
with open("Si.pw.in.template") as f:
    template = f.read()

# Set the k-point grid
k = 8
ecut = 10 # In Ry
alat = 10.26 # The lattice parameter for the cell in Bohr.
psp = "Si.pbe-n-kjpaw_psl.0.1.UPF"

# Loop through a series of values of ecut. Note that ecut is stipulated in Ry
# in PWSCF. 
for ecut in [10, 20, 30, 40, 50]:
    s = template.format(alat=alat, k=k, ecut=ecut, pseudopotential=psp)
    jobname = "Si_%s_%s_%s" % (ecut, k, alat)
    
    # Write the actual input file for PWSCF.
    with open("%s.pw.in" % jobname, "w") as f:
        f.write(s)

    #Print some status messages.
    print("Running with ecut = %s, alat = %s, k = %s..." % (ecut, alat, k))
    # Run PWSCF. Modify the pw.x command accordingly if needed.
    os.system("pw.x < {jobname}.pw.in > {jobname}.out".format(jobname=jobname))

    print("Done")

shutil.rmtree("tmp")
