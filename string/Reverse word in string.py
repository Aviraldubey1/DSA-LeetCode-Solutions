# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.
# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"

class Solution:
    def reverseWords(self, s: str) -> str:
        new = ' '.join(s.split(' ')[::-1]).strip(' ')
        ans = []

        for i,c in enumerate(new):
            if i < len(new) -1 and \
            new[i] == new[i+1] == ' ':
                i += 1
            else:
                ans.append(c)
                i += 1
        return ''.join(ans)