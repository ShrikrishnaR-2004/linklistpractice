def reversestr(str1):
    s=[]
    for i in str1:
        s.append(i)
    for i in str1:
        print(s.pop(),end="")

str1=input("enter string:")
reversestr(str1)