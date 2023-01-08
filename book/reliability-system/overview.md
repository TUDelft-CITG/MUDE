(rel_sys)=
# System Reliability



A structure or system in civil engineering generally consists of a set of *components* (also called *elements*). Whereas the previous chapter focused on the reliability of a single  component, this chapter addresses reliability analysis for systems that consist of multiple components. The consequences of the failure of a component will depend on the type of system that is considered. In some cases, the failure of a component leads to failure of the whole system (progressive collapse). In other cases (and system configurations) there could be no failure if a single component fails and other components take over the function of the failed one.

The techniques introduced in this chapter essential for carrying out step 3 in a risk analysis: quantitative analysis.

## Series and Parallel Systems

In reliability analysis two types of basic systems can be distinguished: series and parallel (see {numref}`sys-series-parallel`).

```{figure} ../figures/system_series_parallel.png
---
height: 400px
name: sys-series-parallel
---
Series (top row) and parallel (bottom row) systems: the building blocks of system reliability analysis.
```
Within a series system, failure of a single component will always lead to the failure of the entire system. An example is a chain, which breaks if any individual link fails. In our flood management example, a dike ring protecting a single area that is made up of multiple segments is also a series system. Within a parallel system, failure of one component can be compensated by the performance of another  component; it represents the concept of redundancy. Drawing on the chain example, it would imply using more than one chain capable of holding the maximum load. An example from flood management would be to build a second dike ring inside the first dike ring. In practice, a complex system can generally be represented by means of a combination of parallel and series subsystems, just as the parallel system of multiple chains (or dikes) is a parallel system of series systems of links (or dike segments).

```{figure} ../figures/system_series_parallel_ex.png
---
height: 400px
name: sys-series-parallel-ex
---
Example of series (top row) and parallel (bottom row) systems, illustrated with a chain and dike ring. Each component in the parallel case is itself a series system: links in the chain and dike segments in the dike ring.
```

Systems are often schematized using a system diagram, as in {numref}`sys-series-parallel`. This also illustrates the function of a system as an input-output diagram, where one can considers the ability to travel from left to right on the figure. It is analagous to many scenarios involving flow: electricity ({numref}`sys-lightbulbs`), water in pipes or transportation routes.

```{figure} ../figures/system_lightbulbs.png
---
width: 400px
name: sys-lightbulbs
---
Series (left) and parallel (right) systems illustrated as a string of lightbulbs.
```

### Definition of Failure

Whereas in component reliabiity problems we defined failure using a function of random variables, in system reliabiltiy problems, we define failure based on the continuity of the system diagram. Failure occurs when we are not able to travel from left to right on the diagram due to one or more broken links.

## Chapter Overview

This chapter contains a brief introduction to the computation of failure probability for series and parallel systems, and illustrates the role of dependence. The final section illustrates these concepts with a simple exercise.

```{admonition} MUDE Exam Information
:class: tip, dropdown
For the exam, you should be able to recognize and solve simple series and parallel systems, as well as describe the influence that dependence between components may have on the calculated probability of interest. You will not need to draw or evaluate a system more complex than those illustrated on this page.
```
### Additional Information

The word 'system' in the title of this chapter refers to a reliability analyses made up of more than one distinct components. It may or may not be the same as the system for which the risk analysis is being done. For example, in the flood risk case we look at a dike ring, which is a series system of dike segments. Each dike segment can fail in a variety of ways (e.g., sliding or eroding), where if *any* of these types of failure occurs, the dike fails; a series system. Thus, the dike ring is a series system, where each component also a series system.

% add a note about systems of systems, and being able to simplify problems. add figure too (there was one in Chapter 3, originally)

%Sometimes the distinction between system and component reliability is made because components are very different. Sometimes it is a matter of convenience, as two components may share a number of random variables through their respective limit-state functions that influence failure.

System reliability analysis can look very similar to component reliability problems, especially when various combinations of discrete and continuous random variables are incorporated. In reality, all of these problems are generalized by the concept of a multivariate probability distribution. The concepts are separated following conventions in engineering practice, as well as for the convenience of illustrating analytic and numerical solutions.

%Table of contents:

% ```{tableofcontents}
% ```