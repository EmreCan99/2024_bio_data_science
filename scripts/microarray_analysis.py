import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# %% Get the data
path1 = "/Users/emrecanciftci/betik/2024_bio_data_science/large_data/07_Ch7/Supplementary files/expression_data.csv"
path2 = "/Users/emrecanciftci/betik/2024_bio_data_science/large_data/07_Ch7/Supplementary files/annotation_file.csv"
df_expression = pd.read_csv(path1)
df_annotation = pd.read_csv(path2)

# %% log2 scale
log_expression = np.log2(df_expression.iloc[:,1:])

# %% Plot
for i in df_expression.columns[1:]:
    sns.kdeplot(log_expression[i], label=i)
    plt.xlabel("expression log2")
    plt.ylabel("frequency")

# %% Boxplot
fig, axes = plt.subplots(figsize=(12,8))
ax = sns.boxplot(log_expression.iloc[:,1:])

# %% Normalization
X_expression = log_expression.iloc[:,1:]
std_expression = (X_expression - X_expression.mean()) / X_expression.std()

print(std_expression.describe())

# %%
def quantileNormalize(input):
    temp = input.copy()
    #compute rank
    dic = {}
    for col in input:
        dic.update({col : sorted(temp[col])})
    sorted_df = pd.DataFrame(dic)
    rank = sorted_df.mean(axis = 1).tolist()
    #sort
    for col in temp:
        t = np.searchsorted(np.sort(temp[col]), temp[col])
        temp[col] = [rank[i] for i in t]
    return temp

Norm_samples = quantileNormalize(df_expression.iloc[:,1:])

Norm_samples


# %%
