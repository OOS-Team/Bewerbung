# Importiere das pandas-Modul und lese eine CSV-Datei
import pandas as pd
df = pd.read_csv("./data/diamonds.csv")

# Zeige die ersten 5 Zeilen des Datensatzes an
df.head()

# Extraktion der Merkmale (carat) und Zielvariable (price)
X = df[["carat"]].values
y = df[["price"]].values

# Teilung des Datensatzes in Trainings- und Testdaten (75% / 25%)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0, train_size = 0.75)

# Fitting eines linearen Regressionsmodells auf die Trainingsdaten
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

# Berechne die Vorhersagegenauigkeit des Modells auf den Testdaten
print(model.score(X_test, y_test))

# Extraktion der Merkmale (x, y, z)
X = df[['x', 'y', 'z']].values
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0, train_size = 0.75)

# Fitting eines linearen Regressionsmodells auf die Trainingsdaten
model = LinearRegression()
model.fit(X_train, y_train)

# Berechne die Vorhersagegenauigkeit des Modells auf den Testdaten
print(model.score(X_test, y_test))

# Transformation der Merkmale mittels PolynomialFeatures mit Grad 2
from sklearn.preprocessing import PolynomialFeatures
pf = PolynomialFeatures(degree=2, include_bias= False)
pf.fit(X_train)
X_train_trans = pf.transform(X_train)
X_test_trans = pf.transform(X_test)

# Fitting eines linearen Regressionsmodells auf die transformierten Trainingsdaten
model = LinearRegression()
model.fit(X_train_trans, y_train)

# Berechne die Vorhersagegenauigkeit des Modells auf den transformierten Testdaten
print(model.score(X_test_trans, y_test))

