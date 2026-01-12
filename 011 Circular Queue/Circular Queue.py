class  circularQueue:
    def __init__(self , size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    
    def isFull(self):
        if (self.rear + 1) % self.size == self.front:
            return True
        return False
    
    def isEmpty(self):
        if self.front == -1:
            return True
        return False
    
    def enqueue(self , data):
        if self.isFull():
            print("Queue is Full")
            return
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(f"{data} Enqueued")
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"{data} Dequeued")
        return data
    
    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        i = self.front
        print("Queue elements are: ", end="")
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
    
if __name__ == "__main__":  
    cq = circularQueue(5)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.display()
    cq.dequeue()
    cq.display()
    cq.enqueue(40)
    cq.enqueue(50)
    cq.enqueue(60)
    cq.display()
    cq.enqueue(70) 