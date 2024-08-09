---
title: DIC Alignment Cheat-Sheet
description: How to align DIC optics for a fixed-stage Olympus BX-51WI microscope
---

A properly aligned light path is critically important for quality DIC imaging in acute brain slices. Once aligned, a DIC microscope will typically stay aligned. However, the cleaning of lenses and filters (necessary to recover after an overflow of ACSF) can misalign the DIC light path, requiring re-alignment. DIC integrity should be frequently assessed, and realignment performed whenever optics appear poor. Aligning DIC optics only takes a few minutes and will improve the quality of your data.

proper alignment                                 | poor alignment                                 
------------------------------------------------ | -----------------------------------------------
<img src="/patch/img/gear/align/alignment-good.png" class="img-fluid"> | <img src="/patch/img/gear/align/alignment-bad.png" class="img-fluid">

<img src="/patch/img/gear/align/microscope-parts.png" class="img-fluid my-5">

> 💡 **Note:** these instructions assume the IR filter is always in the light path and the camera is being used to assess image brightness and quality. This is ideal because it’s the camera light path (not the binocular path) which must be ideally aligned.

## 1. Prepare the Light Path

Note: these instructions assume the IR filter is always in the light path and the camera is being used to assess image brightness and quality. This is ideal because it’s the camera light path (not the binocular path) which must be ideally aligned.

- Take the following OUT of the light path:
  - Adjustable DIC prism
  - Condenser (loosen the condenser lock screw and remove the entire condenser assembly)
- Ensure the following are IN the light path:
  - Lower polarizer
  - Analyzer
  - 10x Objective
- Turn on the microscope lamp and ensure the path selector is fully out (all light goes to camera)
- Fully open the lamp iris (rotate the lamp iris knob maximally clockwise)
- Assess the image quality. If dark spots appear, it is due to dust on the camera (clean it before proceeding).
- Ensure you know which condenser carousel positions are DIC vs BF.
  - Figure this out by looking at the underside of the condenser while holding it in your hand. Rotate the condenser carousel until the DIC prism is in line. Note this position. Also, identify a position where no prism is in line which we will call brightfield (BF). Remember the positions for DIC and BF, since you will need to set these later.

<div class="d-flex justify-content-center">

Polarizer                                | No Polarizer                             
---------------------------------------- | -----------------------------------------
<img src="/patch/img/gear/align/filter.png" class="img-fluid"> | <img src="/patch/img/gear/align/filter2.png" class="img-fluid">

</div>

## 2. Align the Polarizer and Analyzer

- Identify the lower polarizer and rotate it in the light path. Slightly loosen the polarizer lock screw.
- Adjust the lower polarizer rotation knob (silver knob on the side of the polarizer rack) to minimize light intensity.
- Lock the polarizer in place with the lock screw.

## 3. Adjust the compensator

- Insert the condenser back into the microscope and lock it with the condenser lock screw.
- Rotate the condenser carousel to select a DIC position.
- Loosen the compensator screw (just above the compensator) and rotate the compensator to minimize light intensity, then lock it back into place.

## 4. Align the DIC prisms

- Rotate the condenser carousel to select a brightfield (BF) position.
- Insert the top adjustable DIC prism and look through the open eyepiece.
- Adjust the top DIC prism to minimize light intensity.

## 5. Adjust condenser focal point and center position

- Place a small object in the stage (like the slice anchor basket) and focus the objective on it with a low power lens.
- Move the stage so the object is no longer in the field of view.
- Maximally open the condenser iris (by pulling the lever fully toward you)
- Maximally close the lamp iris (by rotating it counterclockwise)
- Move the condenser (with the vertical adjustment knob) until a sharp decagon appears in focus (pictured).
- Slowly open the lamp iris until the decagon is as large as it can be while still being able to see all its sides.
- Center the decagon in the view by adjusting the condenser centering knobs (there are 2, one on each side).
- Enlarge the decagon and repeat, centering the condenser with the centering knobs as necessary until each of the decagon’s corners touch the edge of the field of view. Repeat with the 40x immersion lens.

<div class="d-flex justify-content-center">

Blurry Decagon                                   | Sharp Decagon                                  
------------------------------------------------ | -----------------------------------------------
<img src="/patch/img/gear/align/decagon-blurry.png" class="img-fluid"> | <img src="/patch/img/gear/align/decagon-sharp.png" class="img-fluid">

</div>

## 6. Prepare the microscope for brain slice imaging

- Fully open the lamp iris and condenser iris and focus on a brain slice.
- Ensure the condenser is properly set back to DIC mode (not BF mode)
- Optimal DIC configuration will be obtained by rotating the adjustable DIC prism approximately ¼ turn counter-clockwise from its darkest point. Increasing the rotation will allow a clearer, higher-light image, but have a thicker focal plane. Rotation on each side of its darkest point will invert the light direction.
