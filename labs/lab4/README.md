LaTeX input:        mmd-mavrldoc-header
Title:              NANO266 Lab 4 - Al surfaces
Author:             Shyue Ping Ong
Affiliation:        University of California, San Diego
Address:            9500 Gilman Drive, Mail Code 0448, La Jolla, CA 92093-0448
Web:                http://www.materialsvirtuallab.org
Base Header Level:  2
LaTeX Mode:         mavrldoc
LaTeX input:        mmd-mavrldoc-begin-doc
LaTeX footer:       mmd-mavrldoc-footer
xhtml header:       <script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>


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
need to perform a convergence with respect to both slab and vacuum size. Use an
energy cutoff of 30 Ry with a $k$-point grid of 16 $\times$ 16 $\times$ 1 for the
slab calculations.

1. Start by first finding the equilibrium structure of fcc Al. You have already
   done this in lab 3, but we are going to do this again using the SCF method,
   i.e., by plotting the equation of state of energy versus the lattice
   parameter. Converge your lattice parameter to within 0.001 angstroms. For
   reference, the experimental lattice parameter is 4.05 angstroms. A template
   file `Al.100.bulk.pw.in.template` has already been provided. Please use the
   `scf.py` script to perform these calculations with a default $k$-point grid 
   of 16 $\times$ 16 $\times$ 16. As usual, please scan with fairly coarse grid 
   (e.g., 0.01 increments) before performing scans with a more dense grid near 
   the minimum energy. Record down the lattice parameter in Bohr and energy in Ry.
2. Using the lattice parameter you obtained in part 1, perform a calculation of
   the Al (100) surface. A sample `Al.100.surf.pw.in.template` file has been
   provided to you, as well as a `fcc_surf_gen.py` (type `fcc_surf_gen.py -h`
   for help). Start by typing:

     `python fcc_surf_gen.py --a 7.65 --miller "100" --k 16 --nslab 3 --nvac 3`

   The output should be something like the following:

```
&CONTROL
  calculation = 'relax' ,
  outdir = './tmp' ,
  prefix = 'Al_100_3_3',
  pseudo_dir = './' ,
  tprnfor = .True.,
  tstress = .True.,
/
&SYSTEM
  ibrav = 6,
  celldm(1) = 7.65,
  celldm(3) = 6,
  nat = 12,
  ntyp = 1,
  ecutwfc = 30,
  ecutrho = 150,
  occupations = 'smearing',
  smearing = 'cold',
  degauss = 0.025,
/
&ELECTRONS
  diagonalization = 'david',
  conv_thr = 1.D-6,
  mixing_beta = 0.3,
  mixing_mode = 'local-TF'
/
&IONS
  ion_dynamics = 'bfgs',
/
ATOMIC_SPECIES
  Al   26.98  Al.pbe-n-van.UPF
ATOMIC_POSITIONS crystal
  Al 0.0 0.0 0.0
  Al 0.5 0.5 0.0
  Al 0.5 0.0 0.0833333333333
  Al 0.0 0.5 0.0833333333333
  Al 0.0 0.0 0.166666666667
  Al 0.5 0.5 0.166666666667
  Al 0.5 0.0 0.25
  Al 0.0 0.5 0.25
  Al 0.0 0.0 0.333333333333
  Al 0.5 0.5 0.333333333333
  Al 0.5 0.0 0.416666666667
  Al 0.0 0.5 0.416666666667
K_POINTS automatic
  16 16 1   0 0 0
```

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
     vacuum size**!

   You can write the output to a file by giving it the `--outfile` option:

     python fcc_surf_gen.py --a 7.65 --miller "100" --k 16 --nslab 3 --nvac 3 --outfile Al100_3_3.pw.in

   To do this question, vary nslab and nvac and look at how the energies
   change with nslab and nvac. Start by keeping nslab = 2 and vary nvac
   between 1 and 4. Get a value of nvac that gives a reasonable convergence of
   surface energies (say 0.01 Jm $^{-2}$). Note that the surface energy is
   given by:

   \\[\gamma = \frac{1}{2A} (E_{slab} - N E_{bulk}) \\]

   where $E_{slab}$ is the energy of the slab, $E_{bulk}$ is the energy per
   atom of bulk Al, and N is the number of atoms in the slab.

   Using the converged value of nvac, vary your nslab between 1 and 6. Again,
   determine the value of nslab that converges the surface energies to
   0.01 Jm $^{-2}$. Do not exceed `nslab = 6` for this exercise.

   Report your final surface energy in Jm $^{-2}$. Also discuss how the atoms
   at the surface has relaxed and comment on why.

