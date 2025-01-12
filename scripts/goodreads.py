import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv("/Users/emrecanciftci/betik/2024_bio/data/goodreads_data.csv")
df = df.iloc[:, [1,2,7,8,11,12,13,14,15,18]]

df.rename(columns = {'Exclusive Shelf':"Bookshelf"}, inplace=True)

# %%
df.info()

# %%
sns.histplot(df["My Rating"][df["My Rating"] != 0])
plt.xlabel("Değerlendrime")