from __future__ import division
import numpy as np
import argparse

fcc_coords = np.array(
    [[0.0, 0.0, 0.0],
     [0.5, 0.5, 0.0],
     [0.5, 0.0, 0.5],
     [0.0, 0.5, 0.5]]
)

def generate_slab(args):
    a = args.a
    nslab = args.nslab
    nvac = args.nvac
    nlayers = nslab + nvac

    pos = fcc_coords.copy()

    pos[:, 2] = pos[:, 2] * 1.0 / nlayers

    coords = []
    for i in range(nslab):
        coords.extend(pos + [0, 0, i / nlayers])

    atompos = []
    for i, c in enumerate(coords):
        if i not in range(4, len(coords) - 4):
            atompos.append("  Al %s %s %s" % tuple(c))
        else:
            atompos.append("  Al %s %s %s 0 0 0" % tuple(c))
    atompos = "\n".join(atompos)
    with open("Al100.pw.in.template") as f:
        contents = f.read()
    contents = contents.format(alat=a, calat=nlayers, nslab=nslab, nvac=nvac,
        atompos=atompos, nat=len(coords))
    if args.outfile:
        with open(args.outfile, "wt") as f:
            f.write(contents)
    else:
        print(contents)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='''Simple tool for generating fcc surface structures for PWSCF calculations.''')
    parser.add_argument(
        '-a', '--a', dest='a', type=float, required=True,
        help='a lattice parameter for fcc lattice in Bohr.')
    parser.add_argument(
        '-s', '--nslab', dest='nslab', type=int, required=True,
        help='Number of layers for slab. Must be integer multiples of conventional fcc lattice.')
    parser.add_argument(
        '-v', '--nvac', dest='nvac', type=int, required=True,
        help='Number of layers for vacuum. Must be integer multiples of conventional fcc lattice.')
    parser.add_argument(
        '-o', '--outfile', dest='outfile', type=str,
        help='File to write PWSCF input file to.')
    args = parser.parse_args()
    generate_slab(args)
