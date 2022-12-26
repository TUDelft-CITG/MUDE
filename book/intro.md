# Introduction 

Welcome to the lecture notes for weeks 2.7 and 2.8 which provides an introduction to risk and reliability.

Almost all activities in life are characterized by some level of risk, such as riding a bike or driving a car, boarding an airplane, or living below sea level behind flood protection system. Particularly within the field of civil engineering, risk and safety are key concepts that should be taken into account explicitly in design and management. Failures of systems providing flood protection, water distribution, transportation networks, air quality control, buildings and other infrastructure are expected to occur rarely, but can lead to large consequences. On the other hand, these systems also provide many benefits to humankind on a daily basis. 

*Risk* is often defined simply as the combination of probability and consequences; it is a measure of how bad something can be (the consequence) combined with the chance that it can happen. In mathematical form: 

$$\text{Risk}_\text{bad thing}=\text{Consequence}_\text{bad thing}\cdot\text{Probability}_\text{bad thing}$$

```{note}
:class: dropdown
Why are the variables above written using words? Because many different terms and symbols are used in different fields of science and enginering which refer to about the same mathematical concepts. For example, 'failure probability,' $p_f$, is often used when designing structural components. However, this term may be misleading when applied to the probability that the concentration of a solute in groundwater exceeds a certain value, or the discharge of a river falling below a regulatory threshold for fish migration.
```

As engineers we are typically concerned with making sure bad things don't happen, or, stated more precisely for our purposes: *reducing the **probability** of a bad thing happening to an **acceptable** level.* To determine if this probability results in a situation that is *safe enough,* an acceptable level of risk needs to be defined. The eventual decision about acceptable risk is predominantly a political one, but engineers can have an important role in the discussion and decision-making. They can provide information on failure probabilities and consequences (economic consequences, life loss, etc.) of a given system and highlight trade-offs between investments in safer systems and risk reduction. Risk plays an important role in many current societal discussions. Examples include recent discussions related to Covid-19 vaccination programs and mitigation measures like facemasks, where there was a lot of uncertainty in the effect of on virus spread. Another example is the discussion over nuclear power versus fossil fuels: both activities bring various benefits (energy generation) but also introduce additional risks to the population and environment. A systematic analysis of risks of (proposed) projects can help to inform the broader societal discussions.

Inevitably, the consideration of risk should result in a specific value of probability that can be used in the design or evaluation of something; in other words, a specific criteria for $\text{Probability}_\text{bad thing}$. For standard applications and systems that are frequently constructed, the risk analysis has been done and building codes are available that define acceptable safety levels in such a way that the failure probability of a structure is sufficiently small. For example, Eurocode provides guidance for the design of structures using so-called target values for the failure probability different safety classes. Thus, critical buildings like hospitals are designed to be stronger than a hardware store. However, for other applications, e.g. special structures or new applications like the reliability of renewable energy-generating components, no standard codes or guidelines are available for design and a more explicit analysis of the reliability and risk of the system is required. An example from the past is the design of the Eastern Scheldt barrier. The acceptable probabilities of failure of the structure and non-closure of the gates were determined based on the acceptable risk of flooding of Zeeland. These probability values formed the basis for the so-called probabilistic design of the barrier in the 1970’s.

```{note}
:class: dropdown
Although much of this book focuses on calculating failure probability, or $\text{Probability}_\text{bad thing}$, we call this a reliability analysis, where *reliability* is simply  

$$\text{Reliability}=1-\text{Probability}_\text{bad thing}$$

So in fact, as engineers we are optimistic, otherwise this chapter would be called Risk and *Un*reliability.
```

Throughout this book we will repeatedly draw on the field of flood management to illustrate risk and reliability concepts as this field requires expertise from all perspectives in civil and environmental engineering and geosciences, from climate and hydrologic processes to evacuation and recovery. In addition, this field has driven the development and use of risk and reliability techniques in the Netherlands since the flooding disaster of 1953, not to mention the experience gained during the previous millenium, albeit in a less rigorous mathematical fashion. And finally, new safety standards for primary flood defences in the Netherlands have been in place since 2017 that are formulated as a tolerable failure probability of dike[^dike] segments. As such, dike reinforcements are legally required to be designed according to these new standards, which requires one to show that the failure probability is less than an allowable maximum value.

Despite the focus on flood management, many applications exist in other fields, for example the discussion about the gas extraction in the North of the Netherlands which leads to increased earthquakes, building damage and potential injury to humans. A thorough analysis of the probability of earthquake occurrence, structural safety of various infrastructure (houses, levee, hospitals, pipelines), benefits associated with extracting gas and the resulting level of risk is required to make decisions about how to manage this industry. As with the flood management application, advanced knowledge of probabilistic techniques is needed. 

In short, risk and reliability concepts cannot be defined or applied without *probability.* It is necessary in order to quantify uncertainty and take it into account when making decisions, regardless of whether our specific task is to investigate, assess, design or create policy for a particular engineering problem. Probability theory is a powerful tool because it provides a way to quantify many aspects of uncertainty, for example:
- precision of measurements
- variability in data
- accuracy and precision of data-driven or physics-based models
- stochastic processes
- unknown conditions due to lack of data or 
- inability to predict the outcome of future events with sufficient accuracy or precision
- and many more

