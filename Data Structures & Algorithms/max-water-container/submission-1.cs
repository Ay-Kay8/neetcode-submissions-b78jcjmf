public class Solution {
    public int MaxArea(int[] heights) {
        int l = 0;
		int r = heights.Length - 1;
		int curr_area = 0;
		int max_area = 0;
		
		while (l < r) {
			curr_area = Math.Min(heights[l], heights[r]) * (r - l);
			max_area = Math.Max(max_area, curr_area);
			
			if (heights[l] < heights[r]) {
				l++;
			}
			else {
				r--;
			}
		}
		return max_area;
    }
}
