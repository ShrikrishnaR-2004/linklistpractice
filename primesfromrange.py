def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

lower = int(input("Enter lower number: "))
upper = int(input("Enter upper number: "))

for num in range(lower, upper + 1):
    if prime(num):
        print(num, "is a prime number")

        for digit in str(num):
            digit = int(digit)
            if prime(digit):
                print(digit, "is a prime digit of",num)
            else:
                print(digit, "is not a prime digit of",num)
    else:
        print(num, "is not a prime number")