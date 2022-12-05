---
title: Patch Clamp Internal Solutions
description: Common internal solutions used for whole-cell patch-clamp electrophysiology
---

When a cell enters whole-cell patch-clamp configuration the pipette solution (also called internal solution) fills the the patched cell and largely replaces most of the cytoplasm. Physiological pipette solutions can be used seek to mimic the natural electrical properties of cells, or experiments can use non-physiological pipette solutions to block or enhance the current flow through specific channels. 

Typical pipette solutions for whole-cell patch clamp experiments contain high concentration of a cation (potassium or cesium) and a biologically inert anion (gluconate or methyl sulfate) and lower concentrations of supportive molecules to promote homeostasis.

## Common Pipette Solutions

* **Potassium gluconate (K-glu)** internal solutions are among the most commonly used in patch-clamp electrophysiology. It allows visualization of action potentials.

* **Potassium methyl sulfate (K-MeSO<sub>4</sub>)** internal solutions replace gluconate with methyl sulfate which has greater mobility than gluconate and results in a lower liquid junction potential (LJP). See the [LJP page](../ljp) for details.

* **Cesium gluconate (Cs-Glu)** internal solutions are used to block potassium channels to enhance synaptic currents (by raising membrane resistance) and/or allow the cell to be clamped at very positive potentials (preventing VGKCs from being activated). Because VGKCs are inhibited, action potentials and firing patterns cannot be studied using this internal solution.

## Chloride Concentration

In physiological conditions, GABA<sub>A</sub> (chloride channels) serve primarily to lower membrane resistance rather than pass continuous current. In experimental conditions, chloride concentrations between the ACSF and internal solutions can be tweaked so that the opening of GABA<sub>A</sub> can pass no current, produce an outward inhibitory current, or produce an outward inhibitory current.

* See the [Synaptic Currents page](../../crash/synaptic-currents) for additional information

* See the [Reversal Potential page](../reversal) for additional information

Whether GABA<sub>A</sub> currents are excitatory, inhibitory, or neutral depends on the potential of the cell and the reversal potential of chloride in your bath vs. internal. Use a tool like [NernstCalc](https://swharden.com/software/NernstCalc/) to determine the reversal potential of chloride in your experiment.

### Low Chloride

* Clamping above the chloride reversal potential makes GABA<sub>A</sub> currents outward (inhibitory)

* Low chloride pipette solutions position the chloride reversal potential below the rest potential.

* Low chloride pipette solutions cause GABA<sub>A</sub> openings to produce outward (inhibitory) currents at rest potentials.

### Moderate Chloride

* Clamping near the chloride reversal potential makes GABA<sub>A</sub> pass no current

* Moderate chloride pipette solutions position the chloride reversal potential near the rest potential.

* Moderate chloride pipette solutions do not produce large currents when GABA<sub>A</sub> opens at rest potentials.

### High Chloride

* Clamping below the chloride reversal potential makes GABA<sub>A</sub> currents inward (excitatory)

* High chloride pipette solutions position the chloride reversal potential above the rest potential.

* High chloride pipette solutions cause GABA<sub>A</sub> openings to produce inward (excitatory) currents at rest potentials.

### Pros and Cons

* Low chloride solutions make it easier to distinguish glutamate currents from GABA currents, because one will be inward and another will be outward at rest potentials.

* Chloride has higher ionic mobility than gluconate or methyl sulfate, so internal solutions with more chloride have a lower [LJP error](../ljp/).

## pH Adjustment

Internal solutions are typically adjusted to 7.25-7.30 using HCl, KOH, or CsOH. Keep in mind that adding too much KCl can disrupt chloride concentration of low-chloride internals, and CsOH should be used instead of KOH for adjusting K-free internals.

## Osmolarity Adjustment

Internal solutions are typically adjusted to achieve 290-300 mOsm (slightly less than the osmolarity of the extracellular solution).

## Biocytin

Biocytin (0.5%) can be added to the pipette solution to facilitate labeling. Unlike passively loading cells with fluorophore, biocytin is actively transported throughout the cell, and later can be labeled using a streptavidin-conjugated fluorophore.

## Internal Solution Recipes

### K-Glu (24 mM chloride)

* Described in [Patch-Clamp Analysis](https://link.springer.com/book/10.1007/978-1-59745-492-6) (second edition by Wolfgang Walz, 2007).

* Chloride reversal potential in (168 mM Cl<sup>-</sup> ACSF): -50 mV

Substance | Concentration (mM) | Product
---|---|---
K-gluconate | 110 | [229322500](https://www.fishersci.ca/shop/products/gluconic-acid-potassium-salt-99-thermo-scientific/ac229322500)
HEPES | 10 | [BP310100](https://www.fishersci.com/shop/products/hepes-100g/BP310100)
EGTA | 1.0 | [409910250](https://www.thermofisher.com/order/catalog/product/409910250)
KCl | 20 | [P9333](https://www.sigmaaldrich.com/US/en/product/sial/p9333)
MgCl<sub>2</sub> | 2.0 | [BP214](https://www.fishersci.com/shop/products/magnesium-chloride-hexahydrate-fisher-bioreagents/BP214500)
Na<sub>2</sub>ATP | 2.0 | [A26209](https://www.sigmaaldrich.com/US/en/product/aldrich/a26209)
Na<sub>3</sub>GTP | 0.25 | [G8877](https://www.sigmaaldrich.com/US/en/product/sigma/g8877)
phosphocreatine (di-tris) | 10 | [P1937](https://www.sigmaaldrich.com/US/en/product/sigma/p1937)
