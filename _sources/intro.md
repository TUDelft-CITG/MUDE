# Welcome 

Welcome to the lecture notes for weeks 2.7 and 2.8 which provides an introduction to risk and reliability.

*Risk* is often defined simply as the combination of probability and consequences; it is a measure of how bad something can be (the consequence) combined with the chance that it can happen. In mathematical form: 

$$\text{Risk}_\text{bad thing}=\text{Consequence}_\text{bad thing}\cdot\text{Probability}_\text{bad thing}$$

As engineers we are typically concerned with making sure bad things don't happen, or, stated more precisely for our purposes: *reducing the **probability** of a bad thing happening to an **acceptable** level.* Although much of this document focuses on calculating $\text{Probability}_\text{bad thing}$, we call this a reliability analysis, where *reliability* is simply  

$$\text{Reliability}=1-\text{Probability}_\text{bad thing}$$

So in fact, as engineers we are optimistic, otherwise this chapter would be called Risk and *Un*reliability.

```{note}
:class: dropdown
Why are the variables above written using words? Because this document and many others use a variety of different terms to talk about the same concepts, for example, failure probability, $p_f$, is often used when reliability analyses are done for structural components; however, this term is misleading in the situation where we want to estimate the probability that the concentration of a solute in groundwater exceeds a certain value, or the discharge of a river falling below a regularotry threshold for ship traffic or fish migration.
```

In short, risk and reliability cannot be defined without *probability*. These concepts are necessary in order to quantify uncertainty and take it into account when making decisions, regardless of whether our specific task is to investigate, assess, design or create policy for a particular engineering problem. Probability theory is a powerful tool because it provides a way to quantify many aspects of uncertainty, for example:
- precision of measurements
- variability in data
- accuracy and precision of data-driven or physics-based models
- stochastic processes
- unknown conditions due to lack of data or 
- inability to predict the outcome of future events with sufficient accuracy or precision
- and many more

```{admonition} Exam Information
:class: tip, dropdown
Key concepts from these lecture notes that will be assessed on the MUDE exam are:
- Definitions of risk and steps of a risk analysis
- Schematize simple systems; evaluate system and component reliability (quantitative risk analysis methods)
- Use of probability to design and assess engineering systems and components
- Decision analysis, cost-benefit analysis and economic optimization (risk assessment methods)
- Assessment and quantification of risks for a system with three different risk metrics: individual, societal and economic
- Application and derivation of safety standards for human safety (based on individual and societal risk)
- Application and derivation of standards based on economic risk

Although the list is long, the methods are introduced in a simple form and are applied to simplified systems of engineering problems within Civil and Environmental Engineering and Geosciences.
```

```{note}
This digital document is prepared for CEGM1000: Modeling, Uncertainty and Data for Engineers, a first year MSc course in the Civil Engineering and Geosciences faculty at TU Delft.
```