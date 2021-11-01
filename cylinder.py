# inspiration code for Python Unit Testing Project
# this code is the same exact file as used by the command line project
# it can just be imported as it by the web app
# and also still be used by itself

import math

def surfaceArea(rad, hi):
    surface = 2 * math.pi * rad * hi + 2 * math.pi * rad^2
    return surface

def volume(rad, hi):
    volume = math.pi * rad * rad * hi
    return volume

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A CYLINDER")
    print("----------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    height = int(input("Please Enter the height :"))

    print("\nThe Volume of a Cylinder = ", volume(radius, height))
    print("\nThe surfaceArea of a Cylinder = ", surfaceArea(radius, height))
if __name__ == '__main__':
    prompt()