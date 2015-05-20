import sys
import re

cell_params = []
with open(sys.argv[1]) as f:
    lines = f.readlines()

Bohr2Ang = 0.52917721092

read = False
atompos = []
for l in lines:
    if re.search("bravais-lattice index\s+=\s+(\d+)", l):
        ibrav = int(l.split("=")[-1])
    if re.search("celldm\(1\)=\s+([\d\.]+)\s", l):
        m = re.search("celldm\(1\)=\s+([\d\.]+)\s", l)
        a = float(m.group(1)) * Bohr2Ang
        m = re.search("celldm\(3\)=\s+([\d\.]+)\s", l)
        c = float(m.group(1)) or 1
        c = float(m.group(1)) * a
    if read and l.strip() != "" and "End" not in l:
        atompos.append(l)
    elif "ATOMIC_POSITIONS (crystal)" in l:
        atompos = []
        read = True
    else:
        read = False

if len(atompos) == 0:
    print("No relaxed atomic positions found! ")
    print("This script can only be used on a relaxation run, not SCF!")
    sys.exit(-1)

cif = """
data_Al
_symmetry_space_group_name_H-M   'P 1'
_cell_length_a   {a}
_cell_length_b   {a}
_cell_length_c   {c}
_cell_angle_alpha   90.
_cell_angle_beta   90.
_cell_angle_gamma   {gamma}
_symmetry_Int_Tables_number   1
_chemical_formula_structural   Al
_chemical_formula_sum   Al{nat}
_cell_volume   {vol}
_cell_formula_units_Z   {nat}
loop_
_symmetry_equiv_pos_site_id
_symmetry_equiv_pos_as_xyz
1  'x, y, z'
loop_
_atom_site_type_symbol
_atom_site_label
_atom_site_symmetry_multiplicity
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_occupancy
"""

cif = cif.format(a=a, c=c, nat=len(atompos), vol=a*a*c, gamma=120 if ibrav == 4 else 90)

for i, s in enumerate(atompos):
    toks = s.split()
    sp = toks[0]
    row = "{sp} {sp}{i} 1 {x} {y} {z} 1".format(sp=sp, i=i+1,
            x=float(toks[1]), y=float(toks[2]), z=float(toks[3]))
    cif += row + "\n"

with open(sys.argv[2], "w") as f:
    f.write(cif)
