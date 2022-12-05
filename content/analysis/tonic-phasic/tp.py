"""
tonic phasic analysis demo
"""

import pyabf
import pyabf.filter
import matplotlib.pyplot as plt
import numpy as np

def saveHistogram(trace, bins, filename):
    hist, edges = np.histogram(trace, bins)
    edges = edges[:-1]
    
    plt.figure(figsize=(8, 3))
    plt.bar(edges, hist, width=1.1, linewidth=0)
    plt.xlabel("Current (pA)")

    plt.gca().spines.right.set_visible(False)
    plt.gca().spines.top.set_visible(False)
    plt.gca().spines.left.set_visible(False)
    plt.gca().yaxis.set_ticks([])
    plt.tight_layout()

    plt.savefig(filename)

def saveTrace(abf, sweep):
    abf.setSweep(sweep)
    
    segment = abf.sweepY[abf.dataRate*2:]

    plt.figure(figsize=(8, 3))
    plt.plot(segment)
    plt.ylabel("Current (pA)")
    plt.axis([None, None, -100, 0])

    plt.gca().spines.right.set_visible(False)
    plt.gca().spines.top.set_visible(False)
    plt.gca().spines.bottom.set_visible(False)
    plt.gca().xaxis.set_ticks([])
    plt.tight_layout()

    plt.savefig(f"raw-{sweep}.png")

    bins = np.linspace(-80, 0, 80*2)
    saveHistogram(segment, bins, f"hist-{sweep}.png")

if __name__=="__main__":

    abf = pyabf.ABF("X:/Data/AT2-Cre/NTS-ChR2/abfs/2019_09_10_0047.abf")
    pyabf.filter.gaussian(abf, 1)
    saveTrace(abf, 15)
    saveTrace(abf, 134)

    print("DONE")