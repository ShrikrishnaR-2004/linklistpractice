# Check a number is perfect Two-power or not but without using /,+,pow(),**,* symbol

def perfect_twopower(n):
    if n>=0 and n&(n-1)==0:
        return True

n=int(input())
print(perfect_twopower(n))