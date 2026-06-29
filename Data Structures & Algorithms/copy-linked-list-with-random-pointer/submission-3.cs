public class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
			return null;
		}

        var dict = new Dictionary<Node, Node>();
		// original node -> new node
		
		Node curr = head;
		while (curr != null) {
			var copy = new Node(curr.val);
			dict[curr] = copy;
			curr = curr.next;
		}
		
		curr = head;
		while (curr != null) {
			Node deep_copy = dict[curr];
			deep_copy.next = curr.next != null ? dict[curr.next] : null;
			deep_copy.random = curr.random != null ? dict[curr.random] : null;
			
			curr = curr.next;
		}

		return dict[head];
    }
}
