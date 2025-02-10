# string=> 6D53W41WWPP
# 6+5+3+4+1 = 19
#  EACH P = 10
#  19+10+10 = 30

s=input()
sum=0
for i in s:
    if i.isdigit():
        sum+=int(i)
    elif i=="P":
        sum+=10
print(sum)

