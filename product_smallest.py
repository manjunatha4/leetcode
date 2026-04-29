def psp(a,d):
  if len(a) < 2:
    return -1
  a.sort()
  if a[0]+a[1] <= d:
    return a[0]*a[1]
  else:
    return 0
print(psp([78,34,56,12,38],50))

