transformer --> estimator
https://scikit-learn.org/stable/getting_started.html

<img width="856" height="816" alt="image" src="https://github.com/user-attachments/assets/ce22cd11-7e66-46e2-89f6-7794b4c55c29" /> <br>

made with https://excalidraw.com   <br>




<img width="605" height="678" alt="image" src="https://github.com/user-attachments/assets/27fe816c-58bc-4c4b-9859-b2000b0e0a85" />

model_selection: cross_validation, KFold,
```kfold = KFold(3, True, 1)```
>split data into 3 parts \
>True for shuffling the data \
>1 for pseudorandom number genertor \
https://machinelearningmastery.com/k-fold-cross-validation/

## Example
``` python
# scikit-learn k-fold cross-validation
from numpy import array
from sklearn.model_selection import KFold
# data sample
data = array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
# prepare cross validation
kfold = KFold(3, True, 1)
# enumerate splits
for train, test in kfold.split(data):
	print('train: %s, test: %s' % (data[train], data[test]))
```

```
train: [0.1 0.4 0.5 0.6], test: [0.2 0.3]
train: [0.2 0.3 0.4 0.6], test: [0.1 0.5]
train: [0.1 0.2 0.3 0.5], test: [0.4 0.6]
```

- Estimator: fitting and predicting
- Pipeline: Chaining preprocessor and estimator
-- Pipeline.fit
-- RandimizedSearchCV(pipeline, n_iter = xx, ...)
- Model evaluation
- Automatic parameter searches

  
