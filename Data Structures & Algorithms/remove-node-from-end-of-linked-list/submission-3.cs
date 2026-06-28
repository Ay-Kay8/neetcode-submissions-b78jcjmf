public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        ListNode slow = head;
		ListNode fast = head;
		for (int i = 0; i < n; i++) {
			fast = fast.next;
		}
		
		ListNode prev = null;
		while (fast != null) {
			prev = slow;
			slow = slow.next;
			fast = fast.next;
		}
		
		if (prev != null) {
			prev.next = slow.next;	
		} else {
			// head was the node to be removed
			head = head.next;
		}
		
		return head;
    }
}