# Exercise: Paint System

In this assignment we will consider a paint system that prevents rust and corrosion on a steel structure. A high quality paint system costs €40 per square meter and has a failure probability of 0.002, which assumes that the old paint system is completely stripped off and the steel surface is cleaned prior to installation, which has an additional cost of €20 per square meter. 

Common cost cutting measures are to use a cheaper paint that costs half as much, but is five times more likely to fail, or to simply sand the old paint rather than stripping it off prior to applying a new paint, which increases the failure probability by 10, but only costs €5 per square meter.

During operation of the structure, if a rust spot is found it must be repaired immediately by removing the damaged paint and replacing it. The repair has an additional cost of €500 per square meter. 

Construct a decision tree to evaluate the different options for steel preparation and paint, then use it to answer the following questions. Assume that the owner wants to minimize total costs, that the paint system only fails once in any reference period and that the probability of failure in each year is independent. All costs and probabilities are calculated on a square meter basis. 

1.	What is the probability of each paint system failure per square meter over one year?

*Answer:*

| Paint            | Cleaning   | $P_f$/year |
|-------           |---         | ---        |
|   High-Quality   | Stripping  | 0.002      |
|   High-Quality   | Sanding    | 0.02       |
|   Low-Quality    | Stripping  | 0.01       |
|   Low-Quality    | Sanding    | 0.1        |

2.	What is the probability of each paint system failure per square meter over a 10 year period?

*Answer:*

$$P_{f,10y} = 1 - (1 - p_{f,1y})^{10}$$

| Paint            | Cleaning   | $P_f$/year |
|-------           |---         | ---        |
|   High-Quality   | Stripping  | 0.02       |
|   High-Quality   | Sanding    | 0.18       |
|   Low-Quality    | Stripping  | 0.1        |
|   Low-Quality    | Sanding    | 0.65       |

3.	What is the expected cost per square meter over a one year period if the owner uses the high quality cleaning and high quality paint?

*Answer:* 
$$
40 + 20 + 0.002 * (500 + 40 + 20) = €61.12 / m^2
$$
In Euros

4.	What is the optimal paint system for a one year period?

*Answer:*

$$C_{paint} + C_{cleaning} + P_{f,1y} * (C_{paint} + C_{cleaning} + C_{repair})$$

| Paint            | Cleaning   | Expected cost/year |
|-------           |---         | ---                |
|   High-Quality   | Stripping  | 61.12         	 |
|   High-Quality   | Sanding    | 61                 |
|   Low-Quality    | Stripping  | **45.4**           |
|   Low-Quality    | Sanding    | 83                 |

Low Quality Paint + High Quality Cleaning

5.	What is the optimal paint system for a 10 year period?

*Answer:*

$$C_{paint} + C_{cleaning} + P_{f,10y} * (C_{paint} + C_{cleaning} + C_{repair})$$

| Paint            | Cleaning   | Expected cost/10year |
|-------           |---         | ---                  |
|   High-Quality   | Stripping  | **71.1**        	   |
|   High-Quality   | Sanding    | 150.6                |
|   Low-Quality    | Stripping  | 91.6                 |
|   Low-Quality    | Sanding    | 375.2                |

High Quality Paint + High Quality Cleaning

6.	Upload a photo/scan of your decision tree. Make sure the values and parameters for each branch are clear.

*Answer:*

```{figure} images/decision-tree.png
---
width: 600px
name: decision-tree
---
Decision tree for exercise 6
```

Assume the owner has decided to use the cheap paint system, and is simply going to sand it off (i.e. the cheap cleaning method) and re-apply the same system every year (i.e., for these problems consider a 1-year reference period). You have been asked to assess whether it is worthwhile to use a quick sonic test system to prevent failures during the year, and if it is, the number of tests that should be performed per year. Each test costs about €3 per m2, and if a weak spot is found, a new layer of paint can be easily applied, lowering the failure probability by a factor of 0.45.

7.	What is the annual expected cost due to paint failure if no sonic inspections are done?

*Answer:*
$$
E(D) = P_f * D = 0.1 * 525 = 52.50
$$

8.	What is the annual expected total cost for the paint system if no sonic inspections are done?

*Answer:*
Using the decision tree from above: €77.50/m2

9.	What is the change in risk for 3 sonic inspections?

*Answer:*
$$
\Delta E(D) = (P_{f,0} - P_{f,new}) * D = 45.94
$$

10.	What is the annual expected cost due to paint failure if 3 sonic inspections are done?

*Answer:*
$$
\Delta E(D)=P_f * D={0.5}^3 * 0.1 * 525=6.56
$$

11.	What is the maximum number of inspections per year that can be performed that are cost-effective? Note: Round your answer towards the smallest integer.

*Answer:*
17 per year
$$
\frac{\Delta E(D)}{I}>1
$$

12.	What is the optimum number of sonic inspections to perform each year? Plot a graph, with the Risk, Investment and Total cost curves and clearly indicate the optimum.

*Answer:*
3 per year

```{figure} ../figures/optim-curve.png
---
width: 600px
name: optimization-curve
---
Optimization curve for exercise 12
```