It is crucial that civil and environmental engineers and geoscientists are able to understand and apply the concepts of risk and reliability, as well as probability theory. As such, these lecture provide an introduction to the fundamental techniques and concepts necessary to do so. 

## Chapter Overview

Risk and reliability concepts have been organized into five primary chapters to introduce fundamental concepts and progressively illustrate how they are applied in practice.
- **Probabilistic Design** describes how probability is used in the design process and illustrates key concepts through simple examples and 'patterns' (analytic expressions and visual representations).
- **Risk Analysis** as a process is formally defined and quantitative risk measures are introduced.
- **Component Reliability** and **System Reliability** briefly introduce approaches for evaluating reliability, or $\text{P}_\text{bad thing}$, in order to carry out probabilistic assessment and design quantitatively. This is the *quantitative analysis* step of a risk analysis.
- **Risk Assessment** provides simple quantitative tools and a framework for establishing risk-based safety standards and economic risk criteria. This is a key step in the risk analysis process.

Additional chapters are provided to put these concepts into context, explain industry-specific characteristics or indicate possibilities of additional study for the student.
### MUDE Module Information

This book is prepared for CEGM1000: Modeling, Uncertainty and Data for Engineers (MUDE), a first year MSc module in the Civil Engineering and Geosciences faculty at TU Delft. During the 2022-23 academic year it is only used for two weeks (2.7-2.8) for topics of risk and reliability.

```{admonition} MUDE exam information
:class: tip, dropdown
Key concepts from this book that will be assessed on the MUDE exam are:
- Definitions of risk and steps of a risk analysis
- Simple system and component reliability (quantitative risk analysis methods)
- Use of probability to design and assess engineering systems and components
- Influence of dependence on simple systems and components
- Decision analysis, [cost-benefit analysis](cost_benefit) and economic optimization (risk assessment methods)
- Assessment and quantification of risks for a system with three different risk metrics: individual, societal and economic
- Application and derivation of standards for human safety (individual and societal risk)
- Application and derivation of standards based on economic risk

Although the list is long, the methods are introduced in a simple form and are applied to simplified systems of engineering problems within Civil and Environmental Engineering and Geosciences.
```

```{admonition} MUDE not-on-the-exam information
:class: tip, dropdown
The following concepts or methods are used in this book to illustrate key subjects and examples, but you will *not* be asked to do them on the exam:
- List from memory the steps of a risk analysis and describe all aspects in detail
- Set up a decision tree yourself (note that you may be given a tree with values filled in and asked to interpret it)
- Schematize system reliability problems (we will give you one)
- Define a limit-state function yourself and calculate failure probability
- 
```

### Updates and Citation

The book is a work in progress, and while it will certainly be updated for the second year of MUDE, it will also be used in Q4 as part of the Hydraulic and Offshore Structures track (a unit on probabilistic design) and an elective unit on Flood Risk Analysis in Q1 of the 2023-24 academic year (open to all students at Delft). If you must cite this book, we suggest the following:

`Lanzafame, R. (2023) Risk and reliability analysis for MUDE. Delft University of Technology, the Netherlands. https://tudelft-citg.github.io/MUDE/ `

### License

The contents of this book are licensed for free consumption under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International license ([CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)).

### How the book is made

This book is a Jupyter Book that is written using Markdown, Jupyter notebooks and Python files to generate some figures. The files are stored and compiled from a repository on GitHub within the organization [TUDelft-CITG](https://github.com/TUDelft-CITG/). At the moment the repository is private because we have not decided if and how we should share the source code and solutions to various exercises, quizzes and sample exam questions. We expect to work this out by the beginning of the 2023-24 academic year. If you would like access in the meantime, contact [Robert Lanzafame](https://www.tudelft.nl/staff/r.c.lanzafame/?cHash=e5e7c74400d3d0181a6e635077a912d4).

### Acknowledgements

This book is primarily written by Robert Lanzafame, but uses adapted excerpts from the lecture notes of a previous course, CIE4130 Probabilistic Design, which was last taught at Delft University of Technology in 2022. In particular, the introduction, risk analysis and risk assessment chapters reuse modified material from Professor Bas Jonkman. This book, and the included exercises, would not be possible without the efforts of CIE4130 teachers over the last decades (in alphabetical order): Bas Jonkman, Han Vrijling, Oswaldo Morales Napoles, Pieter van Gelder, Raphaël Steenbergen, Robert Lanzafame, Ton Vrouwenvelder.

Special thanks goes to Caspar Jungbacker, who set up the JupyterBook and GitHub repository to make this book and website possible, and Benjamin Ramousse, who brought the bivariate "patterns" to life with Python.

[^dike]: A dike is a structure, typically made of soil, that protects a specific region from flooding by physically holding back water. Usually associated with rivers, such structures are also widely used on the coast, especially in low elevation areas such as the Netherlands. The Dutch word for levee is *dijk,* but English word *dike* is used in this book. Outside of the Netherlands the words *embankment* and *levee* are used.