# a program to calculate the sum of all number between 1 and a given number (input).

# Get the input 
n = int(input("Input number: "))

# Initialize the sum
sum = 0 

# Check if the number is less than or equal to 0
if n <= 0:
    print("Please enter a positive number greater than zero.")
else:
    # Loop the number from 1 to n
    for i in range(1, n + 1):
        sum += i
        
    # Print the sum
    print("Sum of numbers from 1 to", n, "is:", sum)
    
print("\n--- L200234275 ---")