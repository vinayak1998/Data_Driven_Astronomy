import numpy as np
import time

def hms2dec(h,m,s):
  return 15*(h + (m/60) + (s/3600))

def dms2dec(d,m,s):
  if d>=0:
    return (d + (m/60) + (s/3600))
  return (d - (m/60) - (s/3600))

def angular_dist(r1, d1, r2, d2):   # remove radians, radians mein hi ghusenge
  a = (np.sin(np.abs(d1 - d2)/2))**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  d = 2*np.arcsin(np.sqrt(a + b))
  return d

def crossmatch(cat1, cat2, max_dist):
  max_dist = np.radians(max_dist)
  matches = []
  no_matches = []

  start = time.perf_counter()
  
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  
  sorted_indexes = np.argsort(cat2[:, 1])
  
  id_1 = 0
  for i in cat1:
      best = (0,0,max_dist+1)
      id_2 = 0
      for j in sorted_indexes:
        if(cat2[j][1] > max_dist + i[1]):
          break
        dist = angular_dist(i[0], i[1], cat2[j][0], cat2[j][1])
        if dist<=best[2]:
          best = (id_1,j,dist)
        id_2+=1
      if best[2]<=max_dist:
         matches.append(best)
      else:
         no_matches.append(id_1)
      id_1+=1
 
  time_taken = time.perf_counter() - start
  return (matches, no_matches, time_taken)

if __name__ == '__main__':
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)
