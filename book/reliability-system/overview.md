# System Reliability

This is a key part of step 3 in a risk analysis: quantitative analysis.

Just a few simple examples to illustrate: series and parallel systems, influence of dependence.

Example illustrating difference in failure probability in reality versus model (flooding?).

*Note that 'system' in the title of this chapter refers to a particular set of reliability analyses made up of more than one distinct components. It may or may not be the same as the system for which the risk analysis is being done. For example (the flood risk case), we look at a levee ring, which is a system of levee segments (trajectory, or traject in Dutch), and each segment can be modeled as a series system.*

Sometimes the distinction is made because components are very different. Sometimes it is a matter of convenience, as two components may share a number of random variables through their respective limit-state functions that influence failure.

Key concept: system reliability analysis can look very similar to component reliability problems. We separate it because in practice the analytic and numerical solutions can be quite different, which also reflects the way these methods are used (and even named) in different fields of engineering and mathematics.

```{admonition} MUDE Exam Information
:class: tip, dropdown
For the exam, you should be able to recognize and solve simple series and parallel systems, as well as describe the influence dependence between components may have on the calculated probability of interest.
```

**Sample exam question:** Indicate which of the following statements is true (multiple answers possible):
   1. A parallel system gets stronger if there is a strong positive correlation between failure of the elements.
   2. Dependence between elements is only determined by dependence in loads.
   3. In case of a full dependence between two elements $A$ and $B$, it holds that $P(B|A)=1$.
   4. A flood defence system that is a single line of defence composed of multiple dike sections would best be characterized as a series sytem, not as a parallel system.
   5. A prison with multiple walls and fences would best be characterized as a series system, not as a parallel system.

*Answers 3 and 4 are true.*

%Table of contents:

% ```{tableofcontents}
% ```