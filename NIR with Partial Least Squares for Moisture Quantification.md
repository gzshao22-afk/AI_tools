
* Example Scenario: NIR Analysis of powder samples from different processes
* Data source: 60 powder sample
* Predictors (X): NIR spectra at 88 wavelengths per sample
* Response (Y): Moisture content
* Goal: Build a PLS model using 48 samples to predict and the remaining 12 to validate

Example code:
```python
import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 1. Simulate NIR Data (X: 60 samples, 88 wavelengths) and Responses (Y: 60 samples, 2 components: Moisture, Fat)
# In a real scenario, you would load data here (e.g., pd.read_csv)
np.random.seed(42)
X = np.random.rand(60, 88)  # Simulated NIR Spectra
y = np.random.rand(60, 2)   # Simulated Moisture and Fat values

# 2. Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Build PLS Model
# Determining the optimal number of components (e.g., using cross-validation) is crucial
n_components = 5
pls = PLSRegression(n_components=n_components)
pls.fit(X_train, y_train)

# 4. Predict and Evaluate
y_pred = pls.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.4f}")
print(f"R^2 Score: {r2:.4f}")

# 5. Plotting Predicted vs Actual
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('PLS Regression: Actual vs Predicted')
plt.show()
```

## Follow-up question:
How to automatically find the optimal hyper-parameters? In this case, it will be n_components

#grid_search #BO_optimize

Example code
```python
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
import numpy as np

# Load data and split into training and testing sets
iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5, random_state=0)

# Define the parameter grid to search
param_grid = [
    {'kernel': ['rbf'], 'C': [1, 10, 100, 1000], 'gamma': [1e-3, 1e-4]},
    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}
]
# This defines two separate grids to explore.

# Create a base model
svc = SVC()

# Create the GridSearchCV object
grid_search = GridSearchCV(estimator=svc, param_grid=param_grid, cv=5, scoring='accuracy')

# Fit the GridSearchCV object
grid_search.fit(X_train, y_train)

# View the results
print("Best parameters found:", grid_search.best_params_)
print("Best cross-validation score:", grid_search.best_score_)

# Evaluate the best model on the held-out test data
# GridSearchCV automatically refits the best model by default (refit=True)
best_model = grid_search.best_estimator_
test_score = best_model.score(X_test, y_test)
print("Test set score of the best model:", test_score)
```

What about #pipeline ?
