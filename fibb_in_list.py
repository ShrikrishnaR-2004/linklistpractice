def fibb(n):
    if n <= 1:
        return n
    else:
        return fibb(n-1) + fibb(n-2)

def fibblist(num):
    l=[]
    for i in range(num):
        l.append(fibb(i))
    return l

n=int(input())
print(fibblist(n))
