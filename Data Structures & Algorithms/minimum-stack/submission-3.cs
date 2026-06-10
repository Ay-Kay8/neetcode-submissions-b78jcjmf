public class MinStack {

	// Val, current minimum
	Stack<(int val, int min)> stack = new();
    
    public void Push(int val) {
        if (stack.Count == 0) {
			stack.Push((val, val));
		}
		else {
			int currMin = Math.Min(stack.Peek().min, val);
			stack.Push((val, currMin));
		}
    }
    
    public void Pop() {
     	stack.Pop();   
    }
    
    public int Top() {
        return stack.Peek().val;
    }
    
    public int GetMin() {
		return stack.Peek().min;
    }
}