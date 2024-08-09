---
title: Reversal Potential
description: An introduction to reversal potentials, the Nernst equation, and their effect on synaptic currents
---

In a biological membrane, the **reversal potential** (also known as the **Nernst potential**, or **equilibrium potential**) of an ion is voltage at which there is no net flow of that ion from one side of the membrane to the other. When the voltage of a neuron is at the reversal potential of an ion, opening of an ion channel permeable to that ion will produce no current. Below or above the reversal potential for an ion, the opening of an ion channel permeable to that ion will produce a current. Whether the current is inward out outward depends on the direction of ion flow and the charge of the ion.

## Spontaneous GABAergic IPSCs

-105 mV                                      | -55 mV                                        | +5 mV                                        
-------------------------------------------- | --------------------------------------------- | ---------------------------------------------
<img src="/patch/img/pages/reversal/psc-inward.png" class="img-fluid"> | <img src="/patch/img/pages/reversal/psc-neutral.png" class="img-fluid"> | <img src="/patch/img/pages/reversal/psc-outward.png" class="img-fluid"> |

**Reversal potential of isolated spontaneous GABAA (chloride) currents:** Voltage clamp trace at 3 different voltages demonstrates how cell voltage can determine current direction. In this example, GABAA currents (mediated by Cl- ions) are observed. Pharmacological inhibition of glutamate receptors means these transients are likely all GABA-mediated currents. In these conditions, the reversal potential for Cl- is near -55 mV. Clamping near the Cl- reversal potential minimizes the size of these currents. Clamping below or above the reversal potential magnifies these currents in opposite directions. At negative voltages, opening of chloride channels causes outflow of Cl- ions (inward current). At positive voltages, opening of the same channel causes inflow of Cl- ions (outward current).

## The Nernst equation

The Nernst equation allows you to calculate the reversal potential of an ion by knowing its concentration inside vs. outside the cell, its valence, and the temperature. [NernstCalc](https://swharden.com/software/NernstCalc/) and [Physiology Web](https://www.physiologyweb.com/calculators/nernst_potential_calculator.html) Nernst equation calculators are useful. Although reversal potential for an ion in patch clamp experiments can be predicted using expected concentrations of ion in the internal and bath solutions, it is often measured experimentally. Slight differences in the actual concentrations and measurement errors caused by liquid junction potentials can produce several millivolts of difference between the theoretical and actual reversal potential.

<img src="nernst-equation.png" class="d-block img-fluid mx-auto">

## Biphasic Spontaneous Currents

By voltage-clamping a neuron at the reversal potential of a specific ion, an experimenter can effectively silence currents produced by the flow of that ion. This technique is commonly used to measure isolated GABAA (chloride-mediated) currents and isolated AMPA (sodium-mediated) currents in the same cell by clamping at their reversal potentials in tandem. In addition, the experimenter can clamp between two reversal potentials to simultaneously view both currents which will diverge in opposite directions (sometimes called biphasic current transients).

-55 mV                                        | -25 mV                                          | +5 mV                                          
--------------------------------------------- | ----------------------------------------------- | ---------------------------------------------- 
<img src="/patch/img/pages/reversal/biphasic-in.png" class="img-fluid"> | <img src="/patch/img/pages/reversal/biphasic-both.png" class="img-fluid"> | <img src="/patch/img/pages/reversal/biphasic-out.png" class="img-fluid"> |
