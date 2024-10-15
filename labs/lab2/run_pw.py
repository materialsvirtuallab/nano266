#!/usr/bin/env python

"""
This is a very simple python starter script to automate a series of PWSCF
calculations. If you don't know Python, get a quick primer from the official
Python documentation at https://docs.python.org/3.8/. The script is deliberately
simple so that only basic Python syntax is used and you can get comfortable with
making changes and writing programs.

Author: Shyue Ping Ong, Yiming Chen
"""

# Load the submit_script. 
# Note that the current submit_script does not have any PWSCF commands. 
# Those commands will be appended after the corresponding input is generated.   
submit_script = open("submit_script", 'a')
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
    jobname = f"Si_{ecut}_{k}_{alat}"

    # Write the actual input file for PWSCF.
    with open(f"{jobname}.pw.in", "w") as f:
        f.write(s)

    # Write the command in submit_script.    
    submit_script.write(
            'mpirun --map-by core --mca btl_openib_if_include "mlx5_2:1" ' 
            f'--mca btl openib,self,vader pw.x -input {jobname}.pw.in -npool 1 > {jobname}.out\n')
    print(f"Done with input generation for {jobname}.")

# Append another line in submit_script to cleanup. 
# For this lab, we don't need the files that are dumped into the tmp directory.
submit_script.write("rm -r tmp")
# Close the submit_script after appending all PWSCF commands.
submit_script.close()
