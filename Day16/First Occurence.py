class Solution:
    def firstOccurence(self,txt,pat):
        #code here
        
       
        if txt==pat:
            return 0
        
        n=len(txt)
        m=len(pat)
        
        if m>n: return -1
        
        for i in range(n):
            
            match=True
            
            for j in range(m):
                
                if txt[i+j]!=pat[j]:
                    match=False
                    break
                
                
            if match:
                return i
        
        
        return -1
        
        
        
def main():
    txt="geeksforgeeks"
    pat="geks"
    sol=Solution()
    print(sol.firstOccurence(txt,pat))
    
if __name__=="__main__":    main()