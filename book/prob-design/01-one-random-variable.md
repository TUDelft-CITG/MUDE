# One Random Variable

Consider a river that is protected by dikes: the dikes keep water in the river channel, and the height should be sufficient to pass the maximum discharge in the river, measured in m$^3$/s. A rating curve gives us the relationship between discharge and water depth, $h_w$, so if we know what the maximum discharge is, we can build our dikes to the critical height, $h_{dike}$. But there is a problem---what is the maximum discharge? 

```{warning}
finish point about discharge being random. can always be bigger. add story about PDF and design value
```

Recalling the *safety margin* limit state from the previous section, $M=R-S$, we can see how randomness plays a role in the design process. Failure is defined as $M<0$, which we can 

## Reflection on the Simple Example

Is this an oversimplification of reality? Perhaps, but it gets pretty close. Many flood protection systems in the world use an exceedance proabability approach to probabilistic design: choosing a specific and making sure the component or system can handle the load. This works well when the primary source of uncertainty is the load: the river discharge in this case. 

We also took for granted that a simple relationship between river discharge and water depth is available. However, this is never the case, as such a relationship depends on the cross-sectional shape and roughness of the floodplain, which not only varies along the river trajectory, but also changes due to natural phenomenon and human interventions. This introduces additional uncertainty into our assessment of whether the dikes are high enough.

Fprtunately there is also extra conservatism built into this approach. For example, duration of high water plays a role: if discharge exceeds the capacity of the dike system, but only lasts for a short time (minutes or a couple hours), perhaps the dikes can withstand the overflow without eroding and causing flooding. This can be conceptualized by considering the joint probability of a high discharge *and* degradation of the dike leading to flooding:

$$
P(\text{flooding},h_w>h_{dike})=P(\text{flooding}|h_w>h_{dike})\cdot P(h_w>h_{dike})
$$

where the conditional term represents the probability that the dike erodes (fails) given that the water depth exceeds the height. Assuming failure when the critical water depth is exceeded is conservative because it implies $P(\text{flooding}|h_w>h_{dike})=1.0$, whereas in reality this is not the case, and the 'true' flooding probability is less than that computed in the equation above.

Later chapters of this book will introduce methods for taking these realities into account in the design and decision-making process. For now, we will see how our probabilistic design changes when more than one random variable must be considered.

## Old stuff

Let's consider that the load is random.

Discrete.

Continuous.

Illustration of exceedance probability approach. Compare 1/10,000 with:  
$$
\int_{-\infty}^{+\infty}f(\text{levee failure}|h)\cdot f(h)\: \text{d}h
$$

```{admonition} MUDE exam information
:class: tip, dropdown
Given a probability requirement and distribution for a random variable of interest, you should be able to find the appropriate design value. You should also recognize the influence that the *choice* of distribution or probability requirement may have on the final design, especially in terms of model validity and financial cost. Although the univariate case is simple, it can also be extended to a function of random variables, which we will explore in the next Section. This topic is also covered more thoroughly in the **Component Reliability** chapter.
```