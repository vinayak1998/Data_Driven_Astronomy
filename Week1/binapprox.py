import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import time

def median_bins(data, B):
  mean = np.mean(data)
  std = np.std(data)
  minval = mean - std
  
  bins = np.zeros(B)
  bin_width = (2*std)/B
  smaller = 0
  for i in data:
    binmax = minval
    if i < minval:
      smaller+=1
    else:
      for j in range(B):
        binmax+=bin_width
        if i < binmax:
          bins[j] += 1
          break
  return (mean, std, smaller, bins)

def median_approx(data, B):
  mean, std, total, bins = median_bins(data,B)
  minval = mean - std
  bin_width = (2*std)/B
  target = (len(data)+1)/2
  for i in range(len(bins)):
    total+=bins[i]
    if total>=target:
      return (i*bin_width) + minval + (bin_width/2)
  return (i*bin_width) + minval + (bin_width/2)

# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
