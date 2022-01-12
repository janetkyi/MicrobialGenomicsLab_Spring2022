#!/usr/bin/env python

import sys
from Bio import SeqIO

records = list(SeqIO.parse(sys.argv[1], "genbank"))

for r in records:
    print(r.description)
