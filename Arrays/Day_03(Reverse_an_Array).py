def Reverse_Array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    # Time Complexity = O(n)
    # Space Complexity = O(1)
def default_reverse_function(arr):
    arr.reverse()

    # Time Complexity = O(n)
    # Space Complexity = O(1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Reverse_Array(arr)
print(arr) # Output = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 

default_reverse_function(arr)
print(arr) # Output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

