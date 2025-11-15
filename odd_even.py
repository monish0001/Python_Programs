class Solution:
    def countOddEven(self, arr):
        odd_count = 0
        even_count = 0

        for item in arr:
            if item % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        return odd_count, even_count



obj = Solution()
arr = [1, 2, 3, 4, 5, 6]

odd, even = obj.countOddEven(arr)

print("Array:", arr)
print("Odd count:", odd)
print("Even count:", even)
