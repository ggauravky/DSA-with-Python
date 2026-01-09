class CircularDoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CircularDoublyLinkedListNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def prepend(self, data):
        new_node = CircularDoublyLinkedListNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, key):
        if not self.head:
            return
        current = self.head
        while True:
            if current.data == key:
                if current.next == current:  # Only one node in the list
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:  # Deleting the head node
                        self.head = current.next
                return
            current = current.next
            if current == self.head:
                break

    def display(self):
        elements = []
        if not self.head:
            return elements
        current = self.head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        return elements

# Example usage:
if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()
    cdll.append(10)
    cdll.append(20)
    cdll.prepend(5)
    print("List after appending and prepending:", cdll.display())  # Output: [5, 10, 20]
    cdll.delete(10)
    print("List after deleting 10:", cdll.display())  # Output: [5, 20]