def stackk_o(arr):
    buy=arr[0]
    res=0
    for i in range(1,len(arr)):
        buy=min(buy,arr[i])
        res=max (res,arr[i]-buy)
    return res
print(stackk_o([6,7,1,2,8,5]))  
