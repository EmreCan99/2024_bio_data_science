# %%
import pandas as pd
from Bio import Entrez, SeqIO, SeqRecord
import matplotlib.pyplot as plt
import seaborn as sns
import gzip
from collections import defaultdict

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

# -------------------
# %% Working with FASTQ
file = "/Users/emrecanciftci/betik/2024_bio/large_data/SRR003265.filt.fastq.gz"
recs = SeqIO.parse(gzip.open(file,"rt",encoding="utf-8"), format="fastq")

rec = next(recs)
print(rec.seq)
print(rec.description)

# %% Count the frequency of the bases
cnt = defaultdict(int)

for rec in recs:
    for letter in rec.seq:
        cnt[letter] += 1

tot = sum(cnt.values())

for letter, count in cnt.items():
    print(letter, ": ", (count*100/tot), " ", count)

# G :  20.676842412896093   5359329
# A :  28.59598043556052   7411928
# T :  29.5796307602681   7666885
# C :  21.003681594631065   5444044
# N :  0.14386479664422216   37289

# %% Check the N calls 
n_cnt = defaultdict(int)

for rec in recs:

    for i, letter in enumerate(rec.seq):
        loc = i + 1

        if letter == "N":
            n_cnt[loc] += 1

for a, b in n_cnt.items():
    print(a, " : ", b)

# %%
seq_len = max(n_cnt.keys())
positions = range(1, seq_len + 1)

# %%
fig , ax = plt.subplots(figsize=(16, 9))
ax.plot(positions, [n_cnt[x] for x in positions])
fig.suptitle('Number of N calls as a function of the    distance from the start of the sequencer read')
ax.set_xlim(1, seq_len)
ax.set_xlabel('Read distance')
ax.set_ylabel('Number of N Calls')

# %% Study the distribution of Phred scores

