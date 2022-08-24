        nxt = node.next
        node.val = nxt.val
        node.next = nxt.next
        nxt = None
