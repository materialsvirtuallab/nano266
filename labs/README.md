LaTeX input:        mmd-mavrldoc-header
Title:              NANO266 General Lab Instructions
Author:             Shyue Ping Ong
Affiliation:        University of California, San Diego
Address:            9500 Gilman Drive, Mail Code 0448, La Jolla, CA 92093-0448
Web:                http://www.materialsvirtuallab.org
Base Header Level:  2
LaTeX Mode:         mavrldoc
LaTeX input:        mmd-mavrldoc-begin-doc
LaTeX footer:       mmd-mavrldoc-footer

# Introduction

Welcome to the lab sessions for NANO266. Before you begin, you should read this
carefully and follow all instructions to make sure that your computer /
computing resource is set up properly. Your instructors are on hand to help you
if you run into any problems.

# First Principles Modeling Codes

In the labs, we will be using two open-source first principles modeling codes:

1. NWchem (http://www.nwchem-sw.org) is a computational chemistry code that
   aims to be scalable both in their ability to treat large scientific
   computational chemistry problems efficiently.
2. QuantumEspresso (http://www.quantum-espresso.org/) is an integrated suite of
   computer codes for electronic-structure calculations and materials modeling
   at the nanoscale. It is based on density-functional theory, plane waves, and
   pseudopotentials.

Before you start any of the labs, make sure that you have the software
installed and in your path. You have three options:

## Option 1: Use XSEDE

![XSEDE user portal](XSEDEUserPortal.png)

We have secured an XSEDE allocation for this course. Please go the the XSEDE
portal (https://portal.xsede.org) and create an account as shown above.
After you have done so, email your username to one of the TAs to be added
to the allocation for this course. 
If you are on a MAC machine, you can open the Terminal app and then login to the allocations
with 

```bash
ssh <your_username>@login.expanse.sdsc.edu
```

If you are on a Windows machine, you need to download a SSH client like
[PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).
Once you are logged in, immediately run

```bash
module load gcc/10.2.0 python
```

to make sure that Python are loaded for you. You can also add this line to
your `.bash_profile` so that it will always be loaded for you when you login.

## Option 2: Set up your own Mac

If you have your own Mac, you can use the executables already included in
this repo (see cloning the repo section). Run the following command to add
the bin directory to your path as follows (assuming you are on bash):

```bash
export PATH=$PATH:<path/to/repo>/bin/Mac
# The following is to set the NWChem basis sets used in lab1.
# Be careful that the ending slash is needed!
export NWCHEM_BASIS_LIBRARY=<path/to/repo>/resources/nwchem_basis/
```

## Option 3: Compile your own

You can download the source code for QuantumEspresso or NWChem and install
it yourself. *Attempt this only if you have a fairly good familiarity with
compiling things on Unix-based OSes, or are willing to spend the time to
figure it out!* If you foresee you will be working on such calculations
extensively in future, it is generally useful for you to learn how to do
this. Start with the QuantumEspresso code as it is more straightforward to
compile.

In general, it is not recommended that you run on a native Windows OS for these
labs. Most first principles codes are designed to run primarily on
supercomputing clusters that have Unix-based OSes. If you have a Windows
machine, you should try options 1 or 3 above.

# Cloning the repo

First, go to [Github](https://github.com). Create an account if you do not already
have one.

Next, create a ssh key if you do not have one on XSEDE with the following command:
```
ssh-keygen
``` 

You may press Enter to choose the defaults for all the prompts.

Then, show your *public* SSH key:
```
cat ~/.ssh/id_rsa.pub
```
Copy this key. 

In your Github user profile, under "SSH and GPG keys", add the key you just copied.

On wherever you are performing the calculations for the lab, you should clone
this repo by doing:

```
git clone git@github.com:materialsvirtuallab/nano266.git
```

Check that you have the repo cloned successfully by doing a `ls`. If you are
using XSEDE, make sure that you do the git clone in your home folder, i.e.,
the folder that you are in when you first log into XSEDE. This makes following
the rest of the instructions much easier.

This assumes you already have git installed, which comes by default in XSEDE
and Mac and can easily be installed in Unix-based OSes. To update your repo to
the latest version at any time, you can do:

```
cd ~/nano266
git pull
```

from within the repo.

# Using a Unix-based terminal

If you have never used a Unix-based terminal, there is a bit of a slight
learning curve. But in general, you will be working with only the following
commands:

```bash
cd <dirname>       # change directory to <dirname>
cp <file1> <file2> # copy <file1> to <file2>
mv <file1> <file2> # move <file1> to <file2>
rm <file>          # remove <file>
pwd                # show path to the current directory
mkdir <dirname>    # make a new directory <dirname>
ls                 # list files/directories in the current directory
```

A more comprehensive cheat sheet for Unix is given [here](https://github.com/materialsvirtuallab/nano266/blob/master/labs/Unix%20Cheat%20Sheet.md).

You will also be doing some basic text editing in the terminal. For beginners,
the `nano` command line editor has the smallest learning curve. Other options
are `vi` and `emacs`. 

Finally, you will need to get your results over to your local computer to do
analysis. The easiest way to do this is with:

```bash
scp <username>@login.expanse.sdsc.edu:~/nano266/<location/of/file> .
```

in your local Mac or Linux terminal. If you are on Windows, the equivalent is
[pscp](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).

# Programming in Python

A lot of the labs use Python as a scripting language for automating
calculations and analysis. You should ensure that you have Python 2.7.x
installed with numpy. If you have a Mac, this should be already the case. If
you use the virtual machine, it is also already set up.

If you don't know Python, get a quick primer from the official [Python
documentation](https://docs.python.org/2.7/). You do not really need to know
much more than the basics for the purposes of the labs. Learning how to use a
scripting language like Python can save you loads of time in automating
calculations.
