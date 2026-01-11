'''
Problem Statement
Given a positive integer n, write a function that returns its binary equivalent as a string. The function should not use any in-built binary conversion function.

Examples
Example 1:

Input: 2
Output: "10"
Explanation: The binary equivalent of 2 is 10.
Example 2:

Input: 7
Output: "111"
Explanation: The binary equivalent of 7 is 111.
Example 3:

Input: 18
Output: "10010"
Explanation: The binary equivalent of 18 is 10010.
'''

# My Solution:
class Solution_mine: 
    def decimalToBinary(self, num):
        # convert a decimal into a binary number, returned as a string, w/o using the built-in tools
        '''
        Strategy:
        Divide decimal by 2, record the remainder (either 0 or 1) in a stack/list
        Division stops when remainder is 0
        Reverse stack into a string as the correct binary answer (otherwise backwords)
        '''
        
        rev_binary_stack = []

        if num == 0:
            return "0"

        while num > 0:
            rev_binary_stack.append(str(num % 2))
            num = num // 2

        binary_stack = []
        while rev_binary_stack:
            binary_stack.append(rev_binary_stack.pop())


        return ''.join(binary_stack)


# Given Solution:
class Solution:
    def decimalToBinary(self, num):
        stack = []  # Create an empty stack to hold binary digits.
        while num > 0:  # Continue the loop until num becomes 0.
            stack.append(num % 2)  # Push the remainder of num divided by 2 onto the stack.
            num //= 2  # Update num by integer division (floor division) by 2.
        return ''.join(str(i) for i in reversed(stack))  # Convert the stack to a binary string.

# Test cases
sol = Solution_mine()
print(sol.decimalToBinary(2))    # Output: "10" (Binary representation of 2)
print(sol.decimalToBinary(7))    # Output: "111" (Binary representation of 7)
print(sol.decimalToBinary(18))   # Output: "10010" (Binary representation of 18)