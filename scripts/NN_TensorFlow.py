# %%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# %%
df = pd.read_csv("/Users/emrecanciftci/betik/2024_bio/data/11_Ch11/Supplementary files/heart.csv")

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

# %% Data scaling

scaler = StandardScaler()
X_norm = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.25, random_state=0)

# %%
tf.__version__

# %% Model – As a List of Layers (1of the 2 ways)

model = Sequential(
    Dense(units=2)
    Dense(units=2)
    Dense(units=1)
)

# Jupiter Notebook'tan devam ettim 