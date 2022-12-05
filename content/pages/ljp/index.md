---
title: Liquid Junction Potential
description: What Liquid Junction Potential (LJP) is and how it can be corrected for in patch-clamp experiments
---

## What is LJP?

* When two different ionic solutions meet, a small voltage can form at the junction. In patch-clamp experiments, this occurs at the tip of the pipette where the internal solution meets the bath solution.

* This voltage difference occurs because smaller ions (like Cl<sup>-</sup>) move faster than large ions (like gluconate), so a small standing voltage is present across the liquid junction.

* When patch-clamping cells the amplifier offset voltage is adjusted to zero when the pipette is in open-tip configuration with the bath, but this reading is not _really_ zero because LJP is present. This is the cause of LJP error in patch-clamp experiments.

* When a patch-clamp recording shows a voltage of -70 mV, the voltage isn't actually -70 mV because it is off by the size of the LJP.

* Scientists can measure or calculate the LJP, then use its known value to correct patch-clamp recordings.

* Changing the extracellular solution or intracellular solution will change LJP.


## How to Correct for LJP in Electrophysiology Experiments

Consider the case when you zero your meter as the pipette is in the bath:

V<sub>measured</sub> = V<sub>actual</sub> + LJP

Rearranging this formula, the actual voltage of the cell is what the meter says minus the LJP:

V<sub>actual</sub> = V<sub>measured</sub> - LJP

## How to Calculate LJP

* Calculate LJP using [LJPcalc](https://swharden.com/LJPcalc/)

## How to Measure LJP Experimentally

* Zero the amplifier with intracellular solution in the bath and in your pipette

* Replace the bath with extracellular solution

* The measured voltage is the negative LJP (invert its sign to get LJP)

## Resources

* [LJP Theory and Correction](https://swharden.com/blog/2021-01-13-ljp-theory/)