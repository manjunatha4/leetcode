def stack(arr):
    l = len(arr)
    maxp = 0 
    for i in range(l):
        for j in range(i+1, l):
            profit = arr[j] - arr[i]
            maxp=max(maxp,profit)
    return maxp
print(stack([6,7,1,2,8,5]))  