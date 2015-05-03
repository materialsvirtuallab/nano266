LaTeX input:        mmd-mavrldoc-header
Title:              NANO266 Lab 3 - Bulk properties from Quantum Mechanics
Base Header Level:  2
LaTeX Mode:         mavrldoc
LaTeX input:        mmd-mavrldoc-begin-doc
LaTeX footer:       mmd-mavrldoc-footer


# Introduction

In this lab, we will look at obtaining bulk properties from quantum mechanics.
We will still be using QuantumEspresso. We will also introduce you to the
basics of running calculations on supercomputing resources, e.g., how to submit
jobs, handle queues, etc.

# Initial setup

By this stage, you should already have everything set up. Make sure you are in
the lab3 folder by doing:

```bash
cd <path/to/repo>/labs/lab3
```

# Submitting jobs to the Comet queues



# Q1 (12 points): The bcc-hcp transition in iron

In this problem, you will look at the bcc to hcp transition in iron. We will be 
using the PBE GGA functional that we used in the earlier lab. Use an energy
cutoff of 50 Ry with a charge density cutoff of 250 Ry. You will need to 
determine an appropriate $k$-point mesh for both the bcc and hcp structures. 
The energy differences are very small; choose parameters to converge your 
energies to within 1 meV. 
1. Calculate the ground state energy of Fe in both the bcc and hcp structure.
   Two template files are provided for bcc and hcp. A run_pw.py file is also
   provided that works for bcc, but you need to modify it as appropriate to works
   for hcp. Note that it is important when comparing energies that the k-point
   samplings for both systems are comparable and converged. Determine an
   appropriate $k$-point grid for both structures. Optimize the lattice parameters
   for both bcc and hcp Fe (i.e., $a$ for BCC and $a$ and $c$ for HCP). 
2. Varying the volume of the cell calculate when the HCP structure becomes more
   favorable than the BCC one. Further, (40 points)
3. Calculate and compare the total energy for the BCC structure in the ferromagnetic,
   anti-ferromagnetic, and nonmagnetic states. (20 points)

