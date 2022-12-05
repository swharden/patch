---
title: Passive Properties
description: Electrical features of a cell membrane that do not require channels to actively open or close
weight: 40
---

The electrical excitability of a neuron is determined by the nature of its non-conductive membrane and the conductive ion channels embedded within it. Together, these combine to produce **passive membrane properties** (sometimes called **intrinsic properties**) which can be measured electrically. Drugs or conditions which alter the passive membrane properties of neurons can have profound impacts on their excitability (discussed in detail in the section describing Ohm’s Law). In addition, distinct classes of neurons (e.g., excitatory vs. inhibitory neurons) often have characteristically different combinations of passive membrane properties, making these properties useful in classifying neuron phenotypes. For these reasons, passive properties of neurons are measured, analyzed, and reported for virtually every electrophysiology project. **The primary passive membrane properties are Ih, Rm, and Cm.** It is important that new electrophysiologists develop a conversational understanding these primary membrane properties, their abbreviations, and a biological understanding of what they represent.

> ✔️ **Check:** Passive membrane properties are introduced from a biological perspective on this page and later revisited in greater technical and experimental detail after the section on Ohm’s Law (which describes how each passive property can influence the others). Ensure you have a working knowledge of all terms on this page before proceeding!

## Holding Current (Ih)

At a given voltage, a neuron typically produces a net flow of ions across its membrane. Current is the measurement of the flow of ions, so the current across a neuron’s membrane at a certain voltage is called it’s **steady state current**. This is sometimes termed **holding current**, since it possible for the experimenter to hold (or “clamp”) the neuron at specific voltage. **Holding current is the net current across the neuron’s membrane at a specific voltage.** Since holding current changes according to the voltage of the cell (due to the electrostatic gradient of ions across the membrane as well as voltage-gated channels which open and close), current and voltage can be graphed against each other. This graph (with voltage on the horizontal axis and current on the vertical axis) is called an **I/V curve**.

## Membrane Resistance (Rm)

**Membrane resistance is the measurement of how resistive the neural membrane is to the flow of ions.** Since ions flow through open ion channels, membrane resistance is an indication of **how many ion channels are open** at the time of the measurement. A neuron with high membrane resistance has very few open channels, and vise-versa. If a drug lowers the membrane resistance of a neuron, it means that drug is probably opening ion channels.

## Whole-Cell Capacitance (Cm)

Capacitance is the amount of electrical charge which can be stored across any insulator. In neurons, the primary factor that determines capacitance is the size of its insulator (the cell membrane). The larger a neuron is, the more membrane is has, and the more charge it can store across it. Therefore, **capacitance corresponds to the size of the neuron**. Large neurons have large capacitance.

> 🤓 **Nerd Alert:** Since larger cells have more membrane, holding current (the net current through all open channels) can be difficult to compare across cells with vastly different sizes (since the largest cells will have more current just because they have more membrane, not necessarily a higher density of channels). In rare cases where experimenters desire to compare holding current across cells with vastly different sizes, this can be achieved by dividing Ih by Cm. The resulting term is called current density, and may be abbreviated Id. Also note that since Cm depends on the size of the membrane, it is correlated more to somatic membrane surface area than somatic volume.


# Passive Membrane Properties Revisited

Now that the resistance-dependent relationship between current transients and voltage swings is established, membrane properties will be discussed again in greater detail. This list of passive membrane properties appears in ClampEx when a cell is analyzed using the membrane test.

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

> 🤓 **Nerd Alert:** Tau (τ) also appears in the list of membrane properties, but it’s just used to calculate Cm so you don’t need to worry about it. Tau is the time constant of an exponential decay curve used to calculate capacitance (Cm = τ/Rm). In practice the calculation is more advanced, as discussed in the subsequent section about the membrane test.