'''
Given an integer x, return true if x is a palindrome, and false otherwise.
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''
from collections import deque

class Solution:
    def isPalindrome(self, x: int) -> bool:
        holder = deque()

        # Eliminate all negative numbers here. Or else the first while loop will run infinitely:
        # -121 // 10 == -13
        # -13 // 10 == -2
        # -2 // 10 == -1
        # -1 // 10 == -1   # ← stuck forever
        if x < 0:
            return False

        while x:
            holder.append(x%10)
            x = x // 10
        
        while len(holder) > 1:
            if holder.popleft() != holder.pop():
                return False
            
        return True

  
sol = Solution()
print(sol.isPalindrome(121))  
print(sol.isPalindrome(-121))
print(sol.isPalindrome(12))
