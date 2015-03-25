# Lab 2

## Introduction

In this lab, we will look at convergence issues in bulk calculations
with respect to parameters such as the energy cutoff and k-point grid. We will be using QuantumEspresso (http://www.quantum-espresso.org/), an open scource first principles code.

## Initial setup

To do the lab, you first need QuantumEspresso's pwscf. You have three options:

1. If you have your own Mac or Ubuntu 64-bit, you can use the
   executables already included in this repo. Run the following command to add the bin directory to your path as follows (assuming you are on bash):

    ```
    export PATH=$PATH:/path/to/repo/bin
    ```

## Q1 (10 points): Convergence of *absolute energies* with respect to energy cutoff.



