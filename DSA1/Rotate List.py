class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: # Head is None return None
            return
    
        temp = head # Pointer for traversing. We will need head later to make list circular.
    
        count = 1 # Total count of list nodes
    
        while temp.next:
        
            count += 1
        
            temp = temp.next
    
    # Now temp is at the tail of list and we have got the total nodes count
    
        temp.next = head # Makes list circular. It makes working easy.
    
        temp =  temp.next  # again temp is at first node of list
    
        k %= count # Necessary step as k can be large than total count of nodes
    
        for i in range(count -k-1): # Find the new tail of rotated list
            
            temp = temp.next
    
    # Now we got the new tail. Just we need to connect now.
    
        head = temp.next # head will be now rotated list head.
    
        temp.next = None # makes list non-circular otherwise infinite loop
    
        return head # Return updated head
