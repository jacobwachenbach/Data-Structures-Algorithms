class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next

    def getValue(self):
        return self.value
    
    def getNext(self):
        return self.next
    
    def setValue(self, value):
        self.value = value

    def setNext(self,next):
        self.next = next

    def __str__(self):
        return str(self.value) 
    


class Stack:
    # Define top value
    def __init__(self):
        self.top = None
    # Create node with passed in value, and set next to top
    def push(self, value):
        # Create node, self.top so on start the first node will be set to nothing
        # Next one will be set to this one
        inVal = Node(value,self.top)
        self.top = inVal

    # Pop top value
    def pop(self):
        # If stack is empty return
        if self.top == None:
            return
        else:
            # Get current top value
            valueRet = self.top.getValue()
            # Set top to next node
            self.top = self.top.getNext()
            return valueRet
        
    # Get top value
    def peek(self):
        if self.top is None:
            return
        else:
            return self.top.getValue()
        
    # Return the state of self.top
    def isEmpty(self):
        return self.top is None
    
myNum = Stack()
myNum.push(30)
print(myNum.peek())
myNum.push(7)
print(myNum.peek())