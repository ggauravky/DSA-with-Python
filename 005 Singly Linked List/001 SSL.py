
#! what is Singly Linked List?
# A Singly Linked List is a linear data structure where each element (node) points to the next node in the sequence.
# Each node contains two parts: data and a reference (or pointer) to the next node 

class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next pointer to None

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = None  # Initialize the head of the list to None
        
    def insertAtEnd(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:
            self.head = new_node  # If the list is empty, set the new node as the head
            return
        last = self.head
        while last.next:
            last = last.next  # Traverse to the end of the list
        last.next = new_node  # Link the new node at the end of the list
    
    def insertAtBeginning(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Update the head to the new node
    
    def insertInMid(self , value , x):
        new_node = Node(value) # Create a new node with the given data
        if self.head is None: 
            self.head = new_node  # If the list is empty, set the new node as the head
            return
        current = self.head  # Start from the head of the list
        while current is not None: 
            if current.data == x:
                new_node.next = current.next   # Link the new node to the next node
                current.next = new_node  # Link the current node to the new node
                return  
            current = current.next       # Move to the next node
        print(f"Value {x} not found in the list.")      # If x is not found in the list
        
    def deleteNode(self, key):
        current = self.head
        
        # If the head node itself holds the key to be deleted
        if current is not None:
            if current.data == key:
                self.head = current.next  # Change head
                current = None  # Free the old head
                return
        
        # Search for the key to be deleted, keep track of the previous node
        prev = None
        while current is not None and current.data != key:
            prev = current
            current = current.next
        
        # If the key was not present in the linked list
        if current is None:
            print(f"Value {key} not found in the list.")
            return
        
        # Unlink the node from linked list
        prev.next = current.next
        current = None  # Free the memory
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")  # Print the data of each node
            current = current.next
        print("None")  # Indicate the end of the list

#! Example usage:   
sll = SinglyLinkedList()    
sll.insertAtEnd(10)
sll.insertAtEnd(20)
sll.insertAtEnd(30)
sll.insertAtBeginning(5)
sll.insertInMid(15, 10)  # Insert 15 after the node with value 10
sll.display()  # Output: 5 -> 10 -> 15 -> 20 -> 30 -> Nonein the list.
sll.deleteNode(20)
sll.display()  # Output: 5 -> 10 -> 15 -> 30