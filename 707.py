class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode(0)
        self.size = 0
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummy_head.next
        for _ in range(index):
            cur = cur.next
        return cur.val
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        new_node = ListNode(val)
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1