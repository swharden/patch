---
title: Passive Properties
description: Electrical features of a cell membrane that do not require channels to actively open or close
weight: 30
---

The electrical excitability of a neuron is determined by the nature of its non-conductive membrane and the conductive ion channels embedded within it. The nature of the neural membrane and its conductivity can be described by a few primary **passive membrane properties** (sometimes called **intrinsic properties**) which can be measured electrically. Drugs or conditions which alter the passive membrane properties of neurons can have profound impacts on their excitability. Different classes of neurons often have characteristically different combinations of passive membrane properties, making their measurement useful for classifying neuron phenotypes. 

## Holding Current (I<sub>h</sub>)

When a machine is used to clamp the neuron's voltage at a fixed value it typically results in a continuous flow of ions passing through open channels across its membrane. Since the flow of ions is called current, the flow of ions at a specific holding voltage is termed **holding current** (I<sub>h</sub>). As the clamp voltage changes, the current flowing across the membrane typically changes too.

**Holding current (I<sub>h</sub>) describes the total current flowing across a neuron's membrane at a specific membrane voltage (V<sub>m</sub>).** Since holding current changes according to the voltage of the cell, current and voltage can be plotted against each other. This graph (with voltage on the horizontal axis and current on the vertical axis) is called an **I/V curve** (discussed in greater detail on the [common experiments](../../pages/experiments/) page).

## Membrane Resistance (R<sub>m</sub>)

**Membrane resistance describes how much the neural membrane resists the flow of ions across it.** Since ions flow through open ion channels, membrane resistance is an indication of **how many ion channels are open** at the time of the measurement. A neuron with high membrane resistance has very few open channels, and vise-versa. If a drug lowers the membrane resistance of a neuron, it means that drug is probably opening ion channels. Membrane resistance also determines how large of a voltage change will result from a current input, as described in greater detail in the next section about [Ohm's Law](../ohms-law/).

## Whole-Cell Capacitance (C<sub>m</sub>)

Capacitance is the amount of electrical charge which can be stored across any insulator. In neurons, the primary factor that determines capacitance is the size of its insulator (how large the cell membrane is). The larger a neuron is, the more membrane is has, and the more charge it can separate across it. Therefore, **capacitance corresponds to the size of the neuron**. Large neurons have large capacitance.

## Holding Current Density (Id)

Since larger cells have more membrane, holding current (the net current through all open channels in a membrane) can be difficult to compare across cells with vastly different sizes (since the largest cells will have more current just because they have more membrane, not necessarily a higher density of open channels). 

In most cases experimenters will record from cells of approximately the same size so changes in C<sub>m</sub> will not largely influence R<sub>m</sub> or I<sub>h</sub>. However, in rare cases where experimenters desire to compare holding current across cells with vastly different sizes, normalizing to cell size may be achieved by dividing I<sub>h</sub> by C<sub>m</sub>. The resulting term is called **current density** (I<sub>d</sub>).

## Access Resistance (R<sub>a</sub>)

> 💡 This property describes features of the experimental equipment and not the neuron itself.

Electrical measurements of patch-clamped neurons are performed through the very small opening at the tip of the pipette. The opening is small enough that it poses some resistance to current, and if the tip gets clogged with debris the resistance will increase a large amount. The measurement of resistance through the tip is called **access resistance** (R<sub>a</sub>). Access resistance may be monitored frequently during long recordings to evaluate the quality of the patch pipette throughout the experiment.

## Voltage-Clamp Time Constant (τ)

> 💡 This property describes features of the experimental equipment and not the neuron itself.

When voltage-clamp experiments attempt to rapidly step a neuron from one voltage to another, the cell's actual voltage does not change immediately. There is a limitation in how fast the patch-clamp amplifier can move the voltage of the cell, largely determined by access resistance (R<sub>a</sub>) and cell capacitance (C<sub>m</sub>). The rate at which a voltage-clamp amplifier can move the voltage of a cell is described by the time constant **tau** (τ) which is typically a few milliseconds. The value of τ is approximately C<sub>m</sub>/R<sub>m</sub>, but the [Exploring the Voltage-Clamp Membrane Test](https://swharden.com/blog/2020-10-11-model-neuron-ltspice/) page offers a more thorough discussion.