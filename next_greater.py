def next_greater(arr):
    n = len(arr)
    stk = []
    res = [-1] * n
    for i in range(n - 1, -1, -1):
        while stk and stk[-1] <= arr[i]:
            stk.pop()
        if stk:
            res[i] = stk[-1]
        stk.append(arr[i])
    return res
arr = [4, 5, 2, 10, 8]
print(next_greater(arr))