LaTeX input:        mmd-article-header
Title:              NANO266 Lab 1
Base Header Level:  2
LaTeX Mode:         memoir
LaTeX input:        mmd-article-begin-doc
LaTeX footer:       mmd-memoir-footer

# Lab 1

## Introduction

We will begin our lab sessions with a gentle introduction into quantum
mechanical modeling of molecules. For this purpose, we will be using
computational chemistry techniques to study reaction energies, ionization
energies and electron affinities, vibrational frequencies, etc. We will
be using NWChem, an open source quantum chemistry code. Note that all
calculations in this lab are fairly simple and on very small molecules.
So you can be run them on a modern desktop or laptop in serial mode, i.e., you
do not actually need access to a supercomputing cluster to perform these
calculations.

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

## Initial setup

It is assumed that you have already followed the instructions in the README.md
in the root labs folder and have access to nwchem, either on XSEDE or on your
own computer or virtual machine. Do a git pull so that you are up to date with
the repo. Also, read through the README.md file in the main labs folder and
make sure that you have NWChem setup properly. Try typing `nwchem` in your
terminal to make sure that everything is working. You will get an error message
because there is no input file, but that's not a big deal.

Once you are done with the above, make sure you are in the lab1 folder by doing:

```bash
cd <path/to/repo>/labs/lab1
```

## Q1 (10 points): Geometry optimization and energy of H2

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

```shell
mkdir scratch
cd scratch
```

Now, we copy the input files we want over, and run nwchem:

```shell
cp ../H2.nw .
nwchem H2.nw > H2.nwout
```

After a very short while, the calculation should complete and the results are
in the `H2.nwout` file. To find the final coordinates, search for the final
occurence of:

```shell
grep -A 8 '"geometry" -> ' H2.nwout
```

This command finds all instances that `"geometry" -> ` occurs in `H2.nwout` and
prints out 8 lines after each occurence.

To get the final total energy, we can use grep from the command line:

```bash
grep "Total DFT energy" H2.nwout
```

The final energy line gives the total energy in **Hartree**.

For this question, record down the final bond length of H2 in angstroms and the
final total energy in eV. Keep all output files until the end of the lab.

## Q2 (20 points): Geometry optimization and energy of N<sub>2</sub>

Repeat Q1, but this time with N2. For this question, copy `H2.nw` to `N2.nw` and
then modify the file accordingly. The experimental N<sub>2</sub> bond length is
around 1.1 angstroms.

Again, record down the final bond length of H2 in angstroms and the
final total energy in eV.

## Q3 (20 points): Geometry optimization and energy of NH<sub>3</sub>

The geommetry of ammonia is somewhat more complex, so we have provided an
`NH3.nw` file. Perform the same calculation as in Q1.

For NH<sub>3</sub>, record down the final N-H bond lengths, and also, calculate
the  angle between the bonds. Compare the calculated values with the
experimental ones. Cite the source of your experimental data (e.g., by
providing a journal citation or a weblink.)

Also record down the final energy of the NH<sub>3</sub> molecule in eV.

## Q4 (20 points): Formation enthalpy of NH<sub>3</sub>.

Calculate the formation enthalpy (per molecule) of NH<sub>3</sub> in kJ/mol. To
do this, you need not only the energies from Q1-Q3, you also need to extract
the thermal correction to the enthalpy. For example,

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

## Q5 (30 points)

In this question, you will investigate the effect that functional choice and
basis set choice has on the formation enthalpy of NH<sub>3</sub>. Repeat Q1-Q4,
but now modify your input files to experiment with the HF, PBE and B3LYP
functionals. You can also modify the basis set used between 6-31g and 6-311g.
Note that you can either modify the functional or basis set for the geometry
optimiation and frequency step, or the final energy calculation step, or both.

Discuss the effect of the functional and basis set on the geometries and final
energies. What would be a general recommended strategy for other similar
calculations if you want to perform the calculations as efficiently as possible
while maintaining relatively good accuracy?

Note that this is an open-ended question, and there is no real right or wrong
answer. It is more important for you to understand the tradeoffs and come up
with a good justification for your recommendation.
