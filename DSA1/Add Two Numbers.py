class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""
        tmp1 = l1
        tmp2 = l2
        
        while tmp1:
            s1+=str(tmp1.val)
            tmp1 = tmp1.next
        while tmp2:
            s2+=str(tmp2.val)
            tmp2 = tmp2.next
            
        s = str(int(s1[::-1])+int(s2[::-1]))[::-1]
        
        head = ListNode(s[0])
        tmp = head
        for i in range(1,len(s)):
            nxt = ListNode(int(s[i]))
            tmp.next = nxt
            tmp = tmp.next
            
        return head
