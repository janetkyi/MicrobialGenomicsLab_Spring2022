Install tools for today’s lab
-----------------------------

Last week, I mentioned that you should install some bioinformatic tools
we will be using this week. If you did not have a chance to install them
last week, please do it now. You should be able to install them all
using ``conda``.

sra-tools
~~~~~~~~~

Here, we will use sra-tools to download sequence data from publicly
accessible databases such as NCBI. This tool allows you to download some
sequence files from NCBI directly from your terminal without having to
use your web browser. First, I will check if ``sra-tools`` is on
``conda``.

.. code:: bash

    %%bash
    conda search sra-tools


.. parsed-literal::

    Loading channels: ...working... done
    # Name                       Version           Build  Channel             
    sra-tools                      2.6.2               0  bioconda            
    sra-tools                      2.6.3               0  bioconda            
    sra-tools                      2.7.0               0  bioconda            
    sra-tools                      2.8.0               0  bioconda            
    sra-tools                      2.8.1               0  bioconda            
    sra-tools                      2.8.2               0  bioconda            
    sra-tools                      2.8.2      h550f44e_1  bioconda            
    sra-tools                      2.9.0      h470a237_1  bioconda            
    sra-tools                      2.9.1      h470a237_0  bioconda            
    sra-tools                    2.9.1_1      h470a237_0  bioconda            
    sra-tools                      2.9.6      h0a44026_0  bioconda            
    sra-tools                     2.10.0 pl526h6de7cb9_0  bioconda            
    sra-tools                     2.10.1 pl526h9f37e31_0  bioconda            


Now, you can install ``sra-tools`` by typing

.. code:: bash

   conda install sra-tools

This will install a suite of tools you will need to download publicly
available sequences from NCBI.

FastQC
~~~~~~

FastQC is a tool you will need to use to assess sequence quality and to
see if they are suitable to be used in your analyses. Earlier days,
sequences produced by these so-called “Next-gen” sequencing instruments
(especially in early 2010s) produced sequences with high error rates and
low qualities. And they sometimes include the adapter sequences that
should be removed before they can be used. To check for sequence
quality, there are several tools available but one of the most
well-known (and most widely used) is FastQC. It exists in both graphical
and command line versions. You can install it using ``conda``. First,
search for it.

.. code:: bash

    %%bash
    conda search fastqc


.. parsed-literal::

    Loading channels: ...working... done
    # Name                       Version           Build  Channel             
    fastqc                        0.10.1               0  bioconda            
    fastqc                        0.10.1               1  bioconda            
    fastqc                        0.11.2               1  bioconda            
    fastqc                        0.11.2      pl5.22.0_0  bioconda            
    fastqc                        0.11.3               0  bioconda            
    fastqc                        0.11.3               1  bioconda            
    fastqc                        0.11.4               1  bioconda            
    fastqc                        0.11.4               2  bioconda            
    fastqc                        0.11.5               1  bioconda            
    fastqc                        0.11.5               4  bioconda            
    fastqc                        0.11.5      pl5.22.0_2  bioconda            
    fastqc                        0.11.5      pl5.22.0_3  bioconda            
    fastqc                        0.11.6               2  bioconda            
    fastqc                        0.11.6      pl5.22.0_0  bioconda            
    fastqc                        0.11.6      pl5.22.0_1  bioconda            
    fastqc                        0.11.7               4  bioconda            
    fastqc                        0.11.7               5  bioconda            
    fastqc                        0.11.7               6  bioconda            
    fastqc                        0.11.7      pl5.22.0_0  bioconda            
    fastqc                        0.11.7      pl5.22.0_2  bioconda            
    fastqc                        0.11.8               0  bioconda            
    fastqc                        0.11.8               1  bioconda            
    fastqc                        0.11.8               2  bioconda            
    fastqc                        0.11.9               0  bioconda            


As you can see, there are several versions and if you just type
``conda install fastqc``, it will install the latest version of it.

BBmap
~~~~~

FastQC will help you see what needs to be done to the original raw
sequnce files but it doesn’t actually do anything else. To actually trim
reads of poor quality or to discard sequences that do not meet specific
requirement, you need to use tools like BBmap. It is just one of the
many tools that does similar function.

.. code:: bash

    %%bash
    conda search bbmap


.. parsed-literal::

    Loading channels: ...working... done
    # Name                       Version           Build  Channel             
    bbmap                          35.85               1  bioconda            
    bbmap                          35.85               2  bioconda            
    bbmap                          37.02               0  bioconda            
    bbmap                          37.10               0  bioconda            
    bbmap                          37.10               1  bioconda            
    bbmap                          37.17               0  bioconda            
    bbmap                          37.17               1  bioconda            
    bbmap                          37.52               0  bioconda            
    bbmap                          37.52               1  bioconda            
    bbmap                          37.62               0  bioconda            
    bbmap                          37.62               1  bioconda            
    bbmap                          37.66               0  bioconda            
    bbmap                          37.75               0  bioconda            
    bbmap                          37.77               0  bioconda            
    bbmap                          37.78               0  bioconda            
    bbmap                          37.90               0  bioconda            
    bbmap                          37.95               0  bioconda            
    bbmap                          37.96               0  bioconda            
    bbmap                          37.99               0  bioconda            
    bbmap                          37.99               1  bioconda            
    bbmap                          38.06               0  bioconda            
    bbmap                          38.06               2  bioconda            
    bbmap                          38.16               0  bioconda            
    bbmap                          38.18               0  bioconda            
    bbmap                          38.19      h470a237_0  bioconda            
    bbmap                          38.20      h470a237_0  bioconda            
    bbmap                          38.22      h1de35cc_1  bioconda            
    bbmap                          38.22      h470a237_0  bioconda            
    bbmap                          38.44      h1de35cc_0  bioconda            
    bbmap                          38.45      h1de35cc_0  bioconda            
    bbmap                          38.46      h1de35cc_0  bioconda            
    bbmap                          38.49      h1de35cc_0  bioconda            
    bbmap                          38.51      h1de35cc_0  bioconda            
    bbmap                          38.56      h1de35cc_0  bioconda            
    bbmap                          38.57      h1de35cc_0  bioconda            
    bbmap                          38.58      h01d97ff_0  bioconda            
    bbmap                         38.61b      h01d97ff_0  bioconda            
    bbmap                          38.62      h01d97ff_0  bioconda            
    bbmap                          38.63      h01d97ff_0  bioconda            
    bbmap                          38.65      h01d97ff_0  bioconda            
    bbmap                          38.67      h01d97ff_0  bioconda            
    bbmap                          38.68      h01d97ff_0  bioconda            
    bbmap                          38.69      h01d97ff_0  bioconda            
    bbmap                          38.70      h01d97ff_0  bioconda            
    bbmap                          38.71      h01d97ff_0  bioconda            
    bbmap                          38.72      h01d97ff_0  bioconda            
    bbmap                          38.73      h01d97ff_0  bioconda            
    bbmap                          38.75      h01d97ff_0  bioconda            
    bbmap                          38.76      h01d97ff_0  bioconda            
    bbmap                          38.79      h01d97ff_0  bioconda            
    bbmap                          38.84      h0b31af3_0  bioconda            
    bbmap                          38.84      hf29c6f4_1  bioconda            
    bbmap                          38.86      hf29c6f4_0  bioconda            


This is a collection of tools that you will need to use to remove
poor-quality sequence reads and to trim bad or contaminated sequences
from the pool. Install it by typing:

``conda install bbmap``

Now you have all the tools we will need to use for today’s exercise.
