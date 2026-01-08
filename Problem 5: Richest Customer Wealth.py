'''
Problem Statement
You are given an m x n matrix accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.

Return the wealth that the richest customer has.

Imagine every customer has multiple bank accounts, with each account holding a certain amount of money. The total wealth of a customer is calculated by summing all the money across all their multiple.

Examples
Example 1:

Input: accounts =
[[5,2,3],
 [0,6,7]]
Expected Output: 13
Justification: The total wealth of the first customer is 10 and of the second customer is 13. So, the output is 13 as it's the maximum among all customers.
Example 2:

Input: accounts =
[[1,2],
 [3,4],
 [5,6]]
Expected Output: 11
Justification: Total wealth for each customer is [3, 7, 11]. Maximum of these is 11.
Example 3:

Input: accounts =
 [[5,10,15],
  [10,20,30],
  [15,30,45]]
Expected Output: 90
Justification: Total wealth for each customer is [30, 60, 90]. The wealthiest customer has 90.
Constraints:

m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100
'''

# My Solution:
class Solution:
    def maximumWealth(self,accounts):
        max_wealth = 0  # Initialize max_wealth to 0

        for rowVal in range(len(accounts)):
            currentWealth = 0
            for elementVal in range(len(accounts[rowVal])):
                currentWealth += accounts[rowVal][elementVal]
            if currentWealth > max_wealth:
                max_wealth = currentWealth

        return max_wealth

# Given Solution:
'''
class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0  # Initialize max_wealth to 0
        # Loop through each customer's accounts
        for customer in accounts:
            wealth = sum(customer)  # Sum up the customer's wealth using the sum function
            # Update max_wealth if the current customer's wealth is greater
            if wealth > max_wealth:
                max_wealth = wealth
        # Return the maximum wealth found
        return max_wealth
'''

# Example test cases
sol = Solution()
print(sol.maximumWealth([[5,2,3],[0,6,7]]))  # 13
print(sol.maximumWealth([[1,2],[3,4],[5,6]]))  # 11
print(sol.maximumWealth([[5,10,15],[10,20,30],[15,30,45]]))  # 90