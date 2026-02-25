class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        dict={}
        
        for num in arr:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        
        
        for key,value in dict.items():
            if value%2!=0:
                return key
                
        return -1

def main():
    arr = [1, 2, 3, 2, 3, 1, 3]
    ob = Solution()
    print(ob.getOddOccurrence(arr))
    
if __name__=="__main__":    main()
                