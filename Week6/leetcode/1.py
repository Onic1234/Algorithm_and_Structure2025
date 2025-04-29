# 1539. Kth Missing Positive Number create the code
# https://leetcode.com/problems/kth-missing-positive-number/

def findKthPositive(arr, k):
    missing_count = 0
    current = 1
    index = 0

    while missing_count < k:
        if index < len(arr) and arr[index] == current:
            index += 1
        else:
            missing_count += 1
        current += 1

    return current - 1
 
