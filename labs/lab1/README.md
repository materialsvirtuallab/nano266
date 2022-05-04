LaTeX input:        mmd-mavrldoc-header
Title:              NANO266 Lab 1 - Calculations on Molecules
Author:             Shyue Ping Ong
Affiliation:        University of California, San Diego
Address:            9500 Gilman Drive, Mail Code 0448, La Jolla, CA 92093-0448
Web:                http://www.materialsvirtuallab.org
Base Header Level:  2
LaTeX Mode:         mavrldoc
LaTeX input:        mmd-mavrldoc-begin-doc
LaTeX footer:       mmd-mavrldoc-footer

# Introduction

We will begin our lab sessions with a gentle introduction into quantum
mechanical modeling of molecules. For this purpose, we will be using
computational chemistry techniques to study reaction energies, geometries,
vibrational frequencies, etc. We will be using NWChem, an open source quantum
chemistry code. Note that all calculations in this lab are fairly simple and on
very small molecules. So you can run them on a modern desktop or laptop in
serial mode, i.e., you do not actually need access to a supercomputing cluster
to perform these calculations.

For this lab, we will be studying one of the most important reactions in the
world - the formation of ammonia from nitrogen and hydrogen. Through the
Haber-Bosch process, this is the main industrial reaction for the production of
ammonia, which is then used in the production of fertilizers, etc. It is
estimated that one-third of the Earth's population is sustained by fertilizer
generated from ammonia produced by the Haber process.

In this lab, almost all analyses will be done using Unix-based command line
tools as it is important for you to learn how to find data efficiently using
these tools. Subsequent labs will provide you with the opportunity to use
Python to automate and analyze data more effectively. You are of course welcome
to write your own scripts if you have the know-how.

# Initial setup

It is assumed that you have already followed the instructions in the README.md
in the root labs folder and have access to nwchem, either on XSEDE or on your
own computer or virtual machine. Do a `git pull`
so that you are up to date with
the repo. Also, read through the README.md file in the main labs folder. 
Make sure you are in
the lab1 folder by doing:

```bash
cd <path/to/repo>/labs/lab1
```

# Submitting jobs to the Expanse queues

Expanse uses the Simple Linux Utility for Resource Management (Slurm) job
scheduling system. All supercomputing clusters use a job scheduler of some
sort, e.g., PBS, Sun GridEngine, SLURM. They differ in some features, but work
on the same basic principle. You send jobs to a queue, and they are run
according to some priority system. For more information, you may read the
guide at https://portal.xsede.org/sdsc-expanse

For the purposes of this lab, a sample *submit_script* has been provided. It is imperative that
you understand how the script works as you will be using this for the rest of
this and the next lab. Read the user guide to understand what each of the
options in the preamble means. You can then modify them to suit your needs.

To submit the job, just simply run:

```bash
sbatch submit_script
```

You may check on the status of your job using the following command:

```bash
squeue -u <username>
```

If you make a mistake and need to kill a job for whatever reason. use the
`scancel` command.

```bash
scancel <jobid>
```

# Q1 (10 points): Geometry optimization and energy of H<sub>2</sub>

We will start with one of the simplest molecules, diatomic hydrogen. In the
directory, we have provided a sample `H2.nw` input file. First, open up the
input file and understand its structure. Here's a replica of the input file
with comments added.

    memory total 1000 mb        # This specifies the memory for the job.

    geometry units angstroms    # This section provides a summary of the input
     H 0 0 0                    # geometry of the molecule. You usually get this
     H 0 0 0.7414               # from an experimental source or some chemistry
    end                         # rules

    # This nwchem job comprises three steps - geometry optimization, a frequency
    # calculation, and a final energy calculation at a larger basis set.

    title "H2 dft optimize"     # This is just the title
    charge 0                    # We are doing calculations on neutral H2.
    basis                       # Specifies the basis set for each atomic species
     H library "6-31G"
    end
    dft
     mult 1                     # Spin multiplicity of 1, i.e., singlet state
     xc b3lyp					# Exchange functional used is B3LYP.
    end
    task dft optimize           # Specify that we want to do a geometry optimization

    title "H2 dft freq"
    charge 0
    basis
     H library "6-31G"          # The same basis set must be used for the frequency calculation.
    end
    dft
     mult 1
     xc B3LYP                   # The same functional must be used for the frequency calculation.
    end
    task dft freq               # Specify that we want to do a frequency calculation

    title "H2 dft energy"
    charge 0
    basis
     H library "6-311G"         # A larger basis set is used to get better energies   end
    dft
     mult 1
     xc b3lyp
    end
    task dft energy             # Specify that we want to do an energy calculation

Let us first create a separate directory to run the calculation. This makes it
easier for us to cleanup after we are done.

```bash
mkdir scratch
cd scratch
```

Now, we copy the input file and submit script we want over, and submit the job

```bash
cp ../H2.nw .
cp ../submit_script .
sbatch submit_script
```
One of the most important line in submit script is the last one:
`nwchem H2.nw > H2.nwout`, which calls nwchem binary to use `H2.nw` as input and pipe the output to a new file, `H2.nwout`.

