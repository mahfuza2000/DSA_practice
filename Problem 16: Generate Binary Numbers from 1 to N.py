'''
Problem Statement
Given an integer N, generate all binary numbers from 1 to N and return them as a list of strings.

Examples
Example 1
Input: N = 2
Output: ["1", "10"]
Explanation: The binary representation of 1 is "1", and the binary representation of 2 is "10".
Example 2
Input: N = 3
Output: ["1", "10", "11"]
Explanation: The binary representation of 1 is "1", the binary representation of 2 is "10", and the binary representation of 3 is "11".
Example 3
Input: N = 5
Output: ["1", "10", "11", "100", "101"]
Explanation: These are the binary representations of the numbers from 1 to 5.
'''

from queue import Queue
#from collections import deque

class Solution2:
    def generateBinaryNumbers(self, n):
        res = []
        holder = Queue()
        holder.put("1") # start with 1 in holder

        for i in range(n):
            intermed = holder.get()

            elem1 = intermed + "0"
            elem2 = intermed + "1"

            holder.put(elem1)
            holder.put(elem2)

            res.append(intermed)

            # print("holder: ", elem1, elem2)
            # print("result: ", res)

        return res

# Given Solution:
class Solution: 
    def generateBinaryNumbers(self, n):
        q = Queue()
        q.put("1")

        res = []
        while n > 0:
            res.append(q.get())  # Add the current binary number to the result list.
            s1 = res[-1] + "0"  # Generate the next binary number by adding "0".
            s2 = res[-1] + "1"  # Generate the next binary number by adding "1".
            q.put(s1)  # Enqueue the first generated binary number.
            q.put(s2)  # Enqueue the second generated binary number.
            n -= 1

        return res
    
# Testing
sol = Solution()
# print(sol.generateBinaryNumbers(2))
# print(sol.generateBinaryNumbers(3))
print(sol.generateBinaryNumbers(9))
