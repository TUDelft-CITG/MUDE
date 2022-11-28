# Probabilistic Design

Probabilistic design means using probability to design something. Really it's no different than a deterministic design.
- sometimes it's obvious
- others not
- sometimes there are clear criteria
- others not

A little bit about the design process: there's an assessment, it's iterative, you eventually find something that meets a set of criteria. In probabilistic design, at least one of those criteria is a probability.

Consider the safety factor approach, which compares load[^solicitation], $S$, to resistance, $R$, such that $FS=S/R$.

There is also a safety margin.

Now that this section is complete, we can see that as long as $S$ is less than $R$, or $FS>1$, our thingamajig will never fail. Perhaps this is good enough for some things, for example:
- things that have happened: if you did not recieve a passing grade on your last exam, you have failed. There is no going back. It's over. In probability terms, this is a certain event.
- things that are...
- things that are very predictable: ...

For many things, however, a deterministic analysis is not wise because we cannot be sure that our thingamajig will always survive. When we consider a range of possible values, all of a sudden there is a distinct chance that our thingamajig is not stable. A significant part of this book is about quantifying what that chance is, and to do this, we need to apply probability theory. 

## An overview of this chapter

Terms and definitions first?? Then a series of patterns[^pattern] examples to illustrate key concepts.

Sometimes we don't have a structure. Then we can consider just the *hazard*.

Risk analysis is given as an overall framework. Then important topics are considered in more detail in the chapters on Component and System Reliability. 

Risk and Reliability terms.

Notes:
- This is ‘new’ stuff…a brief story about design with probability to introduce component and system reliability chapters, design process, etc 
- Illustrate/introduce bivariate design paradigm 

Table of contents:

```{tableofcontents}
```

[^solicitation]: $S$ stands for solicitation. While this letter and word EW much more pedantic-sounding than simply using load, or $L$, it is widely used in the structural engineering field, where component reliability methods were pioneered. Here we take a broader approach on the subject. Classical texts are {cite:t}`adk2022`, {cite:t}`moss2020` and {cite:t}`ditlevsen1996`.
[^pattern]: The word *paradigm* is not used because it suggests completeness. The examples here, are meant to be used as illustrations for key concepts, and extended to other situations and higher dimensions, so *pattern* seems more appropriate.