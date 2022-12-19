# Sample Exam Questions

1. Indicate which of the following statements is true (multiple answers possible):
   1. A parallel system gets stronger if there is a strong positive correlation between failure of the elements.
   2. Dependence between elements is only determined by dependence in loads.
   3. In case of a full dependence between two elements $A$ and $B$, it holds that $P(B|A)=1$.
   4. A flood defence system that is a single line of defence composed of multiple dike sections would best be characterized as a series sytem, not as a parallel system.
   5. A prison with multiple walls and fences would best be characterized as a series system, not as a parallel system.

2. A flood protection for an area at a bay consists of a first line of defence (a dam on the coast) and a second line (a dike around the bay) to protect the city against a storm surge that can cause a high water level in the bay. The design team considers two strategies: 1) a single dike around the bay, or 2) a dike around the bay plus a dam (see figure). 

The damage in case of failure is 1 billion $10^9$ Euros. We compare two different investments in the system. In strategy 1 the system failure probability becomes $10^{-3}$ per year at a cost of 10 million ($10 \cdot 10^{6}$). In strategy 2 the system failure probability becomes $3 \cdot 10^{-4}$ per year at a cost of 50 million.

For which value of the interest rate $r$ is strategy 2 the most interesting? (You may consider an infinite lifetime of investments).

```{figure} ../figures/exercise-sample-exam-bay.png
---
width: 400px
name: flood-protection
---
```

3. A full scale risk assessment is made for the system. It leads to the calculated FN curve shown in the figure below. The probabilities shown in the figure are $P(N>10)=10^{-3}$ per year and $P(N>100)=5 \cdot 10^{-5}$ per year. A so-called limit line is given with values with $C = 10^{-1}$; and $\alpha = 2$.

Determine whether this situation is acceptable. You may answer using a few sentences or by submitting a sketch, but either way, you must support your answer quantitatively. If you use a sketch, indicate the scale and relevant points on the plot. 

```{figure} ../figures/exercise-sample-exam-limit-line.png
---
width: 400px
name: limit-line
---
```

4. For a flood prone area, the flooding probability is 1/50 per year and damage is 150 Million Euro. It is questioned whether additional protection is needed and what would be the best solution. The following protection options are considered. Strategy A: To raise the dike, and strategy B: to raise the dike and build a mangrove forest in front which reduces the waves. The graph below indicated the costs of the strategies and how much they reduce the initial failure probability. The interest rate is 4%.

What is the most cost-effective or optimal strategy?

1. Strategy A
2. Strategy B
3. A neither B

```{figure} ../figures/exercise-sample-exam-costs.png
---
width: 400px
name: costs-vs-failure-probability
---
```

5. What are the total costs (NPV value) for the optimal situation?

6. Consider the individual risk of a dike ring (see plan view below). The acceptable individual risk is $10^{-5}$ per year. The conditional probability of death due to flooding is dependent on the water depth and indicated next to the graph. The individual risk level in area A is $10^{-5}$ per year and the water depth is 3 m. The individual risk level in area B is $10^{-5}$ per year and the water depth is 2 m.

What should be the failure probability of the flood defences around the dike ring ($P_{\text{flooding}}$) to meet the standard for individual risk, IR?

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

7. The shaded region in the figure above is $\Omega$, the failure domain of an unknown object (the shaded zone extends further towards positive infinity for $x$ and $y$). $p_f$ is the probability of failure of that object, such that:

$$ 
    p_f = \iint_\Omega f(x,y)dxdy
$$

Where $x$ and $y$ are random variables and $f(x,y)$ is the joint PDF. Identify a specific real-life object of your choosing (it can be anything!) that can be described by this diagram and failure probability and do the following:

- Describe the object and provide a definition of failure using words only, no equations.
- Write a limit-state function for the object
- Describe random variables x and y; specify possible values for the mean ($\mu_x$, $\mu_y$) and standard deviation ($\sigma_x$, $\sigma_y$)
- State how you would find the design point and probability of failure $p_f$, and explain why you chose this approach (limit this to a few short sentences; make sure you clearly state your assumptions)
