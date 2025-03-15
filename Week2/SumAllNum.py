try:
    num = int(input("Give a num: "))
    
    if num <= 0:
        print("Please enter a positive number greater than zero.")
    else:
        total = sum(range(1, num + 1)) 
        print("Sum of numbers from 1 to", num, "is:", total)
except ValueError:
    print("Invalid input! Please enter a valid integer.")