# Definition of risk

Almost all activities in life are characterized by some level of risk. Especially in the design and management of engineering systems risk and safety are key concepts and need to be taken into account explicitly. In social discussions no unambiguous meaning is assigned to the concept of risk. Two definitions given in the Oxford dictionary are: 1) a situation involving exposure to danger; 2) the possibility that something unpleasant or unwelcome will happen.

The first definition focuses on the consequences, the second on the possibility or probability. Quantifying and evaluating risks based on merely the probabilities or consequences is less realistic. For example, the risk of losing € 100 with a probability of 50% is different than the risk of losing € 1000 with the same probability. Also, the risk associated with losing a given sum of money will depend on the probability of the event.
An often-used definition considers risk as expected value:
<br>
<div style="text-align: center"><em> Risk is the probability of an undesired event multiplied by the consequences.</em></div>
<br>

The unit of risk now depends on the units of probability and consequences. The probability of an event is generally expressed as the probability per unit time, for example per year. The consequences of an undesired event are often multi-dimensional, i.e. they can consist of different types of consequences, such as material, ecological damages, injuries and fatalities (see section 3.2.2 for further details). In many applications in engineering consequences are expressed by means of a monetary value. The unit of the risk (or expected value $
 E(d)$ ) then becomes € per year. For a case with one event scenario <em>i</em>  with probability <em>$p_{i}$ </em> it yields:
 $$
 E(d) = p_{i}d_{i} 
 $$ (risk_definition)
 
A more general definition of risk has been given by Kaplan and Garrick (1981):<br>
<br>
<div style="text-align: center"><em> Risk is a set of scenarios ($s_{i}$), each of which has a probability ($p_{i}$) and a consequence ($d_{i}$).</em></div>
<br>

This definition of Kaplan and Garrick allows the use of various so-called risk metrics (or risk measures) to quantify or depict the risk. The expected value of the damage for a set of multiple discrete scenarios{1,....,<em>n</em>} , can be expressed as:
$$
E(d) = \sum_{S_{i=1}}^{n}p_{i}d_{i}
$$ (risk_definition_sum)

```{figure} ../figures/1.png
---
height: 200px
name: FN-curve
---
FN curve, showing the probability of exceedance of a certain number of fatalities N on Log-Log scale.
```

The expected value does not give insight in the magnitude of probability and consequences and the contribution of individual scenarios. Therefore, an often-used alternative risk metric is the risk curve. It shows the probability of exceedance of a certain magnitude of consequences. A well-known example of such a risk curve is the FN curve, which displays the probability of exceedance of <em>N</em> fatalities. The values on both axes are generally shown on a logarithmic scale, see Figure 3.1Figure 3.1 for an example. The FN curve was originally introduced for the assessment of the risks in the nuclear industry (Farmer, 1967; Kendall et al., 1977) and is now used to display and limit risks in various countries and sectors. Further information on the use of FN curves and a simple example of how to construct such a curve are included in section 3.5.1. 

# Other risk definitions
In the remainder of this lecture notes and the course the definitions from the previous paragraph will be applied. Since (civil) engineers will work in a broad domain of applications it is useful to highlight some risk concepts used in other domains.

Within economics, risk is generally associated with a deviation from the expected return or the probability of loss. In social sciences risk is often considered as a contextual notion or social construct. Vlek (1996) has summarized 11 formal definitions used in social sciences, see Table 3.1. In some of these definitions (e.g. numbers 2 and 4) the perceived seriousness of the undesired consequences plays an important role. Examples of other, more informal risk definitions used in psychology are “the lack of perceived controllability”, “set of possible negative consequences” and “fear of loss” (Vlek, 1996). 

Substantial research has focussed on the factors that determine the perception of risk (e.g. Slovic, 1987, Vlek, 1996). Examples of factors that influence risk perception include: the degree of damage, the controllability of and familiarity with the hazards, the extent of benefits from an activity, and voluntariness of exposure. 

Table 3.1 Formal definitions of risk used in social sciences (Vlek, 1996 )

|    |       |
|:----|:---|
| 1  | Probability of undesired consequence                                                                    |
| 2  | Seriousness of (maximum) possible undesired consequence                                                 |
| 3  | Multi-attribute weighted sum of components of possible undesired consequences                           |
| 4  | Probability x seriousness of undesired consequence (‘expected loss’)                                    |
| 5  | Probability-weighted sum of all possible undesired consequences (‘average expected loss’)               |
| 6  | Fitted function through graph of points relating probability to extent of undesired consequences        |
| 7  | Semi variance of possible undesired consequences about their average                                    |
| 8  | Variance of all possible consequences about mean expected consequence                                   |
| 9  | Weighted sum of expected value and variance of all possible consequences                                |
| 10 | Weighted combination of various parameters of the probability distribution of all possible consequences |
| 11 | Weight of possible undesired consequences (‘loss’) relative to comparable possible desired consequences |


The definitions applied in the research on natural hazards, often define risk in terms of more qualitative concepts such as hazard, vulnerability and exposure
* Hazard: A dangerous phenomenon, substance, human activity or condition that may cause loss of life, injury or other health impacts, property damage, loss of livelihoods and services, social and economic disruption, or environmental damage
* Vulnerability: The characteristics and circumstances of a community, system or asset that make it susceptible to the damaging effects of a hazard
* People, property, systems, or other elements present in hazard zones that are thereby subject to potential losses