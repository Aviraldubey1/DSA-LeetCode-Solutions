# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Input: head = [1,2,2,1]
# Output: true

# Input: head = [1,2]
# Output: false
# Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        curr = head
        while curr:
            s.append(curr.val)
            curr = curr.next
        curr = head
        while s:
            if curr.val != s.pop():
                return False
            curr = curr.next
        return True