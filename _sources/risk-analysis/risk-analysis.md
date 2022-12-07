# Risk analysis and risk evaluation

Author: S.N. Jonkman

Parts of this chapter are based on the publication Cur 190 “Kansen in de civiele techniek” (CUR, 1997; also the most recent version of 2015</em>




## **3	RISK ANALYSIS AND RISK EVALUATION  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp;  	              58**
**3.1	Risk &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; 	58**
>
    >3.1.1	General definition of risk 	58<br>
    >3.1.2	Other risk definitions	59<br>

**3.2	Risk Analysis	60**
>
    >3.2.1	General	60<br>
    >3.2.2	Elements in a risk analysis	61<br>
    >3.2.3	Steps in a risk analysis	62<br>

**3.3	Decision-making under uncertainties	65**
>
    >3.3.1	Introduction and basics	65<br>
    >3.3.2	Decision rules	67<br>
    >3.3.3	Utility functions	71<br>

**3.4	Cost Benefit Analysis and economic optimization	73**
>
    >3.4.1	Cost benefit analysis	73<br>
    >3.4.2	Economic optimization	76<br>
    >3.4.3	Application of the economic optimization: optimal dike heightening	78<br>

**3.5	Safety standards	82**
>
    >3.5.1	Introduction	82<br>
    >3.5.2	Limits for individual and societal risk	85<br>
    >3.5.3	The Dutch safety standards for industrial major hazards	87<br>
    >3.5.4	The TAW model: a general model for deriving safety standards	89<br>

**3.6	Probabilistic design: the relationship between safety standards and engineering design	93**

**References	95**

**Appendix 3.1 More detailed scheme for risk assessment (CUR 190)	97**

**Appendix 3.2 FN curves for different distribution types	98**

**Learning objectives of this chapter:**
>* Understand the basic concepts of risk, risk analysis, decision analysis<br>
>* Be able to assess and quantity the risks for a (simplified) system with different risk metrics (individual, societal risk / FN curve, economic risk)<br>
>* Be able to apply (simplified) cost benefit analysis, decision analysis and economic optimization for engineering projects<br>
>* Be able to quantify understand, apply and derive safety standards for individual and societal risk <br>

# **3 Risk Analysis and risk evaluation**

<div style="text-align: justify">This section deals with the analysis and evaluation of risks. Firstly, the concepts of risk (section 3.1) and risk analysis (3.2) are introduced. The sections after that introduce approaches for risk evaluation: general decision theory (3.3), cost benefit analysis (3.4) and safety standards that focus on the risk to life (3.5). The relationship between safety standards and engineering design is indicated in section 3.6.</div.>

## **3.1 Risk**

### **3.1.1 General definition of risk**

<div style="text-align: justify">Almost all activities in life are characterized by some level of risk. Especially in the design and management of engineering systems risk and safety are key concepts and need to be taken into account explicitly. In social discussions no unambiguous meaning is assigned to the concept of risk. Two definitions given in the Oxford dictionary are: 1) a situation involving exposure to danger; 2) the possibility that something unpleasant or unwelcome will happen.</div>
<div style="text-align: justify">The first definition focuses on the consequences, the second on the possibility or probability. Quantifying and evaluating risks based on merely the probabilities or consequences is less realistic. For example, the risk of losing € 100 with a probability of 50% is different than the risk of losing € 1000 with the same probability. Also, the risk associated with losing a given sum of money will depend on the probability of the event.</div>
An often-used definition considers risk as expected value:<br>
<br>
<div style="text-align: center"><em> Risk is the probability of an undesired event multiplied by the consequences</em></div>
<br>

The unit of risk now depends on the units of probability and consequences. The probability of an event is generally expressed as the probability per unit time, for example per year. The consequences of an undesired event are often multi-dimensional, i.e. they can consist of different types of consequences, such as material, ecological damages, injuries and fatalities (see section 3.2.2 for further details). In many applications in engineering consequences are expressed by means of a monetary value. The unit of the risk (or expected value $
 E(d)$ ) then becomes € per year. For a case with one event scenario <em>i</em>  with probability <em>$p_{i}$ </em> it yields:
 $$
 E(d) = p_{i}d_{i}                                         (3.1) 
 $$										
A more general definition of risk has been given by Kaplan and Garrick (1981):
><em>Risk is a set of scenarios (<em>$s_{i}$ </em> ), each of which has a probability (<em>$p_{i}$ </em> ) and a consequence (<em>$d_{i}$ </em>)</em><br>

This definition of Kaplan and Garrick allows the use of various so-called risk metrics (or risk measures) to quantify or depict the risk. The expected value of the damage for a set of multiple discrete scenarios{1,....,<em>n</em>} , can be expressed as:
  	$$
	E(d) = \sum_{S_{i=1}}^{n}p_{i}d_{i}								(3.2)
    $$

 <br> 
   <figure>
