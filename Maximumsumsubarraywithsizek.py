def maxsumarr(arr,k):
    n=len(arr)
    currsum=0
    currsum=sum(arr[:k])

    res=currsum

    for i in range(k,n):
        currsum=currsum + arr[i] - arr[i-k]
        res=max(res,currsum)

    return res

arr=[int(x) for x in input().split()]
k=int(input())
print(maxsumarr(arr,k))