def print2Largest(arr: list) -> int:
    n: int = len(arr)
    first:int = float("-inf")
    second: int = float("-inf") 

    for num in arr:
        if num > first:
            second = first
            first = num
        elif second < num and first != num:
            second = num
    
    if second != float("-inf"):
        return second
    else:
        return -1
# Time Complexity: O(n)
# Space Complexity: O(1)

# Example 
## Case 1
arr: list = [1, 2, 3 ,5, 4, 4, 7 ,6, 8, 8] 
result:int = print2Largest(arr)

if result == -1:
    print("No second value")
else:
    print(f"Second largest value: {result}")

## Case 2
arr: list = [1] 
result:int = print2Largest(arr)

if result == -1:
    print("No second value")
else:
    print(f"Second largest value: {result}")

