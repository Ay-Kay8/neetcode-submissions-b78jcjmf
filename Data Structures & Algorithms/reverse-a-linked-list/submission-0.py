# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            # save connection to next ptr
            temp = curr.next
            # sever the connection
            curr.next = prev

            # move pointer up
            prev = curr
            curr = temp
        return prev