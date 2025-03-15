try:
    num1 = float(input("Enter a Number: "))
    
    if num1.is_integer():
        num1 = int(num1)
        if num1 > 1:
            for i in range(2, num1):
                if (num1 % i) == 0:
                    print(num1, "is not a prime number")
                    break
            else:
                print(num1, "is a prime number")
        else:
            print(num1, "is not a prime number")
    else:
        print("Decimal numbers cannot be prime numbers")
except ValueError:
    print("Invalid input! Please enter a valid number.")
