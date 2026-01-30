
### PCA before t-SNE
For large datasets, it is often recommended to first use a faster linear dimensionality reduction method like PCA to reduce the number of dimensions to a reasonable amount (e.g., 50) before applying t-SNE to suppress noise and speed up computation.

**Typical Data Pipeline**

The standard workflow for high-dimensional visualization is:  
`Raw Data` → `Handle Missing Values (impute)` → `Standardization` → `PCA (to ~50 dims)` → `t-SNE`.

### PCA before linear regression is PCR

### UMAP is the preferrable alternative to t-SNE 


### What about MDS?
