Compuational Exercises
----------------------

Go over last week’s results
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Metagenome assemblies
-  Binning results
-  CheckM results
-  RefineM results

Identification of 16S rRNA genes in MAGs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Today, you will install a tool known as ``barrnap`` to predict ribosomal
RNA-coding regions in genomes. This tool is written by Torsten Seemann
from University of Melbourne in Australia. You can see more about how to
run the tool here: https://github.com/tseemann/barrnap

This tool is sensitive enough to be able to identify 16S, 23S, and 5S
rRNA genes in microbial genomes but also homologous genes found in
eukaryotes and organelles. First, make sure you are connected to
Cerberus and use ``conda`` to install barrnap.

To install, just type:

.. code:: bash

   conda install barrnap

Now, you will navigate into the folder produced by Metabat2 binning work
from last week. For example, in my home, I changed directory to the
following: ``/home/jsaw/exercises/spades_meta/binning/bins`` where the
bins or metagenome-assembled genomes (MAGs) are located.

Create a folder named as ``rRNA`` to store results from the ``barrnap``
program. Next, you will use the following example command(s) to run
``barrnap``.

.. code:: bash

   barrnap --quiet --kingdom bac --reject 0.05 --outseq rRNA/bin.barrnap.fasta bin.fa > rRNA/bin.barrnap

Make sure you notice the positions of parameters entered to run the
tool. The bin name is entered last before the output is redirected using
a “>” to a file named “bin.barrnap”. This is a minimum example of how to
run the tool. You can explore what options are available by typing
``barrnap -h``. In this example, I have specified ``--kingdom bac`` to
indicate that I’m searching for 16S genes using bacterial HMM (Hidden
Markov Model) prebuilt into the tool. If you have an archaeal, you would
ideally indicate that you want to use archaeal HMM by typing
``--kingdom arc``. In practice, it is sensitive enough that it will also
pick up rRNA genes for both domains of life.

Because you have multiple MAGs, to automate the process, I usually type
it in a ``bash`` loop so that I don’t have to type the same command for
multiple MAGs. Here is an example:

.. code:: bash

   for j in `ls *.fa | sed 's/.fa//g'`;do
       barrnap --quiet --kingdom bac --reject 0.05 --outseq rRNA/${j}.barrnap.fasta ${j}.fa > rRNA/${j}.barrnap
   done

The first line is to look for all the files with extension “.fa” and
removing the extensions in the screen output so that just the base names
are left. Then to run the ``barrnap`` command on these files. If you go
into the ``rRNA`` folder to look at the files produced, you will notice
that there are two output files for each MAG: one ends with “.barrnap”
extension and the other with “.barrnap.fasta”. The first one just shows
the coordinates of these genes within the contigs of the MAGs but the
second one extracted those sequences from those regions and put them
into a “fasta” file.

**Warning:** Ideally, you should run this script as an sbatch script and
not run it within the login node. However, ``barrnap`` is quite fast and
it is probably ok for today to run it in the login node.

You will notice that only some of the bins have the 16S rRNA sequences
necessary for you to identify what they are. So, to extract the 16S
sequences from those bins, you will type something like this:

.. code:: bash

   cd rRNA
   for j in `ls *.fasta | sed 's/.barrnap.fasta//g'`;do
       grep "16S" ${j}.barrnap.fasta | sed 's/>//g' | head -1 > ${j}.16S.list
       seqtk subseq ${j}.barrnap.fasta ${j}.16S.list > ${j}.16S.fasta
   done

This command extracted just the 16S sequence from those MAGs that have
them, and then put them into files with “.16S.fasta” file. If they
didn’t have the 16S gene, then you would have empty files. How do you
check for empty files in Unix?

Now, you are ready to run BLAST on these 16S sequences.

