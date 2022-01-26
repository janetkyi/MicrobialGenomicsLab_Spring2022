Genome Assembly using SPAdes
----------------------------

Introduction to SPAdes
~~~~~~~~~~~~~~~~~~~~~~

SPAdes was originally designed as a tool to assemble single-cell genomic
sequences that usualy comprise uneven sequence coverage. In order to be
able to discern such unenven coverages, the authors developed special
algorithms to detect such coverages and to account for such regions.
Also, to correct for errors that might be introduced during
multiple-displacement amplification (MDA), SPAdes incorporates an
“error-correction” step to improve sequence quality in those regions.

Since its intial development in 2012, the assembler has evolved to be
able to handle different types of sequencing technologies and datasets.
Now, it can handle not only single-cell genomic data but also genomic
sequences from isolate genomes (cultures), metagenomes. It can also
handle latest “next-gen sequencing” (NGS) data such as PacBio, Nanopore,
etc. SPAdes is hosted at this website
(https://cab.spbu.ru/software/spades/) but you can also visit their
github page to see the latest version here
(https://github.com/ablab/spades). The github page contains most updated
information on how to run SPAdes and what options you can use.

In today’s computational exercise, you will use SPAdes to assemble a
microbial genome sequenced with Illumina sequencing technology. In order
to be able to run SPAdes, you will need to install SPAdes through the
Miniconda Python package managing system.

Installing SPAdes
~~~~~~~~~~~~~~~~~

To install SPAdes on your laptop, you will first type this following
command:

.. code:: ipython3

    conda search spades


.. parsed-literal::

    Loading channels: done
    # Name                       Version           Build  Channel             
    spades                         3.6.2               0  bioconda            
    spades                         3.7.0               0  bioconda            
    spades                         3.8.0               0  bioconda            
    spades                         3.8.1               0  bioconda            
    spades                         3.9.0               0  bioconda            
    spades                         3.9.0          py27_1  bioconda            
    spades                         3.9.0          py27_2  bioconda            
    spades                         3.9.0          py34_1  bioconda            
    spades                         3.9.0          py35_1  bioconda            
    spades                         3.9.0          py35_2  bioconda            
    spades                         3.9.1               0  bioconda            
    spades                        3.10.0          py27_0  bioconda            
    spades                        3.10.0          py34_0  bioconda            
    spades                        3.10.0          py35_0  bioconda            
    spades                        3.10.1               1  bioconda            
    spades                        3.10.1          py27_0  bioconda            
    spades                        3.10.1          py34_0  bioconda            
    spades                        3.10.1          py35_0  bioconda            
    spades                        3.11.0          py27_0  bioconda            
    spades                        3.11.0          py27_1  bioconda            
    spades                        3.11.0          py35_0  bioconda            
    spades                        3.11.0          py35_1  bioconda            
    spades                        3.11.0          py36_0  bioconda            
    spades                        3.11.0          py36_1  bioconda            
    spades                        3.11.1      h21aa3a5_2  bioconda            
    spades                        3.11.1      h21aa3a5_3  bioconda            
    spades                        3.11.1      hb249e0d_4  bioconda            
    spades                        3.11.1      he4cf2ce_2  bioconda            
    spades                        3.11.1          py27_0  bioconda            
    spades                        3.11.1          py27_1  bioconda            
    spades                        3.11.1          py35_0  bioconda            
    spades                        3.11.1          py35_1  bioconda            
    spades                        3.11.1          py36_0  bioconda            
    spades                        3.11.1          py36_1  bioconda            
    spades                        3.12.0               1  bioconda            
    spades                        3.12.0          py27_0  bioconda            
    spades                        3.12.0          py35_0  bioconda            
    spades                        3.12.0          py36_0  bioconda            
    spades                        3.13.0               0  bioconda            
    spades                        3.13.1               0  bioconda            
    spades                        3.13.1      h21ccd2c_2  bioconda            
    spades                        3.13.1      h8f8a155_1  bioconda            
    spades                        3.13.2      h21ccd2c_0  bioconda            
    spades                        3.14.0      h21ccd2c_0  bioconda            
    spades                        3.14.1      he641558_0  bioconda            
    
    Note: you may need to restart the kernel to use updated packages.


This brings up all the different versions of SPAdes currently on my
``bioconda`` channel. The latest version tends to be at the bottom of
the page. Then to install the latest version, you would just type
``conda install spades``. On my laptop, I have already installed a
version of SPAdes. To check what version I have already install, I can
type like this below:

.. code:: ipython3

    conda list | grep spades


.. parsed-literal::

    spades                    3.13.0                        0    bioconda
    
    Note: you may need to restart the kernel to use updated packages.


So, you can see that I have version 3.13.0 installed. If I want to be
explicit about the specific version of SPAdes I want to install, I can
type like this:

``conda install spades=3.14.0``

This will install version 3.14.0. If you do not specify a version
number, then it will install the latest version by default. Once you
have SPAdes installed, you should be able to type this command
``spades.py`` right away in your terminal.

Running SPAdes
~~~~~~~~~~~~~~

.. code:: bash

    %%bash
    spades.py


.. parsed-literal::

    SPAdes genome assembler v3.13.0
    
    Usage: /Users/jsaw/miniconda3/bin/spades.py [options] -o <output_dir>
    
    Basic options:
    -o	<output_dir>	directory to store all the resulting files (required)
    --sc			this flag is required for MDA (single-cell) data
    --meta			this flag is required for metagenomic sample data
    --rna			this flag is required for RNA-Seq data 
    --plasmid		runs plasmidSPAdes pipeline for plasmid detection 
    --iontorrent		this flag is required for IonTorrent data
    --test			runs SPAdes on toy dataset
    -h/--help		prints this usage message
    -v/--version		prints version
    
    Input data:
    --12	<filename>	file with interlaced forward and reverse paired-end reads
    -1	<filename>	file with forward paired-end reads
    -2	<filename>	file with reverse paired-end reads
    -s	<filename>	file with unpaired reads
    --merged	<filename>	file with merged forward and reverse paired-end reads
    --pe<#>-12	<filename>	file with interlaced reads for paired-end library number <#> (<#> = 1,2,...,9)
    --pe<#>-1	<filename>	file with forward reads for paired-end library number <#> (<#> = 1,2,...,9)
    --pe<#>-2	<filename>	file with reverse reads for paired-end library number <#> (<#> = 1,2,...,9)
    --pe<#>-s	<filename>	file with unpaired reads for paired-end library number <#> (<#> = 1,2,...,9)
    --pe<#>-m	<filename>	file with merged reads for paired-end library number <#> (<#> = 1,2,...,9)
    --pe<#>-<or>	orientation of reads for paired-end library number <#> (<#> = 1,2,...,9; <or> = fr, rf, ff)
    --s<#>		<filename>	file with unpaired reads for single reads library number <#> (<#> = 1,2,...,9)
    --mp<#>-12	<filename>	file with interlaced reads for mate-pair library number <#> (<#> = 1,2,..,9)
    --mp<#>-1	<filename>	file with forward reads for mate-pair library number <#> (<#> = 1,2,..,9)
    --mp<#>-2	<filename>	file with reverse reads for mate-pair library number <#> (<#> = 1,2,..,9)
    --mp<#>-s	<filename>	file with unpaired reads for mate-pair library number <#> (<#> = 1,2,..,9)
    --mp<#>-<or>	orientation of reads for mate-pair library number <#> (<#> = 1,2,..,9; <or> = fr, rf, ff)
    --hqmp<#>-12	<filename>	file with interlaced reads for high-quality mate-pair library number <#> (<#> = 1,2,..,9)
    --hqmp<#>-1	<filename>	file with forward reads for high-quality mate-pair library number <#> (<#> = 1,2,..,9)
    --hqmp<#>-2	<filename>	file with reverse reads for high-quality mate-pair library number <#> (<#> = 1,2,..,9)
    --hqmp<#>-s	<filename>	file with unpaired reads for high-quality mate-pair library number <#> (<#> = 1,2,..,9)
    --hqmp<#>-<or>	orientation of reads for high-quality mate-pair library number <#> (<#> = 1,2,..,9; <or> = fr, rf, ff)
    --nxmate<#>-1	<filename>	file with forward reads for Lucigen NxMate library number <#> (<#> = 1,2,..,9)
    --nxmate<#>-2	<filename>	file with reverse reads for Lucigen NxMate library number <#> (<#> = 1,2,..,9)
    --sanger	<filename>	file with Sanger reads
    --pacbio	<filename>	file with PacBio reads
    --nanopore	<filename>	file with Nanopore reads
    --tslr	<filename>	file with TSLR-contigs
    --trusted-contigs	<filename>	file with trusted contigs
    --untrusted-contigs	<filename>	file with untrusted contigs
    
    Pipeline options:
    --only-error-correction	runs only read error correction (without assembling)
    --only-assembler	runs only assembling (without read error correction)
    --careful		tries to reduce number of mismatches and short indels
    --continue		continue run from the last available check-point
    --restart-from	<cp>	restart run with updated options and from the specified check-point ('ec', 'as', 'k<int>', 'mc', 'last')
    --disable-gzip-output	forces error correction not to compress the corrected reads
    --disable-rr		disables repeat resolution stage of assembling
    
    Advanced options:
    --dataset	<filename>	file with dataset description in YAML format
    -t/--threads	<int>		number of threads
    				[default: 16]
    -m/--memory	<int>		RAM limit for SPAdes in Gb (terminates if exceeded)
    				[default: 250]
    --tmp-dir	<dirname>	directory for temporary files
    				[default: <output_dir>/tmp]
    -k		<int,int,...>	comma-separated list of k-mer sizes (must be odd and
    				less than 128) [default: 'auto']
    --cov-cutoff	<float>		coverage cutoff value (a positive float number, or 'auto', or 'off') [default: 'off']
    --phred-offset	<33 or 64>	PHRED quality offset in the input reads (33 or 64)
    				[default: auto-detect]


I have to type ``%%bash`` before my command in order to be able to show
command line outputs in Jupyter Lab environment. When you are typing
``spades.py`` in your own terminal, you do not need to type this
``%%bash`` command. As you can see, you are given a number of options
that you can specify when running SPAdes. For example, if you are
running a metagenome assembly using SPAdes, then you would add an
``--meta`` flag to indicate the program that you are running a
metagenome assembly.

In today’s exercise, you will run SPAdes to assemble a genome belonging
to a bacterium (*Salmonella enterica*) that you have downloaded
previously from the following website:
https://www.ncbi.nlm.nih.gov/sra/SRX9094324

You have also done processing of this raw data into a form that is
suitable to be used as an input for the SPAdes assembler.

Checking sequence qualities
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To check sequence qualities of the two ``fastq`` files you have
downloaded previously, you will run the ``fastqc`` tool. First, using
your terminal, nagivate to the folder where you have downloaded these
sequences. For example, if you downloaded the sequences in
``/home/yourname/data``, then you would type:

``cd /home/yourname/data``

In my case, I have downloaded them into another folder named ``data``.

To check the quality of the downloaded sequences, you would run the
FastQC tool, which you have installed previously. To run, navigate into
the folder containing the data, then type:

``fastqc *.fastq``

Inspect the quality and statistics reported in this html file to see
what the report is telling you. Remember, these are paired fastq files
and this means “SRR12610971_1_fastqc.html” is only one of the pair. You
will need to inspect the second file “SRR12610971_2_fastqc.html” as
well.

Trimming the sequences
~~~~~~~~~~~~~~~~~~~~~~

To trim the possible Illumina adapter sequences and poor quality
regions, you can use several trimming tools such as Trimmomatic, bbduk,
or cutadapt. Here, you will use bbduk, which is part of a suite of tools
that come with bbmap tool. You can run bbduk with the following
commands:

.. code:: bash

   bbduk.sh -Xmx12g ktrim=r ordered minlen=50 mink=11 tbo=t rcomp=f k=21 ow=t zl=4 \
           qtrim=rl trimq=20 \
           in1=SRR12610971_1.fastq.gz \
           in2=SRR12610971_2.fastq.gz \
           ref=~/databases/adapters/adapters.fa  \
           out1=SRR12610971_1.trimmed.fastq.gz \
           out2=SRR12610971_2.trimmed.fastq.gz

The ``-Xmx12g`` parameter I am providing here is to tell ``bbduk.sh``
that I want to use 12GB of my computer’s memory for this task. This
parameter may look a bit different from the one shown a few weeks ago.

It will take a few minutes to complete this task. Note that I am using
the “\\” to enter the command in multiple lines due to the long list of
parameters I need to specify with this tool. You can actually type the
whole thing in one line without having to type the “\\” but it is more
difficult to see all the options in one screen. There are several
parameters that I am entering here to tell the trimming tool what to do
exactly with the raw sequences. Detailed options/parameters available
with this tool can be seen when you type this:

.. code:: bash

    %%bash
    bbduk.sh -h


.. parsed-literal::

    
    Written by Brian Bushnell
    Last modified March 24, 2020
    
    Description:  Compares reads to the kmers in a reference dataset, optionally 
    allowing an edit distance. Splits the reads into two outputs - those that 
    match the reference, and those that don't. Can also trim (remove) the matching 
    parts of the reads rather than binning the reads.
    Please read bbmap/docs/guides/BBDukGuide.txt for more information.
    
    Usage:  bbduk.sh in=<input file> out=<output file> ref=<contaminant files>
    
    Input may be stdin or a fasta or fastq file, compressed or uncompressed.
    If you pipe via stdin/stdout, please include the file type; e.g. for gzipped 
    fasta input, set in=stdin.fa.gz
    
    Input parameters:
    in=<file>           Main input. in=stdin.fq will pipe from stdin.
    in2=<file>          Input for 2nd read of pairs in a different file.
    ref=<file,file>     Comma-delimited list of reference files.
                        In addition to filenames, you may also use the keywords:
                        adapters, artifacts, phix, lambda, pjet, mtst, kapa
    literal=<seq,seq>   Comma-delimited list of literal reference sequences.
    touppercase=f       (tuc) Change all bases upper-case.
    interleaved=auto    (int) t/f overrides interleaved autodetection.
    qin=auto            Input quality offset: 33 (Sanger), 64, or auto.
    reads=-1            If positive, quit after processing X reads or pairs.
    copyundefined=f     (cu) Process non-AGCT IUPAC reference bases by making all
                        possible unambiguous copies.  Intended for short motifs
                        or adapter barcodes, as time/memory use is exponential.
    samplerate=1        Set lower to only process a fraction of input reads.
    samref=<file>       Optional reference fasta for processing sam files.
    
    Output parameters:
    out=<file>          (outnonmatch) Write reads here that do not contain 
                        kmers matching the database.  'out=stdout.fq' will pipe 
                        to standard out.
    out2=<file>         (outnonmatch2) Use this to write 2nd read of pairs to a 
                        different file.
    outm=<file>         (outmatch) Write reads here that fail filters.  In default
                        kfilter mode, this means any read with a matching kmer.
                        In any mode, it also includes reads that fail filters such
                        as minlength, mingc, maxgc, entropy, etc.  In other words,
                        it includes all reads that do not go to 'out'.
    outm2=<file>        (outmatch2) Use this to write 2nd read of pairs to a 
                        different file.
    outs=<file>         (outsingle) Use this to write singleton reads whose mate 
                        was trimmed shorter than minlen.
    stats=<file>        Write statistics about which contamininants were detected.
    refstats=<file>     Write statistics on a per-reference-file basis.
    rpkm=<file>         Write RPKM for each reference sequence (for RNA-seq).
    dump=<file>         Dump kmer tables to a file, in fasta format.
    duk=<file>          Write statistics in duk's format. *DEPRECATED*
    nzo=t               Only write statistics about ref sequences with nonzero hits.
    overwrite=t         (ow) Grant permission to overwrite files.
    showspeed=t         (ss) 'f' suppresses display of processing speed.
    ziplevel=2          (zl) Compression level; 1 (min) through 9 (max).
    fastawrap=70        Length of lines in fasta output.
    qout=auto           Output quality offset: 33 (Sanger), 64, or auto.
    statscolumns=3      (cols) Number of columns for stats output, 3 or 5.
                        5 includes base counts.
    rename=f            Rename reads to indicate which sequences they matched.
    refnames=f          Use names of reference files rather than scaffold IDs.
    trd=f               Truncate read and ref names at the first whitespace.
    ordered=f           Set to true to output reads in same order as input.
    maxbasesout=-1      If positive, quit after writing approximately this many
                        bases to out (outu/outnonmatch).
    maxbasesoutm=-1     If positive, quit after writing approximately this many
                        bases to outm (outmatch).
    json=f              Print to screen in json format.
    
    Histogram output parameters:
    bhist=<file>        Base composition histogram by position.
    qhist=<file>        Quality histogram by position.
    qchist=<file>       Count of bases with each quality value.
    aqhist=<file>       Histogram of average read quality.
    bqhist=<file>       Quality histogram designed for box plots.
    lhist=<file>        Read length histogram.
    phist=<file>        Polymer length histogram.
    gchist=<file>       Read GC content histogram.
    enthist=<file>      Read entropy histogram.
    ihist=<file>        Insert size histogram, for paired reads in mapped sam.
    gcbins=100          Number gchist bins.  Set to 'auto' to use read length.
    maxhistlen=6000     Set an upper bound for histogram lengths; higher uses 
                        more memory.  The default is 6000 for some histograms
                        and 80000 for others.
    
    Histograms for mapped sam/bam files only:
    histbefore=t        Calculate histograms from reads before processing.
    ehist=<file>        Errors-per-read histogram.
    qahist=<file>       Quality accuracy histogram of error rates versus quality 
                        score.
    indelhist=<file>    Indel length histogram.
    mhist=<file>        Histogram of match, sub, del, and ins rates by position.
    idhist=<file>       Histogram of read count versus percent identity.
    idbins=100          Number idhist bins.  Set to 'auto' to use read length.
    varfile=<file>      Ignore substitution errors listed in this file when 
                        calculating error rates.  Can be generated with
                        CallVariants.
    vcf=<file>          Ignore substitution errors listed in this VCF file 
                        when calculating error rates.
    ignorevcfindels=t   Also ignore indels listed in the VCF.
    
    Processing parameters:
    k=27                Kmer length used for finding contaminants.  Contaminants 
                        shorter than k will not be found.  k must be at least 1.
    rcomp=t             Look for reverse-complements of kmers in addition to 
                        forward kmers.
    maskmiddle=t        (mm) Treat the middle base of a kmer as a wildcard, to 
                        increase sensitivity in the presence of errors.
    minkmerhits=1       (mkh) Reads need at least this many matching kmers 
                        to be considered as matching the reference.
    minkmerfraction=0.0 (mkf) A reads needs at least this fraction of its total
                        kmers to hit a ref, in order to be considered a match.
                        If this and minkmerhits are set, the greater is used.
    mincovfraction=0.0  (mcf) A reads needs at least this fraction of its total
                        bases to be covered by ref kmers to be considered a match.
                        If specified, mcf overrides mkh and mkf.
    hammingdistance=0   (hdist) Maximum Hamming distance for ref kmers (subs only).
                        Memory use is proportional to (3*K)^hdist.
    qhdist=0            Hamming distance for query kmers; impacts speed, not memory.
    editdistance=0      (edist) Maximum edit distance from ref kmers (subs 
                        and indels).  Memory use is proportional to (8*K)^edist.
    hammingdistance2=0  (hdist2) Sets hdist for short kmers, when using mink.
    qhdist2=0           Sets qhdist for short kmers, when using mink.
    editdistance2=0     (edist2) Sets edist for short kmers, when using mink.
    forbidn=f           (fn) Forbids matching of read kmers containing N.
                        By default, these will match a reference 'A' if 
                        hdist>0 or edist>0, to increase sensitivity.
    removeifeitherbad=t (rieb) Paired reads get sent to 'outmatch' if either is 
                        match (or either is trimmed shorter than minlen).  
                        Set to false to require both.
    trimfailures=f      Instead of discarding failed reads, trim them to 1bp.
                        This makes the statistics a bit odd.
    findbestmatch=f     (fbm) If multiple matches, associate read with sequence 
                        sharing most kmers.  Reduces speed.
    skipr1=f            Don't do kmer-based operations on read 1.
    skipr2=f            Don't do kmer-based operations on read 2.
    ecco=f              For overlapping paired reads only.  Performs error-
                        correction with BBMerge prior to kmer operations.
    recalibrate=f       (recal) Recalibrate quality scores.  Requires calibration
                        matrices generated by CalcTrueQuality.
    sam=<file,file>     If recalibration is desired, and matrices have not already
                        been generated, BBDuk will create them from the sam file.
    amino=f             Run in amino acid mode.  Some features have not been
                        tested, but kmer-matching works fine.  Maximum k is 12.
    
    Speed and Memory parameters:
    threads=auto        (t) Set number of threads to use; default is number of 
                        logical processors.
    prealloc=f          Preallocate memory in table.  Allows faster table loading 
                        and more efficient memory usage, for a large reference.
    monitor=f           Kill this process if it crashes.  monitor=600,0.01 would 
                        kill after 600 seconds under 1% usage.
    minrskip=1          (mns) Force minimal skip interval when indexing reference 
                        kmers.  1 means use all, 2 means use every other kmer, etc.
    maxrskip=1          (mxs) Restrict maximal skip interval when indexing 
                        reference kmers. Normally all are used for scaffolds<100kb, 
                        but with longer scaffolds, up to maxrskip-1 are skipped.
    rskip=              Set both minrskip and maxrskip to the same value.
                        If not set, rskip will vary based on sequence length.
    qskip=1             Skip query kmers to increase speed.  1 means use all.
    speed=0             Ignore this fraction of kmer space (0-15 out of 16) in both
                        reads and reference.  Increases speed and reduces memory.
    Note: Do not use more than one of 'speed', 'qskip', and 'rskip'.
    
    Trimming/Filtering/Masking parameters:
    Note - if ktrim, kmask, and ksplit are unset, the default behavior is kfilter.
    All kmer processing modes are mutually exclusive.
    Reads only get sent to 'outm' purely based on kmer matches in kfilter mode.
    
    ktrim=f             Trim reads to remove bases matching reference kmers.
                        Values: 
                           f (don't trim), 
                           r (trim to the right), 
                           l (trim to the left)
    kmask=              Replace bases matching ref kmers with another symbol.
                        Allows any non-whitespace character, and processes short
                        kmers on both ends if mink is set.  'kmask=lc' will
                        convert masked bases to lowercase.
    maskfullycovered=f  (mfc) Only mask bases that are fully covered by kmers.
    ksplit=f            For single-ended reads only.  Reads will be split into
                        pairs around the kmer.  If the kmer is at the end of the
                        read, it will be trimmed instead.  Singletons will go to
                        out, and pairs will go to outm.  Do not use ksplit with
                        other operations such as quality-trimming or filtering.
    mink=0              Look for shorter kmers at read tips down to this length, 
                        when k-trimming or masking.  0 means disabled.  Enabling
                        this will disable maskmiddle.
    qtrim=f             Trim read ends to remove bases with quality below trimq.
                        Performed AFTER looking for kmers.  Values: 
                           rl (trim both ends), 
                           f (neither end), 
                           r (right end only), 
                           l (left end only),
                           w (sliding window).
    trimq=6             Regions with average quality BELOW this will be trimmed,
                        if qtrim is set to something other than f.  Can be a 
                        floating-point number like 7.3.
    trimclip=f          Trim soft-clipped bases from sam files.
    minlength=10        (ml) Reads shorter than this after trimming will be 
                        discarded.  Pairs will be discarded if both are shorter.
    mlf=0               (minlengthfraction) Reads shorter than this fraction of 
                        original length after trimming will be discarded.
    maxlength=          Reads longer than this after trimming will be discarded.
    minavgquality=0     (maq) Reads with average quality (after trimming) below 
                        this will be discarded.
    maqb=0              If positive, calculate maq from this many initial bases.
    minbasequality=0    (mbq) Reads with any base below this quality (after 
                        trimming) will be discarded.
    maxns=-1            If non-negative, reads with more Ns than this 
                        (after trimming) will be discarded.
    mcb=0               (minconsecutivebases) Discard reads without at least 
                        this many consecutive called bases.
    ottm=f              (outputtrimmedtomatch) Output reads trimmed to shorter 
                        than minlength to outm rather than discarding.
    tp=0                (trimpad) Trim this much extra around matching kmers.
    tbo=f               (trimbyoverlap) Trim adapters based on where paired 
                        reads overlap.
    strictoverlap=t     Adjust sensitivity for trimbyoverlap mode.
    minoverlap=14       Require this many bases of overlap for detection.
    mininsert=40        Require insert size of at least this for overlap.
                        Should be reduced to 16 for small RNA sequencing.
    tpe=f               (trimpairsevenly) When kmer right-trimming, trim both 
                        reads to the minimum length of either.
    forcetrimleft=0     (ftl) If positive, trim bases to the left of this position
                        (exclusive, 0-based).
    forcetrimright=0    (ftr) If positive, trim bases to the right of this position
                        (exclusive, 0-based).
    forcetrimright2=0   (ftr2) If positive, trim this many bases on the right end.
    forcetrimmod=0      (ftm) If positive, right-trim length to be equal to zero,
                        modulo this number.
    restrictleft=0      If positive, only look for kmer matches in the 
                        leftmost X bases.
    restrictright=0     If positive, only look for kmer matches in the 
                        rightmost X bases.
    mingc=0             Discard reads with GC content below this.
    maxgc=1             Discard reads with GC content above this.
    gcpairs=t           Use average GC of paired reads.
                        Also affects gchist.
    tossjunk=f          Discard reads with invalid characters as bases.
    swift=f             Trim Swift sequences: Trailing C/T/N R1, leading G/A/N R2.
    
    Header-parsing parameters - these require Illumina headers:
    chastityfilter=f    (cf) Discard reads with id containing ' 1:Y:' or ' 2:Y:'.
    barcodefilter=f     Remove reads with unexpected barcodes if barcodes is set,
                        or barcodes containing 'N' otherwise.  A barcode must be
                        the last part of the read header.  Values:
                           t:     Remove reads with bad barcodes.
                           f:     Ignore barcodes.
                           crash: Crash upon encountering bad barcodes.
    barcodes=           Comma-delimited list of barcodes or files of barcodes.
    xmin=-1             If positive, discard reads with a lesser X coordinate.
    ymin=-1             If positive, discard reads with a lesser Y coordinate.
    xmax=-1             If positive, discard reads with a greater X coordinate.
    ymax=-1             If positive, discard reads with a greater Y coordinate.
    
    Polymer trimming:
    trimpolya=0         If greater than 0, trim poly-A or poly-T tails of
                        at least this length on either end of reads.
    trimpolygleft=0     If greater than 0, trim poly-G prefixes of at least this
                        length on the left end of reads.  Does not trim poly-C.
    trimpolygright=0    If greater than 0, trim poly-G tails of at least this 
                        length on the right end of reads.  Does not trim poly-C.
    trimpolyg=0         This sets both left and right at once.
    filterpolyg=0       If greater than 0, remove reads with a poly-G prefix of
                        at least this length (on the left).
    Note: there are also equivalent poly-C flags.
    
    Polymer tracking:
    pratio=base,base    'pratio=G,C' will print the ratio of G to C polymers.
    plen=20             Length of homopolymers to count.
    
    Entropy/Complexity parameters:
    entropy=-1          Set between 0 and 1 to filter reads with entropy below
                        that value.  Higher is more stringent.
    entropywindow=50    Calculate entropy using a sliding window of this length.
    entropyk=5          Calculate entropy using kmers of this length.
    minbasefrequency=0  Discard reads with a minimum base frequency below this.
    entropytrim=f       Values:
                           f:  (false) Do not entropy-trim.
                           r:  (right) Trim low entropy on the right end only.
                           l:  (left) Trim low entropy on the left end only.
                           rl: (both) Trim low entropy on both ends.
    entropymask=f       Values:
                           f:  (filter) Discard low-entropy sequences.
                           t:  (true) Mask low-entropy parts of sequences with N.
                           lc: Change low-entropy parts of sequences to lowercase.
    entropymark=f       Mark each base with its entropy value.  This is on a scale
                        of 0-41 and is reported as quality scores, so the output
                        should be fastq or fasta+qual.
    NOTE: If set, entropytrim overrides entropymask.
    
    Cardinality estimation:
    cardinality=f       (loglog) Count unique kmers using the LogLog algorithm.
    cardinalityout=f    (loglogout) Count unique kmers in output reads.
    loglogk=31          Use this kmer length for counting.
    loglogbuckets=2048  Use this many buckets for counting.
    khist=<file>        Kmer frequency histogram; plots number of kmers versus
                        kmer depth.  This is approximate.
    khistout=<file>     Kmer frequency histogram for output reads.
    
    Java Parameters:
    
    -Xmx                This will set Java's memory usage, overriding autodetection.
                        -Xmx20g will 
                        specify 20 gigs of RAM, and -Xmx200m will specify 200 megs.  
                        The max is typically 85% of physical memory.
    -eoom               This flag will cause the process to exit if an 
                        out-of-memory exception occurs.  Requires Java 8u92+.
    -da                 Disable assertions.
    
    Please contact Brian Bushnell at bbushnell@lbl.gov if you encounter any problems.
    


As you can see, there are several options and what each of these options
does when you select a certain one. In some cases, you can specify only
one option but not together with another one.

Run fastqc on quality-trimmed sequences to compare its quality with untrimmed sequences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that you have done trimming the raw sequences, you will then check
what the quality looks like. Run fastqc again on trimmed sequences by
typing ``fastqc *.trimmed.fastq.gz`` in the folder where the trimmed
files are located. You should inspect the quality reports produced by
fastqc to make sure it did what you intended it to do.

You can now use the trimmed fastq files as input to run SPAdes.

Running the assembly on your laptop or home computer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SPAdes can be run on your home desktop or a laptop computer with a given
example dataset provided. It will take a while to complete but it will
get done. To run, type the following commands (shown as an example):

.. code:: bash

   spades.py \
       -t 4 \
       --pe1-1 data/SRR12610971_1.trimmed.fastq.gz \
       --pe1-2 data/SRR12610971_2.trimmed.fastq.gz \
       -k 21,33,55,77 \
       -o spades_assembly

This example is one of the simplest examples to run a genome assembly
using this particular assembler. Again, this tool also has a number of
options/parameters that you can specify, depending on the type of data
you have, the size of the data, etc. In this example, ``-t 4`` means I
am using 4 cpus to run this tool. If you have more cpu cores on your
computer, you can specify a larger number. However, with larger datasets
(such as metagenomic data), you will require not only more cpus but also
larger amount of memory. For this, you will require the use of a
high-performance computaional (HPC) clusters that will have larger
memory and cpu cores.

The ``-k 21,33,55,77`` means that I am using 4 different k-mers (read
the original SPAdes paper) to run this assembly. You can specify more
k-mers but this may cause the assembler to run longer and may not
necessarily lead to improved assemblies. This is more of an optimization
problem. By design, k-mers need to be odd numbers.

The ``-o spades_assembly`` parameter tells the program to put output
files into a new directory named ‘spades_assembly’. To see more options,
type:

``spades.py -h``

This particular data set run on my iMac with 4 cpus took less than 1
hour to complete. Let it run until it finishes. Next task for you would
be to check the assembly quality after it is done.

Running the assembly on a cluster at GW
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While the previous example of SPAdes assembly using *Salmonella entrica*
sequences you have downloaded from NCBI can be done on your laptop,
larger datasets such as metagenomes you have downloaded during the 2nd
week of the class are too big to be assembled on your laptop. They will
need to be run on much more powerful computers such as high-performance
computational (HPC) clusters we have at GW.

We will be connceting to a remote HPC cluster known as ``cerberus`` next
week to perform genome or metagenome assemblies of larger datasets.

Checking the quality of assemblies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next thing to do after running these assemblies is to assess how well
the assembly was and some other basic metrics related to the assembly.
Remember, you started with millions of individual DNA fragments which
are only a few hundred bases long and the assembler has magically put
together these highly complicated puzzle pieces into a more complete
picture, i.e., a draft genome assembly. This assembly is not complete by
any means. In fact, most microbial genomes sequenced with only Illumina
reads will not give you a complete genome after you run an assembly
using SPAdes.

So you are still missing a lot of pieces and thus the assemblies will
yield incomplete but partially assembled DNA fragments that are known as
“**contigs**”. They range in size from only a few hundred to hundreds of
thousands of bases. You wouldn’t normally inspect them by using Word
processor to count these bases. There are tools specifically designed
for you to inspect these metrics, thankfully. One of these tools is
known as “**Quast**”” and it happens to be the tool written by the same
authors as SPAdes. You will install Quast using ``conda``.

.. code:: bash

   conda search quast
   conda install quast

Before running Quast on your assemblies, you need to first inspect what
SPAdes produced after the assembly. Let’s check it out.

.. code:: bash

    %%bash
    cd /Volumes/BackupWork/teaching/BISC4234_6234/spades_assembly
    ls


.. parsed-literal::

    K21
    K33
    K55
    K77
    assembly_graph.fastg
    assembly_graph_with_scaffolds.gfa
    before_rr.fasta
    contigs.fasta
    contigs.paths
    corrected
    dataset.info
    input_dataset.yaml
    misc
    params.txt
    scaffolds.fasta
    scaffolds.paths
    spades.log
    tmp


Now, that’s a lot of files and folders. Where do you begin? What is the
most important thing for you to inspect? The only files you would need
after the assembly are ``contigs.fasta`` and ``scaffolds.fasta`` files.
``contigs.fasta`` contains contigs (incomplete DNA fragments of the
genome) of *Salmonella enterica* you just assembled. What about
``scaffolds.fasta`` file? It is basically similar to ``contigs.fasta``
file but it has scaffolding information. For example, if the SPAdes
assembler has determined that two or more contigs should be physically
linked due to pairing information from original reads, then it will put
them together but with “N” characters to indicate that there are missing
pieces that should be filled.

I normally work with contig files instead of scaffold files for a number
of reasons. We will get to that when we start working on genome
annotation. For now, let’s use Quast to inspect the assembly metrics for
the contigs. You need to first be in the folder containing the SPAdes
assembly. Then type:

.. code:: bash

   quast.py contigs.fasta -o quast_contigs

This will run Quast on the contigs file and it will produce a folder
``quast_contigs`` which contains the assembly metrics. Now, let’s see
what Quast found.

.. code:: bash

    %%bash
    cd /Volumes/BackupWork/teaching/BISC4234_6234/spades_assembly
    cat quast_contigs/report.txt


.. parsed-literal::

    All statistics are based on contigs of size >= 500 bp, unless otherwise noted (e.g., "# contigs (>= 0 bp)" and "Total length (>= 0 bp)" include all contigs).
    
    Assembly                    contigs
    # contigs (>= 0 bp)         135    
    # contigs (>= 1000 bp)      67     
    # contigs (>= 5000 bp)      53     
    # contigs (>= 10000 bp)     51     
    # contigs (>= 25000 bp)     43     
    # contigs (>= 50000 bp)     32     
    Total length (>= 0 bp)      5097086
    Total length (>= 1000 bp)   5075927
    Total length (>= 5000 bp)   5039163
    Total length (>= 10000 bp)  5024899
    Total length (>= 25000 bp)  4900465
    Total length (>= 50000 bp)  4481295
    # contigs                   77     
    Largest contig              282699 
    Total length                5082069
    GC (%)                      52.08  
    N50                         170524 
    N75                         94555  
    L50                         12     
    L75                         24     
    # N's per 100 kbp           0.00   


It found 135 contigs in the assembly and the total size of the assembly
is about 5 Mbp, which is roughly the genome size of *Salmonella
enterica*. The largest contig is more than 280 Kbp long! And G+C% of the
geome is about 52%. N50 is another metric that is quite important to
assess how well the assembly went. That is the number at which 50% of
the assembly size is accounted for by contigs that are longer than
170,524 bases. In this example, 12 contigs can account for 50% of the
genome, which is great because fewer contigs mean it’s closer to
finishing the puzzle to obtain the complete genome. Quast also produces
some plots of these metrics in PDF format and an html page containing
visualization of the contigs. You can open ``icarus.html`` file using
your web brower to inspect these plots, which are interactive.

Test trimming parameters and run another SPAdes assembly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A lot of microbial genome assemblies and the qualities are impacted by
how well (either aggressively or less aggressively) you trim the
original raw sequence reads. Now, go back to the step where you used
``bbduk.sh`` command to trim these reads. Change one or two parameters
to see if you can trim more aggressively (eg: increasing ``qtrim`` to a
higher number, for example) and see if your SPAdes assembly improves or
got worse. Make sure to name the assembly differently so that you are
not overwriting the previous assembly or the SPAdes assembler won’t
proceed due to previous assembly folder being present. The parameter you
need to change is ``-o``.

Cluster login info
~~~~~~~~~~~~~~~~~~

For next week, we will be connecting to the HPC cluster known as
``cerberus`` and I have put some useful information to prepare you for
next week’s exercises.

An example command to login to this remote computer is shown below.

.. code:: bash

   ssh jsaw@cerberus.colonialone.gwu.edu

However, before you can connect to this computer, I will need to provide
the system administrator with your email information so that he can give
you permission to connect to this computer. Therefore, you will need to
let me know the email address you are using for your GW user id (the
same as the login name used for your email account).

This remote computer has the following specifications:

-  28 CPU cores
-  128 GB RAM
