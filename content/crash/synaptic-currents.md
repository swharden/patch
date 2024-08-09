---
title: Synaptic Currents
description: Electrical changes in a cell resulting from neurotransmitter released by another cell
weight: 70
---

## Synaptic Currents and Potentials

Consider what happens when an excitatory neurotransmitter (released by an upstream neuron) activates a ligand-gated ion channel and allows positive ions to rush into the cell: the **inward current** produced is excitatory, and the **voltage** of the cell rises slightly. The result is a small excitatory **synaptic current**. In this example the **pre-synaptic** cell is the one that released the neurotransmitter, and the **post-synaptic** cell is the one that reacted to it. 

Patch-clamped neurons can be used to measure spontaneous currents that result from pre-synaptic (upstream) neurons spontaneously firing and releasing neurotransmitter onto the post-synaptic neuron we are recording. Experiments like this use the patched neuron as a "microphone" to listen for chemical signals from upstream neurons.

## Pre-Synaptic vs. Post-Synaptic

<img src="/patch/img/crash/synaptic-currents/synaptic-neuron.png" class="d-block mx-auto img-fluid">

Synapses are the chemical connection between an upstream (pre-synaptic) and downstream (post-synaptic) neuron. When the pre-synaptic neuron fires an action potential (AP), neurotransmitter is released from the axon terminal. In this example, the neurotransmitter is excitatory. When the neurotransmitter acts on the post-synaptic neuron (the neuron being recorded), the excitatory action of that synapse is observed as an excitatory post-synaptic current. Although this method only directly measures currents in the post-synaptic neuron, the frequency of post-synaptic currents is related to the frequency of pre-synaptic action potential firing.

## Abbreviations

Here we reach one of the most common sets of abbreviations in synaptic electrophysiology: **EPSC** (excitatory post-synaptic current) and **IPSC** (inhibitory post-synaptic current). EPSCs and IPSCs are measured in voltage-clamp configuration.

If we allow the voltage of the cell to be influenced by EPSCs and IPSCs, the synaptic currents will result in changes in membrane potential (as described by [Ohm's Law](../ohms-law/)). The voltage swings produced by EPSCs and IPSCs are termed **EPSP** (excitatory post-synaptic potential) and **IPSP** (inhibitory post-synaptic potential). EPSPs and IPSPs are measured in current-clamp configuration.

## Spontaneous vs. Evoked Synaptic Currents

One more layer of abbreviations can be added to indicate if the synaptic currents (or potentials) were spontaneous (due to the pre-synaptic neuron firing an action potential randomly) or evoked (the pre-synaptic neuron fired an action potential in response to electrical optogenetic excitation). Spontaneous synaptic events are abbreviated **sEPSC**, **sIPSC**, **sEPSP**, and **sIPSP**, and evoked synaptic currents are abbreviated **eEPSC**, **eIPSC**, **eEPSP**, **eIPSP**. Other sections discuss [electrically evoked currents](../../pages/evoke/) and [optogenetics](../../pages/optogenetics/) in greater detail.

## Synaptic Currents in VC and IC Modes

Consider the following figure which demonstrates spontaneous excitatory and inhibitory synaptic activity in the same cell measured in voltage-clamp mode and current-clamp modes:

| voltage clamp (VC) | current clamp (IC) |
--- | ---
<img src='/patch/img/crash/synaptic-currents/synaptic-vc.png' class='img-fluid'> | <img src='/patch/img/crash/synaptic-currents/synaptic-ic.png' class='img-fluid'>

**In voltage-clamp configuration** the trace represents net membrane current. Spontaneous post-synaptic currents (EPSCs and IPSCs) are visible. IPSCs are upward deflections representing inhibitory (outward) currents. EPSCs are inward deflections representing excitatory (inward) currents. It is useful to memorize that downward deflections in voltage-clamp configuration represent inward currents and are excitatory.

**In current-clamp configuration** the trace represents net membrane potential (voltage). Spontaneous post-synaptic potentials (EPSPs and IPSPs) are visible. EPSPs are upward representing excitatory events, and IPSCs are downward representing inhibitory events. This is opposite from voltage-clamp trace, but may be easier to remember if you consider that currents which push the voltage more positive are excitatory.