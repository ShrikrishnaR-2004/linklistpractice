def reverseOnlyLetters( s):
    k = ""
    for i in s:
        if i.isalpha():
            k += i
        k = k[::-1]
        i = 0
        j = 0
        l = list(s)
        for i in range(len(l)):
            if l[i].isalpha():
                l[i] = k[j]
                j += 1

        p = "".join(l)
        return p

s='ab-cd'
print( reverseOnlyLetters(s) )