class Node:

    # Has the value and next as the parameter
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def getValue(self):
        return self.value
    
    def getNext(self):
        return self.next
    
    def setValue(self,value):
        self.value = value
    
    def setNext(self,next):
        self.next = next
    def __str__(self):
        return str(self.value)

    
first = Node(40, None)
second = Node(12, first)

print(second.getNext())