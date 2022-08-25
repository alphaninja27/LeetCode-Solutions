class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first,last,cur=head,head,head
        size=0
        while cur:
            size+=1
            cur=cur.next
            
        while last:
            a=[]
            if size>=k:
                for i in range(k):
                    a.append(last.val)
                    last=last.next

                for i in range(k):
                    first.val=a.pop()
                    first=first.next
            else:
                break
            size-=k
                
        return head
