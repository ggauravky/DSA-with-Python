# Deque :
# A double-ended queue implementation using a doubly linked list.

class Deque:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0

    def insertAtEnd(self, item):
        self.items.append(item)
        
    def insertAtFront(self, item):
        self.items.insert(0, item)
    
    def removeFromEnd(self):
        if self.is_empty():
            raise IndexError("removeFromEnd from empty deque")
        return self.items.pop()
    
    def removeFromFront(self):
        if self.is_empty():
            raise IndexError("removeFromFront from empty deque")
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

    def peekFront(self):
        if self.is_empty():
            raise IndexError("peekFront from empty deque")
        return self.items[0]

    def peekEnd(self):
        if self.is_empty():
            raise IndexError("peekEnd from empty deque")
        return self.items[-1]

dq=Deque()
dq.insertAtEnd(10)
dq.insertAtFront(20)
print(dq.removeFromFront())  # Output: 20
print(dq.removeFromEnd())    # Output: 10
print(dq.is_empty())         # Output: True
dq.insertAtEnd(30)
print(dq.peekEnd())         # Output: 30    
dq.insertAtFront(40)
print(dq.peekFront())       # Output: 40    
print(dq.size())            # Output: 2