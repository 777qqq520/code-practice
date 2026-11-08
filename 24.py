# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy_head = ListNode(0)
        dummy_head.next = head
        cur = dummy_head
        while cur.next and cur.next.next:
            node1 = cur.next
            node2 = cur.next.next
            cur.next = node2
            node1.next = node2.next
            node2.next = node1
            cur = node1
        return dummy_head.next