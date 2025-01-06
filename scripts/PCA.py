# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% import the dataset
iris = sns.load_dataset("iris")

# %% Standardize
X = iris.iloc[:,0:4]
Y = iris.iloc[:,4]
x_mean = X.mean()

iris_std = (X - X.mean())/X.std()
iris_std = pd.concat([iris_std,Y], axis=1)

# %% Obtain the Eigenvectors and Eigenvalues
x_std = iris_std.iloc[:,:4].values # features
y = iris_std.iloc[:,4].values # labels

cor_mat = np.corrcoef(x_std.T)
eig_vals, eig_vecs = np.linalg.eig(cor_mat)

# %% eigenvalue and eigenvector pairs
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
eig_pairs.sort()
eig_pairs.reverse()

print("Eigenvalues and eignevector pairs in descending order:")
for i in eig_pairs:
    print(i)

# %% visualise
tot = sum(eig_vals)
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
PC = ["PC1", "PC2", "PC3", "PC4"]
plot = ax.bar(PC,var_exp)
ax.plot(cum_var_exp,"r*-")

def autolabel(plot):
    """Text label above each bar in *rects*, displaying its height."""
    for rect in plot:
        height = rect.get_height()
        ax.annotate("{}".format(round(height,2)),
        xy=(rect.get_x() + rect.get_width() / 2, height),
        xytext=(0, 3), # 3 points vertical offset
        textcoords= "offset points",
        ha="center", va="bottom")
        plt.ylabel("Preserved Variation")
autolabel(plot)
plt.show()

# %% create the transformation matrix
matrix_w = np.hstack(((eig_pairs[0][1].reshape(4,1),eig_pairs[1][1].reshape(4,1))))
print("Matrix W:\n", matrix_w)

# %% transform the original dataset or projection
features= iris.iloc[:,0:4].values
iris_transform = features.dot(matrix_w)
iris_transform = pd.DataFrame(iris_transform,columns = ["PC1","PC2"])
iris_transform = pd.concat([iris_transform,Y],axis=1)
iris_transform.head()

# %% visualise the whole dataset in 2-D
sns.set_style("whitegrid")
sns.scatterplot(x = "PC1",y = "PC2",data = iris_transform,hue = "species",s = 60)