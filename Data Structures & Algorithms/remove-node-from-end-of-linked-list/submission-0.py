# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        curr = head
        prev = None
        for i in range(count - n):
            prev = curr
            curr = curr.next
            
        if prev:
            prev.next = curr.next
        else: # remove first
            head = head.next
        return head