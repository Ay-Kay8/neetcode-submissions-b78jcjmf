public class Solution {
    public List<List<int>> ThreeSum(int[] nums) {
        Array.Sort(nums);
		
		List<List<int>> result = new List<List<int>>();
		
		for (int i = 0; i < nums.Length; i++) {
			if (i != 0 && nums[i - 1] == nums[i]) {
				// If the starting value is the same as the previous, this can lead to
				// duplicates
				continue;
			}
		
			int l = i + 1;
			int r = nums.Length - 1;
			
			int target = -nums[i];
			
			while (l < r) {
				int curr_sum = nums[l] + nums[r];
				if (curr_sum == target) {
					result.Add(new List<int> {nums[i], nums[l], nums[r] });
					//break; // Do not break, there can be multiple value pairs
					
					// Now, we need to change index for both r and l, while still skipping duplicates
					l++;
					r--;
					
					while (l < r && nums[l-1] == nums[l]) {
						l++;
					}
					
                    while (l < r && nums[r+1] == nums[r]) {
						r--;
					}
				}
				else if (curr_sum < target) {
					l++;
				}
				else {
					r--;
				}
			}
		}
		
		return result;
    }
}
