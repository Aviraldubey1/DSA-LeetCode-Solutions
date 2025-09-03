class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        if self.head is None:
            return True
        return False
    def insert_at_begining(self,data):
        new_Node = Node(data)
        if self.is_empty():
            self.head=  new_Node
        else:
            new_Node.next = self.head
            self.head = new_Node
    def insert_at_middle(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        slow = self.head
        fast = self.head
        prev = None  
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = new_node
            new_node.next = slow
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
    def convertArrtoLL(self, arr):
        for i in arr:
            self.insert_at_end(i)

a = SinglyLinkedList()
a.insert_at_begining(10)
a.insert_at_begining(20)
a.insert_at_end(30)
a.insert_at_end(40)
a.insert_at_middle(25)
arr = [1, 2, 3, 4, 5]
a.convertArrtoLL(arr)
a.display()