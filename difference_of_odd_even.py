def summ(a):
  n=len(a)
  evn_sum=0
  odd_sum=0
  if n==0:
    return 0
  for i in range(n):
    if n%2==0:
      even_sum+=a[i]
    else:
      odd_sum+=a[i]
    d= odd_sum - evn_sum
    return d
a=[4, 6, 1, 3, 8]
print("difference is: ",summ(a))
  