---
title: "Turtle Park"
author: Philipp
date: 2025-03-04T14:34:12+01:00
draft: true
socialShare: false
toc: false
tags: [tag]
supressThumbnail: false
thumbnail: /images/blog/generic-thumbs/default.webp
---
For the 3D scan, I used the app Reality Scan. It's free, but note that your files are public. This app uses photogrammetry, and you can download the scan as a GLB file. Blender works well with that format and even includes UV mappings.

![Image of scan](<Screenshot 2025-03-04 at 14.31.03.png>)

To import into Blender and bring it to scale:
1. Measure two points where you did real-world measurements.
2. Calculate the scale factor:

$$ \text{Scale Factor} = \frac{\text{Real Distance}}{\text{Blender Measured Distance}} $$

Here are some initial ideas:

![First ideas](<Screenshot 2025-03-04 at 15.23.08.png>)

I added a cabinet under the turtle house to get more storage room in the kitchen.

![Cabinet addition](image.png)

For measuring and getting the output as measurements, I use the Blender addon MeasureIt.

![MeasureIt addon](<Screenshot 2025-03-05 at 16.40.53.png>)

You can only add the measurements in edit mode, but that's no big deal.

Click the render button.

Then in the compositor, add an alpha layer for the measurements.

![Compositor setup](<Screenshot 2025-03-05 at 16.40.40.png>)

That renders the measurements to your image. You also need to set up a scene with a camera and lights; otherwise, you won't see anything.
