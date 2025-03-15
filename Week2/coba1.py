# a program that checks whether a number is prime or not prime
num = int(input("Input number: "))

# check if the number is less than or equal to 1 or negatif number
if num <= 1:
    print(num, "is not a prime number")
else:
#   Checking whether a number is divisible by any number other than 1 and itself
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

print("\n--- L200234275 ---")