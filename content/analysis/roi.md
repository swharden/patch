---
title: Fluorescence Analysis with ImageJ and Excel
description: How to calculate ΔF/F₀ from a series of fluorescence images
weight: 20
---

**This page describes how to analyze fluorescence intensity (ΔF/F₀) from a series of images using ImageJ and Excel.** While semi-automated custom tools are often used to facilitate rapid analysis of fluorescence data, there is great value in understanding how to realize these analyses using standard and commonly-available software.

<a href="/patch/img/analysis/roi/xmlroi.png">
<img src="/patch/img/analysis/roi/xmlroi.png" class="img-fluid d-block w-75 mx-auto my-5 border shadow">
</a>

## Measure ROI Fluorescence
* Install [ImageJ (Fiji)](https://fiji.sc/)
* Drag/drop a folder of images onto ImageJ to open all images as a stack
* Create a maximum projection (of either channel) to make drawing of ROIs easy. **Image > Stack > Z project** and select _Average_ (not maximum projection!)
  * do all ROI creation on the projection. You can later use these same ROIs on the original data.
* Click **analyze > tools > ROI manager** _(ROI means "region of interest")_
* Use the "freehand sections" tool (as opposed to the square or circle) to outline some cells. 
  * Every time you outline a cell, click the **add** button on the ROI manager.
  * I recommend naming cells as you add them (click the **rename** button).
  * Be sure to indicate whether the thing is a neuron or astrocyte.
* When all cells have been outlined, highlight them all (with shift-click or control-click) and save the ROIs by clicking **more > save**.
  * once ROIs have been saved, you can load the same ROIs on the red stack, green stack, or a projection image
* Deterime what data to analze by clicking **analyze > set measurements**
  * I recommend selecting ONLY "Mean gray value"
* Analyze the data in the ROI manager by clicking **more > multi measure**
* In the results window, click **file > save as** and call it something
  * Excel 2016 may not be able to open the .xls file. You may have to rename it to .tsv (short for tab-separated values) and drag/drop it into a blank excel worksheet.
* Once the data is in excel, add a "time" column and populate its values appropriately 

<a href="/patch/img/analysis/roi/rois.jpg">
<img src="/patch/img/analysis/roi/rois.jpg" class="img-fluid d-block w-75 mx-auto my-5">
</a>

## Calculate Single-Channel ΔF/F₀

Single-channel fluorescence experiments report the change in fluorescence (`ΔF`) normalized to its baseline level (`F₀`). In this example `F` is measured for each ROI in every frame. The following steps are performed for each ROI.

* Calculate `F₀` as the mean fluorescence intensity during the baseline region

* Calculate `ΔF` by subtracting `F₀` from every `F` value

* Calculate `ΔF/F₀` by dividing `ΔF` values by `F₀`

<a href="/patch/img/analysis/roi/excel.jpg">
<img src="/patch/img/analysis/roi/excel.jpg" class="img-fluid d-block w-75 mx-auto my-5">
</a>

## Calculate Ratiometric ΔF/F

The following describes how to measure ratiometric fluorescence from a series of 2D multi-channel images. See [Ratiometric Linescan Analysis with ImageJ and Excel](../linescan) for information specific to analyzing ratiometric linescan images.

Two-channel fluorescence experiments report ΔF/F as the change in one fluorophore relative to another. In this example we will use `G` to represent a calcium-sensitive fluorophore and report the change in its fluorescence relative to a calcium-insensitive fluorophore `R`. In this example `G/R` is measured for each ROI in every time point. The following steps are performed for each ROI.

In this case `F` represents `G/R` so `ΔF/F` is: `[Δ(G/R)]/(G/R)₀`

* Calculate `(G/R)₀` as the mean ratio of fluorescence intensity during the baseline region

* Calculate `Δ(G/R)` by subtracting `(G/R)₀` from every `(G/R)` value

* Calculate `ΔF/F` by dividing `Δ(G/R)` values by `(G/R)₀`