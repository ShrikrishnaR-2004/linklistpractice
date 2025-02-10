#[1,2,3,5,6] ->4 missing no

l=[1,2,3,5,6]
n=len(l)+1
l_sum=sum(l)

sum1=n*(n+1)/2
print(int(sum1-l_sum))