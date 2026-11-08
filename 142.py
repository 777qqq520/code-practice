from typing import Optional #这个参数或者返回值，可能是一个 ListNode 对象，也可能是 None（空值）。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:   #有环，找入口
                index1 = head   
                index2 = slow  #另一个回头节点
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return index1
        return None