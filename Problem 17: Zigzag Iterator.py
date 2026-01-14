'''
Problem Statement
Given two 1d vectors, implement an iterator to return their elements alternately.

Implement the Solution class:

Solution(List<int> v1, List<int> v2) is a constructor.
int next() returns the current element of the iterator and moves the iterator to the next element.
boolean hasNext() returns true if the iterator still has elements, and false otherwise.
Examples
Example 1
Input: V1 = [1,2], v2 = [3,4,5,6]
Expected Output: [1,3,2,4,5,6]
Explanation: The elements will be returned in [1,3,2,4,5,6] order when we make v1.size() + v2.size() number of calls to the next() method.
Example 2
Input: V1 = [1, 2, 3, 4], v2 = [5,6]
Expected Output: [1,5,2,6,3,4]
Explanation: The elements will be returned in [1,5,2,6,3,4] order when we make v1.size() + v2.size() number of calls to the next() method.
Example 3
Input: V1 = [1, 2], v2 = []
Expected Output: [1,2]
Explanation: The elements will be returned in [1, 2] order when we make v1.size() + v2.size() number of calls to the next() method.
'''

# My Solution:
from collections import deque

class Solution:
    def func1 (self, v1, v2):
        v1 = deque(v1)
        v2 = deque(v2)
        res = []

        # for v in (v1, v2):  # won't work bc will not check if either is empty
        while v1 and v2:
                res.append(v1.popleft())
                res.append(v2.popleft())    
        while v1:
            res.append(v1.popleft())    
        while v2:
            res.append(v2.popleft())

        return res



sol = Solution()
print(sol.func1([1, 2], [3, 4, 5, 6]))  #[1, 3, 2, 4, 5, 6]
print(sol.func1([], [3, 4, 5, 6]))  #[3, 4, 5, 6]
print(sol.func1([1, 2], []))  #[1, 2]
print(sol.func1([1, 100], [3, 0, 5, 2]))  #[1, 3, 100, 0, 5, 2]

