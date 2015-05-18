LaTeX input:        mmd-mavrldoc-header
Title:              NANO266 Lab 3 - Phase Stability from Quantum Mechanics
Base Header Level:  2
LaTeX Mode:         mavrldoc
LaTeX input:        mmd-mavrldoc-begin-doc
LaTeX footer:       mmd-mavrldoc-footer


# Introduction

In this lab, we will look at predicting phase equilibrium from quantum mechanics.
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

Comet uses the Simple Linux Utility for Resource Management (Slurm) job
scheduling system. All supercomputing clusters use a job scheduler of some
sort, e.g., PBS, Sun GridEngine, SLURM. They differ in some features, but work
on the same basic principle. You send jobs to a queue, and they are run
according to some priority system. For more information, you may read the
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

If you make a mistake and need to kill a job for whatever reason. use the
`scancel` command.

```bash
scancel <jobid>
```

# Q1 (20 points): The bcc-hcp transition in iron

In this problem, you will look at the bcc to hcp transition in iron. We will be
using the PBE GGA functional that we used in the earlier lab. Use an energy
cutoff of 40 Ry with a charge density cutoff of 400 Ry. You will need to
determine an appropriate $k$-point mesh for both the bcc and hcp structures.
The energy differences are very small; choose parameters to converge your
energies to within 1 meV.

1. Calculate the ground state energy of Fe in both the bcc and hcp structure.
   Two template files are provided for bcc and hcp.  A run_pw.py file is also
   provided that works for bcc, but you need to modify it as appropriate to
   work for hcp. Optimize the lattice parameters for both bcc and hcp Fe
   (i.e., $a$ for bcc and $a$ and $c$ for hcp). In the case of hcp, celldm(3),
   which is the c/a ratio, needs to be provided. Try the following values of
   c/a ratio: [1.72,1.73,1.74] and for each of these ratios, alter the $a_{o}$
   parameter to find the equilibrium sructure in hcp phase. Start with an $a_{o}$ value of 4.8 a.u.
2. Varying the volume of the cell, calculate the pressure at which the hcp structure becomes more
   favorable than the bcc one. Note that it is important when comparing
   energies that the $k$-point samplings for both systems are comparable and
   converged. Determine an appropriate $k$-point grid for both structures. Note
   that the $k$-point should be proportional to the reciprocal lattice vector
   length.
3. Calculate and compare the total energy for the BCC structure in the
   ferromagnetic, and anti-ferromagnetic states. (10 points)

Note that you will need to read the PWSCF manual to figure out how to set
various options to do this work. At this stage of the course, we will not
be providing all the templates and scripts and you need to work through the
manuals to figure out what to do. This is part and parcel of computational
modeling work.

# Q2 (40 points): Stability of the $\mbox{PbTiO}_3$ perovskite

$\mbox{PbTiO}_3$ is a perovskite oxide which is ferroelectric. The
ferroelectric response of $\mbox{PbTiO}_3$ is the result of a displacive
transition where a low temperature tetragonal phase is preferred over the cubic
phase.

For this question, it is important that you note several differences in the
`PbTiO3.pw.in.template` file.

* The `calculation` parameter is set to `relax`, which means we are allowing
  atoms to move.
* There are two additional sections: IONS section with `ion_dynamics = 'bfgs'`,
   and CELL section with `cell_dynamics = 'bfgs'` which chooses the quasi-Newton
   minimization method.
* At the end of the atomic positions for Pb and Ti, there are three additional
  0s. These indicate that the Pb and Ti are not allowed to move in any of the
  coordinates. Conversely, no such restriction is placed on the O atoms, which
  are allowed to relax accordingly.

Please answer the following questions.

1. Calculate and plot the energy of cubic $\mbox{PbTiO}_3$ as a function of
   lattice parameter. Use a 4 $\times$ 4 $\times$ 4 $k$-point mesh with a
   1, 1, 1 offset. Sample lattice parameters with a sufficiently fine grid to
   get a reliable value for the equilibrium lattice constant. To get an idea
   where to begin, note that the room-temperature experimental lattice constant
   is about 3.97 ${\buildrel _{\circ} \over {\mathrm{A}}}$.
