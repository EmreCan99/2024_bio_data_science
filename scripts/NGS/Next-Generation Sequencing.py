# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from Bio import Entrez, SeqIO
from Bio import Medline

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

# %% 
rec = None

for i in recs:
    if i.name == 'KM288867':
        rec = i
        break
print(rec.name)
print(rec.description)

for feature in rec.features:
    if feature.type == 'gene':
        print(feature.qualifiers['gene'])
    elif feature.type == 'exon':
        loc = feature.location
        print('Exon', loc.start, loc.end, loc.strand)
    else:
        print('not processed:\n%s' % feature)

# %%
for name, value in rec.annotations.items():
    print(name, " : ", value)

# %%
print(len(rec.seq))

# %%
refs = rec.annotations["references"]

for ref in refs:
    if ref.pubmed_id != '':
        print(ref.pubmed_id)
        handle = Entrez.efetch(db="pubmed", id = [ref.pubmed_id], rettype="medline", retmode="text")
        records = Medline.parse(handle)
        for med_rec in records:
            for k, v in med_rec.items():
                print(k, " : ", v)
