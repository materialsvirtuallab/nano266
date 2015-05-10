LaTeX input:        mmd-mavrldoc-header
Title:              NANO266 Lab 4 - Adsorption on Cu surfaces
Base Header Level:  2
LaTeX Mode:         mavrldoc
LaTeX input:        mmd-mavrldoc-begin-doc
LaTeX footer:       mmd-mavrldoc-footer


# Introduction

In this lab, we will look surface calculations with PWSCF.

# Initial setup

By this stage, you should already have everything set up. Make sure you are in
the lab4 folder by doing:

```bash
cd <path/to/repo>/labs/lab4
```

# Running calculations

You will still be running the calculations using the queues on Comet. However,
it is important to note that surface calculations can take much longer than
bulk calculations. It is therefore imperative that you perform these
calculations prudently. It is very easy to burn through all the allocated
CPU time if you are not careful.

# Q1 (20 points): The (100) surface of Cu

We will first start by calculating the energy of the (100) surface in Cu. You
need to perform a convergence with respect to both slab and vacuum size. Use an
energy cutoff of 50 Ry with a $k$-point grid of 10 $\times$ 10 $\times$ 1. 

1. Start by first finding the equilibrium structure of fcc Cu. You have already
   done this in lab 3, but we are going to do this again using the SCF method,
   i.e., by plotting the equation of state of energy versus the lattice
   parameter. Converge your lattice parameter to within 0.001 angstroms. For
   reference, the experimental lattice parameter is 3.61 angstroms. A template
   file `Cu.fcc.pw.in.template` has already been provided. Please use the 
   `run_scf.py` script to perform these calculations. As usual, please scan with
   a fairly coarse grid (e.g., 0.01 increments) before performing scans with a
   more dense grid near the minimum energy.
2. Using the lattice parameter you obtained in part 1, perform a calculation of
   the Cu (100) surface. A sample `Cu100.pw.in` file has been provided to you.
   There are several important things to note about this input file:
   * The `calculation` parameter has been set to `relax`. This allows the atoms
     to move, but not the cell shape.
   * The `ibrav` tag has been set to 6, which is a tetragonal cell. To perform
     a surface calculation, we are extending the cell in the $c$-direction and
     removing atoms. So we are breaking symmetry in that direction.
   * The  `celldm(3)` parameter is set to 4. This means that we have constructed
     a supercell where the $c$ lattice parameter is 4 $\times$ that in the $a$ and
     $b$ directions. Finally, we have `nat` = 8 and in the `ATOMIC_POSITIONS`
     section, we have

      ```   
      Cu      0.0    0.0   0.0
      Cu      0.5    0.5   0.0
      Cu      0.0    0.5   0.125
      Cu      0.5    0.0   0.125
      Cu      0.0    0.0   0.25
      Cu      0.5    0.5   0.25
      Cu      0.0    0.5   0.375
      Cu      0.5    0.0   0.375
      ```

     Note in particular the $c$ fractional coordinate of each atom and how the
     bottom four atoms are related to the top four. In effect, we have two layers
     of the conventional fcc cell of Cu occupying the bottom half of the supercell.
     It is absolutely critical that you understand that the $c$ fractional
     coordinate depends on **both your slab size as well as your vacuum size**!
     You will need to modify the cell accordingly to perform your convergence
     studies.

# Q2: The (111) surface of Cu

# Q3: Adsorption of H on Cu
