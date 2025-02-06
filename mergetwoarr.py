#using parallel pointers

def sortedarr(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    if n1==0 and n2==0:
        return None
    arr=[]

    i,j=0,0
    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            arr.append(arr2[j])
            j+=1
        else:
            arr.append(arr1[i])
            i+=1
            j+=1
    while i<n1:
        arr.append(arr1[i])
        i+=1
    while j<n2:
        arr.append(arr2[j])
        j+=1

    return arr

n1=int(input())
arr1=list(map(int,input().split()))
n2=int(input())
arr2=list(map(int,input().split()))
print(sortedarr(arr1,arr2))

