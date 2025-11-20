# Creates a queue of array based class having enqueue and dequeue functions.
# Sliding elements make dequeue operation to be of linear time complexity.

# Implementing a queue using an array
class Queue:
    def __init__(self):
        self.queue = []  # Initializing empty queue

    # Enqueuing element at the end
    def enqueue(self, value):
        self.queue.append(value)  # Adding element to end of queue

    # Dequeuing element from the front
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Removing element from front
        return None

    # Checking if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

# Example usage
q = Queue()
q.enqueue(10)  # Adding element
q.enqueue(20)
print("Dequeued element:", q.dequeue())  # Removing first element
