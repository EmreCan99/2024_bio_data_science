# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from Bio import Entrez, SeqIO

# %% Retrive IDs From NCBI Entrez
Entrez.email = "emrecanciftci99@gmail.com"

handle = Entrez.esearch(db="nucleotide", term= 'CRT[Gene Name] AND "Plasmodium falciparum"[Organism]')
rec_list = Entrez.read(handle)

if int(rec_list['RetMax']) < int(rec_list['Count']): 
    handle = Entrez.esearch(db='nucleotide', 
                            term='CRT[Gene Name] AND "Plasmodium falciparum"[Organism]', 
                            retmax=rec_list['Count'])
    rec_list = Entrez.read(handle)

# %% Retrive properly
id_list = rec_list["IdList"]
hdl = Entrez.efetch(db = "nucleotide", id=id_list, rettype="gb")

# %% 
recs = list(SeqIO.parse(hdl,"gb"))

# %% These for loops should be separeted
selected_recs = []
for rec in recs:
    if rec.name == "KM288867":
        break 
    # print(rec.name)
    # print(rec.description)
    selected_recs.append(rec)

for rec in selected_recs:
    for feature in rec.features:
        if feature.type == 'gene':
            print(feature.qualifiers['gene'])
        elif feature.type == 'exon':
                loc = feature.location
                print(loc.start, loc.end, loc.strand)
        # else: 
            # print('not processed:\n%s' % feature)
