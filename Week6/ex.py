# I have a mountain array called arr. You need to find the peak/highest point of the mountain array arr. 
# The input of the program is the mountain array, and the output is the index of the peak/highest point of the mountain array. 
# Example : Input : [0,2,4,2,0] → Output : 2 Input : [0,5,10,20,10,2,0] → Output : 3

def find_peak(arr):
    kiri, kanan = 0, len(arr) - 1

    while kiri < kanan:
        mid = (kiri + kanan) // 2
        if arr[mid] < arr[mid + 1]:
            kiri = mid + 1
        else:
            kanan = mid

    return kiri

print(find_peak([0, 2, 4, 2, 0]))  
print(find_peak([0, 5, 10, 20, 10, 2, 0]))
