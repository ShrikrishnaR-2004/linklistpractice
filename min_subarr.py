nums=list(map(int,input().split()))
target=int(input())

def min_subarr(nums,target):
    if target==0 or sum(nums)<target:
        return 0
    for i in range(len(nums)):
        if nums[i]>target:
            return 1
    l=[]
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if sum(nums[i:j])>=target:
                l.append(len(nums[i:j]))
    if min(l)!=len(nums):
        return min(l)
    else:
        return 0
print(min_subarr(nums,target))
