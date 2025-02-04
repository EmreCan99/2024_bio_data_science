# %%
import pandas as pd
from Bio import Entrez, SeqIO, SeqRecord


# %% Retrive IDs From NCBI Entrez
Entrez.email = "emrecanciftci99@gmail.com"

hdl = Entrez.efetch(db="nucleotide", id= ['NM_002299'], rettype=  "gb", retmode= "text")

# %%
gb_rec = SeqIO.read(hdl, "gb")

# %%
for feature in gb_rec.features:
    if feature.type == "CDS":
        location = feature.location

cds = SeqRecord.SeqRecord(gb_rec.seq[location.start:location.end], "NM_002299", description='LCT CDS only')

# %% write as fasta
w_hdl= open("example.fasta", "w")
SeqIO.write(cds, w_hdl, format="fasta")
w_hdl.close()

# %% read the fasta file 
seq_read = SeqIO.parse("example.fasta", "fasta")

for rec in seq_read:
    seq = rec.seq
    print(rec.seq)
    print(rec.seq[:10])
    print(rec.description)

# %% transcribe

rna = seq.transcribe()
print(rna)
prot = seq.translate()
print(prot)