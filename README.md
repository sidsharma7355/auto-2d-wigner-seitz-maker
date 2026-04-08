# auto-2d-wigner-seitz-maker (Mk1)
This simple script automatically calculates and plots the Wigner-Seitz cell for any two dimensional lattice, provided the angle and basis vectors which define the lattice are known. 
Current ver.: Mk. 1.

## What is a Wigner-Seitz cell?
A group of atoms, called the basis, can be translated using a specific translation vector $\vec{T}$ to generate an infinte array of evenly spaced bases, which defines the crystal structure. The set of mathematically defined points to which each basis is attached is called the lattice, and every point within this lattice (associated with the basis) is called the lattice point. Any polygon which tesselates this crystal lattice perfectly is called a *unit cell*. Such a polygon (unit cell) may contain one lattice point (in which case it is called a *primitive* unit cell) or more than one lattice point (in which case it is called a *non-primitive* or *conventional* unit cell). A Wigner-Seitz cell is a specific type of primitive unit cell.

The Wigner-Seitz cell is constructed by applying the Voronoi decomposition method to the crystal lattice. The vertex points of the Wigner-Seitz cell are closer to the origin than any other lattice point surrounding the origin, which makes it the smallest possible primitive unit cell that can fully tesselate the lattice space perfectly. Furthermore, the Wigner-Seitz cell always fully retains the point group symmetry of the lattice that generated it. Therefore, even though there are theoretically an infinite number of possible primitive unit cells for any lattice, there is *always* only one possible Wigner-Seitz cell for any given lattice.

## How to use this tool
The tool utilizes both `numpy` and `matplotlib` and requires both to work. Please ensure both are installed before attempting to run. The download instructions for both `numpy` and `matplotlib` are available online for your specific system if they have not already been packaged with your distribution.
When prompted, enter the basis vectors for your lattice (a1 and a2), and the angle between them (b). 
The computed Wigner-Seitz cell will automatically appear as a separate window. The image can then be saved as a .png file.

# Examples
You can see the tool in action by entering the following values for well-known 2D Bravais lattices:

  1. Square lattice (a1 = 2, a2 = 2, b = 90)
  2. Rectangular lattice (a1 = 2, a2 = 3, b = 90)
  3. Hexagonal or triangular lattice (a1 = 2, a2 = 2, b = 120 or 60). 
  
Once you are familiar with these simple types, you may enter any other values by closing the window and running the program again.

# Notes
The tool accepts values for a1 and a2 as integers and floats, but not as fractions (for now). Likewise (for now), the tool only accepts angles for b in degrees (°). Please ensure you provide your a1 and a2 values as integers or decimals only, and your b value in degrees. 

The tool automatically plots a 3x3 lattice generated as per the lattice parameters. The origin is defined (by default) at the point (1a1, 1a2), which cannot be changed (for now).

It has come to my attention that this tool may struggle at 91°. This will be fixed in the coming update Mk. 2.

If saving the images generated through this method, please note that the size of the .png file will depend entirely on the size of the window containing the plot. Ensure you adjust the dimensions of your window as per your specific requirements. More image formats will be added in the coming iterations!

# Coming in Mk. 2!
Interactive sliders to change a1, a2, and b within the plot window.

Fraction and square root support via the parser system, alongside an optimized an comparator function to rectify edge cases. 

Additional functionalities and customizations, such as Wigner-Seitz cell volume, shading, distance and coordinates to vertex points, custom line and lattice point colors, and lattice classifications.

# 
3D version currently under development.

Copyright 2026, Auto-2D-Wigner-Seitz-maker, Mk. 1, by Siddharth Sharma. This work is licensed under the GNU General Public License v3.0.
