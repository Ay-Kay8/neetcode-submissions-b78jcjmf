public class Solution {
    public int LongestConsecutive(int[] nums) {
        // You can directly convert a list to a set this way
		var set = new HashSet<int>(nums);
		
		int longest = 0;
		foreach (int s in set) {
			if (!set.Contains(s-1)) {
				// This is a potential start of a sequence
				int length = 1;
				while (set.Contains(s + length)) {
					length++;
				}
				longest = Math.Max(longest, length);
			}
		}
		
		return longest;
    }
}
