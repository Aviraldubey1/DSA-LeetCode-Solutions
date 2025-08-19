# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Solution
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        n = len(s)
        min_str = float('inf')#max prefix can be the smallest
        i = 0 
        for l in s:
            if len(l) < min_str:
                min_str = len(l)

        while i < min_str:
            for w in s:
                if w[i] != s[0][i]:
                    return s[0][:i]
            i += 1
        return s[0][:i]