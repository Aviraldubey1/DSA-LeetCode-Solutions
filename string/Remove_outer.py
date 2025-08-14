"""
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Emaxple 1:
Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
"""
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt = 0
        res = ''
        for ch in s:
            if ch == '(':
                if cnt > 0:
                    res += ch
                cnt += 1
            else:
                cnt -= 1
                if cnt > 0:
                    res += ch
        return res
