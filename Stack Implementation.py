# Defines a stack class with the operation of push, pop, and peek with the help of an array.
# It exhibits a LIFO behavior of fixed time of insertion and deletion.

# Implementing a stack using an array
class Stack:
    def __init__(self):
        self.stack = []  # Initializing empty stack

    # Pushing element onto stack
    def push(self, value):
        self.stack.append(value)  # Adding element to top of stack

    # Popping element from top
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Removing top element
        return None

    # Peeking at top element without removing
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  # Returning top element
        return None

    # Checking if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

# Example usage
s = Stack()
s.push(10)  # Adding element
s.push(20)
print("Top element:", s.peek())  # Viewing top element
print("Popped element:", s.pop())  # Removing top element
