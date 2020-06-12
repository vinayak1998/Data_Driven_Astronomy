import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u
import time

def crossmatch(cat1, cat2, max_dist):
  matches = []
  no_matches = []

  start = time.perf_counter()
  
  skycat1 = SkyCoord(cat1*u.degree, frame='icrs')
  skycat2 = SkyCoord(cat2*u.degree, frame='icrs')
  closest_ids, closest_dists, closest_dists3d = skycat1.match_to_catalog_sky(skycat2)
  closest_dists = closest_dists.value
  
  for i in range(len(cat1)):
    if closest_dists[i] > max_dist:
      no_matches.append(i)
    else:
      matches.append((i,closest_ids[i],closest_dists[i]))
  
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