# Q2 (30 points): The (111) surface of Al

We will now explore the (111) surface of Al. For this, we need to first get
our slab structure. Unlike the (100) surface that is simply along the cubic
crystallographic axes, getting the (111) surface involves some work.

The first thing to note is that the fcc structure is in fact a stacking of
hexagonally close-packed atoms along the [111] direction.

We will now show you how you can use VESTA (http://jp-minerals.org/vesta/en/)
to generate any surface structure. First download and install VESTA for your
platform. Here is the step by step guide to creating the Al (111) surface.

* Step 1: Open the `Al.cif` in VESTA. This is the standard `fcc` conventional
  unit cell of Al.
* Step 2: Let us now first insert the (111) lattice plane into the crystal for
  easier visualization. Go to `Edit->Lattice Planes`. Click new, then type in
  (111) for your Miller indices and set your `d` to 1. Your dialog box should
  look something like the figure below:

   ![latticeplane][]

* Step 3: Click `Ok`. You will see that a lattice plane has been drawn in your
  crystal. Go to `Edit->Edit Data->Unit Cell`. Click `Remove symmetry` and
  then hit `Apply`. We need to break symmetry before we can create the slab.
  Then go to the `Structure Parameters` tab and assign different labels for
  each of your atoms. This makes it easier to identify the atoms later.
  Hit `Apply` again.
* Step 4: The next step is to generate a larger unit cell as we are going to
  ``cut'' the crystal in a different orientation that goes beyond the limits
  of the unit cell. Go back to the `Unit Cell` tab. Click on `Options` and
  then enter 2 for all the diagonal elements of the rotation matrix. That
  generates a $$2 \times 2 \times 2$$ supercell of your crystal. Click `Ok`
  for all the warnings. Click `Ok` until you close all dialog boxes and see a
  larger version of the Al cell.
* Step 5: Click on `Objects` and check the `L` (label) for the topmost Al. All
  the Al atoms should now be labeled.

   ![labeledsupercell][]

* Step 6: We are going to now redefine our lattice vectors so that our
  **a** and **b** lattice vectors are within the (111) plane
  and our **c** lattice vector is non-parallel (ideally normal to the
  plane). To do this, we can observe that we can define atom `Al2` in the
  figure above to be the origin, and set our new $\mathbf{a}'$ to be the
  vector connecting `Al2` and `Al1`, and $\mathbf{b}'$ to be the vector
  connecting `Al2` and `Al4`. Using the VESTA atom picker, we can determine
  that the crystal coordinates of the atoms to be:

   \\[
   \begin{aligned}
   \mathbf{r_{Al4}} &= (0.25, 0.25, 0)\\
   \mathbf{r_{Al2}} &= (0, 0.25, 0.25)\\
   \mathbf{r_{Al1}} &= (0, 0, 0.5)
   \end{aligned}
   \\]

* Step 7: Go to `Edit->Unit Cell` again, and click `Options`. We then need to
  enter our rotation matrix and origin shift to the values we have determined
  in the previous step. Note the way the lattice vectors are transformed based
  on the documentation (the vectors are in a row format and the matrix is defined in columns). For the last column, we set it  (0.5, 0.5, 0.5), since
  we have already doubled our cell in all directions (see figure below). Click
  `Ok`. Then go to the `Structure Parameters` tab. You will find that there
  are a lot of duplicate atoms due to the mapping of supercell atoms onto each
  other. Just click `Remove duplicate atoms` and you should be left with three
  unique atoms.

   ![transformation][]

* Step 8: Click `Ok` until you end up in the crystal. You will find that you
  now have a hexagonal cell and the (111) lattice plane is now parallel to your
  $\mathbf{a}$ and $\mathbf{b}$ lattice vectors. Export the atom position to a
  file using `File->Export Data`. Choose the VASP POSCAR format, even though
  we will not be using VASP for our calculations.

Using the coordinates (e.g., viewing the POSCAR file in a text editor), you
will need to modify the `fcc_surf_gen.py` to work for the (111) lattice plane.
Look at `Al.111.bulk.pw.in.template` and `Al.111.surf.pw.in.template`. Note
that we are now using a hexagonal Bravais lattice setting.

Repeat your calculations of surface energy in Q1 for the (111) lattice plane.
You do not need to search for the optimal lattice parameters again. You need to
work out the appropriate hexagonal lattice parameters based on your optimal
cubic lattice parameters. Use a $16 \times 16 \times 1$ $k$-point grid for your
slab calculations. Also, you may perform your calculations using 2 vacuum
layers and 3 slab layers. There is no need to redo the convergence study.

Report your final (111) surface energy for Al in Jm $^{-2}$. Discuss how the
atom at the surface has relaxed and comment on why the relaxtion occurs the
way it does.

Comment on the difference in surface energy between the (100) and (111)
surface. Which one is lower in energy? Can you provide a likely physical reason
for the relative stabilities of the surfaces?

# Q3 (50 points): Binding energy of H atom on Al

In the final question, we will investigate the adsorption of a hydrogen atom
on the Al (111) surface. As this is a final question of the course, you should
have enough experience with calculations by now. We will keep only provide a
few guidelines, and you will be responsible for creating the necessary input
files, either manually or using VESTA, and performing the calculations.

The binding energy of an H atom on a surface is given by:

\\[E_b = E(\mbox{slab + H}) - E(\mbox{slab}) - \frac{1}{2} E(\mbox{H}_2) \\]

To calculate this, you need to perform calculations of a slab with the H atom,
as well as the energy of H<sub>2</sub> gas. To do the latter in periodic
boundary conditions, you need to do a ``particle in a box'' calculation, i.e.,
you create a big enough simulation box (typically, sizes ~10 angstroms should
be sufficient, but you need to do your own tests), and put your H<sub>2</sub>
molecule in a non-symmetry position, and perform a calculation that allows
atomic positions but not cell volumes to relax.

For the slab + H calculation, you will need to investigate the different
absorption sites on the Al surface. For the (111) hexagonal surface,
there are three high symmetry sites - the ``on top'' site above an Al
atom, the ``bridge'' site between two nearest neighbor Al atoms, and the
``hollow'' site between three nearest neighbor Al atoms. There are 2 such hollow
sites to be considered. The stacking in the <111> direction is given by the
A-B-C-A-B-C sequence. Assuming the surface ends with a 'C' plane, the hollow-site
will either correspond to a 'A'-plane hollow site or 'B' pane hollow site.
You will need to create simulation cells to model each of them. Note that you will need to
extend your unit cell in the **a** and **b** directions as well to ensure that
H atoms in neighboring periodic images are not too close to each other. Use a
reasonable sized cell, and scale your $k$-point grid accordingly. Because we
are comparing relative energies between different sites rather than absolute
binding energies, you do not need to use very large cells. The calculations
should be doable using a single processor. If your calculations are taking
too long, rethink your supercell and $k$-point grid.

Report all your binding energies in eV. Discuss the relative binding energies
of H on the different sites, and whether the results are in line with your
chemical intuition. Hint: Some H adsorption sites may be unstable. You need to 
check the final position of H atom in each case. Can you estimate the diffusion 
coefficient for H on the Al(111) surface?

[latticeplane]: InsertLatticePlane.png "Lattice Plane Dialog Box in VESTA"
[labeledsupercell]: LabeledAl.png "Labeled Al supercell"
[transformation]: Transform.png "Transformation matrix"
