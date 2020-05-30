"""angular_dist that calculates the angular distance between any two points on 
the celestial sphere given their right ascension and declination.
Angular distances have the same units as angles (degrees)."""

#b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
#d = 2*np.arcsin(np.sqrt(a + b))

import numpy as np

def angular_dist(r1, d1, r2, d2):
"""Trig functions in most languages and libraries (including Python and NumPy) 
take angle arguments in units of radians, but the databases we're working with 
use angles of degrees.

Fortunately, NumPy provides convenient conversion functions:

a_rad = np.radians(a_deg)
a_deg = np.degrees(a_rad)
The variable a_deg is in units of degrees and a_rad is in radians."""  
  r1= np.radians(r1)
  r2= np.radians(r2)
  d1= np.radians(d1)
  d2= np.radians(d2)
  
"""There are other 
equations for calculating the angular distance but this one, called the 
haversine formula, is good at avoiding floating point errors when the two 
points are close together."""

  a = (np.sin(np.abs(d1 - d2)/2))**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  d = np.degrees(2*np.arcsin(np.sqrt(a + b)))
  
  return d

if __name__ == '__main__':
  print(angular_dist(21.07, 0.1, 21.15, 8.2))
  print(angular_dist(10.3, -3, 24.3, -29))

