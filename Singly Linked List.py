# A singly linked list class is defined that has the following operations: insertion, deletion and traversal.
# Each node is connected dynamically so that it can be inserted and removed easily without any movement of elements.

# Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data  # Storing data
        self.next = None  # Initializing next pointer

# Singly linked list implementation
class LinkedList:
    def __init__(self):
        self.head = None  # Initializing empty linked list

    # Inserting element at the end
    def insert(self, value):
        new_node = Node(value)  # Creating a new node
        if not self.head:
            self.head = new_node  # Setting head if list is empty
            return
        current = self.head
        while current.next:
            current = current.next  # Traversing to last node
        current.next = new_node  # Linking new node at end

    # Deleting element by value
    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev:
                    prev.next = current.next  # Bypassing node to delete
                else:
                    self.head = current.next  # Deleting head node
                return
            prev = current
            current = current.next

    # Traversing linked list
    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)  # Collecting node data
            current = current.next
        return elements

# Example usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
print("Linked List:", ll.traverse())  # Displaying linked list
ll.delete(20)
print("After deletion:", ll.traverse())  # Displaying list after deletion
