public class Solution {
    public void ReorderList(ListNode head) {
        if (head == null || head.next == null)
            return;

        // 1. Find middle (slow ends at end of first half)
        ListNode slow = head;
        ListNode fast = head;

        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // 2. Reverse second half
        ListNode second = slow.next;
        slow.next = null;

        ListNode prev = null;
        ListNode curr = second;

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        // 3. Merge two halves
        ListNode first = head;
        ListNode secondReversed = prev;

        while (secondReversed != null) {
            ListNode tmp1 = first.next;
            ListNode tmp2 = secondReversed.next;

            first.next = secondReversed;
            secondReversed.next = tmp1;

            first = tmp1;
            secondReversed = tmp2;
        }
    }
}