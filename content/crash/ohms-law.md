---
title: Ohm’s Law
description: How Membrane Properties Influence Synaptic Currents
weight: 40
---

The [Introduction page](../intro) discussed how neural membranes can pass current (the flow of ions through ion channels) and have resistance (largely determined by the number of open channels in the membrane). An excitatory current passing into a neuron will raise its voltage by an amount dependent on its resistance. 

**The relationship between voltage, current, and resistance is described by Ohm's Law.** Ohm’s Law states that Voltage (V) is equal to current (I) times resistance (R), and is traditionally written as:

<div class="fs-5 m-3" style="font-family: serif";>
V = I × R
</div>

Ohm’s law can be adapted to describe how far a neuron's voltage will swing in response to a current flowing across its membrane:

<div class="fs-5 m-3" style="font-family: serif";>
∆V<sub>m</sub> = ∆I × R<sub>m</sub>
</div>

If we consider ΔV<sub>m</sub> to be an EPSP, and ΔI to be an EPSC, we can see how increasing Rm increases the voltage swing in response to an ESPC.

> 💡 **Note:** We previously discussed that resting voltage is a function largely of the Na<sup>+</sup>/K<sup>+</sup> ATP pump and K<sub>LEAK</sub> channels. It is important to note that Ohm’s Law is not used to determine resting voltage (resting voltage can be estimated by [the Goldman equation](https://en.wikipedia.org/wiki/Goldman_equation)). Instead, Ohm’s Law is best used to describe **voltage transients**, in response to **current transients** (such as synaptic inputs or current injection).

## Passive Membrane Properties Revisited

We [previously introduced](../passive-properties/) the major passive membrane properties, let's reconsider each in the context of Ohm's Law.

### Holding Current (Ih)
* Indicates the current required to clamp a neuron at a defined (holding) voltage.
* Relates to the total amount of current passing through all open ion channels in the neuron.
* Holding current (Ih) is usually called steady state current (Is) in the literature. 
* Since Rm varies with voltage (due to the electrostatic gradient of ions and opening/closing of voltage-gated ion channels), 
* Ih changes with voltage. Therefore, a current/voltage relationship is often plotted (an I/V curve).
* According to Ohm’s Law, Ih will vary inversely with Rm. When Rm is very high, small currents can swing the cell by large voltages. Conversely, the same voltage swing takes less current to achieve.

### Membrane Resistance (Rm)
* Indicates how resistive the neural membrane is to the flow of ions.
* Relates to the number of open channels in the neural membrane (the more open channels, the lower the Rm)
* Conductance is the inverse of resistance. A membrane with low Rm has high conductance. 
* Rm varies with voltage (due to the electrostatic gradient of ions and opening/closing of voltage-gated ion channels). If a neuron is said to have a given Rm, it is often implied that is the Rm at -70 mV.

### Access Resistance (Ra)
* Indicates the resistance between the recording pipette and the neuron.
* The primary source of access resistance is the resistance of the narrowest part of the pipette (the tip).
* Experimenters seek to keep Ra low (discarding all data from cells with Ra is large or unstable).
* A primary cause of high Ra is clogging of the recording pipette tip.
* Access resistance (Ra) is used called series resistance (Rs) in the literature.

### Capacitance (Cm)
* Indicates the size of the neural membrane (a good indicator of soma size)
* Large neurons have a high capacitance
* Neurons of similar size and phenotype are expected to have similar capacitance
