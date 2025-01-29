# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report

# %%
df = pd.read_csv("/Users/emrecanciftci/betik/2024_bio/data/11_Ch11/Supplementary files/heart.csv")
df.info()

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

# %%
X_train, X_test, y_train, y_test = train_test_split(X ,y, test_size= 0.30, random_state= 110)

# %% Run the SVC
classifier = SVC()
classifier.fit(X_train, y_train)

pred = classifier.predict(X_test)

# %%
print(confusion_matrix(y_test, pred))
print("----")
print(classification_report(y_test, pred))

# ------------------------------------
# %% Grid Search

param_grid = {"C": [1,10,100,10000], "gamma": [1,0.1,0.01,0.001,0.0001], "kernel": ["rbf"]}
grid = GridSearchCV(SVC(), param_grid)

grid.fit(X_train,y_train)
grid.best_params_

# %%
grid_pred = grid.predict(X_test)

print(confusion_matrix(y_test, grid_pred))
print("----")
print(classification_report(y_test, grid_pred))

# ------------------------------------
# %% an example
