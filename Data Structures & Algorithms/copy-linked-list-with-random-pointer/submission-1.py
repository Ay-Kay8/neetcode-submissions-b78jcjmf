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
        # In the 2nd pass, it's possible that we have curr.random pointing to null
        # so we'll need to handle the case where original_to_copy[None]
        original_to_copy = {None: None}

        # First pass: Create new deep copies + hashmap (do not link them yet)
        curr = head
        while curr:
            new_node = Node(curr.val)
            original_to_copy[curr] = new_node
            curr = curr.next

        # Second pass: Link everything (.next and .random)
        curr = head # reset head
        while curr:
            copy = original_to_copy[curr]
            copy.next = original_to_copy[curr.next]
            copy.random = original_to_copy[curr.random]

            curr = curr.next

        return original_to_copy[head]