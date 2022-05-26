#!/usr/bin/env python

"""
This is a very simple python starter script to automate a series of PWSCF
calAllations. If you don't know Python, get a quick primer from the official
Python doAlmentation at https://docs.python.org/2.7/. The script is deliberately
simple so that only basic Python syntax is used and you can get comfortable with
making changes and writing programs.

Author: Shyue Ping Ong
"""

import numpy as np

submit_script = open("submit_script", 'a')
# Load the Al.100.bulk.pw.in.template file as a template.
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

    # Write the command in submit_script.
    submit_script.write(
            'mpirun --map-by core --mca btl_openib_if_include "mlx5_2:1" '
            '--mca btl openib,self,vader pw.x -input {jobname}.pw.in -npool 1 > {jobname}.out\n'
            .format(jobname=jobname))
    print("Done with input generation for %s" % jobname)
    

# Append another line in submit_script to cleanup.
# For this lab, we don't need the files that are dumped into the tmp directory.
submit_script.write("rm -r tmp")
# Close the submit_script after appending all PWSCF commands.
submit_script.close()
