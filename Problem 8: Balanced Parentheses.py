'''
Problem Statement
Given a string s containing (, ), [, ], {, and } characters. Determine if a given string of parentheses is balanced.

A string of parentheses is considered balanced if every opening parenthesis has a corresponding closing parenthesis in the correct order.

Example 1:

Input: String s = "{[()]}";
Expected Output: true
Explanation: The parentheses in this string are perfectly balanced. Every opening parenthesis '{', '[', '(' has a corresponding closing parenthesis '}', ']', ')' in the correct order.

Example 2:

Input: string s = "{[}]";
Expected Output: false
Explanation: The brackets are not balanced in this string. Although it contains the same number of opening and closing brackets for each type, they are not correctly ordered. The ']' closes '[' before '{' can be closed by '}', and similarly, '}' closes '{' before '[' can be closed by ']'.

Example 3:

Input: String s = "(]";
Expected Output: false
Explanation: The parentheses in this string are not balanced. Here, ')' does not have a matching opening parenthesis '(', and similarly, ']' does not have a matching opening bracket '['.

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

# My Solution:
class Solution_mine:
    def isValid(self, s):
        stack = []
        opening_symbols = ("(", "[", "{")

        for symbol in s:
            if symbol in opening_symbols:
                stack.append(symbol)
            
            # handle closed symbols
            else:
                # if we see a closed symbol but the stack is empty (aka no opening symbol), return false
                if len(stack) == 0:
                    return False
                elif symbol == ")" and stack[-1] == "(":
                    stack.pop()
                elif symbol == "]"and stack[-1] == "[":
                    stack.pop()
                elif symbol == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
                
        # after all symbols have been read
        if len(stack) == 0:
            return True
        return False


# Given Solution:
class Solution:
    def isValid(self, s: str) -> bool:
        # Creating a stack to keep track of opening parentheses
        stack = []
        
        # Iterating through each character in the input string
        for c in s:
            # If the character is an opening parenthesis, push it onto the stack
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                # If stack is empty and we have a closing parenthesis, the string is not balanced
                if not stack:
                    return False
                
                # Pop the top character from the stack
                top = stack.pop()
                
                # If the character is a closing parenthesis, check whether 
                # it corresponds to the most recent opening parenthesis
                if c == ')' and top != '(':
                    return False
                if c == '}' and top != '{':
                    return False
                if c == ']' and top != '[':
                    return False
        # If the stack is empty, all opening parentheses had a corresponding closing match
        return not stack


# Test cases to verify the solution
sol = Solution()
test1 = "{[()]}"; # Should be valid
test2 = "{[}]";   # Should be invalid
test3 = "(]";     # Should be invalid
test4 = "{[()]]]}"; # Should be invalid

print("Test 1:", sol.isValid(test1))
print("Test 2:", sol.isValid(test2))
print("Test 3:", sol.isValid(test3))
print("Test 4:", sol.isValid(test4))
