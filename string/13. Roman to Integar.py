# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Solution 
class Solution:
    def romanToInt(self, s: str) -> int:
        val ={'I':1,'V':5,'X':10,'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)-1):
            if val[s[i]] < val[s[i + 1]]:
                res -= val[s[i]]
            else:
                res += val[s[i]]
        res += val[s[-1]]
            
        return res