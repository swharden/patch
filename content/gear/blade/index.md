---
title: Preamp Blade Setup
description: How to configure and switch between different preamplifier blades
---

{{< specific >}}

A _preamplifier blade_ is a circuit board that amplifies voltage from PMTs and provides a low impedance signal suitable to send through a long cable run to the GPIO box.

* Old blades (white BNC connectors) work better for galvo/galvo imaging (brighter)

* New blades (black BNC connectors) work better for galvo/resonant imaging (brighter and less streaking)

## Changing Blades (Hardware)

* Unscrew all nuts around BNC connectors
* Unscrew the front panel of the enclosure and remove it
* Slide out the blade you wish to remove
* Metal shields slide in slots between blades

## Changing blades (Software)

The old blades require _legacy mode_ to be enabled but new blades do not. To enable or disable legacy mode:

* Ensure PrairieView is closed
* Open `C:\Program Files\Prairie\Prairie View\PrairieConfigUtility.exe`
* Select the `Channels/PMTs/Preamps` tab
* Check or uncheck the `Legacy` checkbox
* Click Save
* Open PrairieView

## Changing Preamp Scaling

Decreasing the dynamic range increases the overall brightness of images. 
Old preamp blades were run with a maximum input voltage of `1.25 V` and new blades are run at `0.625 V`

* In PrairieView click `Tools` and select `Scan Settings`
* Select the `DAQs/Preamplifier` tab
* Double-right-click the tab to enable editing
* Set the maximum input voltage as desired
