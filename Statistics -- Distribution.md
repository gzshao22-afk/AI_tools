#Gaussian_distribution #Poisson_distribution #Exponential_distribution #Lognormal_distribution #Exponential_modified_Gaussian_distribution #Lorentzian_distribution

Summary of the Connections

|Perspective|Question|Distribution|
|---|---|---|
|**Counting**|"How many spikes occurred in 1 second?"|**Poisson**|
|**Timing**|"How long did I wait for the _next_ spike?"|**Exponential**|
|**Combined**|"Total time = Physical signal + Waiting for the spike"|**ExGaussian**|

Poisson distribution:
$$P(X=k)=\frac{\lambda^k*e^{-\lambda}}{k!}$$
>[!Note]
>+ $k$: the number of occurrences (0, 1, 2, ...)
>+  $\lambda$: the average number of events in the interval (rate)
>+ $e$: Euler's number (~2.718)
>+ $k!$: The factorial of $k$




