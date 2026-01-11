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



# implementing stack using a linked list:
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution2:
    def __init__(self):
        self.top = None # Top of the stack

    '''
    Before push:
    top → A → B → C

    After push:
    top → X → A → B → C
    '''
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top     # The new node’s next pointer now points to what used to be the top node
        self.top = newNode          # The new node becomes the new top of the stack
        print(f"{value} pushed to stack.")



    def pop(self):
        if self.isEmpty():
            print("Stack Underflow! No elements to pop.")
            return -1
        poppedValue = self.top.val  # where top is a node
        self.top = self.top.next
        return poppedValue


    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
            return -1
        return self.top.val

    def isEmpty(self):
        return self.top is None     # If (self.top == None, return true)


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



    stack_ll = Solution2()

    stack_ll.push(10)
    stack_ll.push(20)
    stack_ll.push(30)
    print("Top element:", stack_ll.peek())  # Output: 30

    print("Popped:", stack_ll.pop())  # Output: 30
    print("Popped:", stack_ll.pop())  # Output: 20

    print("Is stack empty?", stack_ll.isEmpty())  # Output: False
    stack_ll.pop()  # Popping last element
    print("Is stack empty?", stack_ll.isEmpty())  # Output: True

# Stack Implementation Using Built-in Data Structures
# Python: Using List as a Stack
stack = []

stack.append(10)  # Push
stack.append(20)
print("Top Element (Peek):", stack[-1])  # Output: 20

print("Popped Element:", stack.pop())  # Output: 20
print("Is Stack Empty?", len(stack) == 0)  # Output: False


'''
Stacks in Python are typically implemented using lists.

Reference:
<< https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks >>

list.append(x)
list.extend(iterable)
list.insert(i, x)
list.remove(x)
list.pop([i])
list.clear()
list.index(x[, start[, end]])
list.count(x)
list.sort(*, key=None, reverse=False)
list.reverse()
list.copy()


Example:

    stack = [3, 4, 5]
    stack.append(6)
    stack.append(7)
    stack
        >>> [3, 4, 5, 6, 7]
    stack.pop()
        >>> 7
    stack
        >>> [3, 4, 5, 6]
    stack.pop()
        >>> 6
    stack.pop()
        >>> 5
    stack
        >>> [3, 4]
'''