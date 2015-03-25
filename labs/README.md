# Introduction

Welcome to the lab sessions for NANO266. Before you begin, you should read this
carefully and follow all instructions to make sure that your computer / 
computing resource is set up properly. Your instructors are on hand to help you
if you run into any problems.

# Cloning the repo

You should first clone this repo by doing:

```
git clone https://github.com/materialsvirtuallab/nano266.git
```

This assumes you already have git installed, which comes by default in Mac
and can easily be installed in Unix. To update your repo to the latest version
at any time, you can do:

```
git pull
```

from within the repo.

# Modeling codes used

In the labs, we will be using two open-source first principles modeling codes:

1. NWchem (http://www.nwchem-sw.org) is a computational chemistry code that
   aims to be scalable both in their ability to treat large scientific
   computational chemistry problems efficiently.
2. QuantumEspresso (http://www.quantum-espresso.org/) is an integrated suite of
   computer codes for electronic-structure calculations and materials modeling
   at the nanoscale. It is based on density-functional theory, plane waves, and
   pseudopotentials.

Before you start any of the labs, make sure that you have the software installed
and in your path. You have three options:

1. If you have your own Mac or Ubuntu 64-bit, you can use the
   executables already included in this repo. Run the following command to add
   the bin directory to your path as follows (assuming you are on bash):
    
    ```bash
    export PATH=$PATH:<path/to/repo>/bin/Mac or Ubuntu
    # The following is to set the NWChem basis sets used in lab1. Be careful
    # that the ending slash is needed!
    export NWCHEM_BASIS_LIBRARY = <path/to/repo>/resources/nwchem_basis/
    ```

2. You can download VirtualBox (https://www.virtualbox.org/), and a
   pre-configured Ubuntu virtual machine at this [link](https://s3.amazonaws.com/mavrl-web/nano266.ova).
   Note that it is a hefty 3 Gb download, so you will want to download this on
   a fast connection. After installing VirtualBox, do File->Import Appliance and
   then select the downloaded `nano266.ova` file. You can then start the
   virtual machine.
3. You can download the source code for QuantumEspresso or NWChem and install it 
   yourself. *Attempt this only if you have a fairly good familiarity with
   compiling things on Unix-based OSes, or are willing to spend the time to
   figure it out!*

In general, it is not recommended that you run on a native Windows OS for these
labs. Most first principles codes are designed to run primarily on
supercomputing clusters that have Unix-based OSes. If you have a Windows
machine, you should try option 2 above.

# Programming code

A lot of the labs use Python as a scripting language for automating calculations
and analysis. You should ensure that you have Python 2.7.x installed with numpy.
If you have a Mac, this should be already the case. If you use the virtual
machine, it is also already set up.
