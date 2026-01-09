class Node:
    def __init__(self, value=None):
        self.data = value
        self.prev = None
        self.next = None
        
class DoublyLL:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next != None:
            last = last.next
        last.next = new_node
        new_node.prev = last
        
    def insertAtBeginning(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def insertAfterNode(self, prev_node, value):
        if prev_node is None:
            print("The given previous node cannot be NULL")
            return
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
    
    def deletionDLL(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # Move head if needed
                    self.head = current.next
                return
            current = current.next 
    
    def printDLL(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next
        print()
        

object=DoublyLL()
object.insertAtEnd(10)
object.insertAtEnd(20)
object.insertAtEnd(30)
object.insertAtBeginning(5)
object.insertAfterNode(object.head.next, 15)  # Insert 15 after 10
object.printDLL()  # Output: 5 <-> 10 <-> 15 <-> 20 <-> 30
object.deletionDLL(20)
object.printDLL()  # Output: 5 <-> 10 <-> 15 <-> 30