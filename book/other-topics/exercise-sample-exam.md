# Sample Exam Questions

A flood protection for an area at a bay consists of a first line of defence (a dam on the coast) and a second line (a dike around the bay) to protect the city against a storm surge that can cause a high water level in the bay. The design team considers two strategies: 1) a single dike around the bay, or 2) a dike around the bay plus a dam (see figure). 

```{figure} ../figures/exercise-sample-exam-bay.png
---
width: 400px
name: flood-protection
---
```

**Question 1:** from the perspective of flooding in the city, the function of the dam and dike together is best described as a (choose one):
a. series system
b. parallel system
c. component system
d. none of the above

**Question 2:** how will dependence between the dam and dike change the system failure probability? (choose one)
a. increase
b. decrease
c. no change

**Question 3:** describe whether or not there is dependence between the dam and dike, and what the source could be.

**Question 4:** the damage in case of flood protection system failure is 1 billion $10^9$ Euros. We compare two different investments in the system. In strategy 1 the system failure probability becomes $10^{-3}$ per year at a cost of 10 million ($10 \cdot 10^{6}$). In strategy 2 the system failure probability becomes $3 \cdot 10^{-4}$ per year at a cost of 50 million.

For which value of the interest rate $r$ is strategy 2 the most interesting? (You may consider an infinite lifetime of investments).


**Question 5:** a full scale risk assessment is made for the system. It leads to the calculated FN curve shown in the figure below. The probabilities shown in the figure are $P(N>10)=10^{-3}$ per year and $P(N>100)=5 \cdot 10^{-5}$ per year. A so-called limit line is given with values with $C = 10^{-1}$; and $\alpha = 2$.

Determine whether this situation is acceptable. You may answer using a few sentences or by submitting a sketch, but either way, you must support your answer quantitatively. If you use a sketch, indicate the scale and relevant points on the plot. 

```{figure} ../figures/exercise-sample-exam-limit-line.png
---
width: 400px
name: limit-line
---
```

**Question X:** for a flood prone area, the flooding probability is 1/50 per year and damage is 150 Million Euro. It is questioned whether additional protection is needed and what would be the best solution. The following protection options are considered. Strategy A: To raise the dike, and strategy B: to raise the dike and build a mangrove forest in front which reduces the waves. The graph below indicated the costs of the strategies and how much they reduce the initial failure probability. The interest rate is 4%.

**Question X:** what is the most cost-effective or optimal strategy?

1. Strategy A
2. Strategy B
3. A neither B

```{figure} ../figures/exercise-sample-exam-costs.png
---
width: 400px
name: costs-vs-failure-probability
---
```

**Question X:** what are the total costs (NPV value) for the optimal situation?

**Question X:** consider the individual risk of a dike ring (see plan view below). The acceptable individual risk is $10^{-5}$ per year. The conditional probability of death due to flooding is dependent on the water depth and indicated next to the graph. The individual risk level in area A is $10^{-5}$ per year and the water depth is 3 m. The individual risk level in area B is $10^{-5}$ per year and the water depth is 2 m.

**Question X:** what should be the failure probability of the flood defences around the dike ring ($P_{\text{flooding}}$) to meet the standard for individual risk, IR?

```{figure} ../figures/exercise-sample-exam-individual-risk.png
---
width: 560px
name: individual-risk-plan
---
```

```{figure} ../figures/exercise-sample-exam-failure-domain.png
---
width: 400px
name: failure-domain
---
```

**Question X:** the shaded region in the figure above is $\Omega$, the failure domain of an unknown object (the shaded zone extends further towards positive infinity for $x$ and $y$). $p_f$ is the probability of failure of that object, such that:

$$ 
    p_f = \iint_\Omega f(x,y)dxdy
$$

Where $x$ and $y$ are random variables and $f(x,y)$ is the joint PDF. Identify a specific real-life object of your choosing (it can be anything!) that can be described by this diagram and failure probability. 

*Describe the object and provide a definition of failure using words only, no equations.*



It is clear that $X$ and $Y$ are both loads, since high values of both variables lead to failure. There are many possible ‘objects’ that are governed by two loads, see below for a list of examples. 

*The following text is included in the exaplanation of this sample exam question to give extra insight; you are not expected to reproduce this on the MUDE exam:

The limit state is a line, which means the variables $X$ and $Y$ should have a linear relationship and can be represented as
$$Z=y_0-(y_0/x_0)\cdot x-y$$
or if $y_0=x_0$ is assumed, simply
$$Z=y_0-x-y$$

We can also describe the random variables x and y; specify possible values for the mean ($\mu_x$, $\mu_y$) and standard deviation ($\sigma_x$, $\sigma_y$)If the object is generally stable the mean values should be below the line; specifically any value such that $mu_x<x_0$, $mu_y<y_0$ and $mu_y<y_0-mu_x$.

Since we want to find the design point we should use FORM, not Monte Carlo. If an object with a non-linear LSF is chosen, or non-normal random varialbes, this will be an approximation of pf but the design point is reliable. If x and y are described by a normal distribution,  pf can be solved for exactly using the std normal dist for z with mu_z=y0-mu_x-mu_y and sigma_z=sqrt(sigma_x^2+sigma_y^2). Beta is the distance between point {mu_x, mu_y} and and the LSF such that the line is perpendicular to the LSF. The design point is the point on the LSF where the perpendicular line crosses which is the maximum probability density.
Common mistakes on this question:
- Not describing what x, y, x0 or y0 were
- Using Z=R-S – this was a big error! Note: ok to write Z=R-S only if you clarify that S was a function of X and Y, and that x0 and y0 determine R (not necessarily as random variables)
- Some tried to assign Y as a resistance with  no explanation
- Accidentally flipping the signs on R or S
- Correct description of X and Y as loads, but not writing an equation that showed it
- Writing Z = R - (X + Y) without an explanation of what R is
- Combining x and y in the limit-state function in a way that makes it non-linear 
- FORM gives you the design point; Monte Carlo does not
Comments about answers that were not quite right (points were not deduced for these):
- Be careful with what you assign as a random variable: technically the length of a beam under load acts as a load variable (longer beam is more fragile), but you wouldn’t always include it as a random variable if the variance in the load is much bigger.
- For large structures that are built once (e.g., a bridge in a valley) you can measure the width and construct the bridge, so it’s not really practical to consider these as the main loads or resistances, even though mathematically speaking (alpha value) it is true.
- Combining load variables that had different units
- Making time a random variable
- Creating an object and/or limit state function that was non-linear (e.g., X*Y instead of X+Y)
Common ‘objects’:
- Dike: x and y are water level and wave load, failure is excessive overtopping
- Steel rod: 2 loads exceed strength; careful that this often results in a non-linear LSF
- Beam: self-weight and length are loads (but this is non-linear)
- Island: x and y are sea level rise and settlement, capacity is elevation; failures is flooding
- 2 things on object with limiting capacity. E.g.: people on a couch or bench, birds in a tree 
- Literally any two loads would have been acceptable, as long as the capacity of the object was a sum of both of them (if not a sum, it’s non-linear)
Honorable mentions: exam grading, stoof pot, student knowledge on exam material, ear damage at a music festival, dog and cat in box, exam desk stability, fingers squeezing a pen, 2 heaters in a room	
