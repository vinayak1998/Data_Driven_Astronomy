def hms2dec(h,m,s):
  return 15*(h + (m/60) + (s/3600))

def dms2dec(d,m,s):
  if d>=0:
    return (d + (m/60) + (s/3600))
  return (d - (m/60) - (s/3600))


if __name__ == '__main__':
  print(hms2dec(23, 12, 6))
  print(dms2dec(22, 57, 18))
  print(dms2dec(-66, 5, 5.1))