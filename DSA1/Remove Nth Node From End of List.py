class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        size = 0
    
        while node:
            node = node.next
            size += 1
    
        if size == n:
            return head.next
    
        node = head
        for i in range(1, size - n):
            node = node.next
    
        node.next = node.next.next
    
        return head
