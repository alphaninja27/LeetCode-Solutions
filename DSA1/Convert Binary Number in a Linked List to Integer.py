class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res=""
        while head:
            res+=str(head.val)
            head=head.next
        return int(res,2)
