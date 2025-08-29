# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.

# Example 1:

# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
# Example 2:

# Input: s = "aabcbaa"
# Output: 17/
# Solution
class Solution:
    from collections import Counter
    def beautySum(self, s: str) -> int:
        # O(n^2), O(1)
        total = 0
        n = len(s)
        for i in range(n):
            freq = Counter()
            for j in range(i, n):
                freq[s[j]] += 1
                if j - i + 1 >= 3: # substr len >= 3
                    total += max(freq.values()) - min(freq.values())
        return total