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

Comet uses the SLURM queuing system. For more information, you may read the
guide at https://www.sdsc.edu/support/user_guides/comet.html. For the purposes
of this lab, a sample *submit_script* has been provided. It is imperative that
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

# Q1 (30 points): The bcc-hcp transition in iron

In this problem, you will look at the bcc to hcp transition in iron. We will be
using the PBE GGA functional that we used in the earlier lab. Use an energy
cutoff of 50 Ry with a charge density cutoff of 250 Ry. You will need to
determine an appropriate $k$-point mesh for both the bcc and hcp structures.
The energy differences are very small; choose parameters to converge your
energies to within 1 meV.

1. Calculate the ground state energy of Fe in both the bcc and hcp structure.
   Two template files are provided for bcc and hcp. A run_pw.py file is also
   provided that works for bcc, but you need to modify it as appropriate to
   work for hcp.
2. Varying the volume of the cell calculate when the hcp structure becomes more
   favorable than the bcc one. Note that it is important when comparing
   energies that the $k$-point samplings for both systems are comparable and
   converged. Determine an appropriate $k$-point grid for both structures.
   Optimize the lattice parameters for both bcc and hcp Fe (i.e., $a$ for bcc and $a$ and $c$ for hcp).
3. Calculate and compare the total energy for the BCC structure in the
   ferromagnetic, anti-ferromagnetic, and nonmagnetic states. (10 points)

Note that you will need to read the PWSCF manual to figure out how to set
various options to do this work. At this stage of the course, we will not
be providing complete scripts and you need to work through the manuals to
figure out what to do. This is part and parcel of computational modeling work.

# Q2 (40 points): Stability of the PbTiO<sub>3</sub> perovskite

PbTiO<sub>3</sub> is a perovskite oxide which is ferroelectric. The
ferroelectric response of PbTiO<sub>3</sub> is the result of a displacive
transition where a low temperature tetragonal phase is preferred over the cubic
phase.

1. Calculate and plot the energy of cubic PbTiO3 as a function of lattice
   parameter. Use a 4 $\times$ 4 $\times$ 4 $k$-point mesh with a 1, 1, 1
   offset. Sample lattice parameters with a sufficiently fine grid to get a
   reliable value for the equilibrium lattice constant. To get an idea where to
   begin, note that the room-temperature experimental lattice constant is about
   3.97 ${\buildrel _{\circ} \over {\mathrm{A}}}$.
2. Using the equilibrium lattice parameter from part (1), plot the energy as a
   function of displacement of the Ti atom along one of the cubic lattice
   directions, allowing the O atoms to fully relax for each displacement.
   Report the Ti displacement at which the total energy is at a minimum. What
   is the energy difference between this configuration and the minimum-energy
   configuration from part (1)? Be aware that for PbTiO$_3$, the Ti
   displacement will be very small.
3. Now allow both the Ti atom and the O atoms to relax and find the minimum
   energy structure, using the minimum-energy Ti displacement from part (B) as
   your starting configuration. Report the final atomic positions and final
   energy.
4. Which phase is the most energetically stable for PbTiO3 and how does that
   relate to the ferroelectric behavior of this material?

# Q3 (30 points): Formation Energy of the Cu$_{1-x}$Au$_x$ alloys

1. Calculate the equation of state (energy versus lattice parameter) for FCC
   Cu and Au, with differences converged to 0.15 mHa? Investigate the k-point
   sampling for FCC Cu and Au with different lattice constants (the
   experimental values are $a_{\mbox{Cu}} = 3.677 {\buildrel _{\circ} \over
   {\mathrm{A}}}$ and $a_{\mbox{Au}} = 4.059 {\buildrel _{\circ} \over
   {\mathrm{A}}}$) and plane-wave energy cutoff ecutwfc =30 Ryd. Use different
   $k$ meshes (e.g. $4\times4\times4$, $8\times8\times8$, $12\times12\times12$,
   $20\times20\times20$ and different ecutrho (120-360 Ryd). Which $k$-point
   mesh provides convergence to 0.15 mHa?
2. We will now investigate the formation energies of Cu$_{1-x}$Au$_x$ at 0K.  will CuAu (in the 50%-50% concentration) prefer to segregate or
   order? Explore the stability of the L10 phase of CuAu. The ordered phase
   L10 between copper and gold, is a body-centered tetragonal (bct) with two
   atoms in the unit cell, and lattice parameters are $a = b \ne c$. You may
   search the internet for the structure and experimental lattice parameters.
   Calculate the equation of state of CuAu, $E = E(a, c)$,
   where $a$=celldm(1) and $c/a$=celldm(3). A good range for c/a is in between
   1, for FCC structures, and $1/\sqrt{2}$, for BCC structures. Modify the job
   script accrodingly ldm(1) and celldm(3). It is helpful to make a first-pass
   check for the best value for c/a, using a sparse $k$-point mesh.
3. Calculate the formation energy of CuAu:
   $$\Delta H_f (\mbox{CuAu}) = E_{tot}(\mbox{CuAu}) − E_b(\mbox{Cu}) − E_b(\mbox{Au})$$
   where Eb(Cu) and Eb(Au) are the total energies for Cu and Au in their FCC
   bulk phase. The total energy CuAu, Etot(CuAu), is chosen for fully relaxed
   equilibrium lattice parameters and internal coordinates.
