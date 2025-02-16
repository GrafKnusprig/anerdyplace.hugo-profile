---
title: "Minimalist Wallet"
author: Philipp
date: 2025-02-16T01:01:18+01:00
draft: false
socialShare: false
toc: false
tags: [3D printing, wallet, minimalist, prusa, slicer]
supressThumbnail: false
---

# 3D printed Minimalist Wallet

## Version 1
![alt text](<Screenshot 2025-02-16 010207.png>)

Version 1 was our first try. We experimented with a screw design which ended up with several quirks:

- **Limited Space:** Not enough room for coins.
- **Design Constraints:** The width was dictated by the minimal screw length.
- **Rubber Band Mechanism:** A rubber band was clamped in and wrapped around the wallet, aiming to secure money bills.

This early version was a stepping stone towards a better design. Future iterations will focus on expanding storage and refining the fastening method.
![alt text](<Screenshot 2025-02-16 010232.png>)

## Version 2

![alt text](<Screenshot 2025-02-16 010326.png>)

Version 2 introduces a refined design approach:

- **Integrated Rubber Band:** The rubber band is now sewed into an endless loop, hidden within the wallet.
- **Custom Covers:** It features custom designed, exchangeable covers that are press-fit. They’re typically glued on for long-term durability.
- **Enhanced Coin Compartment:** The coin compartment is significantly larger and better designed, featuring a click-in-place hinge for secure closure.

![alt text](<Screenshot 2025-02-16 010313.png>)

## Multicolor First Layer Approach

This update gives the wallet a sleek, multicolor finish right from the first layer:

- **Swappable Filaments:** The cover shells allow for filament swaps, making a multicolor print possible.
- **Clean Design:** No extra edges, bridges, or structure—just pure color.
- **Flexible Options:** If you prefer a more structured look over the color effect, simply omit the colored objects and print the shells as they are.

### How to print multicolor
1. **Software Setup:**  
   - Use PrusaSlicer. It supports 3MF files and lets you hide parts of your model.
   ![alt text](<Screenshot 2025-02-16 005428.png>)

2. **Slicing Process:**  
   - Load your 3MF file.
   - Hide the shells and slice only the color infill.
   - Then, hide the color infill and slice only the shell.
   ![alt text](<Screenshot 2025-02-16 005046.png>)
   ![alt text](<Screenshot 2025-02-16 005108.png>)
   ![alt text](<Screenshot 2025-02-16 005206.png>)

3. **Printing Steps:**  
   - Print the color infill.
   - Swap the filament.
   - Print the shell.

4. **Tips:**  
   - Skip the brim or skirt to avoid interference.
   - Keep an eye on the print bed temperature—add custom G-code if needed to prevent it from cooling too much.
   - With an 11-minute print, manual intervention works just fine.
   ![alt text](<Screenshot 2025-02-16 005222.png>)
