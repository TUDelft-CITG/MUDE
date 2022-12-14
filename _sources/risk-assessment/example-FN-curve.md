# Calculation of an FN curve

The following example shows the composition of an FN curve for a system with two mutually exclusive event scenarios.

Accident 1 with $N_{1}=10$ fatalities and a probability of $P_{1} = 10^{-2}$ per year
Accident 2 with $N_{2}=100$ fatalities and a probability of $P_{1} = 10^{-3}$ per year

Based on this information the probability mass function can  be formed (first graph). Consequently, the cumulative  distribution function can be made (second graph). Finally, the probability of exceedance or the FN curve is made (third graph).

Finally, we note that the expected value of the number of fatalities equals: 

$E(N) = P_{1}N_{1} + P_{2}N_{2} = 0.2$ fatalities per year

````{toggle}
```{eval-rst}
.. literalinclude:: ../code/ex_FN_curve_step_01.py
   :language: python
```
````
 
```{figure} ../figures/ex_FN_curve_step_01.svg
---
width: 400
name: ex_FN_curve_step_01
---
Example FN-curve calculation: probability mass function (PMF).
```

````{toggle}
```{eval-rst}
.. literalinclude:: ../code/ex_FN_curve_step_02.py
   :language: python
```
````

```{figure} ../figures/ex_FN_curve_step_02.svg
---
width: 400
name: ex_FN_curve_step_02
---
Example FN-curve calculation: cumulative probability function (CDF).
```

````{toggle}
```{eval-rst}
.. literalinclude:: ../code/ex_FN_curve_step_03.py
   :language: python
```
````
 
```{figure} ../figures/ex_FN_curve_step_03.svg
---
width: 400
name: ex_FN_curve_step_03
---
Example FN-curve calculation: exceedance probability (FN curve).
```
