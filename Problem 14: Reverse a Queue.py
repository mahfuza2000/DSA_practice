'''
Problem Statement
Given the head of a singly linked list, return the head of the reversed list.

Examples
Example 1:
Input: [3, 5, 2]
Expected Output: [2, 5, 3]
Justification: Reversing the list [3, 5, 2] gives us [2, 5, 3].
Example 2:
Input: [7]
Expected Output: [7]
Justification: Since there is only one element in the list, the reversed list remains the same.
Example 3:
Input: [-1, 0, 1]
Expected Output: [1, 0, -1]
Justification: The list is reversed, so the elements are in the order [1, 0, -1].
'''
class Solution2:
    def reverseQueue(self, q):
        stack = []

        while q:
            stack.append(q.pop(0))
        
        while stack:
            q.append(stack.pop())

        return q
    
q2 = [1, 2, 3, 4, 5]
sol2 = Solution2()
print(sol2.reverseQueue(q2))

#########################################################
from queue import Queue

class Solution3:
    def reverseQueue(self, q):
        stack = []

        while not q.empty():
            stack.append(q.get())

        while stack:
            q.put(stack.pop())
        
        return q


q3 = Queue()
for i in range(5):
    q3.put(i+1)

sol3 = Solution3()
#print(sol3.reverseQueue(q3))       # won't work, returns <queue.Queue object at 0x7d77efe77ec0>

sol3.reverseQueue(q3)

result = []
while not q3.empty():
    result.append(q3.get())
print(result)

########################################################
# Given Solution:

from collections import deque
class Solution:
    def reverseQueue(self, q):
        
        stack = []

        while q:
            stack.append(q.popleft())

        while stack:
            q.append(stack.pop())

        return q
    
q = deque([1, 2, 3, 4, 5])
sol = Solution()

q = sol.reverseQueue(q)

# Print each element of the now-reversed deque.
while q:
    print(q.popleft(), end=' ')