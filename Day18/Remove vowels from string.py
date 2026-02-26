#User function Template for python3
class Solution:
	def removeVowels(self, s):
		# code here
		result=""
		all_vowels ="aeiouAEIOU"
		for ch in s:
		    if ch not in all_vowels:
		        result+=ch
		        
		return result
		        