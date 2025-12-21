class Solution:
    def findSum(self, n):
        # Use the formula for the sum of the first n natural numbers
        return n * (n + 1) // 2  # Integer division to avoid floating-point result
        
# Driver Code Starts
if __name__ == "__main__":
    n = int(input())
    ob = Solution()
    print(ob.findSum(n))
# Driver Code Ends
