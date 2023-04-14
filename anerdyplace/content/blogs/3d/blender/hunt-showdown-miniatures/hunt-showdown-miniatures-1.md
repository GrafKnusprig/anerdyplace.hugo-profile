---
title: "Hunt Showdown Miniatures | Part 1"
author: Philipp
date: 2023-04-14T11:10:37+02:00
draft: false
socialShare: false
toc: false
tags: [hunt showdown, blender, miniatures, models, charms, blood bond, dollar]
thumbnail: /blogs/3d/blender/hunt-showdown-miniatures/thumb-1.webp
image: /blogs/3d/blender/hunt-showdown-miniatures/thumb-1.webp
---

# With blender 3.5

...my passion for modeling was awakened anew. My favorite PC game is by far Hunt: Showdown. So I thought, I model a few small things from the game and make them available to the community.

## Blood Bonds

I started with the Blood Bonds. It is the currency in the game, which you can also buy for real money and serves in the game itself only cosmetic purposes.

![image of blood bonds](/blogs/3d/blender/hunt-showdown-miniatures/blood-bonds.webp "")

The Blood Bonds themselves were quite easy to construct and consist only of spheres and many boolean operations.

I posted the thing on reddit and got very positive feedback, so I continued.

## Hunt Dollars

The next thing I did with the hunt dollar. This is the currency in the game.

![image of hunt dollars](/blogs/3d/blender/hunt-showdown-miniatures/hunt-dollars.webp "")

I was able to use the same base as the Blood Bond, but adjusted it a bit. I drew the skulls in outline and then extruded them. The rest I did with my XPPen tablet in sculpting mode.

This was also very well received.

## Hey Effigy

So the next thing I did was the Weapon Charms. 
First, my favorite charm, Hey Effigy.
A little straw doll that you can hang on your weapon in game and then it dangles around.

![image of hey effigy](/blogs/3d/blender/hunt-showdown-miniatures/hey-effigy.webp "")

The fact that the thing ended up looking like real straw was pure coincidence. I tried around a lot. I started with particle systems and hair. Tried to comb everything into shape, but it was very idle and didn't even really look good.

![image of hey effigy](/blogs/3d/blender/hunt-showdown-miniatures/hey-effigy-tries.webp "")

*It looked like everything, but straw. Hair, sticks, Maccaroni, Spaghetti....*

In the end I used Blender's new hair system and created long, thick straws with it. Then converted these into a mesh and then used simple vertex operations to shape them.

The fact that it actually looked like straw in the end is due to the fact that many of the straws intersect. With a subsurface color and the Cycles render engine, the areas darken and it actually looks like straw.

And as a fine bonus, it printed quite well. :)

![image of hey effigy](/blogs/3d/blender/hunt-showdown-miniatures/hey-effigy-print.webp "")

## Arrow Head

Next came the charm Arrow Head. As the name suggests, an arrowhead.
The tip itself was very simple to make. A cone and enie tarpaulin. A few tweaks here and there and done. The real challenge was the cord at the top.
This was the first time I really played around with geometry nodes.

![image from the arrowhead](/blogs/3d/blender/hunt-showdown-miniatures/arrow-head.webp "")

I created a node that draws 2 rotating circles around a curve and wraps them around the curve as long tubes. This worked very well.
After that, I could just draw a path on the surface of the arrowhead and get the cord quite automatically.

I put the longest time into shading here.
I played a lot with the structure of the rope and watched some Youtube tutorials. In the end it came out pretty good.

The arrowhead and the background are procedural materials from Ducky3D, which I modified for my needs.

It's a very good package. You get a lot of materials and you can look up how they are made in the shader nodes and customize a lot of things yourself. Most importantly, you get a feel for what you are achieving and how.

But in the end I think it's a bit expensive, because a lot of the materials are the same and there's just always a lot of noise textures. Ducky probably needs about 2-3 minutes for a material.
