# Component Reliability

This is a key part of step 3 in a risk analysis: quantitative analysis.

Component reliability Analysis:  
- limit states (servicability, ultimate) and limit-state functions; failure definition
- Design frameworks 
- A simple case 
- Special page to illustrate partial safety factor approach. Start with univariate, then show bivariate (pointing out ‘choice’ that must be made for design point, reference it, then move along). 


- other
  - R-S
  - Z = R + S
  - non-linear
  - most of these should probably go in the component reliability chapter


Overview of non-linear problems (distribution and LSF); explanation of LSF; formulations of structural reliability. the area under the curve. Solution techniquest. Partial safety factor approach / LRFD / beta and reliability index.

In MUDE we focus on situations with two variables (the 'bivariate' case) and use simulation (i.e., Monte Carlo simulation) to calculate failure probability. As problems become more complex, so do the methods to formulate limit-state functions and evaluate failure probability.

Our process is: define the region of interest, integrate bivariate PDF to evaluate probability, check requirement, modify component, check requirement, repeat until satisfactory.

To simple slope problem: *this example is borrowed from Moss, which is borrowed from Baecher and Christian. Both are excellent texts on risk and reliability analysis in civil and geotechnical engineering.*

```{admonition} Exam Information
:class: tip, dropdown
For the exam, you will be expected to be able to recognize and solve simple component reliability problems, and describe the influence that dependence between random variables may have on the calculated probability of interest. Given a specific problem of interest, you should be able to describe failure (or non-failure) analytically as a function of random variables and visually in a bivariate plot. Using these simple frameworks, you can modify the component such that the probability of interest meets a specific criteria.
```

Table of contents: