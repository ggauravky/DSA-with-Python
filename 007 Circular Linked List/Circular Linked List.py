class circulaer_linked_list_node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circular_linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = circulaer_linked_list_node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
    def prepend(self, data):
        new_node = circulaer_linked_list_node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
    
    def delete(self, key):
        if not self.head:
            return
        current = self.head
        prev = None
        while True:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    # Deleting the head node
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                    if self.head == self.head.next:
                        self.head = None
                    else:
                        tail.next = self.head.next
                        self.head = self.head.next
                return
            prev = current
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
cll = circular_linked_list()
cll.append(1)
cll.append(2)
cll.prepend(0)
print(cll.display())  # Output: [0, 1, 2]
cll.delete(1)
print(cll.display())  # Output: [0, 2]