1. The Original Matrix is 
	$\begin{bmatrix}3 & 2 & 2 \\ 2 & 3 & -2 \end{bmatrix}$

2. $A*A^T$ gives 
	$A*A^T$ = $\begin{bmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{bmatrix}$ $\begin{bmatrix} 3 & 2 \\ 2 & 3 \\ 2 & -2 \end{bmatrix}$ =$\begin{bmatrix} 17 & 8 \\ 8 & 17 \end{bmatrix}$
3. The eigenvalues and eigenvectors can be found to be $\lambda_1=25$ $\lambda_2=9$
	$u_1=\frac{1}{\sqrt{2}}\begin{bmatrix}1 \\ 1\end{bmatrix}$
	$u_2=\frac{1}{\sqrt{2}}\begin{bmatrix}1 \\ -1\end{bmatrix}$
4. This gives U in $U\Sigma V^T$ as
	$\begin{bmatrix}\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}$

5. Now to find V, first calculate $A^T*A$ = $A*A^T$ =  $\begin{bmatrix} 3 & 2 \\ 2 & 3 \\ 2 & -2 \end{bmatrix}$ $\begin{bmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{bmatrix}$ = $\begin{bmatrix} 13 & 12 & 2 \\ 12 & 13 & -2 \\ 2 & -2 & 8\end{bmatrix}$
6. We use the eigenvalues found previously found eigenvalues  $\lambda_1=25$ $\lambda_2=9$ and $\lambda_3=0$
$\lambda_3=0$
	this gives $\begin{bmatrix}1/\sqrt{2} & 1/3\sqrt{2} & -2/3 \\1/\sqrt{2} & -1/3\sqrt{2} & 2/3 \\0 & 4/3\sqrt{2} & 1/3 \end{bmatrix}$


7. U and V have shared non-zero eigenvalues because:

![500](./assets/Singular%20Value%20Decomposition%20with%20An%20Example/file-20260129073240509.png)



### Example of SVD
![500](./assets/Singular%20Value%20Decomposition%20with%20An%20Example/file-20260129103109307.png)
![500](./assets/Singular%20Value%20Decomposition%20with%20An%20Example/file-20260129103145595.png)

![500](./assets/Singular%20Value%20Decomposition%20with%20An%20Example/file-20260129103213326.png)

![500](./assets/Singular%20Value%20Decomposition%20with%20An%20Example/file-20260129103242979.png)


### Example of PCR

![500](./assets/Singular%20Value%20Decomposition%20with%20An%20Example/file-20260129105433739.png)
![500](./assets/Singular%20Value%20Decomposition%20with%20An%20Example/file-20260129105458613.png)
![500](./assets/Singular%20Value%20Decomposition%20with%20An%20Example/file-20260129105604053.png)

![500](./assets/Singular%20Value%20Decomposition%20with%20An%20Example/file-20260129105711486.png)
![500](./assets/Singular%20Value%20Decomposition%20with%20An%20Example/file-20260129105740244.png)


### sklearn PCR pipeline with grid-search
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression

# 1. Create a sample dataset
X, y = make_regression(n_samples=100, n_features=20, noise=0.1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 2. Define the PCR Pipeline
# n_components can be an integer or a float (percentage of variance)
pcr_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=5)), 
    ('regressor', LinearRegression())
])

# 3. Fit the pipeline
pcr_pipeline.fit(X_train, y_train)

# 4. Predict and Evaluate
score = pcr_pipeline.score(X_test, y_test)
print(f"R^2 Score: {score}")

```

```python
from sklearn.model_selection import GridSearchCV

# Define the grid of values to search
param_grid = {
    'pca__n_components': [1, 5, 10, 15, 20]
}

# Run the grid search
grid = GridSearchCV(pcr_pipeline, param_grid, cv=5)
grid.fit(X_train, y_train)

print(f"Best n_components: {grid.best_params_['pca__n_components']}")

```
