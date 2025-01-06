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

# %% 

