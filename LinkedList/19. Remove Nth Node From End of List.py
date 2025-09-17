class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = head
        f = head
        for i in range(n):
            f = f.next
        if f == None:
            return head.next
        while f.next != None:
            s = s.next
            f = f.next
        s.next = s.next.next
        return head