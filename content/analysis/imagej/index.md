---
title: ImageJ Resources
description: Links, Notes, and Scripts related to Fiji/ImageJ
---

## Distributions

* [NIH ImageJ](https://imagej.nih.gov/ij/) - Website to download the bare bones ImageJ app. Because it has so few features/plugins, it is one of the fastest distributions of ImageJ.

* [Fiji](https://fiji.sc/) - Full-featured ImageJ bundle with many plugins installed by default.

## Programming

* [ImageJ Macro Functions](https://imagej.nih.gov/ij/developer/macro/functions.html)

* [ImageJ Macro Language](https://imagej.nih.gov/ij/developer/macro/macros.html)

* [ImageJ Programmer's Reference](https://imagej.nih.gov/ij/docs/macro_reference_guide.pdf)

* [Boilerplate ImageJ Python plugin](https://github.com/swharden/ImageJ-Python-plugin)

## Plugins

* [TurboReg](http://bigwww.epfl.ch/thevenaz/turboreg/)

## ImageJ Language Reference
* [ImageJ Macro Functions](https://imagej.nih.gov/ij/developer/macro/functions.html)
* [ImageJ Macro Language](https://imagej.nih.gov/ij/developer/macro/macros.html)

## Background Subtract Every Slices of a Stack
```java
print("\\Clear");
for (i=1;i<=nSlices();i++){
	print("Processing slice "+i+" of "+nSlices());
	setSlice(i);
	run("Subtract Background...", "rolling=50");
}
```

## Create CSV of Video TIF Times

This assumes you have a folder of TIFs where filename is system time in seconds:

* 1513963799.597.tif
* 1513963821.472.tif
* 1513963843.327.tif
* 1513963865.207.tif

```python
import numpy as np
import glob
import os
files=sorted(glob.glob("video/*.tif"))
files=[os.path.basename(x) for x in files]
files=[x[:-4] for x in files if x.count(".")==2]
timesSec=np.array(files,dtype=float)
timesSec-=timesSec[0]
timesMin=timesSec/60
with open("times.csv",'w') as f:
    f.write("\n".join(["%.03f"%x for x in timesMin]))
```

## Save RGB Images as 3 Grayscale Images

### Single image

```javascript
print("\\Clear");
dirname="X:\\Data\\projects\\2017-12-11 OTR-Cre mice\\2017-12-11 PFC resp to OXT\\data\\";
basename="171211sh_0000fx10m.tif";
fname=dirname+basename;

print(basename);
open(fname);
run("Split Channels");
selectWindow(basename+" (red)"); saveAs("Tiff", replace(fname,"m.tif","red.tif"));
selectWindow(basename+" (green)"); saveAs("Tiff", replace(fname,"m.tif","green.tif"));
selectWindow(basename+" (blue)"); saveAs("Tiff", replace(fname,"m.tif","blue.tif"));
while(nImages>0) {close();}
```

### Every image in a folder
```javascript
print("\\Clear");
dirname="X:\\Data\\projects\\2017-12-11 OTR-Cre mice\\2017-12-11 PFC resp to OXT\\data\\";
files = getFileList(dirname);
for(i=0;i<files.length;i++){
	if (!(endsWith(files[i],".tif")||endsWith(files[i],".TIF"))) {continue;} // file must be a TIF
	if (indexOf(files[i],"fx10m")<0) {continue;} // file must contain this matching string
	basename=files[i];
	fname=dirname+basename;
	print(basename);
	open(fname);
	run("Split Channels");
	fname=replace(fname,".TIF",".tif");
	selectWindow(basename+" (red)"); saveAs("Tiff", replace(fname,"m.tif","red.tif"));
	selectWindow(basename+" (green)"); saveAs("Tiff", replace(fname,"m.tif","green.tif"));
	while(nImages>0) {close();}
}
```

## Background Subtract each Frame to a ROI
```javascript
// background-subtract the average of a ROI from every frame
// draw a rectangle around a background area before running this
// or DONT draw a rectangle and the whole window will be used

// remember the current selection
getBoundingRect(x, y, width, height);

// don't make black black, make black this value.
offset=100;

// do the thing on every slice
for (i=0;i<nSlices;i++){
	setSlice(i+1);
	makeRectangle(x, y, width, height);
	getStatistics(area, mean, min, max, std, histogram);
	run("Select None");
	subtractValue=mean-50;
	print("frame:"+(i+1)+", subtracting:"+subtractValue);
	run("Subtract...", "value="+subtractValue+" slice");
	//run("Enhance Contrast", "saturated=0.05");
	//run("Apply LUT", "slice");
}

// lastly, manually find a bright slice, 
// adjust contrast/brightness to taste,
// then apply to all slices
```

## Annotate Stack with Time Code
```javascript
// annotate a stack with times (seconds) as labels
// save output as BMP sequence then load it in AVIDEMUX to make AVI

run("RGB Color");
getDimensions(width, height, channels, slices, frames);
fontSize=32;

setSlice(1);
sliceTimeFirst=parseFloat(getInfo("slice.label"));

for (i=0;i<nSlices;i++){
	setSlice(i+1);
	frameTimeSeconds=parseFloat(getInfo("slice.label"))-sliceTimeFirst;
	frameTimeMinutes=frameTimeSeconds/60;
	
	//frameTime=IJ.pad(secPerFrame*i/60,3)+":"+IJ.pad(i%60,2)+'.'+IJ.pad(100*((secPerFrame*i)%1),2);
	frameTimeMsg=round(100*frameTimeMinutes)/100;
	frameTimeMsgWhole=IJ.pad(frameTimeMsg,3);
	frameTimeMsgFrac=IJ.pad(100*(frameTimeMsg-frameTimeMsgWhole),2);
	frameNumber=IJ.pad(i+1,4);
	msg="f"+frameNumber+" | "+frameTimeMsgWhole+"."+frameTimeMsgFrac+"m";

	// add custom messages for certain frame ranges (useful for annotating drugs)
	if (frameTimeMinutes>=15 && frameTimeMinutes<=20){msg=msg+"\n1 uM Ang-II";}
	if (frameTimeMinutes>=30 && frameTimeMinutes<=35){msg=msg+"\n15 uM MT";}

	// draw a black rectangle behind the text
	//makeRectangle(0, 0, 500, 50); setForegroundColor(0, 0, 0); run("Fill", "slice");

	// draw black background shadow
	setFont("Monospaced",fontSize,"bold");
	setForegroundColor(0, 0, 0);
	drawString(msg,12,12+fontSize);
	
	// draw yellow foreground
	setForegroundColor(255, 255, 0);
	drawString(msg,10,10+fontSize);
}
```

## Converting a Folder of images to Video

To create a HTML5-compatible MP4 video file:
```bash
ffmpeg.exe -framerate 10 -y -i "./video2/video%%04d.bmp" -c:v libx264 -pix_fmt yuv420p "video.mp4"
```

To create other output formats:\
Drag/drop the folder onto [AVIDEMUX](http://avidemux.sourceforge.net)