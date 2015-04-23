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

# Q1 (12 points): Convergence of *absolute* energies with respect to energy cutoff

Start by looking at the `Si.pw.in.template`, which is a template for the input
file for PWSCF. You should get yourself familiar with the format, and what each
of the sections and parameters mean. Note that some parameters have
placeholders {xxx}, which will be replaced by our run script. A PWSCF_IO
tutorial is provided in the tutorials folder of this repo to help you
understand the parameters. You may also wish to consult the QuantumEspresso
online documentation. A quick explanation of the key parameters are given as
follows:

```
&control                   # This is the control section
  calculation = 'scf' ,    # Specifies that we are doing a static SCF calculation.
  outdir = './tmp' ,
  pseudo_dir = './' ,      # Location of pseudopotential files.
/
&system                    # Specifies the structure
  ibrav = 2,               # For PWSCF, ibrav = 2 denotes an FCC cell.
  celldm(1) = {alat},      # This specifies the lattice parameter of the fcc cell.
  nat = 2,                 # We have two Si atoms per unit cell.
  ntyp = 1,                # There is only one type of atom (Si)
  ecutwfc = {ecut} ,       # This stipulates the energy cutoff.
/
&ELECTRONS                 # These three sections are not used in this particular calculation.
/
&IONS
/
&CELL
/
ATOMIC_SPECIES             # Specify the pseudopotential for each species.
  Si   28.055  {pseudopotential}
ATOMIC_POSITIONS crystal   # Specifies the atomic positions in frac. coords
  Si      0.00    0.00    0.00
  Si      0.25    0.25    0.25
K_POINTS automatic         # Specifies the k-point grid to be used
  {k} {k} {k}   0 0 0
```

We have also written a Python script called `run_pw.py` to help you in this
simulation. Again, read through the script to understand what it does. It is
heavily commented to aid you in your understanding. Note that this is a
starting point. *You will need to understand enough to make changes in order to
finish this lab.* A second script called `analyze.py` is provided to help you
compile the results into a csv file, which can be opened with most spreadsheet
programs for analysis. To run the scripts, you simply need to type

```python <script>.py <other parameters if necessary>```

1. Using PWSCF, calculate the energy of silicon as a function of cutoff
   energy. A good increment is ~10 Ry, in the range of 10-100 Ry. When changing
   the cutoff, make sure to keep the other variables (lattice constant,
   *k*-points, etc.) fixed. Record and plot your final results. Specify when
   you reach the level of convergence of ~5 meV/atom (you will need to take
   care of the unit conversions). Note that PWSCF calculates energy per
   primitive cell.
2. Do you see a trend in your calculated energies with respect to cutoff?

# Q2 (12 points): Convergence of *absolute* energies with respect to *k*-points

1. Modify the script in Q1 to calculate the energy as a function of *k*-point
   grid size. For each grid, record the number of unique *k*-points. Note that
   this is not the same as the *k* specified in the script and input file. The
   `analyze.py` script reports the number of unique *k*-points extracted from
   the output files. Again, make sure to keep your other variables fixed.
   Record and plot your final results.
   Specify when you reach the level of convergence of ~5 meV/atom.
2. Do you see a trend in your calculated energies with respect to grid size?
   If you see a trend, is this what you expect and why? If not, why?
3. Plot your calculation time against the number of *k*-points. Is there a
   relationship, and if so, what is that relationship? (You will need to figure
   out how to extract the calculation time from the output files.)

# Q3 (12 points): Convergence of forces with respect to cutoff energies

Let us now investigate the convergence of forces on atoms with respect to
cutoff. Displace a Si atom +0.05 in the z direction (fractional coordinates).
Keeping other parameters fixed, calculate the forces on Si as a function of
cutoff. A good force value would be converged to within ~10 meV/Angstrom
(note that PWSCF gives forces in Ryd/bohr). Use a *k*-point grid of 4x4x4.
Plot and record your results, including all relevant parameters.

# Q4 (12 points): Convergence of forces with respect to *k*-points

Repeat Q3, but this time, investigate the converge as a function of *k*-point
grid size. Keep all other parameters fixed. Record your relevant conditions
(lattice parameter, cutoffs, etc.)

# Q5 (12 points): Convergence of energy differences

In practice, only energy differences have physical meaning. Let us now
investigate the convergence of energy differences with respect to energy
cutoff and *k*-points. For this exercise, compute the energy difference
between silicon structures at two lattice parameters. You can calculate the
energies of silicon the experimental lattice parameter (10.26 Bohr), and at
10.30 Bohr, and take the difference between the two. Do a convergence study for
both the energy cutoff and the *k*-point grid. Record all relevant parameters
such as the lattice constant, *k* -points, and so on. A good energy difference
is converged to ~5 meV/atom.

# Q6 (20 points): Selecting the right parameters

Look at the results from the preceding questions. Discuss the changes in the
requirements in terms of cutoff, *k*-point grid, etc. when comparing absolute
energies, forces and energy differences. Explain as far as possible any trends
you see.

# Q7 (10 points): Finding the equilibrium structure

Using an appropriate set of parameters (energy cutoff, *k*-point, etc.),
determine the predicted equilibrium lattice constant for silicon by calculating
the energy of the silicon structure at several lattice parameters. Note that
you may need to use a finer grid near the equilibrium point to get a more
accurate answer.

Also, it should be pointed that PWSCF allows you to specify
`calculation = 'vc-relax'` to automatically perform a full cell relaxation. But
it is important that you understand how to do it using static SCF energy
calculations at different lattice parameters as a demonstration of the
variational principle. You will be using this in your next lab.

# Q8 (10 points): Choice of functional

The calculations you have been doing thus far is based on the PBE GGA
functional. Redo Q7, but now use the `Si.pz-n-kjpaw_psl.0.1.UPF` (LDA)
pseudopotential instead. Comment on any differences in the predicted
equilibrium lattice constant.
