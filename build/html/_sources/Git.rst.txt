Git and Github
==============

What is git?
------------

Git is a tool for version control that allows you to track changes so
that you can work collaboratively in a team environment. A lot of
software developers and engineers use it but scientists also use it to
maintain their software/code generated for research. Although I will
cover some basics on using Git, you will need to read up on what it is
and how to use it at your own time. See here for more information:

https://guides.github.com/introduction/git-handbook/

Here is another resource on Git. It is for Bitbucket repository but
command examples are the same as what you would be using with Github.

https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud

How to install Git
------------------

First, you will try to install ``git`` tool through command line tools
such as Homebrew on Mac.

On **Mac OS**, you will type like this in your terminal:
``brew install git``

On **Windows OS** running **Linux** subsystem with **Ubuntu**, you can
type something like this in your terminal: ``apt-get install git``

And this will install the tool on your command line environment. You may
need root privileges to install tools on Ubuntu. If this happens, you
just type: ``sudo apt-get install git`` and it should work. You will
have to type your password though.

Another way of installing ``git`` is to use your Miniconda package
managing system. It is actually my preferred method of installing new
tools in my commandline environment. If you have set up Miniconda
correctly, then you can just type:

``conda install git`` in either Mac or Windows OS terminal and this
would install ``git`` on your system. Here is an example of what you
will see when you use Miniconda to search if git is in its list of
packages that you can install through ``conda`` command.

.. code:: bash

    %%bash
    conda search git


.. parsed-literal::

    Loading channels: ...working... done
    # Name                       Version           Build  Channel             
    git                           2.12.2               4  conda-forge         
    git                           2.13.3               0  conda-forge         
    git                           2.14.1               0  conda-forge         
    git                           2.14.1               1  conda-forge         
    git                           2.14.1 pl526ha558ef4_2  pkgs/main           
    git                           2.14.1 pl526hcdafd81_2  pkgs/main           
    git                           2.14.2               0  conda-forge         
    git                           2.14.2               1  conda-forge         
    git                           2.14.2               2  conda-forge         
    git                           2.14.2               3  conda-forge         
    git                           2.15.0 pl526h6165b5f_0  pkgs/main           
    git                           2.16.1      h74bb3f6_0  pkgs/main           
    git                           2.16.1 pl526h74bb3f6_1  pkgs/main           
    git                           2.17.0 pl526h028e6c8_0  pkgs/main           
    git                           2.17.1               0  conda-forge         
    git                           2.17.1 pl526h028e6c8_0  pkgs/main           
    git                           2.18.0               0  conda-forge         
    git                           2.18.0 pl526h028e6c8_0  pkgs/main           
    git                           2.18.0 pl526hbb17d3c_1  conda-forge         
    git                           2.19.0 pl526hbb17d3c_0  conda-forge         
    git                           2.19.1 pl526h028e6c8_0  pkgs/main           
    git                           2.19.1 pl526h28b1069_1000  conda-forge         
    git                           2.19.1 pl526h28b1069_1001  conda-forge         
    git                           2.19.1 pl526h6951d83_0  pkgs/main           
    git                           2.19.1 pl526hbb17d3c_0  conda-forge         
    git                           2.19.1 pl526hbb17d3c_1  conda-forge         
    git                           2.19.2 pl526h28b1069_1000  conda-forge         
    git                           2.19.2 pl526hbb17d3c_0  conda-forge         
    git                           2.20.0 pl526h28b1069_1000  conda-forge         
    git                           2.20.0 pl526hbb17d3c_0  conda-forge         
    git                           2.20.1 pl526h28b1069_1000  conda-forge         
    git                           2.20.1 pl526h28b1069_1001  conda-forge         
    git                           2.20.1 pl526h3e3e3d1_1002  conda-forge         
    git                           2.20.1 pl526h6951d83_0  pkgs/main           
    git                           2.20.1 pl526hbb17d3c_0  conda-forge         
    git                           2.21.0 pl526h3e3e3d1_0  conda-forge         
    git                           2.22.0 pl526hbdf3604_0  conda-forge         
    git                           2.23.0 pl526h6951d83_0  pkgs/main           
    git                           2.23.0 pl526hbdf3604_0  conda-forge         
    git                           2.23.0 pl526hbdf3604_1  conda-forge         
    git                           2.23.0 pl526hbdf3604_2  conda-forge         
    git                           2.24.0 pl526hdc91d69_0  conda-forge         
    git                           2.24.0 pl526hdc91d69_1  conda-forge         
    git                           2.25.0 pl526hdc91d69_0  conda-forge         
    git                           2.26.0 pl526h561ab23_0  conda-forge         
    git                           2.26.1 pl526hcc376a2_0  conda-forge         
    git                           2.26.2 pl526hcc376a2_0  conda-forge         
    git                           2.27.0 pl526hcc376a2_0  conda-forge         
    git                           2.28.0 pl526hde3ca24_0  conda-forge         
    git                           2.28.0 pl526hde3ca24_1  conda-forge         


Cloning course repository on Github
-----------------------------------

As a member of the Microbial Genomics Lab 2022, you will have access to
our code repository.

If you log in to Github and visit this URL:

https://github.com/SawLabGW/MicrobialGenomicsLab_Spring2022

you will be able to download the code repository to your laptop. First,
if you haven’t already downloaded the code repository to your drive, you
want to “clone” it.

First, create a folder where you would want to store this repository.
For example, in your command line environment, type ``cd`` to go back to
your home directory. Then to create a folder named “repositories”.

Type: ``mkdir repositories``

Then go into that folder by typing: ``cd repositories``.

Then type:
``git clone https://github.com/SawLabGW/MicrobialGenomicsLab_Fall2020.git``

Now, you will see the folder “MicrobialGenomicsLab_Spring2022” in the
repositories folder.

If you would like to view the computational instructions locally, you
can navigate into ``build/html`` folder and open the ``index.html`` file
using your web browser.

Committing to the repository
----------------------------

For example, if you have a new file named text.txt which created and you
want to make it part of the repository, you will need to type the
command git add text.txt. You may type this command in the folder that
this file is located or from the root folder. If it is in a subfolder
named alison/notes/text.txt, then you want to type git add
alison/notes/text.txt in the root folder.

After adding the file, you will need to type the following command.

``git commit -a``

It will bring up the vim editor, which will prompt you to enter a
message before you can commit this file to the repository. If you would
rather bypass this step, you can specify in your previous git command
like this:

``git commit -m "created a new file"``

Here, you have put in quotes the text you wanted to convey along with
the commit command to let people know that you have created a new file
and added it to the repository. This helps your teammates and
collaborators keep track of what you did to the repository.

Finally, type ``git push origin master`` to “push” your changes to the
repository.

Before committing or pushing anything to the repository, you should
always type ``git pull origin master`` to get the latest updated version
of the repository. This is because there is a built-in check for people
to prevent overwriting things or missing something if someone else had
made a very recent commit to the repository.

**Note:** The repository you just downloaded is read-only and you cannot
add or remove files from it. We will discuss how to create your own
repositories later in the semester.
