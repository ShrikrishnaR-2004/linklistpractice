# 1->A
# 2->B
# 3->C
# ....
# 26->Z
# 27->AA
# 28->AB
# ...
# .. range of input<500

def inttostr(num):
    if num<= 0:
        print("Invalid")
        return
    aplha=[]
    while num>0:
        num-=1
        str1=aplha.append(chr(ord("A")+num%26))
        num//=26
    for i in range(len(aplha)-1,-1,-1):
        print(aplha[i],end="")
num=int(input())
inttostr(num)

