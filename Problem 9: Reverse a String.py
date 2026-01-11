'''
Problem Statement
Given a string, write a function that uses a stack to reverse the string. The function should return the reversed string.

Examples
Example 1:

Input: "Hello, World!"
Output: "!dlroW ,olleH"
Example 2:

Input: "OpenAI"
Output: "IAnepO"
Example 3:

Input: "Stacks are fun!"
Output: "!nuf era skcatS"
Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
'''

# My Solution:
class Solution:
    def reverseString(self, s):
        rev_list = []
        stack = list(s)

        while stack:
            c = stack.pop()
            rev_list.append(c)

        rev_str = "".join(rev_list)
        return rev_str
    
# Given Solution
'''
# Define a class named Solution
class Solution:
    def reverseString(self, s):
        # Create a stack (using a list in Python)
        stack = list(s)

        # Use a list to collect reversed characters
        reversed_list = []

        # Pop characters from the stack and add them to the list
        while stack:
            reversed_list.append(stack.pop())

        # Convert list to string using ''.join()
        return ''.join(reversed_list)

# Create an instance of the Solution class
rs = Solution()

# Test the reverseString method with different input strings and print the results
print(rs.reverseString("Hello, World!"))  # Output: "!dlroW ,olleH"
print(rs.reverseString("OpenAI"))  # Output: "IAnepO"
print(rs.reverseString("Stacks are fun!"))  # Output: "!nuf era skcatS"

'''