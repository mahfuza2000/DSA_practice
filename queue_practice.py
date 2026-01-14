'''
resources:
<<< https://docs.python.org/3/library/queue.html >>>
'''


# a queue made of nodes:

class Node:
    # Node class for storing data and the reference to the next node
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    # Queue class using linked list
    def __init__(self):
        self.front = self.rear = None       # front and rear are Node types
        self.size = 0

    def enqueue(self, data):
        # Add an element to the rear of the queue
        newNode = Node(data)
        if self.rear is None:
            self.front = self.rear = newNode
            self.size += 1
            return
        self.rear.next = newNode    # This line connects the old rear node (C) to the new node (X): (A → B → C → X)
        self.rear = newNode         # This line updates the rear node to be the new node: (rear → X)
        self.size += 1

    def dequeue(self):
        # Remove an element from the front of the queue
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next      # The new front is the next node of the prev front
        if self.front is None:      # If the new front does not exit, then the rear is also non existance
            self.rear = None
        self.size -= 1
        return temp.data
    
    def peek(self):
        # Get the front element of the queue
        if self.front is None:
            return None
        return self.front.data
    
    def is_empty(self):
        # Check if the queue is empty
        return self.size == 0
    
    def get_size(self):
        # Get the number of elements in the queue
        return self.size
    
# Example usage
if __name__ == "__main__":
    queue = Queue()

    # Enqueue elements
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Display front element
    print("Front element:", queue.peek())
    # Dequeue and display the dequeued element
    print("Dequeued:", queue.dequeue())
    # Display front element again
    print("Front element:", queue.peek())
    # Display the size of the queue
    print("Queue size:", queue.get_size())

################################################################################


# Python: Using queue.Queue
from queue import Queue

queue = Queue()

queue.put(10)  # Enqueue
queue.put(20)
queue.put(30)
print("Front element:", queue.queue[0])  # Peek (Output: 10)

print("Dequeued:", queue.get())  # Dequeue (Output: 10)
print("Is Queue Empty?", queue.empty())  # Check if empty