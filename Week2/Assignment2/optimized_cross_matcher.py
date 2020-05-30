import numpy as np
import time

def hms2dec(h,m,s):
  return 15*(h + (m/60) + (s/3600))

def dms2dec(d,m,s):
  if d>=0:
    return (d + (m/60) + (s/3600))
  return (d - (m/60) - (s/3600))

def angular_dist(r1, d1, r2, d2):   # remove radians, radians mein hi ghusenge
  # r1= np.radians(r1)
  # r2= np.radians(r2)
  # d1= np.radians(d1)
  # d2= np.radians(d2)
  a = (np.sin(np.abs(d1 - d2)/2))**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  d = np.degrees(2*np.arcsin(np.sqrt(a + b)))
  return d

def crossmatch(cat1, cat2, max_dist):
  matches = []
  no_matches = []
  start = time.perf_counter()
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  id_1 = 0
  for i in cat1:
      best = (0,0,max_dist+1)
      id_2 = 0
      for j in cat2:
        dist = angular_dist(i[0], i[1], j[0], j[1])
        if dist<=best[2]:
          best = (id_1,id_2,dist)
        id_2+=1
      if best[2]<=max_dist:
         matches.append(best)
      else:
         no_matches.append(id_1)
      id_1+=1
  return (matches, no_matches, time.perf_counter() - start)