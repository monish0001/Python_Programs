class Solution:    
    def printNos(self,n):
        #Code here
        if n==0:
            return
        self.printNos(n-1)
        print(n, end=" ")
        
        
def main():
    n = 5
    ob = Solution()
    ob.printNos(n)

if __name__=="__main__":    main()