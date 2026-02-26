
class Solution:
    def binarySubstring(self, s):
        #code here
        
        N=len(s)
        ones=0
        
        for i in range(N):
            if s[i]=='1':
                ones+=1
            
        return (ones * (ones - 1)) // 2
        
    
                    
                    
def main():
    s="001101"
    ob=Solution()
    print(ob.binarySubstring(s))
    
if __name__ == "__main__":    
    main()