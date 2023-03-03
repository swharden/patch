---
title: Image Stabilization with ImageJ
description: How to correct for motion in time-series 2D and 3D images
---

## Sample data

**Download:** [sample.tif](sample.tif)

Original | TurboReg | Descriptor | Correct2D | MoCo
---|---|---|---|---
![](sample.gif)|![](stabilized.gif)|![](stabilized2.gif)|![](stabilized3.gif)|![](stabilized3.gif)

I find TurboReg/StackReg to be reliably superior to other ImageJ alignment plugins.

## 2D Image Stabilization

**TurboReg** is an ImageJ plugin for aligning images using a subpixel registration algorithm described by [Thévenaz et al., 1998](https://ieeexplore.ieee.org/document/650848). StackReg is an ImageJ plugin that applies TurboReg alignment to stacks. 

**Download:** [StackReg](http://bigwww.epfl.ch/thevenaz/stackreg/) (requires [TurboReg](http://bigwww.epfl.ch/thevenaz/turboreg/))

**Launch:** Plugins > StackReg

**Multichannel images** can be converted to RGB, stabilized, then converted back to multi-channel composite images.

## 3D Image Stabilization

3D image alignment is slower and more complex, so ensure it is truly needed for your application before proceeding.

* If your goal is to analyze projection images, I recommend projecting 3D times-series data to create a 2D stack then use StackReg to align it.

* If your goal is to perform analyses at distinct Z positions over time, 3D alignment is required.

**Correct 3D Drift** is an ImageJ plugin for 3D time-series alignment. It uses a phase correlation based algorithm described by [Preibisch et al., 2009](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2682522/). This plugin ships with FIJI and does not have to be manually installed. This plugin can be used on 2D images, but I find its performance inferior to TurboReg/StackReg.

**Download:** [Correct_3D_Drift](https://github.com/fiji/Correct_3D_Drift)

**Launch:** Plugins > Registration > Correct 3D Drift

## Additional Resources

The strategies above are those I typically recommend, but additional tools are available for 2D and 3D image alignment:

* [Descriptor Based Series Registration](https://github.com/fiji/Descriptor_based_registration) - An ImageJ plugin (provided with Fiji) which may have superior sub-pixel alignment performance but I find it produces output images which are too blurry for my applications.

* [Motion Correlation (MoCo)](https://github.com/NTCColumbia/moco) - An ImageJ plugin based on [Dubbs et al., 2016](https://doi.org/10.3389/fninf.2016.00006) optimized for rodent brain imaging. This project does not appear to be maintained, and the repository is poorly documented. I find performance to be inferior to TurboReg.