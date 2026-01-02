transformer --> estimator
https://scikit-learn.org/stable/getting_started.html

<img width="856" height="816" alt="image" src="https://github.com/user-attachments/assets/ce22cd11-7e66-46e2-89f6-7794b4c55c29" /> <br>

made with https://excalidraw.com   <br>




<img width="605" height="678" alt="image" src="https://github.com/user-attachments/assets/27fe816c-58bc-4c4b-9859-b2000b0e0a85" />

model_selection: cross_validation, KFold,
```kfold = KFold(3, True, 1)```
>split data into 3 parts
>True for shuffling the data
>1 for pseudorandom number genertor
https://machinelearningmastery.com/k-fold-cross-validation/


- Estimator: fitting and predicting
- Pipeline: Chaining preprocessor and estimator
-- Pipeline.fit
-- RandimizedSearchCV(pipeline, n_iter = xx, ...)
- Model evaluation
- Automatic parameter searches

  
