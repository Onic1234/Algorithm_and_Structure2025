# A program to find one missing number in a given array of numbers between 1 and 10

def find_missing_number(arr):
    """Find the missing number in the given array."""
    expected_sum = sum(range(1, 11))  # Sum of numbers from 1 to 10
    actual_sum = sum(arr)  # Sum of numbers in the given array
    missing_number = expected_sum - actual_sum  # The difference is the missing number
    return missing_number

# Example usage
input_array = [1, 2, 3, 4, 5, 6, 8, 9, 10]
missing_number = find_missing_number(input_array)
print(f'Missing number is {missing_number}')

# Example usage 2
input_array1 = [1,3, 4, 5, 6, 7, 8, 9, 10]
missing_number = find_missing_number(input_array1)   
print(f'Missing number is {missing_number}')

print('\n--- Oleh L200234275 ---')