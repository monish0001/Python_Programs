class Solution:
    def findSum(self, n):
        
        return n * (n + 1) // 2  
        

if __name__ == "__main__":
    n = int(input())
    ob = Solution()
    print(ob.findSum(n))

