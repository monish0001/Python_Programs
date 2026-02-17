class Solution:
    def nonRepeatingChar(self,s):
        #code here
        dict={}
        for ch in s:
            if ch in dict:
                dict[ch]+=1
            else:
                dict[ch]=1
            
        for ch in s:
            if dict[ch]==1:
                return ch
            
        
        return '$'