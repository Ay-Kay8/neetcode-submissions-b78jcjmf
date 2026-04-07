# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 5
# 7

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = l1
        curr2 = l2
        
        carry = 0
        head = ListNode()
        res = head
        
        while curr1 or curr2:

            # If node is empty (in the case that one list is longer than the other)
            # set it to a new node with value 0
            curr1 = curr1 or ListNode(0)
            curr2 = curr2 or ListNode(0)

            sum = curr1.val + curr2.val + carry

            # For example: 15 -> 1 and 5
            carry = sum // 10
            sum = sum % 10

            res.next = ListNode(sum)

            res = res.next
            curr1 = curr1.next
            curr2 = curr2.next

        # If the sequence ends but carry is non empty
        if carry != 0:
            res.next = ListNode(carry)
        
        return head.next