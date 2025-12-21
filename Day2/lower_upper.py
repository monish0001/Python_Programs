class Solution:
    def modify(self, s):
        if s[0].islower():
            return s.lower()
        else:
            return s.upper()

        
obj = Solution()
print(obj.modify("Hello"))   # Output: HELLO
print(obj.modify("world"))   # Output: world
