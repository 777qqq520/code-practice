#法一：读取旧链表+头插法
#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        dummy_head = ListNode(0)
        cur = head
        while cur is not None:
            new_node = ListNode(cur.val)
            new_node.next = dummy_head.next
            dummy_head.next = new_node
            cur = cur.next
        return dummy_head.next
        
#法二：双指针（原地反转）
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        cur = head
        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp
        return prev