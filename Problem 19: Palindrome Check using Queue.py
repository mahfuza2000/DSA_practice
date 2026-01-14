'''
Problem Statement
Given a string s, determine if that string is a palindrome using a queue data structure. Return true if the string is a palindrome. Otherwise, return false.

A palindrome is a word, number, phrase, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

Examples
Example 1
Input: s = "madam"
Output: true
Explanation: The word "madam" reads the same forwards and backwards.
Example 2
Input: s = "openai"
Output: false
Explanation: The word "openai" does not read the same forwards and backwards.
Example 3
Input: s = "A man a plan a canal Panama"
Output: true
Explanation: The phrase "A man a plan a canal Panama" reads the same forwards and backwards when we ignore spaces and capitalization.
'''

# My SOlution:
from collections import deque

class Solution:
    def checkPalindrome(self, s):
        s = s.replace(" ", "")
        s = s.lower()
        s = deque(s)

        while len(s) > 1:
            front = s.popleft()
            end = s.pop()
            if front != end:
                return False

        return True

# Given Solution:
class Solution: 
    def checkPalindrome(self, s):
        # Remove all non-alphanumeric characters and convert to lowercase
        s = ''.join(filter(str.isalnum, s)).lower()
        # Create a deque (double-ended queue) from the string
        q = deque(s)

        # Continue until there is 0 or 1 character left
        while len(q) > 1:
            # Remove and compare characters from both ends
            if q.popleft() != q.pop():
                return False

        return True

sol = Solution()
print(sol.checkPalindrome('madam'))  # returns: True
print(sol.checkPalindrome('openai'))  # returns: False
print(sol.checkPalindrome('A man a plan a canal Panama'))  # returns: True