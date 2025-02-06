def palindrome(str1):
    if len(str1) == 0:
        return "String is empty"
    str1 = str1.lower()
    new=''
    for i in str1:
        if i.isalnum():
            new+=i.lower()
    left,right = 0,len(new)-1
    while left < right:
        if new[left] != new[right]:
            return False
        left += 1
        right -= 1
    return True

str1=input()
print(palindrome(str1))


