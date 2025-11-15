# class Solution:
#     def convertFive(self, n):
#         # Code here
#         return int(str(n).replace('0','5'))





class Solution:
    def convertFive(self, n):
        if n == 0:
            return 5
        
        result = 0
        place = 1
        
        while n > 0:
            digit = n % 10
            if digit == 0:
                digit = 5
            
            result = digit * place + result
            place *= 10
            n //= 10
        
        return result
    
    
obj = Solution()
print(obj.convertFive(1020))   # Output: 1525
print(obj.convertFive(0))      # Output: 5
print(obj.convertFive(909))    # Output: 959
