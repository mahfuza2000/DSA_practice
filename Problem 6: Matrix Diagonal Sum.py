'''
Problem Statement
Given a square matrix (2D array), calculate the sum of its two diagonals.

The two diagonals in consideration are the primary diagonal that spans from the top-left to the bottom-right and the secondary diagonal that spans from top-right to bottom-left. If a number is part of both diagonals (which occurs only for odd-sized matrices), it should be counted only once in the sum.

Examples
Example 1:
Input:
[[1,2,3],
 [4,5,6],
 [7,8,9]]
Expected Output: 25
Justification: Summing up the two diagonals (1+5+9+3+7), we get 25. Please note that the element at [1][1] = 5 is counted only once.
Example 2:
Input:
[[1,0],
 [0,1]]
Expected Output: 2
Justification: The sum of the two diagonals is 1+1 = 2.
Example 3:
Input:
[[5]]
Expected Output: 5
Justification: Since there's only one element, it is the sum itself.
Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
'''

# My Solution:
class Solution:
    def diagonalSum(self, mat):
        total_sum = 0  # Initialize the total sum
        row_num = len(mat) # Since this is a square matrix, we just need the rumber of rows
        
        # Go through each row of the square matrix, 
        # add the value where matix row number and column number are equal, 
        # then add the value that is opposite to that position
        for row in range(row_num):
            total_sum += mat[row][row] + mat[row][row_num - row -1]

        # If the matrix has an odd number of rows/columns, then the above for-loop counted the center value twice. Subtract it.
        if row_num % 2 == 1:
            total_sum -= mat[row//2][row//2]  #Integer Division!!!
        
        return total_sum  # Return the calculated total sum

# Given Solution:
'''
class Solution:
    def diagonalSum(self, mat):
        n = len(mat)  # Get the size of the matrix
        total_sum = 0  # Initialize the total sum
        
        # Loop through each row
        for i in range(n):
            total_sum += mat[i][i] + mat[i][n-i-1]  # Add primary and secondary diagonal elements
        
        # If n is odd, subtract the central element
        if n % 2 != 0:
            total_sum -= mat[n//2][n//2]
        return total_sum  # Return the calculated total sum
    
# Test the examples
sol = Solution();
print(sol.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))  # Output: 25
print(sol.diagonalSum([[1,0],[0,1]]))  # Output: 2
print(sol.diagonalSum([[5]]))  # Output: 5
'''
    
