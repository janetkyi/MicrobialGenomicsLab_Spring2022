Exercises for Week4
-------------------

Virtual environments in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Miniconda/Bioconda is a fantastic way to manage and install tools but
sometimes, you will encounter that some tools are incompatible with the
Python version you have currently installed. For example, the Quast tool
you will be using to assess SPAdes assembly metrics requires an earlier
version of Python (3.6) and won’t run if you have latest version of
Python if it’s higher than 3.6. If this happens you can create a Python
virtual environment to install an earlier version of Python so that you
can install Quast.

To create a new Python virtual environment, type something like this:

.. code:: bash

   conda create -n quast_env python=3.6

Here, ``-n quast_env`` flag means you are trying to create a new virtual
environment with the name ``quast_env``, something descriptive so that
you remember what that environment is for. And you have specified that
you want the Python version to be 3.6. To activate this new virtual
environment, type:

.. code:: bash

   conda activate quast_env

You will notice in your terminal that the name ``quast_env`` is inside
the paranthese at the very beginning of your command prompt. This
indicates that you are in this virtual environment. Now, you can install
Quast using conda. Type:

.. code:: bash

   conda install quast

And it should install fine now. To return to your original (base) Python
environment, you type:

.. code:: bash

   conda deactivate

Now, you will see that the command prompt shows ``base`` at the very
beginning.

Virtual environments are useful ways to test and install new tools that
might otherwise break or mess up with your base Python environment. You
can also remove the virtual environment you just created by typing:
``conda env remove --name quast_env``. To list all the virtual
environments you have created, type: ``conda env list``. To further
learn how to use conda, here’s a cheat sheet with all the useful
commands.

.. code:: ipython3

    from IPython.display import IFrame
    IFrame("https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf", width=800, height=800)




.. raw:: html

    
    <iframe
        width="800"
        height="800"
        src="https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf"
        frameborder="0"
        allowfullscreen
    ></iframe>




Connecting to GW HPC cluster (Cerberus)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Today, you will be remotely connecting to a high performance computing
(HPC) cluster at GW. This cluster has 10 nodes (think of it as 10
computers) with 128 GB of RAM and 28 CPU cores each. This means you can
parallelize certain bioinformatic tasks over multiple CPUs and even
across multiple nodes. Glen MacLachlan, who is helping us to set up this
computing cluster is here with us today and he will be able to answer
any questions you may have regarding this cluster.

Today, you will be connecting to a high-performance computing (HPC)
cluster at GW, which is given a name ``cerberus``. This is where you
will be transferring the two datasets you have downloaded over the past
few weeks. To remotely connect to ``cerberus``, you will need to use
SSH, which stands for “Secure Shell”. SSH (Secure Shell) is a network
protocol that uses encryption technology to securely connect to another
computer or securely transfer files to a remote computer. You can read
more about ssh in the following links:

https://www.ssh.com/ssh/

https://en.wikipedia.org/wiki/Ssh_(Secure_Shell)

Before even attempting to connect to the server, you need to first
download and install VPN client on your laptop. Here is where you
download the client: https://my.gwu.edu/mod/downloads/?category=VPN

There are both Windows and Mac versions. Choose the correct one. Only
after installing the VPN and logging into GW’s VPN, you can attempt to
access ``cerberus``.

The command to connect to ``cerberus`` is ``ssh``. You will be using
your GW NetID and password to connect to the server. To connect, an
example command is shown below:

.. code:: bash

   ssh jsaw@cerberus.colonialone.gwu.edu

Here, I am using my NetID, which is ``jsaw``. You will replace it with
your NetID. If this is the first time you are connecting to the server,
it will ask you a few questions and you should type “y” to say yes to
the answers. When it asks for your password, type your password for the
NetID (same as your email password, I believe). Once you’re logged in,
you can type ``uname -a`` and this will print some information about the
operating system running on this machine, which is Linux and will aslo
print the host name, which is ``cerberus.colonialone.gwu.edu``.

To logout, just type ``exit``.

Using ssh keys to log in to ``cerberus``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each time you log in to a remote computer with the ``ssh`` command, it
will ask you to enter the password. It can get pretty tiring if you have
to type this information every single time to log on to a remote
computer. To get around this problem, you can use a **ssh key** to log
in without having to type your password every single time. In order to
generate a ssh key, you type ``ssh-keygen`` command. Detailed
instructions on how to set up a ssh key and copy it to a remote computer
are shown here:

https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys–2

Briefly, the steps involve the following:

.. code:: bash

   ssh-keygen -t rsa
   ssh-copy-id xxxx@cerberus.colonialone.gwu.edu

The first command will generate a ssh key and it will ask you to enter a
“passphrase”. This is not a password but a phrase you should remember
when using ssh key to connect to a remote machine. Usually, you enter
this passphrase once and it will not ask for it again until you restart
your computer. You can also leave it blank (no passphrase) but it is not
recommended.

The second command ``ssh-copy-id`` will copy your public key to the
remote computer (``cerberus``) and this is the id it will check to
autheticate your remote computer (laptop) every time you try to log in.
Make sure to replace the “xxxx” with your NetID.

