public class Solution {
    public ListNode ReverseList(ListNode head) {
		 if (head == null)
        	return null;
	
		ListNode curr = head;
		ListNode prev = null;
		
        while (curr != null) {
			var next = curr.next;
			curr.next = prev;
			prev = curr;
			curr = next;		
		}
		return prev;
    }
}
