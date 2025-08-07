class Solution:
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
            
    def rotateArr(self, arr, d):
        n = len(arr)
        # Calculate effective rotations
        d = d % n
        
        if d < 0:
            d += n
            
        # Step 1: Reverse the first 'd' elements
        self.reverse(arr, 0, d - 1)
        
        # Step 2: Reverse the remaining elements
        self.reverse(arr, d, n - 1)
        
        # Step 3: Reverse the entire array
        self.reverse(arr, 0, n - 1)

# Time Complexity O(n)
# Space Complexity O(1)

