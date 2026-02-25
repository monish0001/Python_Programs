class Solution:
    def concatenatedString(self,s1,s2):
        #code here
        
        result=""
        
        for ch in s1:
            if ch not in s2:
                result+=ch
        
        for ch in s2:
            if ch not in s1:
                result+=ch
                
        
        if result=="":
            return -1
                
        
        return result
    
def main():
    s1 = "aacdb"
    s2 = "gafd"
    ob = Solution()
    print(ob.concatenatedString(s1, s2))
    
if __name__=="__main__":    main()