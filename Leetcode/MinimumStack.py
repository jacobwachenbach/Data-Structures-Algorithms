

class MinStack:
    # Initialized stack and minStack for the smallest values
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # If minStack is empty
        if not self.minStack:
            self.stack.append(val)
            self.minStack.append(val)
        # If minStack has items
        else:
            if val <= self.minStack[-1]:
                self.stack.append(val)
                self.minStack.append(val)
            # If minStack has items
            else:
                self.stack.append(val)
    # Pop top item in stack and minStack if they match
    def pop(self) -> None:
        # Match
        if self.minStack[-1] == self.stack[-1]:
            self.stack.pop(-1)
            self.minStack.pop(-1)
        else: # Pop stack
            self.stack.pop(-1)
        
    # Return last item in array
    def top(self) -> int:
        return self.stack[-1]
        
    # If minStack is not empty return last item in array
    def getMin(self) -> int:
        if not self.minStack:
            return
        else:
            return self.minStack[-1]


minStack = MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.pop()
print(minStack.top())
print(minStack.getMin())