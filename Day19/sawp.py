class Solution:
    	def swapElements(self, arr):
	    #Code here
	    N=len(arr)
        
        for i in range(N):
            if (i+2)<N:
                arr[i],arr[i+2]=arr[i+2],arr[i]
        
        
        return arr