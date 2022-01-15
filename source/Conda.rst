Install and configure Miniconda and Bioconda
--------------------------------------------

Go here to download Miniconda package manager:
https://docs.conda.io/en/latest/miniconda.html

Install Miniconda
~~~~~~~~~~~~~~~~~

Follow instructions for both Mac and Windows. Choose Python 3.7 version.

For **Mac**, I recommend you download the “pkg” version which is a
graphical version of the installer.

For **Windows/WSL**, open your Ubuntu shell (right-click on the icon and
run as Administrator). Then type:

.. code:: bash

   cd /mnt/c
   mkdir tools
   cd tools
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   chmod +x Miniconda3-latest-Linux-x86_64.sh
   ./Miniconda3-latest-Linux-x86_64.sh

Follow the instructions along and make sure you say “yes” at the very
end when it asked you if you want the installer to prepend it to path.

You can visit this page for more tips on how to instlall Miniconda on
WSL.

https://gist.github.com/kauffmanes/5e74916617f9993bc3479f401dfec7da

**After installation:**

For **Mac**:

Close your terminal and open it again. Try typing ``conda`` to see if
the command works. You will see a bunch of options you can type with the
conda command.

For **Windows**:

Close your Ubuntu shell, then restart it by right-cliking on the Ubuntu
icon and run it as Administrator. Try typing ``conda`` to see if it
shows options.

Install Bioconda
~~~~~~~~~~~~~~~~

After Miniconda is installed, you will need to configure Bioconda
channels. Bioconda allows you to install *most* bioinformatics tools
with ease without learning to use compilers or to figure out software
dependencies.

Install bioconda by typing the following commands in your terminal:

::

   conda config --add channels defaults
   conda config --add channels bioconda
   conda config --add channels conda-forge

These commands will add bioinformatics related tools “channels” to
miniconda. Now, you should be able to search and install tools locally
on your computer. Try install jupyter first.

::

   conda search jupyter
   conda install jupyter

   conda search jupyterlab
   conda install jupyterlab

After you have configured the bioconda channels, most of the
bioinformatics tools we will use in this course should be available for
installation through ``conda``.
