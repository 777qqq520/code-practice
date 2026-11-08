from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        pA = headA
        pB = headB
        while pA != pB:       #两个指针分别遍历两个链表，指针走到末尾时，跳到另一个链表的头部继续遍历
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA