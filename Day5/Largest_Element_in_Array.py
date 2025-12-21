
class Solution:
    def largest(self, arr):
        ans = arr[0]
        for num in arr:
            ans = max(ans, num)
        return ans

if __name__=="__main__":
    n = int(input("Enter number of elements in array: "))
    arr = list(map(int, input("Enter the elements of the array: ").strip().split()))[:n]
    ob = Solution()
    result = ob.largest(arr)
    print(f"The largest element in the array is: {result}")