<center><img src="1.png" style="width: 300px; height: 200px;"/></figure><br>Figure 3.1 FN curve, showing the probability of exceedance of a certain number of fatalities N on Log-Log scale.</center>
<figcaption align = "center"></figcaption>                               
<br>       
The expected value does not give insight in the magnitude of probability and consequences and the contribution of individual scenarios. Therefore, an often-used alternative risk metric is the risk curve. It shows the probability of exceedance of a certain magnitude of consequences. A well-known example of such a risk curve is the FN curve, which displays the probability of exceedance of <em>N</em> fatalities. The values on both axes are generally shown on a logarithmic scale, see Figure 3.1Figure 3.1 for an example. The FN curve was originally introduced for the assessment of the risks in the nuclear industry (Farmer, 1967; Kendall et al., 1977) and is now used to display and limit risks in various countries and sectors. Further information on the use of FN curves and a simple example of how to construct such a curve are included in section 3.5.1. 

### **3.1.2 Other risk definitions**
In the remainder of this lecture notes and the course the definitions from the previous paragraph will be applied. Since (civil) engineers will work in a broad domain of applications it is useful to highlight some risk concepts used in other domains.

Within economics, risk is generally associated with a deviation from the expected return or the probability of loss. In social sciences risk is often considered as a contextual notion or social construct. Vlek (1996) has summarized 11 formal definitions used in social sciences, see Table 3.1. In some of these definitions (e.g. numbers 2 and 4) the perceived seriousness of the undesired consequences plays an important role. Examples of other, more informal risk definitions used in psychology are “the lack of perceived controllability”, “set of possible negative consequences” and “fear of loss” (Vlek, 1996). 

Substantial research has focussed on the factors that determine the perception of risk (e.g. Slovic, 1987, Vlek, 1996). Examples of factors that influence risk perception include: the degree of damage, the controllability of and familiarity with the hazards, the extent of benefits from an activity, and voluntariness of exposure. 

Table 3.1 Formal definitions of risk used in social sciences (Vlek, 1996 )

|    |       |
|:----|:---------------------------------------------------------------------------------------------------------|
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


The definitions applied in the research on natural hazards, often define risk in terms of more qualitative concepts such as hazard, vulnerability and exposure<br> 

>>* Hazard: A dangerous phenomenon, substance, human activity or condition that may cause loss of life, injury or other health impacts, property damage, loss of livelihoods and services, social and economic disruption, or environmental damage<br> 
>>* Vulnerability: The characteristics and circumstances of a community, system or asset that make it susceptible to the damaging effects of a hazard<br> 
>>* People, property, systems, or other elements present in hazard zones that are thereby subject to potential losses<br>

## **3.2 Risk Analysis**

### **3.2.1 General** 
The previous section made it clear that risk is a function of probabilities and consequences. The risk analysis therefore consists of an analysis of probabilities and consequences of undesired events in a given system. Alternative terms used in literature are risk assessment and quantitative risk analysis (QRA). 

A risk analysis is carried out because involved parties (e.g. designers, managers, decision makers) want to identify and evaluate the risks and decide on their acceptability. Outcomes of risk analysis can be used in the design process to decide on the required safety levels of new systems (e.g. a new tunnel) or to support decisions on the acceptability of safety levels and the need for measures in existing systems (e.g. a flood defence system). A quantitative measure of some form is needed to transfer decisions on acceptable safety into a technical domain (Voortman, 2004). Examples are choices in the design of civil structures, such as the height of a flood defence or the strength of a building. Also, risk analysis can be used to analyse the effectiveness of risk reduction measures, incl. management and maintenance strategies. Overall, the risk analysis aims to support rational decision-making regarding risk-bearing activities (Apostolakis, 2004). Moreover, a risk analysis provides insight in mechanisms of system failure and the associated failure probabilities and consequences. As such, it can also serve as a tool of communication and management. Insights of the risk analysis can be used to optimize system design and management and often there is a direct link to quality assurance. 

### **3.2.2 Elements in a risk analysis**

