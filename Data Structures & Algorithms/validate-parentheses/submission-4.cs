public class Solution {
    public bool IsValid(string s) {
        Stack<char> stack = new Stack<char>();
		Dictionary<char, char> parenthesis = new Dictionary<char, char>
		{
		    { '(', ')' },
		    { '{', '}' },
		    { '[', ']' }
		};
		
		
		foreach (char c in s) {
			if (parenthesis.ContainsKey(c)) {
				stack.Push(parenthesis[c]);
			}
			else {
				if (stack.Count == 0 || stack.Peek() != c) {
					return false;
				}
				stack.Pop();
			}
		}
		
		return stack.Count == 0;
    }
}
