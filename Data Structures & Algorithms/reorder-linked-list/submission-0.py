# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Fast is set to head.next to handle when the list
        # is even. If we set it to head, the slow pointer wouldn't
        # be at the end of the first list
        slow, fast = head, head.next
        # Find middle of array
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse 2nd half
        prev = None
        curr = slow.next
        while curr:
            # Reverse link
            temp = curr.next
            curr.next = prev

            # Advance pointers
            prev = curr
            curr = temp

        # Cut list into two
        slow.next = None
        
        list1 = head
        list2 = prev

        curr = list1
        added = list2

        # Create new list
        while curr and added:
            curr_temp = curr.next
            added_temp = added.next

            curr.next = added
            added.next = curr_temp

            curr = curr_temp
            added = added_temp