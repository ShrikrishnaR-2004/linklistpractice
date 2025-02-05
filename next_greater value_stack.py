# find the next greater value in the stack
#
# [10,20,1,6,10]->[20,0,6,10,0]

n=[int(x) for x in input().split()]
s=[]
for i in range(len(n)-1):
    if n[i]<n[i+1]:
        s.append(n[i+1])
    else:
        s.append(0)
s.append(0)
print(s)
