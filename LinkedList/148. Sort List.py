class Solution:
    def findmiddle(self,head):
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        return s
    def merge(self,list1, list2):
        dummy = ListNode(0)
        curr = dummy
        while (list1 != None) and (list2 != None):
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return dummy.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        middle = self.findmiddle(head)
        r = middle.next
        middle.next = None
        l = head
        left = self.sortList(l) 
        right = self.sortList(r)  
        return self.merge(left, right)