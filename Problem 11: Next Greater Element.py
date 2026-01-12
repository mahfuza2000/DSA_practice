'''
Problem Statement
Given an array, print the Next Greater Element (NGE) for every element.

The Next Greater Element for an element x is the first greater element on the right side of x in the array.

Elements for which no greater element exist, consider the next greater element as -1.

Examples
Example 1:

 Input: [4, 5, 2, 25]
 Output: [5, 25, 25, -1]
Example 1:

 Input: [13, 7, 6, 12]
 Output: [-1, 12, 12, -1]
Example 1:

 Input: [1, 2, 3, 4, 5]
 Output: [2, 3, 4, 5, -1]

 Solution:
A simple algorithm is to run two loops: the outer loop picks all elements one by one, and the inner loop looks for the first greater element for the element picked by the outer loop. However, this algorithm has a time complexity of .

We can use a more optimized approach using Stack data structure. The algorithm will leverage the nature of the stack data structure, where the most recently added (pushed) elements are the first ones to be removed (popped). Starting from the end of the array, the algorithm always maintains elements in the stack that are larger than the current element. This way, it ensures that it has a candidate for the "next larger element". If there is no larger element, it assigns -1 to that position. It handles each element of the array only once, making it an efficient solution.

Detailed Step-by-Step Walkthrough

The function receives an array arr.

Initialize an empty stack s and an output array res of size equal to the input array, with all elements initialized to -1. res will store the result, i.e., the next larger element for each position in the array.

Start a loop that goes from the last index of the array to the first (0 index).

In each iteration, while there are elements in the stack and the top element of the stack is less than or equal to the current element in the array, remove elements from the stack. This step ensures that we retain only the elements in the stack that are larger than the current element.

After the popping process, if there is still an element left in the stack, it is the next larger element for the current array element. So, assign the top element of the stack to the corresponding position in the res array.

Now, push the current array element into the stack. This action considers the current element as a possible "next larger element" for the upcoming elements in the remaining iterations.

Repeat steps 4-6 for all the elements of the array.

At the end of the loop, res will contain the next larger element for each position in the array. Return this array res.

Algorithm Walkthrough
Let's consider the input and observe how above algorithm works.

Initialize Data Structures:

Input Array: [13, 7, 6, 12]
Result Array: [0, 0, 0, 0] (Initially set to zeros)
Stack: Empty (Will store elements during iteration)
Processing Each Element (Reverse Order):

The algorithm processes the array from right to left.
Last Element (Value 12):

Stack is empty, indicating no greater element for 12.
Result Array: [0, 0, 0, -1] (Updates the last position to -1)
Push element 12 onto the stack.
Third Element (Value 6):

Stack's top element is 12, which is greater than 6.
Result Array: [0, 0, 12, -1] (Updates the value at the third position to 12)
Push element 6 onto the stack.
Second Element (Value 7):

Stack's top element is 6, which is less than 7, so it's popped.
Next, the stack's top element is 12, which is greater than 7.
Result Array: [0, 12, 12, -1] (Updates the value at the second position to 12)
Push element 7 onto the stack.
First Element (Value 13):

Stack's top element is 7, which is less than 13, so it's popped.
Next, stack's top element is 12, which is also less than 13, so it's popped.
Stack is now empty, indicating no greater element for 13.
Result Array: [-1, 12, 12, -1] (Updates the first position to -1)
Push element 13 onto the stack.
'''

# My Solution:
'''
range(start, stop, step)
 start → where counting begins
 stop → where counting stops before (exclusive)
 step → how much to move each time
'''
class Solution2:
    def nextLargerElement2(self, arr):
        n = len(arr)
        res = [-1]*n
        process_stack = []  # keep track of all numbers larger than arr[i], all num in this stack are added from arr from right to left

        for i in range(n-1, -1, -1):  # iterate backwards, where range(start, stop before, step number)
            while process_stack and process_stack[-1] <= arr[i]:
                process_stack.pop()
            if process_stack and process_stack[-1] > arr[i]:
                res[i] = process_stack[-1]
            process_stack.append(arr[i])
        
        return res

# Given Solution:
class Solution:
    def nextLargerElement(self, arr):
        # Initialize an empty stack and a result list with -1 values
        s = []
        res = [-1] * len(arr)

        # Iterate through the array in reverse order
        for i in range(len(arr) - 1, -1, -1):
            # While the stack is not empty and the top element of the stack is less than or equal to the current element
            while s and s[-1] <= arr[i]:
                s.pop()  # Pop elements from the stack until the condition is met
            
            if s: 
                res[i] = s[-1]  # If the stack is not empty, set the result for the current element to the top element of the stack
            s.append(arr[i])  # Push the current element onto the stack

        return res

sol = Solution()
print(sol.nextLargerElement([4, 5, 2, 25]))  # Example usage
print(sol.nextLargerElement([13, 7, 6, 12]))  # Example usage
print(sol.nextLargerElement([1, 2, 3, 4, 5]))  # Example usage
