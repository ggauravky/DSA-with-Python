# Queue:
# A queue is a linear data structure that follows the First In First Out (FIFO) principle.

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        
q=Queue()
q.enqueue(1)
q.enqueue(2)
print(q.items)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2
print(q.is_empty()) # Output: True