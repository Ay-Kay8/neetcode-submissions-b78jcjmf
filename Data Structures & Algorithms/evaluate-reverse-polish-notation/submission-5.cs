public class Solution {
    public int EvalRPN(string[] tokens) {
		Stack<string> stack = new Stack<string>();
		var strToOperand  = new Dictionary<string, Func<int, int, int>> 
		{
			{"+", (a, b) => a + b},
			{"-", (a, b) => a - b},
			{"*", (a, b) => a * b},
			{"/", (a, b) => a / b},
		};
		
		
		// When we encounter an operand, there will always be two strings in the stack
		foreach (string token in tokens) {
			if (strToOperand.ContainsKey(token)) 
			{
				int b = int.Parse(stack.Pop());
				int a = int.Parse(stack.Pop());
				stack.Push(strToOperand[token](a, b).ToString());
			}
			else 
			{
				stack.Push(token);
			}
		}
		
		return int.Parse(stack.Peek());
    }
}

