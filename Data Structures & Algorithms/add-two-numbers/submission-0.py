# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        n1 = str(curr1.val)

        while curr1.next:
            n1 = "".join([str(curr1.next.val), n1])
            curr1 = curr1.next

        curr2 = l2
        n2 = str(curr2.val)

        while curr2.next:
            n2 = "".join([str(curr2.next.val), n2])
            curr2 = curr2.next
        
        sum = str(int(n1) + int(n2))

        dummy = ListNode()
        curr = dummy

        for value in reversed(sum):
            curr.next = ListNode(value)
            curr = curr.next

        return dummy.next