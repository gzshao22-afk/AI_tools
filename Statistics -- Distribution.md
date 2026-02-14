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

If we know the rate of occurrences, the probability of 0 occurrence happening in the upcoming time period of $t$ is:
$$P(X=0)=\frac{\lambda_t^0e^{-\lambda_t}}{0!}=e^{-\lambda_t}$$
where $\lambda_t$ is the adjusted occurrence rate in for the new time frame.

Poisson distribution:
$$P(X=k)=\frac{\lambda^k*e^{-\lambda}}{k!}$$
>[!Note]
Given a Poisson distribution for occurrences, the wait time between event is an exponential distribution.



