(prob_design_2_rv)=
# Two Random Variables

The previous section illustrated the how a decision for dike height, $h_{dike}$, can take into account uncertainty in river discharge. We used a maximum allowable probability of flooding to derive the specific value of discharge, $q_{design}$, that should be used to choose $h_{dike}$. This was necessary because there was otherwise no way of establishing what the maximum discharge should be. The only variable considered to be random was the maximum river discharge that occurs each year. This Section considers how the design process becomes more complicated when *two* random variables are considered (two load variables).

## Discharge from Two Rivers

In this scenario our objective for choosing $h_{dike}$ is still the same, except now we recognize that our location on the river is downstream of a confluence of two smaller rivers. The discharge at the location of our dike is thus the sum of the dicharge from Rivers 1 and 2:

$$
Q_{dike}=Q_1+Q_2
$$

where the same rating curve applies, giving $h_w$ as a function of $Q_{dike}$. As before, acknowledging that the maximum discharge per year in each river is a random variable, we can approach the design problem in the same way: choose $h_{dike}$ such that it retains water when $Q_{dike}$ takes a value with probability of exceedance 0.001. For now, we can assume the distribution for River 1 and River 2 are the same as in the previous Section, and that they are independent.

But now we have two distributions, how do we do it?

### Incorrect Approach 1

Find the discharge $Q$ in each River 1 and River 2 such that the probability of exceeding the discharge is 0.001.

$$
1-F_{Q}(Q_{\mathrm{design}})=0.001
$$

$$
q_{\mathrm{design}}=F_{Q}^{-1}(1-0.001)
$$

$$
q_1=q_2=q_{\mathrm{design}}
$$

*Why is this approach incorrect?*

The probability of these two conditions occurring is not 0.001, it's actualy 0.001$^2$=0.000001.

```{figure} ../figures/temp.svg
---
height: 400px
name: two-rv-and-discharge
---
And probability for 2 random variables.
```

### Incorrect Approach 2

Find the discharge $Q$ in each River 1 and River 2 such that the joint probability of exceeding these values is 0.001. Since the two rivers are independent, we can solve for our design probability, $p_{design}$:

$$
\left(p_{design}\right)^2=0.001\: \rightarrow \: p_{design}=\sqrt{0.001}=0.0316
$$

$$
1-F_{Q}(Q_{\mathrm{design}})=0.0316
$$

$$
q_{\mathrm{design}}=F_{Q}^{-1}(1-0.0316)
$$

$$
q_1=q_2=q_{\mathrm{design}}
$$

*Why is this approach incorrect?*

It only considers one scenario! 

There are infinite alternative scenarios that also result in a joint probability of exceedance of 0.001, for example 0.1 and 0.01:

$$
P(Q_1) \cdot P(Q_2) = 0.1 \cdot 0.01 = 0.001
$$

which results in a totally different dike height.

```{figure} ../figures/temp.svg
---
height: 400px
name: two-rv-and-discharge-2
---
And probability for 2 random variables.
```

### Incorrect Approach 3

We can use the 'OR' probability, or union! In other words, Find the discharge $Q$ for each River 1 and River 2 such that the probability of either of them being exceeded is 0.001.

The union probability is:

$$
P(Q_1 \cup Q_1)=P(Q_1)+P(Q_1)-P(Q_1,Q_2)=0.001
$$

given the assumtion of independence, the exceedance probability for each river is simply 0.001/2-0.0005:

$$
1-F_{Q}(Q_{\mathrm{design}})=0.0005
$$

$$
q_{\mathrm{design}}=F_{Q}^{-1}(1-0.0005)
$$

$$
q_1=q_2=q_{\mathrm{design}}
$$

*Why is this approach incorrect?*

As with the first two incorrect approaches, it also only considers one specific scenario!

There are infinite combinations of $Q_1$ and $Q_2$ such that the union is 0.001.

```{figure} ../figures/temp.svg
---
height: 400px
name: two-rv-or-discharge
---
Or probability for 2 random variables.
```

### Correct Approach

Function of random variables. Get distribution of $Q_{dike}$ directly.

## Reflections on the Simple Example

% Dependence considered in componenet reliability part (and system!)
% Design point consideration NOT included here, and probably not in this book!!!

We need to be explicit in what we are trying to evaluate. In this case, it is the distribution of a function of random variables, $Q_{dike}$.

Sometimes we can't get the distribution of the function of random variables analyticaly. There are two main reasons: 1) non-Gaussian distributions, and 2) non-linear function of random variables. Fortunately it is easy to find it numerically through sampling techniques. This will be discussed elsewhere.

The 'and' and 'or' approaches (intersection and union) are simple, but really only limited to discrete cases. As illustrated above, they cannot be used in the case of continuous random variables, or with functions of random variables because one must integrate across all possible scenarios leading to failure. Nonetheless, these approaches are extremely useful for many situations, and are the basis of *system reliability* problems.

The situation illustrated here is often referred to as a *component reliability* problem, where the 'component' is defined by a function of random variables.
 Although nothing more than a function of random variables,is nothing more than an integration over a specific region of a multivariate probability density function. Often this region describes failure of a component, which we will try to keep below an acceptable level.

```{admonition} MUDE exam information
:class: tip, dropdown
Given a specific scenario, you should be able to identify the design condition and an appropriate method for calculating a probability of interest (as illustrated here). Functions of random variables are illustrated more thoroughly in the **Component Reliability** chapter.
```

<!-- ```{admonition} MUDE exam information
:class: tip, dropdown
Given a specific scenario, you should understand the difficulty associated with choosing specific design values when more than one random variable is considered, and be able to represent the failure probability analytically and graphically. For simple measures of dependence (correlation coefficient, $\rho$) you can describe the quantitative influence on failure probability. You should also recognize how a function of random variables can be used the univariate case is simple, it can also be extended to a function of random variables, which implicitly assumes a more complex multivariate probability distribution though the marginal distributions of the (random) input variables. This topic is covered more thoroughly in the **Component Reliability** chapter.
``` -->