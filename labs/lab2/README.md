# Lab 2

## Introduction

In this lab, we will look at convergence issues in bulk calculations
with respect to parameters such as the energy cutoff and k-point grid. We will be using QuantumEspresso (http://www.quantum-espresso.org/), an open scource first principles code.

## Initial setup

It is assumed that you have already cloned this repo, and done a git pull so that you are up to date with the repo.

To do the lab, you first need QuantumEspresso's pwscf. You have three options:

1. If you have your own Mac or Ubuntu 64-bit, you can use the
   executables already included in this repo. Run the following command to add the bin directory to your path as follows (assuming you are on bash):

    ```
    export PATH=$PATH:<path/to/repo>/bin/Mac or Ubuntu
    ```

2. You can download VirtualBox, and a Ubuntu virtual machine at this link and
   setup it up.
3. You can download the source code for QuantumEspresso and install it 
   yourself. *Attempt this only if you have a fairly good familiarity with compiling things on Unix-based OSes, or are willing to spend the time to figure it out. The compilation is pretty straightforward, but if you are not familiar with Unix-based OSes, it will be a challenge!*

Once you are done with the above, make sure you are in the lab2 folder by doing:

    ```
    cd <path/to/repo>/labs/lab2
    ```

## Q1 (10 points): Convergence of *absolute energies* with respect to energy cutoff.

a. Using PWSCF, calculate the energy of silicon as a function of cutoff
   energy. A good increment is ~10 Ryd, in the range of 10-100 Ryd. When changing the cutoff, make sure to keep the other variables (lattice constant, *k*-points, etc.) fixed. Record all relevant parameters such as lattice constant, *k*-points, and so on. Record and plot your final results. Specify when you reach the level of convergence of ~5 meV/atom (you will need to take care of the unit conversions). Note that PWSCF calculates energy per primitive cell. In this directory, a run_pw.py script as well as 
b. Do you see a trend in your calculated energies with respect to cutoff? 
   If you see a trend, is this what you expect and why? If not, why?

## Q2 (10 points): Convergence of absolute energies with respect to *k*-points.

