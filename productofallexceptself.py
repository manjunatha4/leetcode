def uu(arr):
    p = 1
    n = len(arr)
    for i in range(n):
        p *= arr[i]
    res = [1] * n
    for i in range(n):
        res[i] = p // arr[i]  
    return res
print(uu([12, 4, 5, 7]))