# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

# Example 1:

# Input: s = "(1+(2*3)+((8)/4))+1"

# Output: 3

# Explanation:

# Digit 8 is inside of 3 nested parentheses in the string.

# Example 2:

# Input: s = "(1)+((2))+(((3)))"

# Output: 3

# Explanation:

# Digit 3 is inside of 3 nested parentheses in the string.

# Example 3:

# Input: s = "()(())((()()))"

# Output: 3
# solution
def maxDepth(self, s: str) -> int:
        # O(n)
        curr = 0
        Max = 0
        for i in s:
            if i == '(':
                curr += 1
                Max = max(curr, Max)
            elif i == ')':
                curr -= 1
        return Max