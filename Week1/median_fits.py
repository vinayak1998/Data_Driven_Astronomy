import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import time

def median_fits(filenames):
  start = time.perf_counter()
  memory = 0
  n = len(filenames)
  collect = [0]*n
  for i in range(len(filenames)):
    hdulist = fits.open(filenames[i])
    collect[i] = hdulist[0].data
    memory += collect[i].nbytes
  collect = np.array(collect)
  answer = np.median(collect, axis=0)
  end = time.perf_counter() - start
  memory/=1024
  return (answer , end, memory)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])