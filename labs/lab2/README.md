# Lab 2

## Introduction

In this lab, we will look at convergence issues in bulk calculations
with respect to parameters such as the energy cutoff and k-point grid. We will be using QuantumEspresso (http://www.quantum-espresso.org/), an open scource first principles code. Note that all calculations in this lab are fairly simple and can be run on a modern desktop or laptop in serial mode, i.e., you do not actually need access to a supercomputing cluster to perform these calculations. 

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

Start by looking at the `Si.pw.in.template`, which is a template for the input file for PWSCF. You should get yourself familiar with the format, and what each of the sections and parameters mean. Note that some parameters have placeholders {xxx}, which will be replaced by our run script. A PWSCF_IO tutorial is provided in the tutorials folder of this repo to help you understand the parameters. You may also wish to consult the QuantumEspresso online documentation.

We have also written a Python script called `run_pw.py` to help you in this simulation. Again, read through the script to understand what it does. It is fairly heavily commented to aid you in your understanding. Note that this is a starting point. *You will need to understand enough to make changes in order to finish this lab.* A second script called `analyze.py` is provided to help you compile the results into a csv file, which can be opened with most spreadsheet programs for analysis. To run the scripts, you simply need to type

```python <script>.py <other parameters if necessary>```

i.  Using PWSCF, calculate the energy of silicon as a function of cutoff
    energy. A good increment is ~10 Ryd, in the range of 10-100 Ryd. When changing the cutoff, make sure to keep the other variables (lattice constant, *k*-points, etc.) fixed. Record all relevant parameters such as lattice constant, *k*-points, and so on. Record and plot your final results. Specify when you reach the level of convergence of ~5 meV/atom (you will need to take care of the unit conversions). Note that PWSCF calculates energy per primitive cell. 
ii. Do you see a trend in your calculated energies with respect to cutoff? 
    If you see a trend, is this what you expect and why? If not, why?

## Q2 (10 points): Convergence of absolute energies with respect to *k*-points.

