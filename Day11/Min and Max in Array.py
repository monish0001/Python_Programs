
class Solution:
    def getMinMax(self, arr):
        
        min_element= float('inf') 
        max_element= float('-inf') 
        
        for i in range(len(arr)):
            min_element=min(arr[i],min_element)
            max_element=max(arr[i],max_element)
            
        return min_element,max_element
    
def main():
    arr=[1, 2, 3, 4, 5]
    obj=Solution()
    print(obj.getMinMax(arr))

if __name__ == "__main__":    main()
            