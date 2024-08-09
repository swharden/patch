---
title: Electrically Evoke Synapses
description: Using an electrical stimulator to evoke synaptic currents
---

So far, we have discussed spontaneous EPSCs and IPSCs in detail. However, there are some cases where the experimenter may desire to **evoke** synaptic release of neurotransmitter using an electrical stimulator rather than passively wait for it to occur spontaneously. 

## Reasons to Evoke Synapses

* Evoked currents are useful when the frequency of spontaneous currents is low. Synapses may be present, but if the pre-synaptic neuron does not fire spontaneously the current will never be visualized. Evoking synapses can study synaptic currents in pathways too silent to study spontaneous release in.

* Evoking strong pathways can result in currents representing the coordinated activation of tens or hundreds of synapses. Since these currents are additive, the resulting trace is very large, very smooth, and easy to measure. 

* An electrical stimulator lets you activate synapses of a specific pathway depending on where the stimulator is placed (e.g., on the basal or apical side of the neuron being recorded). In contrast, there is no way to know where spontaneous currents originate. 

* The effect of drugs in modulating the pre-synapse vs. the post-synapse can be assessed by delivering two pulses in rapid succession and inspecting the paired pulse ratio.  Changes in the postsynaptic neuron typically reveal themselves as a change in both pulses (e.g., they both grew bigger) whereas changes in the pre-synaptic neuron are typically associated with a change in the paired pulse ratio (e.g., the second pulse grew larger than the first)

## Paired Pulse

<img src="/patch/img/pages/evoke/evoke-dic.png" class="img-fluid w-75 border shadow mx-auto d-block my-5">

<img src="/patch/img/pages/evoke/evoke-paired-pulse.png" class="img-fluid my-5">

Electrical Paired Pulse Stimulation. Two electrical stimuli (identified by the presence of a stimulus artifact) evoke two inward currents. Compared to baseline (dark trace), the addition of drug (light trace) increased the amplitude of both pulses without changing the paired pulse ratio.

## Types of Electrical Stimulator

There are several types of electrical stimulator to choose from and selecting the right stimulator for your project is important in ensuring its success. This section reviews the types of stimulators you are most likely to see around the laboratory.

### Glass Pipettes
Single-channel glass pipettes filled with bath solution work well as point stimulators. Place the positive wire in the pipette and place the negative wire (it should have an AgCl pellet on the end) in the bath. Note that the current will flow from the tip of the pipette to the pellet. Although the current will flow over a large distance, it is strongest at the open tip of the pipette. Narrower open tip sizes result in a higher resistance, so larger tips take less current to elicit similar responses. If wider stimulation is desired, it may be worth trying to pull a pipette with a wider tip, or to break off the tip of the stimulator pipette. Note that using chloride-coated silver wire can reduce stimulus artifacts.

### Theta Glass
For excitation of an extremely small or very precise region of tissue, theta glass may be desired. Theta glass is the term for glass pipettes containing a glass divider down the middle (the glass forms a theta symbol when looking down its length). After being pulled, positive and negative wires of the stimulator can be placed in each of the two internal channels, and current will only flow between the tubes at the tip of the pulled pipette. Note that using chloride-coated silver wire can reduce stimulus artifacts.

## Monopolar Tungsten Stimulator
To excite a field larger than the tip of a glass pipette, a metal stimulator may be used. Monopolar tungsten stimulators have a conducting tip and a nonconductive sheath down its length. When attached to the positive lead of a stimulus isolator (with the negative lead attached to an AgCl pellet in the bath), these stimulators produce a moderate amount of field stimulation but are still small enough that it can be easily localized.

## Concentric Tungsten Stimulator
To excite an extremely large field, concentric bipolar stimulators may be used. They are concentric rings of two conductors sandwiched between layers of insulating material. They are extremely delicate and can break with the slightest touch if handled incorrectly. Because their electrode has a large surface area, they require much more current than other electrodes to produce the same excitatory voltage. They are often too large to use in fine circuits or small animals (such as mice). 


## Stimulus Isolation Unit (SIU)

The purpose of the stimulus isolator is to allow the patch-clamp system to deliver high voltage to the electrode. The current of the stimulator is set with the knob on the top right of the stimulus isolation unit. According to Ohm’s Law, the voltage the stimulator will produce when triggered is a function of the current (set by the knob) and the resistance (a function of the type of stimulator being used). Although there is a “unipolar/bipolar” switch, but unipolar should virtually always be selected. There is a “polarity select” button, which can be toggled to invert the polarity of the outputs. The preferred output polarity is that which produces the cleanest waveform on the recorder and should be determined at recording time by the experimenter. Often, one polarity will be more effective at reliably stimulating a slice than the other. 

<img src="/patch/img/pages/evoke/siu.png" class="img-fluid my-5 w-75 d-block mx-auto">