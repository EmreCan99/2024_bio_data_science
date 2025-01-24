# %%
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


# %%
path = Path(__file__).parents[1] / "data/10_Ch10/Supplementary files/heart.csv"

df = pd.read_csv(path)
df.info()

# %%
X = df.iloc[:,:-1]
y = df.iloc[:,-1]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

# %%
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
confusion_matrix(y_test, y_pred)
# ([[31,  9],
#   [ 8, 43]])
print(classification_report(y_test, y_pred)) # accuracy 0.81

# %% Random Forests

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=200)
classifier.fit(X_train, y_train)
rfc_pred = classifier.predict(X_test)
print(confusion_matrix(y_test,rfc_pred))
print(classification_report(y_test,rfc_pred))

# %% Predicting Prognosis of Diabetes Using Random Forest
path = Path(__file__).parents[1] / "data/11_Ch11/Supplementary files/diabetes.csv"
df = pd.read_csv(path)
df.info()

# %%
X = df.iloc[:,1:-1]
y = df.iloc[:,-1]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25,random_state = 0)

# %%
classifier = RandomForestClassifier(n_estimators=10)
classifier.fit(X_train, y_train)

rfc_pred = classifier.predict(X_test)
print(classification_report(y_test, rfc_pred))

# %% Cross-Validation
from sklearn.model_selection import cross_validate

classifier = RandomForestClassifier(n_estimators=10)
cross_validator = cross_validate(classifier, X, y, cv=5, return_estimator=True, scoring="accuracy")

# %%
print(cross_validator["estimator"][1])
print(cross_validator["test_score"].argmax())