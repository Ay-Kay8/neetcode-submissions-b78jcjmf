public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        
		int[] sol = new int[temperatures.Length];
		Stack<(int val, int index)> stack = new Stack<(int val, int index)>();

		for (int i = 0; i < temperatures.Length; i++) {
			if (stack.Count == 0) {
				stack.Push((temperatures[i], i));
				continue;
			}

			while (stack.Count > 0 && temperatures[i] > stack.Peek().val) {
				sol[stack.Peek().index] = i - stack.Peek().index;
				stack.Pop();
			}
			stack.Push((temperatures[i], i));
		}
		return sol;
    }
}
