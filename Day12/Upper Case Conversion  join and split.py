class Solution:
    def convert(self, s):
        # code here
        list=s.split()
        ans=[]
        for item in list:
           ans.append(item[0].upper()+item[1:])
            
        return ' '.join(ans)
    
def main():
    s = "geeks for geeks"
    ob = Solution()
    print(ob.convert(s))
    
    
if __name__=="__main__":
    main()