File and folder organization on ``cerberus``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you’re logged on, you will be directed to your home folder. For me,
it is ``/home/jsaw``. Here, you should create the following folders:

-  tools
-  exercises
-  data
-  projects

You will be downloading Miniconda to ``tools`` folder so that you can
install your own copy of Miniconda on ``cerberus`` to manage and install
additional bioinformatic tools (similar to what you have already done on
your laptop).

The ``data`` folder should be where you store your raw sequence files
and actual work should be done inside the ``exercises`` folder. Later
on, you will be working on group/individual projects and you should
store those work in the ``projects`` folder.

Transferring files to/from ``cerberus``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will soon realize that it becomes a necessity to transfer files
to/from a remote computer. You can run computational analyses on a
remote computer but if you want to inspect the results on your laptop
using graphical tools, then you will need to download those files to
your laptop computer. There are several tools that will allow you to
transfer files between computers. GUI-based (graphical user interface)
tools such as Filezilla or Cyberduck can do these tasks.

In this course, though, you will learn how to use command line based
tools such as ``rsync`` or ``scp`` to copy or sync files between local
and remote computers. I use ``rsync`` exclusively because it is a very
powerful tool that can automate things in a terminal environment and you
can programmatically transfer files of a certain type or format, for
example. Today, you will learn how to transfer the “adapters.fa” file
you downloaded from last week to do sequence quality trimming and upload
it to ``cerberus``.

**To transfer file from your laptop to a remote computer**

You should first go into the folder where you stored the adapter file.
It should be named as ``adapters.fa``. Then an example command to
transfer this adapter file to my home folder on ``cerberus`` would look
something like this:

::

   rsync -avzP adapters.fa jsaw@cerberus.colonialone.gwu:~/

This will upload the ``adapters.fa`` file to Cerberus and the file will
go directly into your home folder. Instead of ``jsaw``, which is my
username, you should type your NetID.

To download files or folders from ``cerberus`` to your laptop computer,
you can type something like this:

::

   rsync -avzP jsaw@cerberus.colonialone.gwu.edu:~/file.txt .

The dot at the very end of this command is just to indicate that you
want to download the remote ``file.txt`` file to current folder or
directory on your laptop. You can also use wild-card characters like
``*`` to transfer multiple files or folders. I will show some examples
in class.

Installation of Miniconda and Bioconda on ``cerberus``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You have already done Miniconda and Bioconda installation previously on
your laptop and this shouldn’t be too problematic for you this time
around. First, log in to ``cerberus`` using ``ssh``. Once you’re in your
home folder, change directory into the ``tools`` folder then type the
following:

.. code:: bash

   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   chmod +x Miniconda3-latest-Linux-x86_64.sh
   ./Miniconda3-latest-Linux-x86_64.sh

Follow the instructions, don’t change anything, and say yes to
everything. Then logout by typing ``exit``. Log back onto ``cerberus``
again. Then add the Bioconda channels by typing:

.. code:: bash

   conda config --add channels defaults
   conda config --add channels bioconda
   conda config --add channels conda-forge

Now your ``conda`` is set up to install the necesary bioinformatic
tools.

File transfer between computers using ``rsync``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Today, we will be running SPAdes on ``cerberus`` but before doing that,
you need to transfer either the raw or trimmed fastq files to the remote
server. Since you have already done trimming using ``bbduk.sh`` tool, I
recommend you transfer the trimmed fastq files to the ``data`` folder on
``cerberus``. How do you do that? This is where the ``rsync`` command
comes in handy.

``rsync`` is a really useful tool to transfer files or folders between
two computers or even between different locations within the same
computer. Here, you can read more about several examples of how you can
use ``rsync``.

https://www.linuxtechi.com/rsync-command-examples-linux/

There are more examples than I have time to go through with you today.
Please check it out at your own time. Today, you will use ``rsync`` to
copy the trimmed fastq files from your laptop to the remote computer.
First, using your terminal, navigate to the folder on your laptop
computer where you have these trimmed fastq files. Then type:

.. code:: bash

   rsync -avzP *trimmed.fastq.gz xxxx@cerberus.colonialone.gwu.edu:~/data/

Make sure to replace xxxx with your NetID. If you have created the
``data`` folder on ``cerberus``, the above command should copy the 2
trimmed fastq files to ``cerberus``.

Submitting jobs on ``cerberus``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now, you have those two files ready on the remote computer and you can
start running a SPAdes assembly. But one thing you need to be aware of
when working on a remote HPC computer like ``cerberus``, you need to
work with job schedulers that will prioritize these jobs according to
the resources requested upon job submission. Read more about job
schedulers here:

https://en.wikipedia.org/wiki/Job_scheduler

Here, we are using **SLURM (Simple Linux Utility for Resource
Management)** to schedule and manage jobs. In order to submit a job to
the job scheduler, you need to write a script with a few parameters
telling what exactly you are doing, for how long, and the resources
needed. For example, to run SPAdes, an example command I provided for
you to run on your laptop is like this below:

