# Conceptual reference for how to implement a stack in python

# implementing stack using array:
class Solution:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [0] * capacity     # size of stack should be capacity times data type
        self.top = -1                   # stack is empty initially, so top is -1

    def push(self, value):
        # check if we're already at the top of the stack. 
        # If yes, then adding another value will lead to stack overflow
        if self.top == self.capacity - 1:
            print(f"Stack overflow! Can't push {value} to the stack...")
            return
        
        # if permissible push, move top up one, add value at that spot
        self.top += 1
        self.stack[self.top] = value
        print(f"{value} added to stack...")

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow! No elements to pop.")
            return -1  # Return -1 to indicate error
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
            return -1
        return self.stack[self.top]

    def isEmpty(self):
        # Return Bool True if top == -1, else return false
        return self.top == -1

if __name__ == "__main__":
    stack = Solution(5)

    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top element:", stack.peek())  # Output: 30

    print("Popped:", stack.pop())  # Output: 30
    print("Popped:", stack.pop())  # Output: 20

    print("Is stack empty?", stack.isEmpty())  # Output: False
    stack.pop()  # Popping last element
    print("Is stack empty?", stack.isEmpty())  # Output: True