import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from scipy import stats

# %% Get the data
path1 = "/Users/emrecanciftci/betik/2024_bio_data_science/large_data/07_Ch7/Supplementary files/expression_data.csv"
path2 = "/Users/emrecanciftci/betik/2024_bio_data_science/large_data/07_Ch7/Supplementary files/annotation_file.csv"
df_expression = pd.read_csv(path1)
df_annotation = pd.read_csv(path2)

# %% log2 scale
log_expression = np.log2(df_expression.iloc[:,1:])

# %% Plot
# for i in df_expression.columns[1:]:
#     sns.kdeplot(log_expression[i], label=i)
#     plt.xlabel("expression log2")
#     plt.ylabel("frequency")

# %% Boxplot
# fig, axes = plt.subplots(figsize=(12,8))
# ax = sns.boxplot(log_expression.iloc[:,1:])

# %% Normalization
X_expression = log_expression.iloc[:,1:]
std_expression = (X_expression - X_expression.mean()) / X_expression.std()

# %% Normalization
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
log_norm_expression = np.log2(Norm_samples)

# %% transpose and standardization
expression_transpose = log_norm_expression.T
expression_transpose_std = (expression_transpose - expression_transpose.mean())/expression_transpose.std()

expression_transpose_std = expression_transpose_std.replace([np.inf, -np.inf], np.nan)
expression_transpose_std = expression_transpose_std.dropna(axis=1)

# %% PCA
sklearn_pca = PCA(n_components=2)
print(expression_transpose_std.shape)
PCs = sklearn_pca.fit_transform(expression_transpose)
print(PCs.shape)
print(sklearn_pca.explained_variance_ratio_) # 0.20351873 0.18757078

# %%
expression_PCs = pd.DataFrame(PCs,columns=["PC1","PC2"])
expression_PC1 = expression_PCs.set_index(
np.array((["Control"]*4)+["Treated"]*4))
expression_PC2 = expression_PCs.set_index(expression_transpose.index)

# fig, axes = plt.subplots(figsize=(10,8))
# sns.set_style("whitegrid")
# sns.scatterplot(x="PC1",y="PC2",data = expression_PC2, hue =expression_PC1.index, s=200)

# %% t-test 
control_mean = log_norm_expression.iloc[:,4:].mean(axis=1)
treated_mean = log_norm_expression.iloc[:,:4].mean(axis=1)
compare_means = pd.DataFrame(columns=["Control_Mean","Treated_Mean"])
compare_means.Control_Mean = control_mean
compare_means.Treated_Mean = treated_mean
compare_means["log2_fold_change"] = (compare_means.Control_Mean - compare_means.Treated_Mean)

t_test_values = pd.DataFrame(stats.ttest_ind(log_norm_expression.iloc[:,4:], log_norm_expression.iloc[:,:4], axis=1)).T
t_test_values.columns = ["Statistics", "p-Value"]

compare_means = pd.concat([df_expression.iloc[:,0], compare_means, t_test_values], axis = 1)

# %% merge with annotations
merged_table = pd.merge(df_annotation, compare_means, on="ID_REF")

significant_table = merged_table[merged_table["p-Value"] <= 0.05]

Upregulated_genes = significant_table[significant_table["log2_fold_change"] > 1.5]
Downregulated_genes = significant_table[significant_table["log2_fold_change"] < -1.5]
DEGs = pd.concat([Upregulated_genes,Downregulated_genes])

# %% Cluster Map
log_expression = pd.concat([df_expression.iloc[:,0], log_expression], axis=1)
table  = pd.merge(DEGs.iloc[:,:3], log_expression, on="ID_REF")

index = table.iloc[:,1]
table.set_index(index)
table = table.iloc[:,3:].set_index(index)

sns.clustermap(table, cmap="coolwarm")

# %% Gene Enrichment Analysis (GEA
import gseapy as gp

GB_ACC = pd.merge(DEGs.iloc[:,:3], log_expression, on="ID_REF").iloc[:,1]

enr = gp.enrichr(
    gene_list= GB_ACC.tolist(),
    gene_sets=["GO_Biological_Process_2017b"],
    description="test_name",
    outdir="test/enrichr_kegg",
    cutoff= 0.5 # test dataset, use lower value from range(0,1))
)

enr.results[["Gene_set","Term","Overlap","P-value","Genes"]]


