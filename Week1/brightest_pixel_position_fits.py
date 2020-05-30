import numpy as np
import time
from astropy.io import fits
import matplotlib.pyplot as plt

def load_fits(filename):
  start = time.perf_counter()
  hdulist = fits.open(filename)
  data = hdulist[0].data
  result = np.where(data == np.amax(data))
  coornidates = list(zip(result[0],result[1]))
  end = time.perf_counter() - start
  return coornidates[0]
  
if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image1.fits')
  print(bright)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()