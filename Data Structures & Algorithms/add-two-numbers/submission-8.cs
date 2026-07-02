public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode curr1 = l1;
        ListNode curr2 = l2;

		ListNode head = new ListNode();		
		ListNode res = head;

		int carry = 0; 
		while (curr1 != null || curr2 != null) {
			
			int sum = (curr1 != null ? curr1.val : 0) + 
					  (curr2 != null ? curr2.val : 0) + 
					  carry;
					  
			if (sum > 9) {
				carry = sum / 10;
				sum = sum % 10; // remainder
			}
			else {
				carry = 0;
			}
			
			res.next = new ListNode(sum);
		
			if (curr1 != null) {
				curr1 = curr1.next;
			}

			if (curr2 != null) {
				curr2 = curr2.next;
			}
		
			res = res.next;
		}
		
		if (carry == 1) {
			res.next = new ListNode(1);
		}
		
		return head.next;
    }
}