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


# Q2 (40 points): Stability of the PbTiO$_3$ perovskite

PbTiO$_3$ is a perovskite oxide which is ferroelectric. The ferroelectric response
of PbTiO3 is the result of a displacive transition where a low temperature tetragonal
phase is preferred over the cubic phase. In this problem, we will study the energetics of cubic PbTiO3 and use
first principles calculations to gather information pertaining to the displacive transition to
the tetragonal phase.
A. Calculate and plot the energy of cubic PbTiO3 as a function of lattice parameter. Use a
4 × 4 × 4 k-point mesh with a 1,1,1 offset (see example script in the handout). Sample
lattice parameters with a sufficiently fine grid to get a reliable value for the equilibrium
lattice constant. To get an idea where to begin, note that the room-temperature
experimental lattice constant is about 3.97°A(1 °A= 0.529177 bohr).
B. Using the equilibrium lattice parameter from part (A), plot the energy as a function of
displacement of the Ti atom along one of the cubic lattice directions, allowing the O
atoms to fully relax for each displacement. Report the Ti displacement at which the
total energy is at a minimum. What is the energy difference between this configuration
and the minimum-energy configuration from part (A)? Be aware that for PbTiO3, the
Ti displacement will be very small.
C. Now allow both the Ti atom and the O atoms to relax and find the minimum energy
structure, using the minimum-energy Ti displacement from part (B) as your starting
configuration. Report the final atomic positions and final energy.
D. Which phase is the most energetically stable for PbTiO3 and how does that relate to the
ferroelectric behavior of this material?


# Q3: Formation Energy of the CuAu alloy

1. Calculate the equation of state (energy versus volume) for FCC Cu and Au,
   with differences converged to 0.15 mHa? Investigate the k-point sampling for 
   FCC Cu and Au with different lattice constants (the experimental values are 
   aCu = 3.677 °Aand aAu = 4.059 °A) and plane-wave energy cutoff ecutwfc =30 
   Ryd. Use different k-meshes (e.g. 4×4×4, 8×8×8, 12×12×12, and 20×20×20); and 
   different ecutrho (e.g. 120 up to 360 Ryd). Which k-point mesh provides 
   convergence to 0.15 mHa?
2. At 0K, will CuAu (in the 50%-50% concentration) prefer to segregate or order?
   Explore the stability of the L10 phase of CuAu. As explained in the Handout, 
   the ordered phase L10 between copper and gold, is a body-centered tetragonal 
   (bct) with two atoms in the unit cell, and lattice parameters are a = b 6= c
3. Calculate the equation of state of CuAu E = E(a, c), where a=celldm(1) and c/
   a=celldm(3). A good range for c/a is in between 1, for FCC structures, and 1/
   p2, for BCC structures. We strongly recommend to use a job-script, to change 
   automatically the value of celldm(1) and celldm(3). It would be useful to 
   make a first-pass check for the best value for c/a, using a sparse k-point 
   mesh.
4. Calculate the formation energy of CuAu:
   $$\Delta H_f (\mbox{CuAu}) = E_{tot}(\mbox{CuAu}) − E_b(\mbox{Cu}) − E_b(\mbox{Au})$$
   where Eb(Cu) and Eb(Au) are the total energies for Cu and Au in their FCC 
   bulk phase. The total energy CuAu, Etot(CuAu), is chosen for fully relaxed 
   equilibrium lattice parameters and internal coordinates.
