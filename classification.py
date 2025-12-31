'''
SVD of iris data
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD
from sklearn.datasets import load_iris
import pandas as pd

# 1. Load Data
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# 2. Apply Truncated SVD for dimensionality reduction to 2 components
# TruncatedSVD is often used when data is not centered, such as TF-IDF matrices
# For standard data visualization, PCA (which centers the data) is also common.
svd = TruncatedSVD(n_components=2, random_state=42)
X_r = svd.fit_transform(X) # X_r contains the data projected onto the new components

# The explained variance ratio shows how much information is retained by the components
print(f"Explained variance ratio of the two components: {svd.explained_variance_ratio_}")

# 3. Plot the transformed data
plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=.8, lw=lw,
                label=target_name)

plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('SVD of IRIS dataset (truncated to 2 components)')
plt.xlabel('First Singular Component')
plt.ylabel('Second Singular Component')
plt.show()
