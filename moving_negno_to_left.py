def moving_negno_to_left(arr):
    l=[]
    for i in range(len(arr)):
        if arr[i] < 0:
            l.append(arr[i])
    for i in range(len(arr)):
        if arr[i] >= 0:
            l.append(arr[i])

    return l

arr=list(map(int,input().split()))
print(moving_negno_to_left(arr))
