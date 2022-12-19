# Probabilistic Design

Stated as simply as possible, the term *probabilistic design* implies the use of probability to design something. Although this may sound complex, there is actually not much different than a deterministic approach, where values used to design something are not assumed to be random. For example, the load on a beam, or the maximum discharge expected in a river. In a typical design process, the problem and functional requirements are first defined, the system or component is evaluated and then refined {cite:p}`voorendt2017`. It is ideally an iterative process, where tradeoffs between competing requirements must be considered in order to arrive at an optimal configuration. During much of your university education you have probably learned a variety of techniques to evaluate interesting problems in your field of study; however, only towards the end of a bachelor or master program do you begin to *design* things and take into count information beyond what is written in a simple exam problem to make decisions. The design process is often challenging because there is no single right answer. 

Consider some arbitrary object--let's call it a thingamajig--which we must design and eventually build, and we would like to apply the safety factor approach, which compares load[^solicitation], $S$, to resistance, $R$, such that $FS=S/R$. As long as $S$ is less than $R$, or $FS>1$, our thingamajig will never fail, which makes the design process quite simple. This is a great approach for many situations, for example, if the values of $R$ and $S$:
1. are well known, or never change (at least not on short time scales). For example, gravity will keep a sewer manhole in place.
2. are confirmed by many observations, for example, pumping up your bicycle tire to 4 or 5 bar
3. are easy to measure, such as the strength of steel or the density of water
In situations like this you can make your design decision and rest assured that there won't be any lawyers knocking on your door in the near future.

For many situations, however, a deterministic analysis is not wise because we cannot guarantee that our thingamajig will always survive. When we consider a range of possible values, all of a sudden there is a distinct chance that our thingamajig is not stable. For example, reflecting on the examples above, we may worry about:
1. TO-DO
2. TO-DO
3. TO-DO

We might call these examples *failures,* and a significant part of this book is concerned with the quantification of the probability of it happening. Another focus of this book is to determine what the allowable failure probability should be. Specifically, probability theory is useful to incorporate in the process of engineering because it allows us to quantitatively account for:
1. randomness in some of our important design variables
2. imprecise measurements or models
3. risk-based design criteria and safety standards
Thus, to conclude: the distinguishing feature of a probabilistic design from a conventional deterministic one is that at least one design criteria is a probability.

%Sometimes we have criteria, sometimes we do not.

## An overview of this chapter

%Terms and definitions first??
%Aleatoric and epistemic.
%Sometimes we don't have a structure. Then we can consider just the *hazard*.

The remainder of this chapter uses the evaluation and design of a river flood protection system to introduce key aspects of risk and reliability, as well as the design process. A distinction is made between using probability to assess engineering components and systems (reliability analysis) and to derive design criteria (risk assessment), which are introduced formally in later chapters after the general risk analysis framework is discussed.

Key concepts are often illustrated in a simple way by considering two random variables, which can be referred to as a *bivariate* situation. This is more insightful than the univariate case because it allows us to consider the quantitative and qualitative influence of dependence, as well as the functional relationship between two variables and their join probability density (e.g., union, intersection or limit-states).

Table of contents:

```{tableofcontents}
```

[^solicitation]: $S$ stands for solicitation. While this letter and word EW much more pedantic-sounding than simply using load, or $L$, it is widely used in the structural engineering field, where component reliability methods were pioneered. Here we take a broader approach on the subject. Classical texts are {cite:t}`adk2022`, {cite:t}`moss2020` and {cite:t}`ditlevsen1996`.
%[^pattern]: The word *paradigm* is not used because it suggests completeness. The examples here, are meant to be used as illustrations for key concepts, and extended to other situations and higher dimensions, so *pattern* seems more appropriate.