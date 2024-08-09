---
title: Optogenetics
description: Using light-activated ion channels to optically excite specific cell populations
---

When investigating synaptic currents in acute brain slices electrical stimulation is often used, but it indiscriminately activates all neurons near the electrode.

**Channelrhodopsin-2 (ChR2)** is a light-gated cation channel which can be selectively placed in specific types of neurons thanks to genetic engineering. A flash of blue light transiently opens ChR2, allowing cations (primarily Na+) to rush into the cell, often resulting in action potentials. When combined with genetic engineering to selectively express ChR2 only in certain classes of neurons, blue light can be used to activate specific subpopulations populations of neurons. Optogenetics is the field of study where genetic engineering is used to express light-sensitive ion channels in cells. Light-gated ion channels are called opsins. While ChR2 is the most commonly used opsins in neuroscience, halorhodopsin (light-gated anion channel) is also used to produce light-sensitive inhibitory currents.

<img src="/patch/img/pages/optogenetics/opto.jpg" class="img-fluid d-block mx-auto">

## Recording from ChR2+ Neurons

Neurons with ChR2 are easy to identify because they will rapidly respond to light. The response to light is always extremely fast (less than 1ms from onset). In this example, a CRH-ChR2+ neuron is shown to produce an excitatory current in voltage clamp in response to blue light stimulation (shaded area).

<img src="/patch/img/pages/optogenetics/opto-evoke.png" class="img-fluid d-block mx-auto">

## Light-Evoked Synaptic Currents

Although one can record from ChR2+ neurons, typically the most common use of ChR2 in acute brain slice preparations is to facilitate the study of synaptic neurotransmission. In these lines of experiments, pre-synaptic neurons express ChR2 and post-synaptic neurons (targeted for patch-clamp analysis) receive light-evoked EPSCs in response to blue light.

<img src="/patch/img/pages/optogenetics/opto-evoke2.png" class="img-fluid d-block mx-auto">

There are two ways to know the neuron you are recording is receiving an EPSC in response to blue light (synaptic in origin) vs. directly responding to blue light itself (what you would expect if the recorded neuron expressed ChR2). First, light-evoked synaptic currents take a few ms to occur (due to the charging of the presynaptic axon, propagation of action potential release of neurotransmitter, etc). Second, pharmacological blockade of the receptors underlying the synaptic current will eliminate the light-evoked current. This result would not be observed if the post-synaptic neuron expressed ChR2.

Control                                | DNQX                                          
-------------------------------------- | ----------------------------------------------
<img src="/patch/img/pages/optogenetics/epsc.png" class="img-fluid"> | <img src="/patch/img/pages/optogenetics/epsc-blocked.png" class="img-fluid">
