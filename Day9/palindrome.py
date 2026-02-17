import sys

sys.stdin=open('input.txt', 'r')
sys.stdout=open('output.txt', 'w')


from typing import List


class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        # code here
        
        N=len(arr)
        
        i=0
        while i<N//2:
            if arr[i]!=arr[N-i-1]:
                return False
            i+=1
                
         
        return True       
        
        
def main():
    # Read input
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))

    obj = Solution()
    
    result = obj.isPerfect(arr)
    print(result)
    
if __name__ == "__main__":
    main()