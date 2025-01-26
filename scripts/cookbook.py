# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% vdata import 
vdata = pd.read_csv("/Users/emrecanciftci/betik/2024_bio/large_data/2021VAERSData/2021VAERSDATA.csv.gz", encoding="iso-8859-1")

# %% inspect the size of each column

for name in vdata.columns:
    col_bytes = vdata[name].memory_usage(index=False, deep=True)
    col_type = vdata[name].dtype
    print(name, col_bytes // (1024 ** 2),"Mb", col_type)

# %% 
vdata.DIED.memory_usage(index=False, deep=True)
vdata.DIED.fillna(False).astype(bool).memory_usage(index=False, deep=True)

# %% vax import and set index
vax = pd.read_csv("2021VAERSData/2021VAERSVAX.csv.gz", encoding="iso-8859-1").set_index("VAERS_ID")
vax.groupby("VAX_TYPE").size().sort_values()
vax19 = vax[vax.VAX_TYPE == "COVID19"]

# %% dead - vax19 join
vdata.DIED.value_counts(dropna=False)
vdata["is_dead"] = (vdata.DIED == True)
dead = vdata[vdata["is_dead"]]
vax19_dead = dead.join(vax19)

# %%

v = vax19_dead.STATE.head()

print(v)
print("\n-------\n")