# 225. Implement Stack using Queues

class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        

    def push(self, x: int) -> None:
        self.queue1.append(x)
        

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        popped_element = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped_element
        

    def top(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        top_element = self.queue1.pop(0)
        self.queue2.append(top_element)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element
        

    def empty(self) -> bool:
        return len(self.queue1) == 0
    