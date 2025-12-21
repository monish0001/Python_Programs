#User function Template for python3

class Solution:
    def count (self,s):
        # your code here
        lowercase=0
        uppercase=0
        special=0
        numeric=0
        
        for ch in s:
            if ch.islower():
                lowercase+=1
            elif ch.isupper():
                uppercase+=1
            elif ch.isdigit():
                numeric+=1
            else:
                special+=1
        return uppercase,lowercase,numeric,special
            

if __name__=="__main__":
    s = input("Enter your string: ")
    ob = Solution()
    uppercase,lowercase,numeric,special = ob.count(s)
    print(uppercase,lowercase,numeric,special)