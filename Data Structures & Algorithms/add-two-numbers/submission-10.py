class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2

        head = ListNode()
        curr_res = head

        carry_over = 0
        while curr1 or curr2:
            # In case either list ends, it'll be replaced by 0
            curr1 = curr1 or ListNode(0)
            curr2 = curr2 or ListNode(0)

            sum = curr1.val + curr2.val + carry_over

            curr_res.next = ListNode(sum % 10)
            carry_over = sum // 10

            curr_res = curr_res.next
            curr1 = curr1.next
            curr2 = curr2.next

        if carry_over != 0:
            curr_res.next = ListNode(carry_over)

        return head.next