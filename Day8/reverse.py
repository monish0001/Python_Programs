import sys

sys.stdin=open('input.txt', 'r')
sys.stdout=open('output.txt', 'w')

class Solution:
    def revStr(self, s: str) -> str:
       
        return s[::-1]


def main():
    # Read input string
    s = input().strip()
    

    obj = Solution()
    
   
    result = obj.revStr(s)
    print(result)


if __name__ == "__main__":
    main()