In general the following elements can be identified within risk analysis, see the scheme in Figure 3.2 (Based on (CUR, 1997; CIB, 2001; Faber and Stewart, 2003; Jongejan, 2008): 

>>* System definition and setting the scope and objectives of the analysis;
>>* Qualitative analysis of undesired events; 
>>* Quantitative analysis of the risk;
>>* Risk evaluation (of the acceptability of the risk)

Some more information on these steps is given in the following paragraph. In addition to the steps in risk assessment of a given system, risk management also includes the element ‘risk reduction and control’. Dependent on the outcome of the former phase measures can be taken to reduce the risk. This will lead to changes in the system configuration and the risk level. If the risk analysis is used in the design of systems, the steps are often repeated several times with adjusted system specifications to obtain an optimal design. It should also be determined how the risks can be controlled, for example by monitoring, inspection or maintenance.

<figure>
<center><img src="2.png" style="width: 250px; height: 300px;"/></center></figure>
<figcaption align = "center">Figure 3.2 Schematic view of steps in risk assessment and risk management.</figcaption> <br>


It is noted that a (probabilistic) risk analysis is different  from a (deterministic) scenario analysis. A risk analysis is based on quantitative analysis of all (known) undesired events and their probabilities and consequences. A scenario analysis considers one (or a limited number) of design scenarios, often without considering its failure probability. Both approaches are complementary, as a scenario analysis considers one of the scenarios from the risk analysis. 

In the Netherlands, scenario analysis is often used for evaluating disaster preparedness and designing the capabilities of emergency management services. For example, in the design of the Green Heart Tunnel which is a part of the high speed rail line in the Netherlands, a single accident scenario was chosen to design the emergency exits out of the tunnel. Analysing a high impact, low probability scenario in detail may provide helpful clues about the effectiveness of particular safety measures or crisis management actions. While such analyses may be helpful, it would be wrong to assume that such high-impact, low probability scenarios should always be properly manageable by emergency responders. This is because the probability of harm should be an integral part of any cost-benefit or cost-effectiveness analysis (Jongejan et al., 2011).

### **3.2.3 Steps in Risk management**

This section gives some more information on the steps in the risk analysis and some fundamental concepts in risk analysis.
>>**1. System definition**

This step entails the definition and description of the system as well as the scope and objectives of the analysis.  The process or system under consideration can usually be described as a so-called input-output element. Here the system is assumed to be failing if no output takes place. Usually a system is divided into components and subsystems, which can all be schematised as an input-output elements. By means of the internal relations the components and subsystems together form a configuration that is representative of the total system. Further information on the decomposition and analysis of system is provided in section 3.5 of these lecture notes.

A system can be represented in terms of physical components, organizations and users, and an external environment. In order to analyse failure and risks, not only physical components, but also organizations and operators and users need to be considered (see e.g. Bea, 1998). Different groups of organizations and persons will be involved in different roles. There are the professionals responsible for the operations and management of the system (e.g. the pilots and crew in an aircraft), potential users of a system (passengers), and external partiers  (people living near the airport exposed to risk and noise). Each of this group has a different “relationship” and attitude towards the risk and this could affect its acceptability. For example, a higher risk might be acceptable for pilots and crews in an aircraft (who have a direct benefit) than for regular passengers. Finally, the external environment (e.g. wind or waves) will determine the loads on the system and affect the potential failure mechanisms.
<br> 
>>**2 Qualitative analysis**

In this step, potential hazards, undesired events, failure mechanisms and scenarios are identified and described. An important goal of this phase is to gain insight, as complete as possible, into all possible undesired events and their consequences. For most systems, multiple undesired events can be distinguished. For example, two events with different impacts that can both lead to flooding of a polder are 1) the inflow of large amounts of water due to a dike failure; 2) the inflow of smaller amounts of water when a sluice gate is not closed. 

When a system or part of it no longer fulfils one or more desired functions, this is known as failure. It means that the state of the system changes from normal operation of failure. The state of failure can be reached through different failure mechanisms (or failure modes). For example, a dike can fail due to overtopping, but also due to geotechnical failure mechanisms such as instability or piping. A **limit state** is a condition of a structure beyond which it no longer fulfils the relevant design criteria (Eurocode, 2001). In practice two types of limit states are distinguished: the serviceability and the ultimate limit states abbreviated as SLS and ULS respectively.  

