public class MinStack {

	// Val, minimium before pushing
	Stack<(int, int)> stack;
	int currMinimum = int.MaxValue;

    public MinStack() {
    	stack = new Stack<(int, int)>();
    }
    
    public void Push(int val) {
        stack.Push((val, currMinimum));
		currMinimum = Math.Min(currMinimum, val);
    }
    
    public void Pop() {
        (int value, int val) = stack.Pop();
		// Set minimum to what is was before
		currMinimum = val;
    }
    
    public int Top() {
        return stack.Peek().Item1;
    }
    
    public int GetMin() {
		return currMinimum;
    }
}
