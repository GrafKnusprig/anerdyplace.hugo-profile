---
title: "Arduino Micro Isp"
author: Philipp
date: 2020-02-24
draft: false
socialShare: false
tags: [arduino, isp, programming]
thumbnail: /images/blogs/arduino/arduino-micro-isp/thumb.webp
---

## Description

A PWM signal is generated at output PB3 without timer prescaler. The register OCR0 (0..255) defines the duty cycle. The timer runs in non inverting mode. Thus, the output becomes high when the counter jumps from 255 to 0 and the output becomes low when the coampare match takes place and the counter is equal to OCR0.


## Sourcecode
[*FastPWM.c*](/files/arduino/FastPWM.c)
```c
{{% include "static/files/arduino/FastPWM.c"%}}
```

## Signal Plot
![signal plot](/images/blogs/arduino/arduino-micro-isp/signal-plot.png)
