'''
Problem Statement
Given a one-dimensional array of integers, create a new array that represents the running sum of the original array.

The running sum at position i in the new array is calculated as the sum of all the numbers in the original array from the 0th index up to the i-th index (inclusive). Formally, the resulting array should be computed as follows: result[i] = sum(nums[0] + nums[1] + ... + nums[i]) for each i from 0 to the length of the array minus one.

Examples
Example 1

Input: [2, 3, 5, 1, 6]
Expected Output: [2, 5, 10, 11, 17]
Justification:
For i=0: 2
For i=1: 2 + 3 = 5
For i=2: 2 + 3 + 5 = 10
For i=3: 2 + 3 + 5 + 1 = 11
For i=4: 2 + 3 + 5 + 1 + 6 = 17
Example 2

Input: [1, 1, 1, 1, 1]
Expected Output: [1, 2, 3, 4, 5]
Justification: Each element is simply the sum of all preceding elements plus the current element.
Example 3

Input: [-1, 2, -3, 4, -5]
Expected Output: [-1, 1, -2, 2, -3]
Justification: Negative numbers are also summed up in the same manner as positive ones.
Constraints:

1 <= nums.length <= 1000
'''

# My Solution:
class Solution:
    def runningSum(self, nums):
        result = [0] * len(nums) 
        #result[0] = nums[0]
        total_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]
            result[i] = total_sum
        return result

def main():
    solution = Solution()
    test_case = [3, 1, 4, 2, 2]
    output = solution.runningSum(test_case)
    print(output)


if __name__ == "__main__":
    main()

# Given Solution:
'''
class Solution:
    def runningSum(self, nums):
        # Check if the array is None or has no elements and return an empty list if true
        if nums is None or len(nums) == 0:
            return []
        
        # Initialize a list to store the running sum
        result = [0] * len(nums)
        result[0] = nums[0]
        
        # Loop through the list starting from index 1, adding the previous sum to the current element
        for i in range(1, len(nums)):
            result[i] = result[i - 1] + nums[i]
        
        # Return the list containing the running sum
        return result

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    testInputs = [
        [2, 3, 5, 1, 6],
        [1, 1, 1, 1, 1],
        [-1, 2, -3, 4, -5]
    ]

    for input_arr in testInputs:
        output = solution.runningSum(input_arr)
        
        # Print the output list
        print(" ".join(map(str, output)))

'''
