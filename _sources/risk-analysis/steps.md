(risk_steps)=
# Steps in a Risk Analysis


The previous section made it clear that risk is a function of probabilities and consequences. The risk analysis therefore consists of an analysis of probabilities and consequences of undesired events in a given system. Alternative terms used in literature are risk assessment and quantitative risk analysis (QRA). 

A risk analysis is carried out because involved parties (e.g. designers, managers, decision makers) want to identify and evaluate the risks and decide on their acceptability. Outcomes of risk analysis can be used in the design process to decide on the required safety levels of new systems (e.g. a new tunnel) or to support decisions on the acceptability of safety levels and the need for measures in existing systems (e.g. a flood defence system). A quantitative measure of some form is needed to transfer decisions on acceptable safety into a technical domain (Voortman, 2004). Examples are choices in the design of civil structures, such as the height of a flood defence or the strength of a building. Also, risk analysis can be used to analyse the effectiveness of risk reduction measures, incl. management and maintenance strategies. Overall, the risk analysis aims to support rational decision-making regarding risk-bearing activities (Apostolakis, 2004). Moreover, a risk analysis provides insight in mechanisms of system failure and the associated failure probabilities and consequences. As such, it can also serve as a tool of communication and management. Insights of the risk analysis can be used to optimize system design and management and often there is a direct link to quality assurance. 

In general, the following elements can be identified within risk analysis, see the scheme in Figure 3.2 (Based on (CUR, 1997; CIB, 2001; Faber and Stewart, 2003; Jongejan, 2008): 

1. System definition and setting the scope and objectives of the analysis;
2. Qualitative analysis of undesired events; 
3. Quantitative analysis of the risk;
4. Risk evaluation (of the acceptability of the risk)

Each of these steps is described in more detail below, and provides context for the following chapters in this book. In addition to the steps in risk assessment of a given system, *risk management* also includes the element ‘risk reduction and control’. Dependent on the outcome of the former phase measures can be taken to reduce the risk. This will lead to changes in the system configuration and the risk level. If the risk analysis is used in the design of systems, the steps are often repeated several times with adjusted system specifications to obtain an optimal design. It should also be determined how the risks can be controlled, for example by monitoring, inspection or maintenance.

```{figure} ../figures/risk-steps.PNG
---
width: 250px
name: risk-steps
---
Schematic view of steps in risk assessment and risk management.
```

## 1. System definition

This step entails the definition and description of the system as well as the scope and objectives of the analysis.  The process or system under consideration can usually be described as a so-called input-output element. Here the system is assumed to be failing if no output takes place. Usually a system is divided into components and subsystems, which can all be schematised as an input-output elements. By means of the internal relations the components and subsystems together form a configuration that is representative of the total system. Further information on the decomposition and analysis of system is provided in section 3.5 of these lecture notes.

A system can be represented in terms of physical components, organizations and users, and an external environment. In order to analyse failure and risks, not only physical components, but also organizations and operators and users need to be considered (see e.g. Bea, 1998). Different groups of organizations and persons will be involved in different roles. There are the professionals responsible for the operations and management of the system (e.g. the pilots and crew in an aircraft), potential users of a system (passengers), and external partiers  (people living near the airport exposed to risk and noise). Each of this group has a different “relationship” and attitude towards the risk and this could affect its acceptability. For example, a higher risk might be acceptable for pilots and crews in an aircraft (who have a direct benefit) than for regular passengers. Finally, the external environment (e.g. wind or waves) will determine the loads on the system and affect the potential failure mechanisms.

## 2. Qualitative analysis

In this step, potential hazards, undesired events, failure mechanisms and scenarios are identified and described. An important goal of this phase is to gain insight, as complete as possible, into all possible undesired events and their consequences. For most systems, multiple undesired events can be distinguished. For example, two events with different impacts that can both lead to flooding of a polder are 1) the inflow of large amounts of water due to a dike failure; 2) the inflow of smaller amounts of water when a sluice gate is not closed. 

When a system or part of it no longer fulfils one or more desired functions, this is known as failure. It means that the state of the system changes from normal operation of failure. The state of failure can be reached through different failure mechanisms (or failure modes). For example, a dike can fail due to overtopping, but also due to geotechnical failure mechanisms such as instability or piping. A **limit state** is a condition of a structure beyond which it no longer fulfils the relevant design criteria (Eurocode, 2001). In practice two types of limit states are distinguished: the serviceability and the ultimate limit states abbreviated as SLS and ULS respectively.  

