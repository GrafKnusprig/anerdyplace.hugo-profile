---
title: "Purge Wizard"
author: Philipp
date: 2023-07-25T13:19:20+02:00
draft: false
socialShare: false
toc: false
tags: [csharp, batch, purgewizard, delete files]
---

# A friend of mine ...

... needed a program that can do repetitive file deletion tasks for him.

First, I started with a batch script. This way is fast, easy and the file size is small.

The small script simply gets 2 textfiles as an input.
One textfile, which contains the path to the folder, where you want do do your deletion task, and another file which contains a list of the filenames you want to delete.

That way you can delete similar named files from different locations. Which was the main requirement.

[*purge.cmd*](purge.cmd)
```cmd
{{% include "purge.cmd"%}}
```

# It was a good start,

but the requirements became more demanding.

A function was needed, that you can also delete files by using name patterns and even wildcards.

As a batch script is not the most intuitive to use for non programmers, I thought to myself, that I want to write a litte .net application. With an easy to use UI and bulletproof to wrong user inputs.

![purgewizard screenshot](purgewizard.webp)

You can even import the old txt based file lists via the import function. This also works with patterns.

Once you have created your deletion task, you can easily save your config for future uses. The app saves your data into a serealized json and uses the data format .pwiz.

You can get the App and the source code at:

[https://github.com/GrafKnusprig/PurgeWizard](https://github.com/GrafKnusprig/PurgeWizard)

Have fun :)