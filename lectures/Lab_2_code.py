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