.. code:: bash

   spades.py \
       -t 4 \
       --pe1-1 data/SRR12610971_1.trimmed.fastq.gz \
       --pe1-2 data/SRR12610971_2.trimmed.fastq.gz \
       -k 21,33,55,77 \
       -o spades_assembly

On ``cerberus``, you cannot simply type those commands as soon as you
are logged in. The computer to which you are logged in is known as the
“login node” and you should not be running anything on the login node.
You will write a script containing lines as shown below:

.. code:: bash

   #!/bin/bash
   #SBATCH -o asm%j.out
   #SBATCH -e asm%j.err
   #SBATCH -D /home/jsaw/exercises
   #SBATCH -J ASM
   #SBATCH -N 1
   #SBATCH -t 1:00:00
   #SBATCH -p defq

   module load spades/3.14.1

   spades.py \
       -t 16 \
       --pe1-1 ../data/SRR12610971_1.trimmed.fastq.gz \
       --pe1-2 ../data/SRR12610971_2.trimmed.fastq.gz \
       -k 21,33,55,77 \
       -o spades_assembly

Here, I am specifying several things to tell the job scheduler:
``#SBATCH -D /home/jsaw/exercises`` is to tell the scheduler that I want
to run this task in this folder, ``#SBATCH -N 1`` means I am requesting
one compute node for this task, ``#SBATCH -t 1:00:00`` means I am
requesting time limit of 1 hour. This means if you don’t finish this
assembly within 1 hour, the job is terminated. So you want to make sure
you know how long certain tasks should take. ``#SBATCH -p defq`` means I
am submitting the job to default queue (don’t worry about it for now as
we only have default nodes at the moment on ``cerberus``). There are
more parameters you can specify but I won’t go into that for now.

There is a line that says: ``module load spades/3.14.1``. Cerberus comes
with SPAdes already installed on it and to use it, you need to load it
into your environment. If you don’t specify this, SPAdes won’t start. To
see what else is installed on ``cerberus``, type ``module avail`` and
you can see what is already available.

You will then save this script into a file, let’s say
``run_assembly.sh``. So how to create this script file on a remote
computer?? Here, you can use command line text editors such as ``vim``,
``nano``, ``pico``, ``ed``, or ``emacs`` to create text files, edit and
save them. My favorite editor is ``vim``. There is a steep learning
curve to use ``vim`` (see here:
https://opensource.com/article/19/3/getting-started-vim) but it has a
lot of advantages over other tools like ``nano`` or ``pico``. Some
people prefer ``emacs`` over ``vim`` but that’s a matter of personal
preference.

See below for a joke:

.. figure:: images/xkcd.jpg
   :alt: xkcd

   xkcd

Then to submit the job to run this assembly, type:
``sbatch run_assembly.sh``. This will submit the job to the queue. To
check and see whether your job has started running or not, type:
``squeue``. This will display your job information and if it is running
you should see an “R” under the “ST” header. You will notice that the
assembly run on ``cerberus`` will be done significantly faster than if
it were run on your laptop computer.

Checking assembly results
~~~~~~~~~~~~~~~~~~~~~~~~~

Once you are done with SPAdes assembly (by typing ``squeue`` and
checking if there is no job shown in the status), use Quast to assess
assembly results. You can either view the results on ``cerberus`` using
the ``less`` command or download the results to your laptop using the
``rsync`` command, then viewing them locally. If you download the Quast
results, you will be able to see graphs and plots generated by the tool.

Viewing assemblies with Bandage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After assembling genomes using SPAdes or other assemblers, sometimes it
is good have a graphical overview of how good the assembly really is. To
do that, you can use a graphical tool known as “Bandage” to view
connections between the contigs. If an assembly has very convoluted
graph paths, you would see this quite quickly. Ideally, if you have
one-to-one connection between contig edges, that means the assembler had
figured out the optimal path between the contigs and it has made
connections between them in the ``.gfa`` file that it produces. Bandage
can take this file with the ``.gfa`` extension and produce a graphical
representation of contigs and their connections to other contigs.

The tool is graphical and you will need to visit this website to
download the version compatible with your computer’s OS.

https://rrwick.github.io/Bandage/

An example of what the *Salmonella enteria* assembly looks like for me
is shown below.

.. figure:: images/bandage.png
   :alt: *S. enterica* assembly

   *S. enterica* assembly

The thicker arcs are contigs and the thinner arcs connecting the thicker
ones mean that these contigs should be physically linked. The SPAdes
assembler has determined that even though they are separate contigs,
there is information indicating that they should be linked. Those in the
bottom without any links indicate singletons that have no known physical
links to other contigs. These could be either artefacts of assembly and
not part of the genome (usually very small contigs) or plasmids.
Plasmids are extra-chromosomal DNA that encode things like virulence
factors or other genetically selfish elements.

Transfer metagenomic data to ``cerberus`` for next week
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After you are done running SPAdes and checking the assembly results
using Bandage, run the ``rsync`` command again to upload the trimmed
metagenomic data you have downloaded to your laptop. Follow the example
I have provided earlier (scroll up) to see how to use ``rsync`` to the
``data`` folder on ``cerberus``.