- In the case of the exceedance of ultimate limit state (ULS) failure or collapse of a system or structure occurs. This, for instance, occurs if the breakwaters of a harbour entrance are destroyed as a result of extreme conditions. An example from structural engineering is the collapse of a roof of a building
- In the case of exceedance of the serviceability limit state (SLS) exceedance leads to temporary and/or partial failure. An example of this state is the non-workability in a harbour, due to waves that are temporarily too high. Another example could be too much vibration of a structure, so that the users experience discomfort. 

   Further information on the use of the SLS and ULS concepts in civil engineering is included in chapter 10.

   In a risk analysis, it is very important to get an overview of the various undesired events and failures before proceeding with a quantitative analysis. In practice, many accidents are caused by failing to identify failure modes.
   Finding a list of threats and failing modes that is as complete as possible, is not an easy task. Aids are data banks, literature studies, interviews, experiences with comparable systems, brainstorm sessions et cetera. Techniques for systematically identifying undesired events (e.g. FMEA (Failure Modes and Effects Analysis) are treated in more detail in section 9.4 of the chapter on reliability of systems.


## 3. Quantitative analysis

The probabilities and consequences of the defined undesired events are determined in this step. The risk is quantified in a risk number or graph as a function of probabilities and consequences (see section 3.5.2 for an example).
The probability of failure can be quantified using the (previously) introduced limit state. A limit state Z can be assessed by considering the resistance R and the loads S, i.e.
$$
Z = R-S                                        
$$  
Failure occurs when $R<S$, so when $Z<0$ . Techniques for computing the probability of failure, i.e. $ P(Z<0)$, are treated in more detail in later sections of these lecture notes.
After failure has been defined and analysed, the consequences of the event are quantified. First, the physical effects associated with the undesired event have to be considered, e.g. heat and / or smoke from fire, or inflow of water due to dike breach. Depending on whether people or objects are exposed to the physical effects, damages, life loss or other impacts can occur.
As an example the failure of a dike for a set of discrete events is considered:

- The probability that a dike fails, $P(E_{1})$
- The conditional probability that water flows into the polder given a dike breach $P(E_{2}|E_{1})$
- The probability of damage given dike breach and inflow into the polder $P(D|E_{1}\cap E_{2})$

The probability of damage can now be computed by combining these terms 

$$P(D)=P(E_{1})P(E_{2}|E_{1})P(D|E_{1}\cap E_{2})$$                        

As introduced in section 3.1, multiple types of consequences can be caused by one disaster. Table 3.2 gives an overview of the different types of consequences of the failure of large engineering systems. The damage is divided into tangible and intangible damage, depending on whether or not the losses can be assessed in monetary values. Another distinction is made between the direct damage, caused by physical effects of the event, and damages occurring outside the directly exposed area. The latter occurs when companies outside a flooded area experience damages, due to loss of demand from customers in the flooded area. In a risk analysis it is desired to take into account a complete set of impacts. Since a lot of the items from the table cannot be quantified easily, the quantitative analysis and risk evaluation are often focused  on economic damages and life loss.
   Table 3.2 General classification of damages, based on (Vrouwenvelder and Vrijling, 1996)

|          | Tangible                                      | Intangible                     |
|----------|-----------------------------------------------|--------------------------------|
| Direct   | Residences                                    | Fatalities                     |
|          | Structure inventory                           | Injuries                       |
|          | Vehicles                                      | Animals                        |
|          | Agriculture                                   | Utilities and communication    |
|          | Infrastructure and other public facilities    | Historical and cultural losses |
|          | Business interruption                         | Environmental losses           |
|          | Evacuation and rescue operations              |                                |
|          | Reconstruction of flood defences              |                                |
|          | Clean up costs                                |                                |
| Indirect | Damage for companies outside the exposed area | Societal disruption            |
|          | Substitution of production outside the area   | Damage to government           |
|          | Temporary housing of evacuees                 |                                |

## 4. Risk evaluation


In the risk evaluation phase the decision is made whether the risk is acceptable or not and whether risk reduction measures need to be implemented. Or in other words, it is attempted to answer the question “how safe is safe enough?” (Starr, 1967). The results of the quantitative analysis provide input for risk evaluation and decision making. 
Different quantitative approaches can be used to support risk evaluation, which will be outlined more in detail in the coming sections.

**Decision making under uncertainties** (Section 3.3): Recording different variants, with associated risks, costs and benefits, in a matrix or decision tree, serves as an aid for making decisions. With this, the optimal selection can be made from a number of alternatives.

**Cost benefit Analysis** (section 3.4.1): the costs and benefits of risk reduction measures are considered.  When a very large number of design choices are possible, an **economic optimization** (section 3.4.2) can be applied to select an optimal system design, based on costs and benefits of risk reduction.

**Safety standards** (section 3.5): Comparing the risk with predetermined safety standards which often focus on loss of life.

However, given the nature of the key question (how safe is safe enough?) several political, psychological and social processes play a role in the evaluation of risk. This means that risk evaluation is not a purely technical process, but will involve many subjective elements. One of the difficulties facing regulators is that people’s preferences and risk attitudes may diverge and that costs and benefits may not be distributed evenly. This means that a single, collective decision, in practice, has to be based on strongly divergent individual preferences. In practice, this implies that devising collective decision making procedures is inevitably political. This ambiguity can also be found in the numerous interpretations of “the” precautionary principle, which is interpreted by some as a decision making criterion that requires proof of harmlessness (a scientific impossibility), whereas it is seen by others as a decision making procedure that puts emphasis on dialogue and stakeholder involvement, (e.g. Jongejan, (2008 ).

## Risk reduction and risk control

If the risks are considered unacceptable several forms of risk reduction can be implemented. These can be changes to the engineered system, or changes to the organization and management.  From analysis of accidents it appears that human and organizational errors are still a major cause of failure in civil engineering. It seems that the only suitable way to reduce human errors is by the incorporation of sufficient control in the different phases of the construction process (Taerwe, 1986) and by a thorough education of all personnel involved. Therefore, an extensive interaction between the safety methodology and the quality management is a necessity in order to guarantee the safety of our structures.

