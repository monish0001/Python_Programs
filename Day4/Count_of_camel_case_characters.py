#User function Template for python3

class Solution:
    def countCamelCase (self,s):
        # your code here
        cnt=0;
        for ch in s:
            if ch>='A' and ch<='Z':
                cnt+=1
        
        return cnt
    
    
    
    
if __name__=="__main__":
    s = input("Enter your string: ")
    ob = Solution()
    result = ob.countCamelCase(s)
    print(result)