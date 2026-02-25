#User function Template for python3

class Solution:
    def solve(self,A,B,m,n):
        
        
        if m==0:
            return True
        
        if n==0:
            return False
        
        if A[m-1]==B[n-1]:
            return self.solve(A,B,m-1,n-1)
        
        return self.solve(A,B,m,n-1)
        
    def isSubSequence(self, A, B):
        
        
        
        m=len(A)
        n=len(B)
        
        return self.solve(A,B,m,n)
        
        
        #code here
        
        # i,j=0,0
        
        # n,m=len(A),len(B)
        
        # while(i<n and j<m):
            
        #     if (A[i]==B[j]):
        #         i+=1
        #     j+=1
        
        
        # return i==n
        
        
def main():
    A = "gksrek"
    B = "geeksforgeeks"
    ob = Solution()
    print(ob.isSubSequence(A, B))   
    
if __name__=="__main__":    main()
        
        
        
            
                