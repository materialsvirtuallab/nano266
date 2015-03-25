# Lab 1

## Introduction

We will begin our lab sessions with a gentle introduction into quantum
mechanical modeling of molecules. For this purpose, we will be using 
computational chemistry techniques to study reaction energies, ionization
energies and electron affinities, vibrational frequencies, etc. We will
be using NWChem, an open source quantum chemistry code. Note that all
calculations in this lab are fairly simple and on very small molecules. 
So you can be run them on a modern desktop or laptop in serial mode, i.e., you
do not actually need access to a supercomputing cluster to perform these
calculations. 

For this lab, we will be studying one of the most important reactions in the
world - the formation of ammonia from nitrogen and hydrogen. Through the
Haber-Bosch process, this is the main industrial reaction for the production of
ammonia, which is then used in the production of fertilizers, etc. It is
estimated that one-third of the Earth's population is sustained by fertilizer
generated from ammonia produced by the Haber process.

In this lab, almost all analyses will be done using Unix-based command line
tools as it is important for you to learn how to find data efficiently using
these tools. Subsequent labs will provide you with the opportunity to use
Python to automate and analyze data more effectively. You are of course welcome
to write your own scripts if you have the know-how.

## Initial setup

It is assumed that you have already cloned this repo, and done a git pull so
that you are up to date with the repo. Also, read through the README.md file in
the main labs folder and make sure that you have NWChem setup properly. Try
typing `nwchem` in your terminal to make sure that everything is working.

Once you are done with the above, make sure you are in the lab2 folder by doing:

    cd <path/to/repo>/labs/lab1

## Q1 (10 points): Geometry optimization of H2

We will start with one of the simplest molecules, diatomic hydrogen. In the
directory, we have provided a sample `H2.nw` input file. First, open up the
input file and understand its structure. Here's a replica of the input files
with additional comments added.

	memory total 1000 mb 		# This specifies the memory for the job.

	geometry units angstroms    # This section provides a summary of the input
	 H 0 0 0                    # geometry of the molecule. You usually get this
	 H 0 0 0.7414               # from an experimental source or some chemistry
	end                         # rules

	title "H2 dft optimize"
	charge 0
	basis
	 H library "6-31++G*"
	end
	dft
	 mult 1
	 xc b3lyp
	end
	task dft optimize

	title "H2 dft freq"
	charge 0
	basis
	 H library "6-31++G*"
	end
	dft
	 mult 1
	 xc b3lyp
	end
	task dft freq

	title "H2 dft energy"
	charge 0
	basis
	 H library "6-311++G**"
	end
	dft
	 mult 1
	 xc b3lyp
	end
	task dft energy

