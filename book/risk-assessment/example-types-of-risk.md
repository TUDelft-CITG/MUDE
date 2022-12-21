(ex-3-risk-types)=
# Example: 3 Risk Metrics

We consider application of the three criteria to the case of dike rings in the Netherlands. There are about  100  dike  rings  in  the  Netherlands  of  different  sizes.  A  dike  ring  is  a  flood  prone  area protected from flooding by flood defences and high grounds. The conditional probability of death given  flooding depends on the depth of the polder and flood characteristics. Research on loss of life due to floods shows that a conservative estimate would lead to 
$P_{d|f} = 0.1$

First, we consider the individual risk. A value of $\beta = 0.1$ is proposed as being exposed is considered as an involuntary acctivity with some benefit (i.e. living in a prosperous delta).  This leads to an acceptable individual risk value of $10^{-5}$ per year. This limit has also been proposed by the Dutch government in the year 2014 (“basisveiligheid”).

The acceptable flooding probability according to the individual risk becomes:

$P_{f} \leq \beta \cdot 10^{-4} / P_{d|f} = 0.1 \cdot 10^{-4} / 0.1 = 10^{-4}$ per year.

First, we consider the individual risk. A value of $\beta = 0.1$ is proposed as being exposed is considered as an involuntary acctivity with some benefit (i.e. living in a prosperous delta). This leads to an acceptable individual risk value of $10^{-5}$ per year. This limit has also been proposed by the Dutch government in the year 2014 (“basisveiligheid”).

The acceptable flooding probability according to the individual risk becomes:

$P_{f} \leq \beta \cdot 10^{-4} / P_{d|f} = 0.1 \cdot 10^{-4} / 0.1 = 10^{-4}$ per year

The societal risk criterion can be determined according to the equation above. Assuming a risk averse criterion $\alpha = 2$. We can determine the constant C of the limit line for $N_{A} = 100$ installations and $\beta = 0.1$.

$C=\left(\frac{\beta \cdot 100}{k \sqrt{N_A}}\right)^2=\left(\frac{0.1 \cdot 100}{3 \sqrt{100}}\right)^2 = 0.11$The societal risk criterion can be determined according to the equation above. Assuming a risk averse criterion $\alpha = 2$. We can determine the constant C of the limit line for $N_{A} = 100$ installations and $\beta = 0.1$.

$C=\left(\frac{\beta \cdot 100}{k \sqrt{N_A}}\right)^2=\left(\frac{0.1 \cdot 100}{3 \sqrt{100}}\right)^2 = 0.11$

The limit line for societal risk becomes $1-F_{N}(n) \leq 0.11 / n^{2}$ . Both the individual and societal risk criteria are  plotted in the figure below. As a third criterion the  economic optimization can be added. The optimal or acceptable  probability of failure depends on the damage and investment costs. A relationship with the graph below can be established by assuming that the number of fatalities is related to the economic damages. A dike ring with many inhabitants and potential fatalities will generally also represent a large economic value. For the sake of the example we assume that every fatality corresponds to an economic damage of $5 \cdot 10^{7}$ (note: this is not equal to the value of a human life). To calculate the economic optimum for the example we assume arbitrary values of r = 0.025 and $I = 5 \cdot 10^{6}$; B = 0.33. The figure below shows the combination for the three criteria.

For a given number of fatalities in a dike ring the acceptable failure probability according to the three criteria can be  derived. The individual risk criterion is independent on the  number of fatalities. The economic criterion shows a linear  relation between the failure probability  and damage or  number of fatalities. The societal criterion is risk averse  so shows a decreasing quadratic relationship between acceptable failure probability and consequences.

For a given number of inhabitants and potential fatalities  for a dike ring, the acceptable failure probability can be determined. For dike rings with between 1 and 10 fatalities –generally small areas- the individual  risk  criterion  is  the  most  stringent. For dike rings with large numbers of fatalities, the risk averse societal risk criterion becomes dominant.

Several extensions of this model are possible. One can consider to add the economic value of life loss or consider a different distribution of the nationally acceptable societal risk over dike rings with different sizes.
The limit line for societal risk becomes $1-F_{N}(n) \leq 0.11 / n^{2}$ . Both the individual and societal risk criteria are plotted in the figure below. As a third criterion the  economic optimization can be added. The optimal or acceptable  probability of failure depends on the damage and investment costs. A relationship with the graph below can be established by assuming that the number of fatalities is related to the economic damages. A dike ring with many inhabitants and potential fatalities will generally also represent a large economic value. For the sake of the example we assume that every fatality corresponds to an economic damage of $5 \cdot 10^{7}$ (note: this is simply used as a way to approximate the value of infrastructure in more densely populated regions, and is *not* equal to the value of a human life). To calculate the economic optimum for the example we assume arbitrary values of $r = 0.025$, $I = 5 \cdot 10^{6}$; $B = 0.33$. The figure below shows the combination for the three criteria.

````{toggle}
```{eval-rst}
.. literalinclude:: ../code/risk_types.py
   :language: python
```
````
 
```{figure} ../figures/risk-types.svg
---
width: 400
name: risk-types
---
Combination of individual, societal and economic risk criteria for a
hypothetical example.
```

For a given number of fatalities in a dike ring the acceptable failure probability according to the three criteria can be  derived. The individual risk criterion is independent on the  number of fatalities. The economic criterion shows a linear relation between the failure probability and damage or number of fatalities. The societal criterion is risk averse so shows a decreasing quadratic relationship between acceptable failure probability and consequences.

For a given number of inhabitants and potential fatalities for a dike ring, the acceptable failure probability can be determined. For dike rings with between 1 and 10 fatalities-–generally small areas--the individual risk  criterion is the most stringent. For dike rings with large numbers of fatalities, the risk averse societal risk criterion becomes dominant.

Several extensions of this model are possible. One can consider to add the economic value of life loss or consider a different distribution of the nationally acceptable societal risk over dike rings with different sizes.