# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x, y = 0, 0
        while l1:
            x = x * 10 + l1.val
            l1 = l1.next
        while l2:
            y = y * 10 + l2.val
            l2 = l2.next
        ans = x + y
        curr = head = ListNode(0)
        if ans == 0:
            return head
        while ans > 0:
            head.next = ListNode(ans % 10)
            head = head.next
            ans //= 10
        prev = None
        head = curr.next
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
