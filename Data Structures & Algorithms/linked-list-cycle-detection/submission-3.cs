/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    public bool HasCycle(ListNode head) {
        ListNode curr = head;
		var visited = new HashSet<ListNode>();
		while (curr != null) {
			if (visited.Contains(curr)) {
				return true;
			}
			visited.Add(curr);
			curr = curr.next;
		}
		
		return false;
    }
}
