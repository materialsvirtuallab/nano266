#!/usr/bin/env python

"""
This is a very simple python starter script to automate a series of PWSCF
calculations. If you don't know Python, get a quick primer from the official
Python documentation at https://docs.python.org/2.7/. The script is deliberately
simple so that only basic Python syntax is used and you can get comfortable with
making changes and writing programs.

Author: Shyue Ping Ong
"""

# Load the submit_script.
# Note that the current submit_script does not have any PWSCF commands.
# Those commands will be appended after the corresponding input is generated.
submit_script = open("submit_script", "a")

# Load the Fe.pw.in.template file as a template.
with open("Fe.bcc.pw.in.template") as f:
    template = f.read()

# Set default values for various parameters
k = 8  # k-point grid of 8x8x8
alat = 5.42  # The lattice parameter for the cell in Bohr.

# Loop through different k-points.
for k in [8]:
    # This generates a string from the template with the parameters replaced
    # by the specified values.
    s = template.format(alat=alat, k=k)

    # Let's define an easy jobname.
    jobname = "Fe_bcc_%s_%s" % (alat, k)

    # Write the actual input file for PWSCF.
    with open("%s.pw.in" % jobname, "w") as f:
        f.write(s)

    # Write the command in submit_script.
    submit_script.write(
        'mpirun --map-by core --mca btl_openib_if_include "mlx5_2:1" '
        "--mca btl openib,self,vader pw.x -input {jobname}.pw.in -npool 1 > {jobname}.out\n".format(
            jobname=jobname
        )
    )
    print("Done with input generation for %s" % jobname)


# Append another line in submit_script to cleanup.
# For this lab, we don't need the files that are dumped into the tmp directory.
submit_script.write("rm -r tmp")
# Close the submit_script after appending all PWSCF commands.
submit_script.close()
