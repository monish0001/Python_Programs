class Solution:
    def valueEqualToIndex(self, arr):
        result_list=[]
        
        for i in range(len(arr)):
            if arr[i]==(i+1):
                result_list.append(arr[i])
                
        return result_list