from __future__ import division #division results in a float number
from math import *

def polysum(n,s):
    """
    Polysum function
    The function takes two arguments, n (i.e number of sides) and s (i.e each side length).
    The function returns the sum the area and square of the perimeter of the regular polygon.
    """
    
    area = 0.25*n*s**2/tan(pi/n)
    perimeter = s*n
    
    return round(area + perimeter**2,4)