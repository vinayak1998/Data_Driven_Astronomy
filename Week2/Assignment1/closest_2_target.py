import numpy as np

def hms2dec(h,m,s):
  return 15*(h + (m/60) + (s/3600))

def dms2dec(d,m,s):
  if d>=0:
    return (d + (m/60) + (s/3600))
  return (d - (m/60) - (s/3600))

def angular_dist(r1, d1, r2, d2):  
  r1= np.radians(r1)
  r2= np.radians(r2)
  d1= np.radians(d1)
  d2= np.radians(d2)
  a = (np.sin(np.abs(d1 - d2)/2))**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  d = np.degrees(2*np.arcsin(np.sqrt(a + b)))
  return d

def import_bss():
  cat = np.loadtxt('bss.dat', usecols=range(1, 7))
  loaded = []
  count = 1
  for i in cat:
    loaded.append((count, hms2dec(i[0],i[1],i[2]), dms2dec(i[3],i[4],i[5])))
    count+=1
  return loaded

def import_super():
  cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  loaded = []
  count = 1
  for i in cat:
    loaded.append((count, i[0], i[1]))
    count+=1
  return loaded

def find_closest(catalogue,target_ra, target_dec):
  min_distance = 9999999
  ID = 0
  for i in catalogue:
    distance = angular_dist(i[1], i[2], target_ra, target_dec)
    if distance<min_distance:
      min_distance = distance
      ID = i[0]
  return (ID,min_distance)


if __name__ == '__main__':
  cat = import_bss()
  print(find_closest(cat, 175.3, -32.5))
  print(find_closest(cat, 32.2, 40.7))