Running BLAST to identify the MAGs with 16S genes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now, you will need to install ``blast`` on ``cerberus``. Use ``conda``
as it is the easiest way to install it. You may have used ``BLAST``
through a web interface, such as on the NCBI BLAST website
(https://blast.ncbi.nlm.nih.gov/Blast.cgi) but today, we will first
learn how to use command line ``BLAST`` tool. Install it by typing:

.. code:: bash

   conda install blast

The latest version is 2.10.1 as of today. An example command to run a
remote ``BLAST`` within the terminal environment is shown below:

.. code:: bash

   blastn -query bin.10.16S.fasta -db nt -remote -out test.blastn

As of this morning, remote BLAST on ``cerberus`` is not working
correctly. I would suggest that you first download the bins and
resulting files from ``barrnap`` to your local drive, install ``BLAST``
locally, then run it on your laptop.

**Update:** Upon further inspection the problem stems from an earlier
version of BLAST being installed, which was 2.5. If you install the
latest version of BLAST by typing ``conda install BLAST=2.10.1``, then
it works perfectly fine.

You can also produce html files using the command line BLAST. The
command for that is:

.. code:: bash

   blastn -query bin.10.16S.fasta -db nt -remote -html -out test.blastn.html

Now, using the ``bash`` for-loop I have shown as an example for running
``barrnap``, run remote BLAST on all the 16S sequences identified by
``barrnap``. After this, inspect the results to see what you were able
to identify from these BLAST results. What are the organisms identified
from these BLAST searches?

Running Web-based BLAST searches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next, you will use web-based databases to identify your organisms.
First, go to NCBI BLAST website
(https://blast.ncbi.nlm.nih.gov/Blast.cgi) and click on “Nucleotide
BLAST”. Here, you can paste your 16S sequence(s) from the MAGs and run
the same tool and against a reference database. First, paste one of the
16S sequences of your MAGs into the text box provided to enter
sequences.

Note that in the drop-down menu for “Database”, you can choose which
database to search against specifically. For example, if you choose
“nr/nt” under “Standard databases”, it is a comprehensive database of
all nucleotide sequences in NCBI so it will be slower and longer to
search. You can also search against “rRNA/ITS databases” and it will run
a little bit quicker, since it’s only containing ribosomal RNA or
related sequences.

Another website you should try to classify your organisms is to search
against the Silva database (https://www.arb-silva.de/). This contains a
manually curated database of all the 16S and 23S rRNA gene sequences and
they are more quality-controlled than NCBI nr/nt database. And searching
against the Silva 16S (or otherwise known as SSU - Small Subunit rRNA)
database will give you a better estimate of what your unknown organism
might be. This is due to the fact that 16S sequences in NCBI are
saturated by non-curated sequences that are simply annotated as
“uncultured bacteria” or “uncultured archaea” without any attempt to
further classify them. This makes it incredibly difficult to simply
identify your organism (especially if it happens to be previously
unknown organism) through BLAST searches.

Click on “Search” and choose “Sequence Search”. Paste a 16S sequence
into the search box and run the tool. Compare your results from NCBI and
Silva searches. Which database gave you a better idea of the identities
of the MAGs you obtained from the binning work?

Install GTDB-TK on Cerberus
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Genome Taxonomy Database Toolkit (GTDB-Tk) is a software toolkit that
will assign taxonomic classification to bacterial and archaeal genomes
based on the Genome Taxonomy Database (GTDB). You can actually search
for GTDB classification of different bacteria and archaea here:
https://gtdb.ecogenomic.org/

They essentially developed a classification system of prokaryotes
(*Bacteria* and *Archaea*) by using genomic information. By utilizing
conserved single-copy marker genes in thousands of genomes, they were
able to assign a more objective classification system than if one were
using just the 16S rRNA gene sequence. Their classification system
created a bit of headache because they renamed quite a number of
organisms based on their system and some names became a bit more
confusing to people who are not familiar with the new ones. For example,
if you look for the phylum *Chloroflexi*, which is a name of a phylum in
NCBI taxonomic classification system, they have renamed it to
*Chloroflexota*.

It remains to be seen if more microbiologists will adapt to the new
names in the near future. You can read their papers describing the GTDB
here (https://pubmed.ncbi.nlm.nih.gov/30148503/) and the toolkit here
(https://pubmed.ncbi.nlm.nih.gov/31730192/).

To install, first go here to read the detailed installation
instructions:
https://ecogenomics.github.io/GTDBTk/installing/bioconda.html#installing-bioconda

You have already done **step 1**. For step 2, you need to create an
environment for ``gtdbtk``. As shown in the page, type:

.. code:: bash

   conda create -n gtdbtk -c bioconda gtdbtk

This command will actually create a conda environment named ``gtdbtk``
and also install it at the same time. Next, you will need to activate
this environment. Type ``conda activate gtdbtk`` to activate the
environment, then type ``gtdbtk -h`` to see if it is correctly
installed. It will complain that you don’t have a reference database set
up yet. Normally, you will need to download the data, which is quite
large (~27 GB compressed). Because of this large file size, I have
downloaded for the class and all you need to do is to reference this
database in your Miniconda installation.

First, make sure that you have this file on ``cerberus``:

::

   ~/miniconda3/envs/gtdbtk/etc/conda/activate.d/gtdbtk.sh

Check by typing:
``ls ~/miniconda3/envs/gtdbtk/etc/conda/activate.d/gtdbtk.sh``

If it is there, the terminal will print the full path to the file. If
not, it will say “File not found”. Essentially, I’m trying to make sure
that you have this file created during installation of ``gtdbtk``
through ``conda``. The actually path will depend on how you first
installed Miniconda on ``cerberus``. If you followed default
installation paths, then it should be the same as shown here. Next, you
will type this command to replace the template “path” information stored
in the ``gtdbtk.sh`` file.

.. code:: bash

   echo "export GTDBTK_DATA_PATH=/groups/bisc4234/gtdb-tk_data/release95/" > ~/miniconda3/envs/gtdbtk/etc/conda/activate.d/gtdbtk.sh

I have downloaded the GTDB latest release in the folder
``/groups/gtdb-tk_data/release95`` and ``gtdbtk`` needs this reference
data in order to run it correctly. After typing this command, log out of
``cerberus`` and log back in. Now, activate the ``gtdbtk`` environment
again and type ``gtdbtk -h``. Now this tool should be running correctly.
However, ``gtdbtk`` may still fail to run properly on ``cerberus`` due
to high memory requirement of one of the dependent tools known as
``pplacer``. This usually happens when you specify to many CPUs to be
used when running ``pplacer``. As of now, ``gtdbtk`` tool does not run
properly due to the computational nodes not having enough memory for the
``pplacer`` component.

Test run GTDB-TK on Cerberus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once ``gtdbtk`` is correctly installed, you can run this tool to
classify the metagenomic bins produced by Metabat2. First, if you are
checking the bins produced by Metabat2 on a metaSPAdes assembly, go into
the ``binning`` subfolder first. Then create a sbatch script similar to
the one shown below:

.. code:: bash

   #!/bin/bash
   #SBATCH -o gtdb.%j.out
   #SBATCH -e gtdb.%j.err
   #SBATCH -p defq
   #SBATCH -N 1
   #SBATCH -D /home/jsaw/exercises/spades_meta/binning
   #SBATCH -J GTDBTK
   #SBATCH -t 4:00:00

   gtdbtk classify_wf --genome_dir bins/ --out_dir gtdb-tk_out --cpus 24 -x fa

And submit a job to run ``gtdbtk``. It is quite CPU and memory intensive
program so it will take quite a while to run. At the end of the run, it
will produce a folder named ``gtdb-tk_out``. There, you will find
summary files listing the taxonomic classifications of the bins being
checked.

Web-based GTDB-TK on KBase
~~~~~~~~~~~~~~~~~~~~~~~~~~

GTDB-Tk may or may not run properly on Cerberus. It is a very
memory-intensive tool that require a large amount of RAMs to run. If it
is not running or failing, you can run GTDB-Tk on a website known as
KBase, which is hosted by Joint Genome Institute (Department of Energy).

The Joint Genome Institute (JGI) hosts this web-based version of GTDB-Tk
on its website known as “KBase”. KBase has a suite of bioinformatic
tools that are designed to be user-friendly for users who have little or
no experience with the command line environment. The website is here:
https://www.kbase.us/

You will first need to create an account (free) and log in. Once you’re
in, you can upload the MAGs produced by Metabat2 to it. To start,

-  first create a “New Narrative” (see top right of the page).
-  Then click on the “Add Data” red button on the left. A panel will pop
   up on the right.
-  Click on “Import”, then click on the box. Upload your bins/MAGs. It
   will upload the bins onto “staging” area.
-  Next, expand the “Upload” menu on the lower left of the page and
   click “Batch Import Assembly from Staging Area”. This app will allow
   you to batch upload the bins to your narrative.
-  In the parameters box, type your user name after the “/” sign, then
   choose from “Assembly type”, “Metagenome-assembled genome (MAG)”,
   then give this dataset a name under the “Output Objects”. This can be
   any name but it is needed for the batch upload to work. Then click on
   “Run” green button.
-  The tool will import your bins to the “Data” section of the page.
   After this is done, select from the “Apps”, “Microbial Communities”,
   then choose “GTDB-Tk classify”. This will open an inferface to run
   GTDB-Tk on Kbase.
-  Choose from “Assembly input”, the name of the dataset you just
   provided earlier to upload the bins. And click on “Run” button. This
   will run the GTDB-Tk tool to classify your MAGs and it could take a
   few hours or so.
-  Observe the results after the run is completed to see the lineages
   the tool was able to identify. You can also download the result as a
   CSV file.

Retrieve related sequences to construct a phylogeny
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We will use the NCBI BLAST website to search and retrieve 16S rRNA
sequences that are related to your query of interest. The main page for
NCBI BLAST is located here: https://blast.ncbi.nlm.nih.gov/Blast.cgi

There are many flavors of BLAST, which stands for Basic Local Alignment
Search Tool and was designed to perform pairwise comparison of DNA or
amino acid sequences. The tool was first pubished in 1990 (see here:
https://pubmed.ncbi.nlm.nih.gov/2231712/)

You can use BLAST to identify any DNA or amino acid sequences. In order
for this to work, one must search a query sequence (in your case, the
16S rRNA gene sequence) against a database of either DNA or protein
sequences. These are massive databases that are impractical for you to
download locally and search them using the command line BLAST.
Therefore, NCBI databases are critical for biologist to identify and
characterize any sequencing data they product in their labs.

Scroll down to find this tool known as “MOLE-BLAST” near the bottom of
the page. This is a new feature implemented to help us classify 16S rRNA
sequences of unknown organisms (I recommend you watch this video to
learn more about how to use this tool:
https://www.youtube.com/watch?v=wBbh_1vXgsY). Those identified in your
MAGs would fit this description well. Click on the “MOLE-BLAST” icon and
it will bring up a web interface to enter your sequence.

**Steps:**

-  Copy and paste a 16S rRNA gene sequence of one of the MAGs produced
   by Metabat2 (from metaSPAdes assembly) in the text box under “Enter
   Query Sequences”.
-  Click on the drop-down menu next to “Database” and select “16S
   ribosomal RNA sequences (Bacteria and Archaea)”.
-  Click on the “+” sign next to “Advanced parameters”
-  Change the “Maximum target sequences” to 50
-  Change the “Number of database sequences” under “Multiple Alignment
   Parameters” to 20
-  Click on “Show results in a new window” and click on “Align”

It will take several minutes for this to finish. At the end of this run,
you will be shown a phylogenetic tree. It will display the closest
relatives of your query sequence and will show approximate distances of
it to nearest neighbor. You should be aware that this tree is build
using “Fast Minimum Evolution” method and not a robust method to build
an accurate phylogenetic tree. We will download the alignment
(containing your query sequence and the neighbors) from this website and
run the phylogenetic analysis using better tools.

**To download the alignment:**

-  Click on “See alignment” link near the top of the page.
-  This will display the accession numbers of close neighbors and also
   the query sequence
-  You can see the positions that are aligned and also unaligned
   positions along the sequence length (shown as “-” and known as gaps)
-  Click on “Download” link near the top of the page and choose “Fasta
   plus gaps” to download the multiple sequence alignment
-  Save it in your exercises folder on your laptop but make sure to
   rename it so that you remember what it is (make sure there are *no*
   spaces in your file name!)

Now, we can begin to construct a simply phylogenetic tree using this
alignment as an input file. Note that because we chose 20 for “Number of
database sequences” under “Multiple Alignment Parameters”, you will have
21 sequences (including your query) in this alignment file.

Construct a simple phylogenetic tree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now, using your terminal, install a few tools needed to align the
sequences, visualize alignments, trim them, and to infer phylogenetic
trees. Use conda to install the following tools:

::

   - mafft
   - trimal
   - iqtree
   - figtree

**We will install and run these tools on your laptop computer.**

To view multiple sequence alignments (MSA), download and install this
tool known as “Seaview” which has multiple versions for different
operating systems. Download it here:
http://doua.prabi.fr/software/seaview

**Aligning sequences**

We will use ``mafft`` to align your sequences. It is a high-performance
tool that can utilize multiple CPUs to speed up the alignment process
and has been benchmarked to be one of the best performing tools. The
paper describing the tool can be found here:
https://pubmed.ncbi.nlm.nih.gov/12136088/

Before aligning the sequences, we need to reformat the fasta headers so
that the final tree you build will contain the proper labels with names
of organisms included in the tree tips. To do that, type:

.. code:: bash

   sed 's/[ ,.|]/_/g' sequences.fa > tmp.fa
   mv tmp.fa sequences.fa

These commands remove space and other characters that might interfere
with the tree viewing program. Next, to align the fasta file you just
downloaded from the MOLE-BLAST page, let’s say if it is named as
``sequences.fasta``, for example, type in your terminal:

.. code:: bash

   mafft --auto --reorder sequences.fa > alignment.fa

Now, start the Seaview program and open the ``alignment.fasta`` file to
see what a MSA looks like. See if and where gaps appear in the
alignment. Seaview has built-in phylogenetic inference tools that can
build trees but we will use the tools we just installed using ``conda``
first.

**Trimming aligned sequences**

Next step before you run a phylogenetic inference tool is to trim
phylogenetically uninformative regions in the alignment. For example,
when you inspect the alignment using Seaview, you’ll notice that there
are some regions with only gaps and perhaps one or two taxa may have a
base in that position. Since it does not provide any information for the
substitution models being used by the phylogenetic inference tool, it is
best to remove them. Again, this is a subjective thing and how much data
to trim really depends on a lot of things. The tool we will be using to
trim the alignment is known as trimAl and the paper describing the tool
is found here: https://pubmed.ncbi.nlm.nih.gov/19505945/

To trim your alignment, type:

.. code:: bash

   trimal -in alignment.fa -automated1 -out trimmed_alignment.fa

We used the ``-automated1`` option to tell ``trimal`` to automatically
check what to trim based on heuristics. You can also manually specify
gap thresholds by providing the ``-gt`` flag with fractions (eg: 0.5
means to trim away a position if more than 50% of the taxa have a gap
character at a given position). Now, use Seaview to check the alignment
again. Did you notice the difference between the original
``alignment.fa`` file and ``trimmed_alignment.fa`` file?

Now, we can continue with a phylogenetic inference program to construct
a phylogenetic tree.

**IQ-Tree**

We will use the tool known as IQ-Tree to constuct a phylogenetic tree of
your query with best hits. IQ-Tree has become one of the most popular
tools to construct phylogenetic trees and to calculate statistics for
phylogenetic/phylogenomic related analyses. I personally prefer using it
than any other tools out there. A recent paper describing the tool can
be found here: https://pubmed.ncbi.nlm.nih.gov/32011700/

*Model Test*

Before running an actual tree, we will run a model test to identify the
best substitution model to use for DNA sequences. Type:

.. code:: bash

   iqtree -m TESTONLY -s trimmed_alignment.fa -st DNA -pre model_test -nt 4

This will run a model test tool that is part of the IQ-Tree tool. If you
are curious to know what each of these parameters mean, type
``iqtree -h`` to see all the options and detailed explanation of each
parameter. Once the model test is done, look at the log file produced by
``iqtree``. The quickest way to just parse the best fit model in the log
file is to type like this:

.. code:: bash

   grep "Best-fit" model_test.log

In my example, this is the output I see:

::

   Best-fit model: GTR+F+G4 chosen according to BIC

So IQ-Tree has found the model ``GTR+F+G4`` as the best-fit model based
on Bayesian Information Criterion
(https://en.wikipedia.org/wiki/Bayesian_information_criterion). So we
will use this model to run IQ-Tree.

*IQ-Tree*

To run IQ-Tree with the model chosen, type:

.. code:: bash

   iqtree -m GTR+F+G4 -s trimmed_alignment.fa -st DNA -nt 4 -bb 1000 -pre iqtree_bin

The ``-bb 1000`` is a parameter for ultrafast bootstrap processes needed
to calculate bootstrap support for the tree. A number of 1000 is a
recommended number. It should run quite quickly. Now you can view the
resulting phylogenetic tree using a tree viewing program.

Viewing the phylogenetic tree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We will use this tool known as FigTree to view the resulting
phylogenetic tree locally on your laptop. If you have not already
installed FigTree on your local computer, use ``conda`` to install it
first. Next download the results from IQ-Tree analysis to your laptop
using ``rsync``.

Once the files are downloaded, you can type in your terminal:

.. code:: bash

   figtree iqtree_bin.contree

This will open a graphical interface of FigTree and it will prompt you
to enter a label for support values. Type “bootstrap” in the box. You
will see your Query sequence label as one of the tips in this tree.
Expand the menu under “Trees” on the left and check “Root tree”, then
check “Midpoint”. We are now rooting the tree using mid-point rooting
method. Check the box “Order nodes”. Now the tree is a little bit easier
to view. You can export the tree in various formats (such as PDF, SVG,
PNG, etc). Go to “File” menu and you can see the export options.

From this phylogenetic tree, you should be able to see the closest
relative of your MAG. What is the closest relative of your MAG based on
this tree? Again, this depends a bit of how novel the 16S sequence of
your MAG is. If it has sequence identity below 80% to the best match, it
is not going to be very easy to identify/classify them.
