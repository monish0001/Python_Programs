#User function Template for python3
class Solution:
	def firstAlphabet(self, S):
		# code here
		str_list=S.split()
		ans=""
		for item in str_list:
		    ans+=item[0]
		    
		return ans

def main():
    S="geeks for geeks"
    sol=Solution()
    print(sol.firstAlphabet(S))
    
if __name__=="__main__":    main()  