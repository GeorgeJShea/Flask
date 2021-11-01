# inspiration code for Python Unit Testing Project
import math

def surfaceArea(radius):
    sur = 4 * math.pi * radius ^ 2
    return sur

def volume(radius):
    vol = (4/3) * math.pi * radius^ 3
    return vol

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))

    print("\nThe Volume of a sphere = ", volume(radius))
    print("\nThe surfaceArea of a sphere = ", surfaceArea(radius))
if __name__ == '__main__':
    prompt()
