import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import time

def mean_fits(filenames):
  start = time.perf_counter()
  n = len(filenames)
  collect = [0]*n
  for i in range(len(filenames)):
    hdulist = fits.open(filenames[i])
    collect[i] = hdulist[0].data
  collect = np.array(collect)
  for i in collect[1:]:
    collect[0]+=i
  collect[0]=collect[0]/n
  end = time.perf_counter() - start
  return (collect[0])

if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()