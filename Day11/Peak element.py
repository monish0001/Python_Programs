class Solution:   
    def peakElement(self, arr):
        # Code here
        
        N=len(arr)
        
        if N==1:
            return 0
        
        elif arr[0]> arr[1]:
            return 0
        elif arr[N-1]> arr[N-2]:
            return N-1
        else:
            for i in range(1,N-1):
                if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                    return i
        
        
        return False
                
        
        
        
def main():
    arr=[1, 2, 3, 4, 5]
    obj=Solution()
    print(obj.peakElement(arr))

if __name__ == '__main__':
    main()