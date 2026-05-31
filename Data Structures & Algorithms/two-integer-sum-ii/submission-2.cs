public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        int l = 0;
		int r = numbers.Length - 1;
		
		while (l < r) {
			int currSum = numbers[l] + numbers[r];
			
			if (currSum < target) {
				l++;
			}
			else if (currSum > target) {
				r--;
			}
			else {
				break;
			}
		}
		
		return new int[] {l + 1, r + 1};
    }
}
