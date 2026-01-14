'''
Problem Statement
Implement a stack using only two queues. The stack should behave like a typical last-in-first-out (LIFO) stack, meaning that the last element added should be the first one to be removed.

Implement a Solution class that supports the following operations:

Solution(): A constructor to initialize the object.
push(int x): Adds an element x to the top of the stack.
pop(): Removes the element from the top of the stack and returns it.
top(): Retrieves the element on the top of the stack without removing it.
empty(): Checks whether the stack is empty or not and returns true or false accordingly.
Note: You can only use the basic operations of a queue, such as adding an element to the back, removing an element from the front, checking the size, and verifying if the queue is empty.

Input and Output Format
The input and output for this problem are structured using two separate arrays:

Input Arrays:

Method Names Array: This is an array of strings where each string represents a method to be called on the Solution class. The first element is always "Solution", indicating the initialization of the stack.
Arguments Array: This is a nested array where each sub-array contains the arguments for the corresponding method in the Method Names Array. For methods that do not require any arguments (like Solution, pop, top, and empty), the sub-array will be empty.
Output Array:

The output is a single array that captures the return value of each method call in the order they were invoked.
For methods that do not return any value (Solution constructor and push operations), the corresponding output is null.
For methods that return values (pop, top, and empty), the actual returned value is included in the output array.
Examples
Example 1

Input:

["Solution", "push", "push", "top", "pop", "empty"]
[[], [5], [10], [], [], []]
Expected Output: [null, null, null, 10, 10, false]

Explanation:

push(5) adds 5 to the stack.
push(10) adds 10 to the top of the stack.
top() returns 10 since it's the top element.
pop() removes 10 and returns it.
empty() returns false because 5 is still in the stack.
Example 2

Input:
["Solution", "push", "push", "push", "pop", "top", "pop", "empty"]
[[], [1], [2], [3], [], [], [], []]
Expected Output: [null, null, null, null, 3, 2, 2, false]
Explanation:
push(1) adds 1 to the stack.
push(2) adds 2 on top of 1.
push(3) adds 3 on top of 2.
pop() removes 3 and returns it.
top() returns 2, the new top element.
pop() removes 2 and returns it.
empty() returns false since 1 is still in the stack.
Example 3

Input:
["Solution", "push", "top", "pop", "empty"]
[[], [99], [], [], []]
Expected Output: [null, null, 99, 99, true]
Explanation:
push(99) adds 99 to the stack.
top() returns 99.
pop() removes 99 and returns it.
empty() returns true because the stack is now empty.
Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
'''

# My Solution:
'''
My Approach:

We need to implement a stack using 2 queues.
In a stack, we can push 1, 2, 3, and then pop 3, pop 2 from the top:
    (bottom) [1] [2] [3] (top)  --> (bottom) [1] [2] (top)  --> (bottom) [1] (top)

The pop fc is the problem/diff btwn the stack and queue. While push and enqueue will both add elem to the end away fron index 0, 
pop will take away from index 0 while deque will take at index 0.

Essentially, we need to put all elem in the queue in the BACKWARDS ORDER of the stack so the last elem of the stack will leave as the first elem of the queue.
So, we keep a main q1 that will be the ultimate representation of the stack (but all elem in reverse order), 
and we will keep a helper q2 that keeps the new elem being pushed at the bottom so all of q1's elem can be put on top of it.
Then we switch q1 and q2 and continue.

In the queue solution, we can push 1, 2, 3, and then pop 3, pop 2 like this:
    q1: (front) [1] (rear)
    q2: (front) [] (rear)

    q1: (front) [1] (rear)  <= dequeue onto q2
    q2: (front) [2] (rear)

    q1: (front) [] (rear)  
    q2: (front) [2] [1] (rear)

    q2: (front) [3] (rear)  
    q1: (front) [2] [1] (rear)  <= dequeue onto q2

    q2: (front) [3] [2] [1] (rear)  
    q1: (front) [] (rear)

    q1: (front) [3] [2] [1] (rear)  
    q2: (front) [] (rear)

    q1: (front) [3] [2] [1] (rear)  -->  q1: (front) [2] [1] (rear)  -->  q1: (front) [1] (rear) 

'''
from collections import deque

class Solution2:
    # Constructor to initialize the queues
    def __init__(self):
        self.q1 = deque()   # for current stack
        self.q2 = deque()   # for temp queue for push operation

    # Push element x onto the stack
    def push(self, x: int) -> None:
        self.q2.append(x)

        # add all elem of q1 onto q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # switch q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    # Pop element from the stack
    def pop(self) -> int:
        # q1 will have the elem to pop
        return self.q1.popleft()

    # Get the top element
    def top(self) -> int:
        # show the first elem of q1
        return self.q1[0]

    # Check if the stack is empty
    def empty(self) -> bool:
        if not self.q1:
            return True
        return False
    
# Given Solution:
from collections import deque

class Solution:
    # Constructor to initialize the queues
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    # Push element x onto the stack
    def push(self, x: int) -> None:
        # Add the element to queue2
        self.queue2.append(x)
        
        # Move all elements from queue1 to queue2 to maintain stack order
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        
        # Swap the names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

    # Pop element from the stack
    def pop(self) -> int:
        return self.queue1.popleft()  # Remove and return the front of queue1, which is the stack's top

    # Get the top element
    def top(self) -> int:
        return self.queue1[0]  # Peek at the front of queue1, which is the stack's top

    # Check if the stack is empty
    def empty(self) -> bool:
        return not self.queue1  # Check if queue1 is empty


# Main method to test the stack implementation
if __name__ == "__main__":
    myStack = Solution()
    myStack.push(5)
    myStack.push(10)
    print(myStack.pop())  # 10
    print(myStack.top())  # 5
    print(myStack.pop())  # 5
    print(myStack.empty()) # True