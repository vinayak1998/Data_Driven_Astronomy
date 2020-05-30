import numpy as np

def hms2dec(h,m,s):
  return 15*(h + (m/60) + (s/3600))

def dms2dec(d,m,s):
  if d>=0:
    return (d + (m/60) + (s/3600))
  return (d - (m/60) - (s/3600))

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

if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)