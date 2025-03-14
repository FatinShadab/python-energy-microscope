# Towers of Hanoi

## Problem Definition
The **Towers of Hanoi** is a classic recursive problem that consists of three rods and `N` disks of different sizes, stacked in decreasing order of size on one of the rods (source). The objective is to move all the disks from the **source rod** to the **target rod** using an **auxiliary rod**, following these rules:

1. Only **one disk** can be moved at a time.
2. A disk can only be placed **on top of a larger disk** or on an **empty rod**.
3. No disk can be placed **on top of a smaller disk**.

## Algorithm
The **recursive approach** follows these steps:

1. Move `N-1` disks from **Source** to **Auxiliary**, using **Target** as a temporary rod.
2. Move the **Nth disk** (largest) from **Source** to **Target**.
3. Move `N-1` disks from **Auxiliary** to **Target**, using **Source** as a temporary rod.

### Time Complexity:
- **O(2ⁿ - 1)** (exponential time complexity)

### Example:
```
For, n=3 and disk: 'A', 'B' and 'C':

Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

This recursive approach provides an **optimal solution** to the Towers of Hanoi problem.