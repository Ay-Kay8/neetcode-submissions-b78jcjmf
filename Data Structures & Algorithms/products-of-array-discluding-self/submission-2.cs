public class Solution {	

	public int[] ProductExceptSelf(int[] nums) {

		// nums: 1, 2, 4, 6
		// pre: 1, 1, 2, 8

		int[] res = new int[nums.Length];
		
		int preProduct = 1;
		for (int i = 0; i < nums.Length; i++) {
			res[i] = preProduct;
			preProduct *= nums[i];
		}
		
		// res currently contains the values for pre
		// nums: 1, 2, 4, 6
		// res: 48, 24, 12, 8
		int sufProduct = 1;
		for (int i = nums.Length - 1; i >= 0; i--) {
			res[i] *= sufProduct;
			sufProduct *= nums[i];
			
		}

		return res;
	}
}