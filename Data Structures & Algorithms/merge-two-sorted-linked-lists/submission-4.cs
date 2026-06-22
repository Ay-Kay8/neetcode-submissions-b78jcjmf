public class Solution {
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
		ListNode head = new ListNode();
		
		ListNode merged = head;
		
		ListNode curr1 = list1;
		ListNode curr2 = list2;
		
		// Stop execution when one of the 2 lists are null
		while (curr1 != null && curr2 != null) {
			if (curr1.val <= curr2.val) {
				merged.next = curr1;
				curr1 = curr1.next;
			}
			else {
				merged.next = curr2;
				curr2 = curr2.next;
			}
			merged = merged.next;
		}
		
		if (curr1 != null) merged.next = curr1;
		if (curr2 != null) merged.next = curr2;
		
		return head.next;
    }
}

