"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node = head
        while node:
            copy = Node(node.val, node.next, node.random)
            node.next = copy
            node = copy.next
        node = head.next
        while node:
            if node.next:
                node.next = node.next.next
            if node.random:
                node.random = node.random.next
            node = node.next
        return head.next
