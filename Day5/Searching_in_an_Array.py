from typing import List

class Solution:
    def search(self, k: int, arr: List[int]) -> int:
        idx = -1
        for i in range(len(arr)):
            if arr[i] == k:
                idx = i+1
                break
        return idx
    
if __name__=="__main__":
    n = int(input("Enter number of elements in array: "))
    arr = list(map(int, input("Enter the elements of the array: ").strip().split()))[:n]
    k = int(input("Enter the element to search: "))
    ob = Solution()
    result = ob.search(k, arr)
    if result != -1:
        print(f"Element found at position: {result}")
    else:
        print("Element not found in the array.")