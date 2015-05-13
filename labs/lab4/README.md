LaTeX input:        mmd-mavrldoc-header
Title:              NANO266 Lab 4 - Al surfaces
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

# Q1 (20 points): The (100) surface of Al

We will first start by calculating the energy of the (100) surface in Al. You
need to perform a convergence with respect to both slab and vaAlum size. Use an
energy cutoff of 50 Ry with a $k$-point grid of 8 $\times$ 8 $\times$ 1.

1. Start by first finding the equilibrium structure of fcc Al. You have already
   done this in lab 3, but we are going to do this again using the SCF method,
   i.e., by plotting the equation of state of energy versus the lattice
   parameter. Converge your lattice parameter to within 0.001 angstroms. For
   reference, the experimental lattice parameter is 4.05 angstroms. A template
   file `Al.fcc.pw.in.template` has already been provided. Please use the
   `scf.py` script to perform these calculations. As usual, please scan with
   a fairly coarse grid (e.g., 0.01 increments) before performing scans with a
   more dense grid near the minimum energy. Record down the lattice parameter
   in Bohr and energy in Ry.
2. Using the lattice parameter you obtained in part 1, perform a calculation of
   the Al (100) surface. A sample `Al100.pw.in.template` file has been
   provided to you, as well as a `fcc_surf_gen.py`. Start by typing:

     `python fcc_surf_gen.py --a 7.65 --nslab 3 --nvac 3`

   The output should be something like the following:

     &CONTROL
      calculation = 'relax' ,
      outdir = './tmp' ,
      prefix = 'Al_100',
      pseudo_dir = './' ,
      tprnfor = .True.,
      tstress = .True.,
     /
     &SYSTEM
      ibrav = 6,
      celldm(1) = 6.92,
      celldm(3) = 6,
      nat = 12,
      ntyp = 1,
      ecutwfc = 50,
      ecutrho = 250,
      occupations = 'smearing',
      smearing = 'cold',
      degauss = 0.025,
     /
     &ELECTRONS
      diagonalization = 'david',
      conv_thr = 1.D-6,
      mixing_beta = 0.7,
     /
     &IONS
      ion_dynamics = 'bfgs',
     /
    ATOMIC_SPECIES
      Al   26.98  Al.pbe-n-kjpaw_psl.0.1.UPF
    ATOMIC_POSITIONS crystal
      Al 0.0 0.0 0.0
      Al 0.5 0.5 0.0
      Al 0.5 0.0 0.0833333333333
      Al 0.0 0.5 0.0833333333333
      Al 0.0 0.0 0.166666666667 0 0 0
      Al 0.5 0.5 0.166666666667 0 0 0
      Al 0.5 0.0 0.25 0 0 0
      Al 0.0 0.5 0.25 0 0 0
      Al 0.0 0.0 0.333333333333
      Al 0.5 0.5 0.333333333333
      Al 0.5 0.0 0.416666666667
      Al 0.0 0.5 0.416666666667
    K_POINTS automatic
      8 8 1   0 0 0

   There are several important things to note about this input file:

   * The `calculation` parameter has been set to `relax`. This allows the atoms
     to move, but fixes the cell shape.
   * The `ibrav` tag has been set to 6, which is a tetragonal cell. To perform
     a surface calculation, we are extending the cell in the $c$-direction and
     removing atoms. So we are breaking symmetry in that direction.
   * The  `celldm(3)` parameter is set to 6. This means that we have
     constructed a supercell where the $c$ lattice parameter is 6 $\times$
     that in the $a$ and $b$ directions.
   * In the ATOMIC_POSITIONS section, note the $c$ fractional coordinate of
     each atom. The conventional fcc cell has four atoms. Look at how each
     group of four atoms are related to each other by a translation in the $c$
     direction. It is absolutely critical that you understand that the $c$
     fractional coordinate depends on **both your slab size as well as your
     vacuum size**! Also, we have fixed all atoms except for the top and
     bottom two atomic layers (denoted by the `0 0 0` after the coordinates.

   You can write the output to a file by giving it the `--outfile` option:

     python fcc_surf_gen.py --a 7.65 --nslab 3 --nvac 3 --outfile Al100_3_3.pw.in

   To do this question, vary nslab and nvac and look at how the energies
   change with nslab and nvac. Start by keeping nslab = 2 and vary nvac
   between 1 and 4. Get a value of nvac that gives a reasonable convergence of
   surface energies (say 0.01 Jm $^{-2}$). Note that the surface energy is
   given by:

   \\[\gamma = \frac{1}{2A} (E_{slab} - N E_{bulk} ) \\]

   where $E_{slab}$ is the energy of the slab, $E_{bulk}$ is the energy per
   atom of bulk Al, and N is the number of atoms in the slab.

   Using the converged value of nvac, vary your nslab between 1 and 4. Again,
   determine the value of nslab that converges the surface energies to
   0.01 Jm $^{-2}$.

   Report your final surface energy in Jm $^{-2}$.

# Q2: The (111) surface of Al

# Q3: Adsorption of H on Al