2. Using the equilibrium lattice parameter from part (1), plot the energy as a
   function of displacement of the Ti atom along one of the cubic lattice
   directions, allowing the O atoms to fully relax for each displacement.
   Report the Ti displacement at which the total energy is at a minimum. What
   is the energy difference between this configuration and the minimum-energy
   configuration from part (1)? Note that the Ti displacement will be very
   small.
3. Now allow both the Ti atom and the O atoms to relax and find the minimum
   energy structure, using the minimum-energy Ti displacement from part (B) as
   your starting configuration. Report the final atomic positions and final
   energy.
4. Which phase is the most energetically stable for $\mbox{PbTiO}_3$ and how
   does that relate to the ferroelectric behavior of this material?

# Q3 (40 points): Formation Energy of the $\mbox{Cu}_{1-x}\mbox{Au}_x$ intermetallics

In this problem, we will investigate the formation energies of the
$\mbox{Cu}_{1-x}\mbox{Au}_x$ for $x$ = 0.25, 0.5 and 0.75. See Ozolins et al.
Cu-Au, Ag-Au, Cu-Ag and Ni-Au intermetallics: First-principles study of phase
diagrams and structures, Phys. Rev. B, 1997, 57, 19,
doi:10.1103/PhysRevB.57.6427.

1. Calculate the ground state energy for fcc Cu, Au and
   $\mbox{Cu}_{1-x}\mbox{Au}_x$.  Here, we will use PWSCF's *vc-relax* option
   to avoid having to manually do a equation of state analysis. Start with the
   end members and the CuAu ($x$ = 0.5) intermetallic and do a $k$-point
   convergence such that your formation energies are within
   5 meV / atom. Start with a relatively small grid, e.g., 4 $\times$ 4 $\times
   4. For CuAu, you should use the L10 phase, which is a body-centered
   tetragonal (bct) with two atoms in the unit cell, and lattice
   parameters are $a = b \ne c$. A sample file is provided. Please note that starting
   configuration is a simple cubic structure with face-centered and corner lattice points
   occupied such that there are alternate layers of Cu and Au. You may
   search the internet for the experimental lattice parameters and use those to
   set your initial guesses for $a$ = celldm(1) and $c/a$ = celldm(3) (in case you start with a
   ibrav = 7, tetragonal structure). You should use good guesses to minimize the computational time.
2. Calculate the formation energy of $\mbox{Cu}_{1-x}\mbox{Au}_x$ :
   $$\Delta H_f (\mbox{Cu}_{1-x}\mbox{Au}_x) = E(\mbox{Cu}_{1-x}\mbox{Au}_x) − (1 - x) E(\mbox{Cu}) − x E(\mbox{Au})$$
   where E(Cu) and E(Au) are the total energies for Cu and Au in their fcc
   bulk phase. Note that you must normalize the energies accordingly. We want the formation energies per atom, i.e., 0.5 $\times$ the formation energy per CuAu.
3. Repeat the calculations for $\mbox{Cu}_3\mbox{Au}$ and $\mbox{CuAu}_3$. For
   both these structures, start with a fcc Cu or Au structure, and replace all
   corner atoms with atoms of the other type. For example, to create
   the $\mbox{Cu}_3\mbox{Au}$, you can start from the fcc Cu unit cell, and set
   the Cu atoms to be on the faces, which gives one Au (1 / 8 $\times$ 8) and
   three Cu (1 / 2 $\times$ 6). Note that in order to create this structure,
   you need to decrease the symmetry from the fcc to simple cubic, and then add
   atoms accordingly. Review your crystallography and PWSCF's input file format
   so that you understand how to do this.
4. Plot the formation energy of the $\mbox{Cu}_{1-x}\mbox{Au}_x$ phases you have
   calculated against $x$. Discuss which of the ordered intermetallic
   structures are stable at 0K.
