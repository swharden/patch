---
title: Tonic/Phasic Analysis
description: How to separate slow (tonic) changes in holding current from fast (phasic) synaptic currents in voltage-clamp recordings
---

We often report "holding current" as the mean current over a range of time in a voltage-clamp recording, but how do we cleanly measure holding current if fast synaptic neurotransmission (EPSCs and IPSCs) influence this mean? **This page describes how to measure holding current (_tonic_ current) in a way that is not influenced by fast (_phasic_) synaptic currents.**

## Experimental Data

Consider this voltage-clamp experiment that adds a drug that changes holding current, but is confounded by the fact that it also changes sIPSC frequency. How do we measure the change in holding current (the slow upward shift of the trace) in a way that is not confounded by the fact that the drug also changes frequency and amplitude of synaptic events (fast downward deflections)? This is the problem that tonic/phasic analysis solves.

<div align="center">

Raw Trace | Mean Current
---|---
<img src="/patch/img/analysis/tonic-phasic/a.png" class="img-fluid">|<img src="/patch/img/analysis/tonic-phasic/b.png" class="img-fluid">

</div>

## How to Isolate Tonic Current

* Mean current (tonic current) in voltage-clamp traces is "pulled" in the direction of spontaneous currents synaptic currents (phasic currents).

* If a voltage-clamp trace has no spontaneous synaptic currents, it is essentially a straight line. In practice the trace bobbles up and down because of noise. 

<div align="center">

Raw Trace With Synaptic Currents | Raw Trace Without Synaptic Currents
---|---
<img src="/patch/img/analysis/tonic-phasic/raw-15.png" class="img-fluid">|<img src="/patch/img/analysis/tonic-phasic/raw-134.png" class="img-fluid">

</div>

* Noise is _normally distributed_, so if we represent all values from raw traces as a **histogram of currents** it will will appear as a **Gaussian curve** centered at the mean holding current.

<div align="center">

Histogram With Synaptic Currents | Histogram Without Synaptic Currents
---|---
<img src="/patch/img/analysis/tonic-phasic/hist-15.png" class="img-fluid">|<img src="/patch/img/analysis/tonic-phasic/hist-134.png" class="img-fluid">

</div>

* The current value at the **peak of the histogram** represents _tonic current_ and it is largely immune to _phasic currents_.

* Revisiting the original data, using the peak of the histograms to measure holding current allows reporting of true _tonic current_ even though spontaneous currents influence the _mean current_.

<div align="center">

Raw Trace | Fitted Histograms
---|---
<img src="/patch/img/analysis/tonic-phasic/a.png" class="img-fluid">|<img src="/patch/img/analysis/tonic-phasic/c.png" class="img-fluid">

</div>

# Advanced Analyses

## Curve Fitting

* A Gaussian curve may be fitted to the clean portion of the histogram (uninfluenced by phasic currents), and the area of the histogram that falls outside the Gaussian curve serves as a quantitative measurement of phasic current. 

* Fitting a Gaussian curve to the histogram and reporting its center is slightly more accurate than simply reporting the value of the peak histogram bin.

* The center of the Gaussian curve fitted to the center of the histogram is a good prediction of the _tonic current_ which ignores the influence of _phasic currents_ away from the center of the curve.

* If phasic currents only extend in one direction (e.g., GABAergic IPSCs present when glutamatergic EPSCs are blocked with DNQX and AP5) you can fit the Gaussian curve to the data which is clean in the other direction.

## Moving Baseline Subtraction

If recordings drift slowly up and down and/or the noise floor is extremely low, slow drift will influence the shape of the histogram more than the noise itself, complicating curve fitting and segregation of tonic and phasic currents.

One approach to overcome this issue is to measure the drift using a weighted moving window average (black line) then subtract it from the original trace to create a flatter trace. 

Although this allows improved quantification of isolated _phasic_ currents, this complicates the ability to determine _tonic_ current since the trace is now centered at 0 pA.


<div align="center">

Drift Subtraction | Fitted Histogram
---|---
<img src="/patch/img/analysis/tonic-phasic/baseline.png" class="img-fluid">|<img src="/patch/img/analysis/tonic-phasic/baseline2.png" class="img-fluid">

</div>

## Percentile Analysis

In conditions with extremely large and frequent spontaneous currents, an improved Gaussian curve may be fitted to only those values in the quietest portions of the trace. To achieve this, the trace can be broken into many segments a few milliseconds in length, then those segments are sorted by their standard deviation, and the lowest percentile segments can be included in the tonic/phasic analysis.

<div align="center">

Segment Noise Measurement | Segments Sorted by Noise
---|---
<img src="/patch/img/analysis/tonic-phasic/noise1.png" class="img-fluid">|<img src="/patch/img/analysis/tonic-phasic/noise2.png" class="img-fluid">

</div>


<div align="center">

Histogram by Noise Percentile | Fitted Histogram by Noise Percentile
---|---
<img src="/patch/img/analysis/tonic-phasic/percentile1.png" class="img-fluid">|<img src="/patch/img/analysis/tonic-phasic/percentile2.png" class="img-fluid">

</div>

## Additional Resources

* [Methods for recording and measuring tonic GABA<sub>A</sub> receptor-mediated inhibition](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3852068/pdf/fncir-07-00193.pdf) (Bright and Smart, 2013)

* [Python script](tp.py) used to generate these figures