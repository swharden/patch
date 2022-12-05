---
title: Spectral Noise Reduction
description: How to remove periodic noise from electrophysiology traces
---

This page outlines how to improve electrophysiological containing 60 Hz noise. Note that European noise may be 50 Hz, but the primary concept being demonstrated is that noisy traces can be improved by spectrally filtering-out the fundamental frequency and its harmonics.

## Procedure

- **convert data into frequency domain with FFT** - frequency units can be difficult to work with. Usually the array that comes out is a mirrored (real/imaginary) trace where the horizontal axis is frequency (starting at real 0, peaking to length(data)/2 in the center, and ending back at imaginary 0) and the vertical frequency is the power of that frequency in i/j units. Note that the maximum frequency you can measure is the number of data points/2. Also your frequency units are multiplied by the ratio of the number of your data points measured and your sample rate.

- **Set FFT[I]=0 where I is odd harmonics** - if you've figured out your horizontal axis untits, this becomes trivial. You _may_ decide to only silence odd harmonics, but it probably won't produce much differnece on the output.

- **convert data into time domain with iFFT** - this will output your smoothed trace and you're done.

<img src="noise-reduction.png" class="img-fluid">

## Python Example

The following code performs the noise suppression demonstrated above

```py
import os
import sys
import pyabf
import matplotlib.pyplot as plt
import numpy as np

# load noisy trace
abfFile=R"demo.abf"
abf=pyabf.ABF(abfFile) 
Xs,Ys=abf.sweepX,abf.sweepY 
baseFrequency=60 

### convert to frequency domain, silence harmonics, then back to time domain
FFT=np.fft.fft(Ys) # frequency data (i/j vectors starting at 0Hz)
for i in range(50): # first 50 odd harmonics
    I=int(baseFrequency*i+baseFrequency*len(Ys)/abf.pointsPerSec)
    FFT[I],FFT[-I]=0,0 # remember to silence from both ends of the FFT
Ys2=np.fft.ifft(FFT) # all done

### plot the original and new data in X/Y-linked subplots
plt.figure(figsize=(15,10))
ax1=plt.subplot(211)
plt.grid()
plt.title("Original Data")
plt.plot(Xs,Ys,alpha=.75)
plt.margins(0,.1)
plt.subplot(212,sharex=ax1,sharey=ax1)
plt.grid()
plt.title("Harmonic Suppression")
plt.plot(Xs,Ys2,alpha=.75)
plt.margins(0,.1)
plt.tight_layout()
plt.show()
```

## Characterizing Noise Frequencies

Plotting the raw frequency component and highlighting 60 Hz and every third harmonic, it becomes evident that not every odd harmonic is an offender. I could selectively silence just the bad ones, but it doesn't make a huge difference as compared to just silencing all of them.

<img src="noise-freq.png" class="img-fluid">
