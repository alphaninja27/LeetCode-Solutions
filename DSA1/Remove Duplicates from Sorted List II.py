if not head or not head.next:
            return head
        l = ListNode()
        l.next = head
        p = l
        while p.next and p.next.next:
            if p.next.val == p.next.next.val:
                temp = p.next.val
                while p.next and p.next.val == temp:
                    p.next = p.next.next
            else:
                p = p.next
        return l.next
