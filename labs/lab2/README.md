# Lab 2

## Introduction

In this lab, we will look at convergence issues in bulk calculations
with respect to parameters such as the energy cutoff and k-point grid. We will be using QuantumEspresso (http://www.quantum-espresso.org/), an open scource first principles code. Note that all calculations in this lab are fairly simple and can be run on a modern desktop or laptop in serial mode, i.e., you do not actually need access to a supercomputing cluster to perform these calculations. 

## Initial setup

It is assumed that you have already cloned this repo, and done a git pull so that you are up to date with the repo.

To do the lab, you first need QuantumEspresso's pwscf. You have three options:

1. If you have your own Mac or Ubuntu 64-bit, you can use the
   executables already included in this repo. Run the following command to add the bin directory to your path as follows (assuming you are on bash):
    
    export PATH=$PATH:<path/to/repo>/bin/Mac or Ubuntu

2. You can download VirtualBox, and a Ubuntu virtual machine at this link and
   setup it up.
3. You can download the source code for QuantumEspresso and install it 
   yourself. *Attempt this only if you have a fairly good familiarity with compiling things on Unix-based OSes, or are willing to spend the time to figure it out. The compilation is pretty straightforward, but if you are not familiar with Unix-based OSes, it will be a challenge!*

Once you are done with the above, make sure you are in the lab2 folder by doing:

    cd <path/to/repo>/labs/lab2

## Q1 (10 points): Convergence of *absolute energies* with respect to energy cutoff.

Start by looking at the `Si.pw.in.template`, which is a template for the input file for PWSCF. You should get yourself familiar with the format, and what each of the sections and parameters mean. Note that some parameters have placeholders {xxx}, which will be replaced by our run script. A PWSCF_IO tutorial is provided in the tutorials folder of this repo to help you understand the parameters. You may also wish to consult the QuantumEspresso online documentation.

We have also written a Python script called `run_pw.py` to help you in this simulation. Again, read through the script to understand what it does. It is fairly heavily commented to aid you in your understanding. Note that this is a starting point. *You will need to understand enough to make changes in order to finish this lab.* A second script called `analyze.py` is provided to help you compile the results into a csv file, which can be opened with most spreadsheet programs for analysis. To run the scripts, you simply need to type

```python <script>.py <other parameters if necessary>```

1. Using PWSCF, calculate the energy of silicon as a function of cutoff
   energy. A good increment is ~10 Ry, in the range of 10-100 Ry. When changing the cutoff, make sure to keep the other variables (lattice constant, *k*-points, etc.) fixed. Record and plot your final results. Specify when you reach the level of convergence of ~5 meV/atom (you will need to take care of the unit conversions). Note that PWSCF calculates energy per primitive cell. 
2. Do you see a trend in your calculated energies with respect to cutoff? 
   If you see a trend, is this what you expect and why? If not, why?

## Q2 (10 points): Convergence of absolute energies with respect to *k*-points.

1. Modify the script in Q1 to calculate the energy as a function of k -point
   grid size. For each grid, record the number of unique *k*-points. Note that this is not the same as the *k* specified in the script and input file. The `analyze.py` script reports the number of unique *k*-points. Again, make sure to keep your other variables fixed. Record and plot your final results. Specify when you reach the level of convergence of ~5 meV/atom.
2. Do you see a trend in your calculated energies with respect to grid size?
   If you see a trend, is this what you expect and why? If not, why?
3. Plot your calculation time against the number of *k*-points. Is there a
   relationship, and if so, what is that relationship? (You will need to figure out how to extract the calculation time from the output files.)

## Q3 (10 points): Convergence of forces with respect to cutoff energies.

1. Let us now investigate the convergence of forces on atoms with respect to 
   cutoff. Displace a Si atom +0.05 in the z direction (fractional coordinates). Keeping other parameters fixed, calculate the forces on C as a function of cutoff. A good force value would be converged to within ~10 meV/Angstrom (note that PWSCF gives forces in Ryd/bohr). Use a *k*-point grid of 4x4x4. Plot and record your results, including all relevant parameters.

## Q4 (10 points): Convergence of forces with respect to *k*-points.

1. Repeat Q3, but this time, investigate the converge as a function of 
   *k*-point grid size. Keep all other parameters fixed. Record your relevant conditions (lattice parameter, cutoffs, etc.)

## Q5 (5 points): Convergence of energy differences with respect to energy cutoffs.
In practice only energy differences have physical meaning, as opposed to absolute energy scales, which can be arbitrarily shifted. Therefore, it is important to understand the convergence properties. Using PWSCF, calculate the energy difference between diamond structures at two lattice parameters as a function of cutoff. For example, you could calculate the energy of diamond at the experimental lattice parameter (6.74 bohr), the calculate the energy at 6.70 bohr (or any lattice parameter close to the minimum), take the difference between the two, and repeat for many energy cutoffs. Make sure to keep your other variables (lattice constant, k points, etc.) fixed while changing the cutoff. Record all relevant parameters such as the lattice constant, k -points, and so on. A good energy difference is converged to ~5 meV/atom (convert this to Ryd).
Problem 6 (10 points) Comparing Probs. 1, 2, 3, and 4, and 5:
How do the cutoff requirements change when looking at absolute energies vs.

looking at forces vs. energy differences? How do the k -point grid
requirements change? Can you explain this?
Page
