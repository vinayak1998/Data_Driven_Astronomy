import numpy as np
import time
from astropy.io import fits
import matplotlib.pyplot as plt

from running_mean_std_FITS import running_stats

def median_bins_fits(filenames,B):
  mean, std = running_stats(filenames)
  smaller = np.zeros(mean.shape) #200x200
  bins = np.zeros((mean.shape[0],mean.shape[1],B))
  minval = mean-std
  bin_width = (2*std)/B
  
  for i in filenames:
    hdulist = fits.open(i)
    image = hdulist[0].data
    
    for x in range(mean.shape[0]):
      for y in range(mean.shape[1]):
        binmax = minval[x][y]
        pixel = image[x][y]
        
        if pixel<minval[x][y]:
          smaller[x][y]+=1
        else:
          for j in range(B):
            binmax+=bin_width[x][y]
            if pixel<binmax:
              bins[x][y][j]+=1
              break
  return (mean, std, smaller, bins)    
  
def median_approx_fits(filenames,B):
  
  mean, std, total, bins = median_bins_fits(filenames,B)
  
  minval = mean - std
  bin_width = (2*std)/B
  target = (len(filenames)+1)/2
  answer = np.zeros(mean.shape)
  for x in range(answer.shape[0]):
    for y in range(answer.shape[1]):
      for i in range(B):
        total[x][y]+=bins[x][y][i]
        if total[x][y]>= target:
          answer[x,y] = (i*bin_width[x,y]) + minval[x,y] + bin_width[x,y]/2
          break
  return answer


if __name__ == '__main__':
  # Run your function with examples from the question.
  mean, std, left_bin, bins = median_bins_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  median = median_approx_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)