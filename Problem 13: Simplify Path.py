'''
Problem Statement
Given an absolute file path in a Unix-style file system, simplify it by converting ".." to the previous directory and removing any "." or multiple slashes. The resulting string should represent the shortest absolute path.

Examples
Example 1
Input: path = "/a//b////c/d//././/.."
Expected Output: "/a/b/c"
Explanation:
Convert multiple slashes (//) into single slashes (/).
"." refers to the current directory and is ignored.
".." moves up one directory, so "d" is removed.
The simplified path is "/a/b/c".
Example 2
Input: path = "/../"
Expected Output: "/"
Explanation:
".." moves up one directory, but we are already at the root ("/"), so nothing happens.
The final simplified path remains "/".
Example 3
Input: path = "/home//foo/"
Expected Output: "/home/foo"
Explanation:
Convert multiple slashes (//) into single slashes (/).
The final simplified path is "/home/foo".
Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
'''

# My Solution:
class Solution2:
    def simplifyPath(self, path): 
        # simplify it by converting ".." to the previous directory and 
        # removing any "." or multiple slashes "/". 

        # Input: path = "/a//b////c/d//././/.."
        # Expected Output: "/a/b/c"

        symbols_stack = []
        path_stack = path.split('/')

        while path_stack:
            # if path_stack[-1] == '/':
            #     path_stack.pop()
            # else:
                symbols_stack.append(path_stack.pop())
                # print("Symbol Stack: ", symbols_stack)
        
        return_stack = []

        while symbols_stack:
            if symbols_stack[-1] == '' or symbols_stack[-1] == '.':
                symbols_stack.pop()
            elif symbols_stack[-1].isalpha():
                return_stack.append('/')
                return_stack.append(symbols_stack.pop())
                # print("Returned Stack: ", return_stack)
            elif symbols_stack[-1] == '..':
                symbols_stack.pop()
                if return_stack:
                    return_stack.pop() #symbol  
                    return_stack.pop() # /
                # print("Returned Stack: ", return_stack)

        return_path = ''.join(return_stack)
        if not return_path:
            return '/'
        
        return return_path
    
# Given Solution:
class Solution:
    def simplifyPath(self, path):
        # Create a stack to store the simplified path components
        stack = []
        
        # Split the input path string using '/' as a delimiter
        for p in path.split('/'):
            if p == '..':
                # If the component is '..', pop the last component from the stack
                if stack:
                    stack.pop()
            elif p and p != '.':
                # If the component is not empty and not '.', push it onto the stack
                stack.append(p)
        
        # Reconstruct the simplified path by joining components from the stack
        return '/' + '/'.join(stack)

# Test cases
sol = Solution2()
print(sol.simplifyPath("/a//b////c/d//././/..")) # Expected output: "/a/b/c"
print(sol.simplifyPath("/../")) # Expected output: "/"
print(sol.simplifyPath("/home//foo/")) # Expected output: "/home/foo"
