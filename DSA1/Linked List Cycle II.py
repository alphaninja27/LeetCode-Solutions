class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        flag = False
        slow = head
        fast = head
#         checking whether there is any cycle or not
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                flag = True
                break
        if not flag:
            return None
#        head of cycle
        slow = head
       
        while (slow != fast):
            slow = slow.next
            fast = fast.next
        return slow