After the calculation is finished, check the output through:

```bash
grep -A 8 '"geometry" -> ' H2.nwout
```

This command finds all instances that `"geometry" -> ` occurs in `H2.nwout` and
prints out 8 lines after each occurence. The last configuration gives the final geometry of H2.

To get the final total energy, we can use grep from the command line:

```bash
grep "Total DFT energy" H2.nwout
```

The last energy line gives the total energy in **Hartree**.

For this question, record down the final bond length of H<sub>2</sub> in
angstroms and the final total energy in eV. Keep all output files until the end
of the lab.

# Q2 (10 points): Geometry optimization and energy of N<sub>2</sub>

Repeat Q1, but this time with N<sub>2</sub>. For this question, copy `H2.nw` to
`N2.nw` and then modify the input and submit script accordingly. 

Tip: People can use `vi` for file editing. The basic commands for `vi` is covered in this [link](https://www.guru99.com/the-vi-editor.html). 

The experimental N<sub>2</sub> bond  length is around 1.1 angstroms.

Again, record down the final bond length of N<sub>2</sub> in angstroms and the
final total energy in eV.

# Q3 (25 points): Geometry optimization and energy of NH<sub>3</sub>

The geommetry of ammonia is somewhat more complex, so we have provided an
`NH3.nw` file. Perform the same calculation as in Q1.

For NH<sub>3</sub>, record down the final N-H bond lengths, and also, calculate
the angle between the bonds, i.e., the H-N-H bond. Compare the calculated
values with the experimental ones. Cite the source of your experimental data
(e.g., by providing a journal citation or a weblink.)

Now, modify the file to add polarization functions to the basis set. The
easiest way is to change all "6-31G" to "6-31+G\*" and all "6-311G" to
"6-311+G\*" (technically, this adds diffuse as well as polarization functions,
but we are limited by the choice of basis sets available) Redo the calculation
and determine the bond lengths and angles again. Comment on the difference in
answer between the calculation with and without polarization functions.

Tip: One of the fastest ways to make changes to a file is using the unix command line tool called *sed*. For example, you can do the following:

```bash
sed 's/\(6-31[1]*\)G/\1+G*/' NH3.nw > NH3_polarized.nw
```

which will effectively replace all "6-31G" and "6-311G" with "6-31+G\*" and
"6-311+G\*" in the file "NH3.nw". The first argument to *sed* is the regular
expression. "s/" denotes that this is substitution. "\\\(6-31[1]*\\\)G"
denotes that we want to match all instances of "6-31(1)G", where the second 1
is optional. The brackets denote that we want to store the match before the G
in the first variable. The second half of the expressions "/\\1\+G\*/" denotes
that we want to replace all matches with the stored variable "\\1" followed by
"+G\*". Finally, the last part of the command "> NH3_polarized.nw" means we
want to pipe the output to a new file "NH3_polarized.nw".

Also record down the final energy of the NH<sub>3</sub> molecule in eV.

# Q4 (25 points): Formation enthalpy of NH<sub>3</sub>.

Calculate the formation enthalpy (per molecule) of NH<sub>3</sub> in kJ/mol. To
do this, you need to make sure that all calculations are done with the same
basis set. So redo the calculations for Q1 and Q2 with the same basis set with
polarization functions as in Q3.

Once you completed the calcualtions, you need to extract the thermal
corrections to the enthalpy as well as the energies. For example,

```bash
grep "Thermal correction to Enthalpy" H2.nwout
```

Note the units stipulated by NWChem in the output.

The enthalpy *H* is then given by the energy + the correction. The formation
energy of NH<sub>3</sub> is given by the enthalpy change of the following:

0.5 N<sub>2</sub> + 1.5 H<sub>2</sub> -> NH<sub>3</sub>

Compare your calculated formation enthalpy with experimental values. The NIST
Chemistry Webbook (http://webbook.nist.gov/chemistry/) is a good source of
data for many common molecules.

# Q5 (30 points)

In this question, you will investigate the effect that functional choice and
basis set choice has on the formation enthalpy of NH<sub>3</sub>. Repeat Q1-Q4,
but now modify your input files to experiment with the HFexch, PBE96 and B3LYP
functionals. You can also modify the basis set used between 6-31+g\* and 6-311+g\*. 
Note that you can either modify the functional or basis set for the geometry 
optimiation and frequency step, or the final energy calculation step, or both.

Discuss the effect of the functional and basis set on the geometries and final
energies. What would be a general recommended strategy for other similar
calculations if you want to perform the calculations as efficiently as possible
while maintaining relatively good accuracy?

Note that this is an open-ended question, and there is no right or wrong
answer. It is more important for you to understand the tradeoffs and come up
with a good justification for your recommendation.

# Bonus (10 points)

The formation enthalpy of ammonia is negative, but generally the reaction does
not take place (or does so very slowly) under normal conditions. That is why
the Haber process is performed under high pressures and temperatures with a
catalyst. The main reason is that N<sub>2</sub> is very unreactive. Can you
give a rough estimate of the reaction barrier using a few simple calculations,
assuming that one has to break the N<sub>2</sub> triple bond for the reaction?
