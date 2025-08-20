'''Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
 A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.'''
 
# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true
#Solution 1
# Time Complexity = O(N^2) space = O(N)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = list(s) 
        for _ in range(len(s)):
            if "".join(s) == goal: #Convert the list into string
                return True
            ch = s.pop(0) #remove first element
            s.append(ch) #place 1 element at the end if not match
        return False
    
#Solution 2
# Time Complexity = O(N) space = O(1)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)
                           
            
                           
            
