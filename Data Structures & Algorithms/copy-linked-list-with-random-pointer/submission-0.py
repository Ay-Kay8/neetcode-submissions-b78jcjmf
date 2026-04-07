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
        addresses = {None: None}
        # node address -> random address
        newHead = Node(0)

        curr = head
        newCurr = newHead
        while curr:
            newNode = Node(curr.val)
            # Build dict
            addresses[curr] = newNode

            newCurr.next = newNode
            newCurr = newCurr.next
            curr = curr.next

        # Ok now we have our new list and a dict
        curr = head
        newCurr = newHead.next
        while newCurr:
             newCurr.random = addresses[curr.random]
             curr = curr.next
             newCurr = newCurr.next
        return newHead.next  