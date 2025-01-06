# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% vdata import and set index
vdata = pd.read_csv("2021VAERSData/2021VAERSDATA.csv.gz", encoding="iso-8859-1")
vdata = vdata.set_index("VAERS_ID")

# %% vax import and set index
vax = pd.read_csv("2021VAERSData/2021VAERSVAX.csv.gz", encoding="iso-8859-1").set_index("VAERS_ID")
vax.groupby("VAX_TYPE").size().sort_values()
vax19 = vax[vax.VAX_TYPE == "COVID19"]

# %% dead - vax19 join
vdata.DIED.value_counts(dropna=False)
vdata["is_dead"] = (vdata.DIED == "Y")
dead = vdata[vdata["is_dead"]]
vax19_dead = dead.join(vax19)

# %%

v = vax19_dead.STATE.head()

print(v)
print("\n-------\n")