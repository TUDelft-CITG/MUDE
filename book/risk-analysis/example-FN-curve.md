(ex-FN-curve)=
# Example: FN curve Calculation

The following three figures illustrate the computation of an FN curve for a system with two mutually exclusive event scenarios:
- Accident 1 with $N_{1}=10$ fatalities and a probability of $P_{1} = 10^{-2}$ per year
- Accident 2 with $N_{2}=100$ fatalities and a probability of $P_{1} = 10^{-3}$ per year

First, the probability mass function is created $f_N(n)=P(N=n)$, taking care that the probability of no fatalities is included:

$$ P(0) = 1 - P_{1} + P_{2} = 1 - 0.01 - 0.001 = 0.989 $$

The cumulative  distribution function, $F_N(n)=P(N\leq n)$, can thus be easily computed, as well as the probability of exceedance, $1-F_N(n)$, also known as the *FN curve.* Note that if a risk metric such as damage in Euros was being used, we would call this the *FD curve* and use $D$ to denote the random variable, as in $f_D(d)$ and $F_D(d)$

While the curves below illustrate probability and consequences associated with specific scenarios, the expected value of the distribution can be computed, which is equivalent to the area under the FN curve. This is useful can be used to assess the entire system. For this example, the expected value of fatalities per year for all scenarios can be computed as follows: 

$$E(N) = P_{1}N_{1} + P_{2}N_{2} = 0.2\quad \textsf{(fatalities per year)}$$


<!-- ````{toggle}
```{eval-rst}
.. literalinclude:: ../code/ex_FN_curve_step_01.py
   :language: python
```
```` -->
 
```{figure} ../figures/ex_FN_curve_step_01_py.svg
---
width: 400
name: ex_FN_curve_step_01
---
Probability mass function (PMF), $f_N(N)$.
```

<!-- ````{toggle}
```{eval-rst}
.. literalinclude:: ../code/ex_FN_curve_step_02.py
   :language: python
```
```` -->

```{figure} ../figures/ex_FN_curve_step_02_py.svg
---
width: 400
name: ex_FN_curve_step_02
---
Cumulative distribution function (CDF), $F_N(n)$.
```

<!-- ````{toggle}
```{eval-rst}
.. literalinclude:: ../code/ex_FN_curve_step_03.py
   :language: python
```
```` -->
 
```{figure} ../figures/ex_FN_curve_step_03_py.svg
---
width: 400
name: ex_FN_curve_step_03
---
Exceedance probability (FN curve), $1-F_N(n)$.
```
