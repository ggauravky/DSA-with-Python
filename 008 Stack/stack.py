
#! Stack:
# A stack is a linear data structure that follows the Last In First Out (LIFO) principle.

class Stack:
    def __init__(self):
        self.s = []
    
    def length(self):
        return len(self.s)
    
    def push(self, item):
        self.s.insert(0, item)
    
    def peek(self):
        if len(self.s) == 0:
            return Exception("Stack is empty")
        else:
            return self.s[0]
    
    def pop(self):
        if len(self.s) == 0:
            return Exception("Stack is empty")
        else:
            return self.s.pop(0)
    
    def printstack(self):
        return self.s
        

stk= Stack()
stk.push(1)
stk.push(2)
stk.push(3)
print(stk.length())  # Output: 3
print(stk.peek())    # Output: 3
print(stk.pop())     # Output: 3
print(stk.length())  # Output: 2
print(stk.printstack())  # Output: [2, 1]