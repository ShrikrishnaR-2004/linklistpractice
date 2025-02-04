def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def digitprime(num):
    for i in str(num):
        i=int(i)
        if not prime(i):
            return False
    return True

lower = int(input("Enter lower number: "))
upper = int(input("Enter upper number: "))

for num in range(lower, upper + 1):
    if prime(num) and digitprime(num):
        print(num)