>>* In the case of the exceedance of ultimate limit state (ULS) failure or collapse of a system or structure occurs. This, for instance, occurs if the breakwaters of a harbour entrance are destroyed as a result of extreme conditions. An example from structural engineering is the collapse of a roof of a building
>>* In the case of exceedance of the serviceability limit state (SLS) exceedance leads to temporary and/or partial failure. An example of this state is the non-workability in a harbour, due to waves that are temporarily too high. Another example could be too much vibration of a structure, so that the users experience discomfort. 
	
	Further information on the use of the SLS and ULS concepts in civil engineering is included in chapter 10.
	
	In a risk analysis, it is very important to get an overview of the various undesired events and failures before proceeding with a quantitative analysis. In practice, many accidents are caused by failing to identify failure modes.
	Finding a list of threats and failing modes that is as complete as possible, is not an easy task. Aids are data banks, literature studies, interviews, experiences with comparable systems, brainstorm sessions et cetera. Techniques for systematically identifying undesired events (e.g. FMEA (Failure Modes and Effects Analysis) are treated in more detail in section 9.4 of the chapter on reliability of systems.
	
**3 Quantitative analysis**

The probabilities and consequences of the defined undesired events are determined in this step. The risk is quantified in a risk number or graph as a function of probabilities and consequences (see section 3.5.2 for an example).
The probability of failure can be quantified using the (previously) introduced limit state. A limit state Z can be assessed by considering the resistance R and the loads S, i.e.
$$
  Z = R-S										(3.3)
$$  
Failure occurs when $R<S$, so when $Z<0$ . Techniques for computing the probability of failure, i.e. $ P(Z<0)$, are treated in more detail in later sections of these lecture notes.
After failure has been defined and analysed, the consequences of the event are quantified. First, the physical effects associated with the undesired event have to be considered, e.g. heat and / or smoke from fire, or inflow of water due to dike breach. Depending on whether people or objects are exposed to the physical effects, damages, life loss or other impacts can occur.
As an example the failure of a dike for a set of discrete events is considered:

>>* The probability that a dike fails, $P(E_{1})$
>>* The conditional probability that water flows into the polder given a dike breach $P(E_{2}|E_{1})$
>>* The probability of damage given dike breach and inflow into the polder $P(D|E_{1}\cap E_{2})$<br>

The probability of damage can now be computed by combining these terms 

  >>>>>$P(D)=P(E_{1})P(E_{2}|E_{1})P(D|E_{1}\cap E_{2})$	(3.4)

As introduced in section 3.1, multiple types of consequences can be caused by one disaster. Table 3.2Table 3.2 gives an overview of the different types of consequences of the failure of large engineering systems. The damage is divided into tangible and intangible damage, depending on whether or not the losses can be assessed in monetary values. Another distinction is made between the direct damage, caused by physical effects of the event, and damages occurring outside the directly exposed area. The latter occurs when companies outside a flooded area experience damages, due to loss of demand from customers in the flooded area. In a risk analysis it is desired to take into account a complete set of impacts. Since a lot of the items from the table cannot be quantified easily, the quantitative analysis and risk evaluation are often focused  on economic damages and life loss.
>>>Table 3.2 General classification of damages, based on (Vrouwenvelder and Vrijling, 1996)

|          	| Tangible                                      	| Intangible                     	|
|----------	|-----------------------------------------------	|--------------------------------	|
| Direct   	| Residences                                    	| Fatalities                     	|
|          	| Structure inventory                           	| Injuries                       	|
|          	| Vehicles                                      	| Animals                        	|
|          	| Agriculture                                   	| Utilities and communication    	|
|          	| Infrastructure and other public facilities    	| Historical and cultural losses 	|
|          	| Business interruption                         	| Environmental losses           	|
|          	| Evacuation and rescue operations              	|                                	|
|          	| Reconstruction of flood defences              	|                                	|
|          	| Clean up costs                                	|                                	|
| Indirect 	| Damage for companies outside the exposed area 	| Societal disruption            	|
|          	| Substitution of production outside the area   	| Damage to government           	|
|          	| Temporary housing of evacuees                 	|                                	|<br>

**4 Risk evaluation**


<div style="text-align: justify">In the risk evaluation phase the decision is made whether the risk is acceptable or not and whether risk reduction measures need to be implemented. Or in other words, it is attempted to answer the question “how safe is safe enough?” (Starr, 1967). The results of the quantitative analysis provide input for risk evaluation and decision making. 
Different quantitative approaches can be used to support risk evaluation, which will be outlined more in detail in the coming sections.<br>

>> 
  >* **<div style="text-align: justify">Decision making under uncertainties** (Section 3.3): Recording different variants, with associated risks, costs and benefits, in a matrix or decision tree, serves as an aid for making decisions. With this, the optimal selection can be made from a number of alternatives.

  >* **<div style="text-align: justify">Cost benefit Analysis** (section 3.4.1): the costs and benefits of risk reduction measures are considered.  When a very large number of design choices are possible, an **economic optimization** (section 3.4.2) can be applied to select an optimal system design, based on costs and benefits of risk reduction.

  >* **<div style="text-align: justify">Safety standards** (section 3.5): Comparing the risk with predetermined safety standards which often focus on loss of life.</div>


<div style="text-align: justify">However, given the nature of the key question (how safe is safe enough?) several political, psychological and social processes play a role in the evaluation of risk. This means that risk evaluation is not a purely technical process, but will involve many subjective elements. One of the difficulties facing regulators is that people’s preferences and risk attitudes may diverge and that costs and benefits may not be distributed evenly. This means that a single, collective decision, in practice, has to be based on strongly divergent individual preferences. In practice, this implies that devising collective decision making procedures is inevitably political. This ambiguity can also be found in the numerous interpretations of “the” precautionary principle, which is interpreted by some as a decision making criterion that requires proof of harmlessness (a scientific impossibility), whereas it is seen by others as a decision making procedure that puts emphasis on dialogue and stakeholder involvement, (e.g. Jongejan, (2008 ).</div>

**Risk reduction and risk control**

<div style="text-align: justify">If the risks are considered unacceptable several forms of risk reduction can be implemented. These can be changes to the engineered system, or changes to the organization and management.  From analysis of accidents it appears that human and organizational errors are still a major cause of failure in civil engineering. It seems that the only suitable way to reduce human errors is by the incorporation of sufficient control in the different phases of the construction process (Taerwe, 1986) and by a thorough education of all personnel involved. Therefore, an extensive interaction between the safety methodology and the quality management is a necessity in order to guarantee the safety of our structures.</div>

## **3.3 Decision-making under uncertainties**

<div style="text-align: justify">Decision-making under uncertain conditions is part of everyday life, e.g. when choosing to buy a lottery ticket or choosing to take an umbrella during cloudy weather. In contrast to the rather intuitive decision making in everyday matters, a structured analysis of different alternatives with associated risks, costs and benefits is very useful for decisions in (civil) engineering. This chapter offers a very basic introduction into the decision theory with applications to decision problems in the civil engineering domain. Further reference is made to the work by other scholars for more rigorous and detailed treatment of this topic, see for example (Raiffa and Schlaifer, (1961); Benjamin and Cornell, (1970 ).</div>

### **3.3.1 Introduction and basics**

Making a decision is in fact choosing from alternatives. The decision theory  is based on the classic “Homo Economicus” model. The Homo Economicus:
>>
	>* has complete information about the decision situation;
	>* knows all the alternatives;
	>* knows the existing situation;
	>* knows which advantages and disadvantages each alternative provides, be it in the form of random variables;
	>* strives to maximise that advantage (formally called utility).

<div style="text-align: justify">
The decision-making concept discussed in these lecture notes assumes this model. Decision-making in practice is often different since the above conditions will not be fulfilled. There can be multiple decision makers and multiple objectives. Also, the decision maker does not know all the alternatives or their outcomes. For many practical cases this has led to an extension of the decision model, but not to a fundamental adjustment of the classical model.
Within a decision problem the following characteristics can be distinguished: </div>
>>
	>* the set of all possible actions or decisions $\textit{(a)}$, from which the decision maker can choose
	>* the set of all (natural) circumstances ( $\theta$ ) that influence the outcomes
	>* the  set of the set of all possible results ( $\omega$ ), which are functions of the actions and circumstances: $\omega = f ( \textit{a} ,\theta )$

The actions, natural circumstances and the outcomes can be shown in a so-called decision tree (Figure 3.3).

<figure>
<center><img src="3.png" style="width: 600px; height: 300px;"/></center></figure>
<figcaption align = "center">Figure 3.3 Decision tree .
 </figcaption><br>
 

<div style="text-align: justify">
Based on the possible results a choice is made for an action. To be able to assess the different results, a numerical value is assigned to each outcome of $\omega$ , which can be used to establish the benefit of each outcome. This number can be a monetary value, a number on an arbitrary scale or utility - as long as the decision maker(s) can establish a consistent ranking of the outcomes with it. In the last two cases the benefit has no absolute value, but only gives the relative value of the different outcomes. Utility *( u )*  is a concept used to rank the possible outcomes according to the preferences of the decision maker. Utility *(<em> u </em> )*  values are between $0\leq\textit u ({\omega})\leq 1$ . A utility function can be used to characterize the relative utility of various outcomes. The elaborations below are based on the monetary values as a measure for the outcomes and assume a risk neutral decision maker. This is a decision maker who is indifferent between choices with equal expected outcomes, even if one choice is riskier than the other. For example, a risk neutral decision maker would have the same preference for a € 400 pay out, or a 50/50 bet with a coin toss with outcomes of € 0 (head) or € 800 (tail). Utility and risk aversion are further discussed in section 3.3.3</div>

### **3.3.2 Decision rules**
<div style="text-align: justify">
Once a set of actions, circumstances and outcomes is known, various approaches can be used to come to a preferred decision. Various deterministic decisions  rules are available which do not take into account the probabilities of the possible circumstances and outcomes. One example of such a decision rule is the minimax criterion: a decision maker wants to minimize maximum losses. This is in fact a risk-averse criterion. Another example is the maximax criterion: a decision maker chooses the option with the maximum income and is risk seeking. 

Although these decision rules are helpful in some cases, the probability of occurrence of certain circumstances is a key feature of the decision problem. Information on the probability of outcomes is needed for an optimal choice of action(s). For example, when making a decision to start a business in soup or ice cream, the decision maker would want to know what the probabilities of rainy or sunny weather are. Selling ice cream in Dutch winter will probably not make a good (expected) profit, but it would be a profitable business in a Mediterranean summer.

Therefore it is necessary to include information on the probabilities of circumstances and outcomes, in order to determine a rational action with the highest expected value of the benefit. This theory is known as the Bayesian decision theory. In a probabilistic or Bayesian decision framework the optimal action a* is defined as the one maximizing the expected utility. The following formula is found for the case with discrete outcomes.</div>
$$
a^*: \max_a E(u(a, \theta))=\max _a \sum_\theta u(a, \theta) P\left(\theta_i\right)
$$						(3.5)
In which $u(a, \theta)$  – utility of action a under circumstance $\theta$. $P(\theta)$  is the probability that circumstance $\theta_{i}$ occurs.

A rational decision is choosing the action with the highest expected (utility) value or highest benefit if outcomes are expressed in monetary values. This is illustrated in the example below. Note that other examples in these lecture notes will also be based on monetary values.

**Example 3.1: buying shares or bonds?**

Suppose a person has EUR 1000 at his or her disposal and is given the choice to invest this money in bonds or in shares of a given company.  It is known that, on a yearly basis, 3 % of the current market value is distributed as interest on the bonds. The dividend of the shares depends on the company’s profit. Suppose that the board of directors have made the following agreements: 
>>* for a profit smaller than 5 % of the shareholders capital, no dividend is paid;
>>*	for a profit larger than 5 % of the shareholders capital, dividend is paid, the percentage of which corresponds to 3 % of the current market value of the shares;
>>* for a profit larger than 10 % of the shareholders capital, the dividend corresponds to 6 % of the current market value of the shares.

The set of actions A has two elements: <em>$a_{1}$</em>   = investing in shares AND <em>$a_{2}$</em> = investing in bonds
The set or market circumstances N has three elements, namely:  
>>$\theta_{1}$ = company profit ≤5 %<br>
>>$\theta_{2}$= 5 % < company profit ≤ 10 %<br>
>>$\theta_{3}$= company profit > 10 %<br>

Assume the inflation amounts to 2 %. The set of outcomes ω contains three possible outcomes for the shares:<br>
>>$\omega_{1}$= return (0 % -2 %)   = -2 % per annum<br>
>>$\omega_{2}$	 = return (3 % -2 %) =  1 % per annum<br>
>>$\omega_{3}$	 = return (6 % -2 %) =  4 % per annum<br>

Note that for the bonds the net outcome always yields $\omega_{2}$  =1% (i.e. 3% interest – 2% inflation). The outcomes can be shown in a decision tree (see Figure 3.4Figure 3.4) or in a table (see Table 3.3).<br>
Table 3.3 Outcomes given the decisions (a1,a2) and market conditions ($\theta_{1}$,$\theta_{2}$,$\theta_{3}$). 
	
	  
  
  |  ||Market circumstances||
  |---|-------------------|---|---|
  |Actions|$\theta_{1}$|$\theta_{2}$|$\theta_{3}$
  |<em>$a_{1}$</em> : buy shares|-2 %|1 %|4 %|
  |<em>$a_{2}$</em> : buy bonds |1 %|1 %|1 %|
<br>
<figure>
<center><img src="4.png" style="width: 600px; height: 300px;"/></center></figure>
<figcaption align = "center">Figure 3.4 Decision tree for the example of buying shares (a_{1}) or bonds ($a_{2}$).</figcaption><br>
 

The deterministic decision rules can be applied to this example. Minimax would result in investing in bonds ($a_{2}$), maximax would result in buying shares.
The optimal decision can be found by taking into account the probabilities of the market circumstances. These three circumstances are assumed to be exhaustive and mutually exclusive (i.e. outcomes cannot overlap and the sum of probabilities equals 1). The probabilities are estimated at $\textit P(\theta_{1})$ = 0.2; $\textit P(\theta_{2})$ = 0.3; $\textit P(\theta_{3})$ = 0.5. These probabilities can now be included in the decision tree. The expected value of the return of the actions is as follows:

>>>Buying shares: 0.2(-2 %) + 0.3 (1 %) + 0.5 (4 %) = 1.9 %.<br>
>>>Buying bonds: 1%<br>

In this case the expected outcome is larger for buying shares than for buying bonds. So for a risk neutral decision maker buying shares (a1) would be the preferred action. Note that this action also includes a probability of 0.2 of a loss. This is also  expressed by a higher standard deviation of the expected outcomes for buying shares. The above example can also be extended by applying different utility functions for various outcomes.

In the previous example, the number of circumstances is limited and the probability distribution of the circumstances is discrete. For many decision problems this is not the case. The state of nature, for instance, can assume many values that cannot be made discrete. This, for example, would have been the case if the dividend in example 0 had been a percentage of the profit. In such cases a probability density function can be used to characterize the spectrum of outcomes. Using a continuous form of formula (3.5)(3.5), the expected value of various actions, and the optimal action / decision can be identified. 
In taking decisions with uncertainties, it appears that probabilistic calculation techniques are a valuable aid to reach a rational choice. This is particularly the case if risks are dependent on the possible decisions. In such cases, Bayesian decision theory minimizes the total costs (i.e. investment costs plus risk in terms of potential losses). This can best be illustrated by means of an example from the civil engineering domain.

**Example 3.2: drainage of a construction site – decision tree**

In a river polder a basement has to be built in an excavated construction site. The construction site is made of sheet piling and the bottom is sealed off with a clay layer with a thickness (d) of, on average, $\mu_{d}$ = 2.5 m. The thickness is not known exactly; it follows from measurements that the thickness has a normal distribution and a standard deviation of $\sigma_{d}$ = 0.2 m.
The river cuts through the clay layer and the underlying sand layer is fed by the river (see Figure 3.5). The groundwater potential in the upper layer equals the potential in the deep sand layer. The upward water pressure under the sealing layer is assumed to be a direct function of the river levels. The fluctuating river levels result in fluctuations of the upward pressure under the sealing layer.<br>
Measurements of the groundwater levels over a long period have given an insight into the extreme groundwater levels. The maximum upward pressure $(\textit h)$ under the sealing layer in the construction period has an a normal distribution with an expected value of $\mu_{\textit h}$ = 4 m water column and a standard deviation of   $\sigma_{\textit h}$= 0.75 m water column.<br>
From these values the probability of flooding due to bursting of the clay layer due to upward water pressure can be calculated for the construction period. We define a limit state function $\textit Z = R - S$ <br>
$\textit R$ is the strength consisting of the weight of the clay layer and $\textit S$ is the water pressure. We find:
  $$ 
  Z=\rho_c d-\rho_w h (3.6)
  $$									
In which: $\rho_c$  – density of clay (=20kN/m3); $\rho_w$  – density of water (=10 kN/m3) 
The probability of failure $\textit P(Z<0)$ for this situation can be found by calculating the mean and standard deviation of $\textit Z$ :<br>
   $$
   \mu_Z=\rho_c \mu_d-\rho_w \mu_h=202.5-104= 10 \mathrm{kN} / \mathrm{m}^2 \\
   $$
   $$
   \sigma_z=\left(\rho_{\mathrm{c}}^2 \sigma_{\mathrm{c}}^2+\rho_{\mathrm{w}}{ }^2 \sigma_{\mathrm{h}}^2\right)^{0.5}=8.5 \mathrm{kN} / \mathrm{m}^2                             (3.7)
   $$           							
According to Chapter 2.6.1, we find  $\textit P(Z<0)=\Phi\left(-\mu_z / \sigma_z\right)=\Phi(-1.17)=0.12$. This is indicated as the initial failure probability $P_{f, 0}$   .

<figure>
<center><img src="5.png" style="width: 400px; height: 200px;"/></center></figure>

<figcaption align = "center">Figure 3.5 Situation: Excavation near a river </figcaption><br>
 
The effect of a drainage system in the construction site (see Figure 3.6) on the groundwater levels has been reviewed using groundwater flow calculations. It appears that it reduces the mean value of the maximum water levels to $\mu _{h}$ = 3.52m and the standard deviation remains the same. In this case the failure probability is reduced to 0.04. Such a drainage system costs EUR 150,000.
 
<figure>
<center><img src="6.png" style="width: 400px; height: 200px;"/></center></figure>
<figcaption align = "center">Figure 3.6 Drainage around the excavation. </figcaption><br>

The flooding of the construction site will result in the buoyancy of the basement resulting in damages are estimated at EUR 5,000,000. The designer of the construction site is faced with the choice whether or not to include drainage facilities in the design of the construction site. 
To provide insight the decision problem is illustrated with a decision tree. For this, the sets of actions, circumstances and outcomes have to be defined first:<br>
The set of actions A consists of:<br>
>>$\textit a_{1}$= excavation without drainage<br>
>>$\textit a_{1}$= excavation with drainage<br>

The set of circumstances N is formed by:<br>
>>$\theta_{1}$= the sealing layer remains intact <br>
>>$\theta_{2}$= the water pressure exceeds the weight of the sealing layer<br>

The set of outcomes $\Omega$ consists of:<br>
    
>>$\omega_{1}$ = nothing happens; loss = € 0<br>
>>$\omega_{2}$ = the construction excavation is flooded: loss =€5,000,000<br>

The previous eligibility analysis has shown that the probability of flooding of the excavation equals $P_{f}$ = 0.12 for a situation without drainage and $P_{fd}$ = 0.04 with drainage.<br>

Without drainage, the risk, defined as the expected value of the loss, is: 0.12 · € 5,000,000 = € 600,000. With drainage the risk is: 0.04 · € 5,000,000 = € 200,000.Costs and probabilities can also be shown in the decision tree (see Figure 3.7). The expected values of the costs can be calculated for the different actions by adding the present values of the cost of actions and risk:<br>
>>$\textit a_{1}$ : expected value (additional) costs = risk =€ 600,000<br>
>>$\textit a_{2}$ : expected value (additional) costs = extra costs + risk = €150,000 + € 200,000 
= € 350,000<br>

This implies that the construction of the drainage system is rationally speaking the best decision for a risk neutral decision maker.
 
<figure>
<center><img src="7.png" style="width: 600px; height: 300px;"/></center></figure>
<figcaption align = "center">Figure 3.7 Decision tree with probabilities and costs.</figcaption><br>


### **3.3.3 Utility functions**

The elaborations in the previous sections were based on monetary values as a metric for outcomes and a risk neutral decision maker. This section will provide some basic information on utility functions and various risk attitudes.

Utility is a concept used to rank the possible outcomes according to the preferences of the decision maker. Utility $(\textit u)$ values are between $0\leq \textit{u}(\omega)\leq 1$. A utility function can be used to characterize the relative utility of various outcomes. The utility function depends on the preferences and attitude of the decision maker. An example of three different utility functions is given in Figure 3.8Figure 3.8 for an example of an activity with potential monetary benefits between € 0 and € 1000. In the case of a risk neutral decision maker the utility increases linearly with the benefits. In the case of the risk aversion relatively small benefits are already given a high utility. A risk seeking decision maker gives a relatively low value to smaller benefits, but high utility values to larger incomes. 

<figure>
<center><img src="8.png" style="width: 600px; height: 300px;"/></center></figure>
<figcaption align = "center">Figure 3.8 Example of a utility function for monetary benefits.
</figcaption><br>
 
**Example 3.3: a bet**

The utility functions can be applied to a simple example. Assume that a student has the chance to receive a guranteed payout of €400. Alternatively, a bet can be organized with a $\textit p$ =  0.5 chance of a payout of € 800, and a (1-$\textit p$) = 0.5 chance of no payout. A risk neutral decision maker would be indifferent between both choices, as they have the same expected outcome – i.e. €400 gain – and a utility value of $\textit u$(€400) = $\textit{pu}$(€800)+(1-$\textit p$)$\textit u$(€0)$ = 0.4.<br>
We now apply the two other utility functions. For the risk averse function  we find the following:

The expected utility of the direct payout equals $u_{R A}( € 400 )=0.75 \\$= 0.75<BR>
The expected utility of the bet becomes: $0.5 u_{R A}(€ 800)+0.5 u_{R A}(€ 0)=0.5 \cdot 0.97+0.5 \cdot 0=0.485$<br>

In this case the expected utility of the direct payout is higher and this is the preferred decision of the risk averse decision maker. For the risk seeking function  we find the following:

The expected utility of the direct payout equals $u_{R A}( € 400 )$  = 0.1<br>
The expected utility of the bet becomes: $0.5 u_{R S}(€ 800)+0.5 u_{R S}(€ 0)=0.5 \cdot 0.57+0.5 \cdot 0=0.285$<br>
In this case the expected utility of the bet is higher. The preferred decision of the risk seeking decision maker is the bet.

So for the example of the bet, the risk neutral decision maker is indifferent between the bet and the direct payout. The risk averse decision maker would accept a lower payout, rather than taking the bet. The risk seeking decision maker accepts the bet, even if the guaranteed payout is higher than the expected outcomes of the bet. The same concept can also be applied to losses, a decision-maker can be risk averse against events with large consequences. For example, a civil engineering company could be risk averse in making decisions about bidding for projects with financial risks that could threaten the financial stability of the company. On the other hand, a government with a large portfolio of projects may actask  more risk neutral. The various risk attitudes can also play a role in making investment decisions (see also 3.4.2)section 0 ). A risk averse investor would prefer investments (such as bonds or guaranteed loans with relatively low expected returns) over investments in stocks that have higher expected returns, but also a higher chance of losing money. The principle of risk aversion is also related to decisions about insurances. For example, most people are risk averse against losing their belongings in a large house fire. They are willing to pay an annual premium that is higher than the expected losses due to the fire. Finally, a further discussion of a related risk aversion concept regarding  s accidents with large numbers of fatalities is included in section 3.5.
