class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.mins:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[-1]))

        self.stack.append(val)

    def pop(self) -> None:
        self.mins.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]        
