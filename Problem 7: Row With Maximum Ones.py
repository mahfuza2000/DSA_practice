'''
Problem Statement
Given a binary matrix that has dimensions , consisting of ones and zeros, determine the row that contains the highest number of ones and return two values: the zero-based index of this row and the actual count of ones it possesses.

If there is a tie, i.e., multiple rows contain the same maximum number of ones, we must select the row with the lowest index.

Examples
Example 1:

Input: [[1, 0], [1, 1], [0, 1]]
Expected Output: [1, 2]
Justification: The second row [1, 1] contains the most ones, so the output is [1, 2].
Example 2:

Input: [[0, 1, 1], [0, 1, 1], [1, 1, 1]]
Expected Output: [2, 3]
Justification: The third row [1, 1, 1] has the most ones, leading to the output [2, 3].
Example 3:

Input: [[1, 0, 1], [0, 0, 1], [1, 1, 0]]
Expected Output: [0, 2]
Justification: Both the first and third rows contain two ones, but we choose the first due to its lower index, resulting in [0, 2].
Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
'''


# My Soulution:
class Solution:
    def findMaxOnesRow(self, mat):
        maxOnesIdx, maxOnesCount = 0, 0  # Initialize tracking variables
        currOnesIdx = 0
        
        for m in range(len(mat)):
            currOnesCount = 0
            for n in range(len(mat[0])):
                if mat[m][n] == 1:
                    currOnesCount += 1
                    if currOnesCount > maxOnesCount:
                        maxOnesCount = currOnesCount
                        maxOnesIdx = m

        return [maxOnesIdx, maxOnesCount]  

# Given Solution:
'''
class Solution:
    def findMaxOnesRow(self, mat):
        maxOnesIdx, maxOnesCount = 0, 0  # Initialize tracking variables
        for i, row in enumerate(mat):  # Traverse through rows
            onesCount = sum(row)  # Count ones in the current row
            # Check and update tracking variables if needed
            if onesCount > maxOnesCount:  
                maxOnesIdx, maxOnesCount = i, onesCount  
        return [maxOnesIdx, maxOnesCount]  

# Testing
sol = Solution()
# Applying example inputs
print(sol.findMaxOnesRow([[1, 0], [1, 1], [0, 1]]))  # Output: [1, 2]
print(sol.findMaxOnesRow([[0, 1, 1], [0, 1, 1], [1, 1, 1]]))  # Output: [2, 3]
print(sol.findMaxOnesRow([[1, 0, 1], [0, 0, 1], [1, 1, 0]]))  # Output: [0, 2]

'''