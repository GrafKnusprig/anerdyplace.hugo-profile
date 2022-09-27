---
title: "Webp Image Converter"
author: Philipp
date: 2022-09-13T14:29:06+02:00
draft: false
toc: true
tags: [batch, webp, script, programming]
socialShare: false
thumbnail: /images/blogs/generic-thumbs/batch.webp
---

## Introduction

I needed a small batch script to quickly convert all types of images into webp.

## An image format for the Web

WebP is a modern image format that provides superior lossless and lossy compression for images on the web. Using WebP, webmasters and web developers can create smaller, richer images that make the web faster.

WebP lossless images are 26% smaller in size compared to PNGs. WebP lossy images are 25-34% smaller than comparable JPEG images at equivalent SSIM quality index.

Lossless WebP supports transparency (also known as alpha channel) at a cost of just 22% additional bytes. For cases when lossy RGB compression is acceptable, lossy WebP also supports transparency, typically providing 3× smaller file sizes compared to PNG.

Lossy, lossless and transparency are all supported in animated WebP images, which can provide reduced sizes compared to GIF and APNG.

*From https://developers.google.com/speed/webp*

## Installation

Get cwebp from **https://developers.google.com/speed/webp/docs/cwebp**.

## Batch file
[*convert_to_webp.cmd*](/files/scripts/convert_to_webp.cmd)
```c
{{% include "static/files/scripts/convert_to_webp.cmd"%}}
```

**%1** gives us the first file from the stack. The command **shift** iterates through the stack. If **%1** is empty, we go to **eof** and end the script.

**%~n1** gives us our filename without the extension. So we can add **.webp**.

## Windows right click -> send to

Add the script to your SendTo folder.
You can access the folder with the shortcut **Win + R** and type **shell:sendto**.

Or go to *C:\Users\\[username]\AppData\Roaming\Microsoft\Windows\SendTo*