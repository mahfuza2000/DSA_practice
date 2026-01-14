'''
Problem Statement
Given an integer array arr and an integer k, return the result list containing the maximum for each and every contiguous subarray of size k.

In other words, result[i] = max(arr[0],..., arr[k]), result[1] = max(arr[1],...arr[k+1]), etc.

Examples
Example 1
Input: arr = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
Output: [3, 3, 4, 5, 5, 5, 6]
Description: Here, subarray [1,2,3] has maximum 3, [2,3,1] has maximum 3, [3,1,4] has maximum 4, [1,4,5] has maximum 5, [4,5,2] has maximum 5, [5,2,3] has maximum 5, and [2,3,6] has maximum 6.
Example 2
Input: arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13], k = 4
Output: [10, 10, 10, 15, 15, 90, 90]
Description: Here, the maximum of each subarray of size 4 are 10, 10, 10, 15, 15, 90, 90 respectively.
Example 3
Input: arr = [12, 1, 78, 90, 57], k = 3
Output: [78, 90, 90]
Description: Here, the maximum of each subarray of size 3 are 78, 90, and 90 respectively.
'''

# My Solution:
# o(n*k) ... can be more efficient if not checking max() of every window
from collections import deque

class Solution2:
    def printMax(self, arr, k):
        result = []
        arr = deque(arr)
        count = k
        
        # sliding window of length k
        wind = deque()

        while count > 0:
            wind.append(arr.popleft())
            count -= 1
        
        while arr:
            result.append(max(wind))
            wind.popleft()
            wind.append(arr.popleft())

        result.append(max(wind))

        return result

class Solution:
    def printMax(self, arr, k):
        dq = deque()  # Deque to store indices
        result = []  # List to store the result
        n = len(arr)

        for i in range(n):
            
            # [left ....... right] is the window, and right = i
            # then right - left = k + 1 (if k = 3, then window at i = 3 is 1, 2, 3 so right-left = 2.)
            # therefore left boundary = i - k + 1
        
            # Remove elements which are out of this window leftside
            while dq and dq[0] < i - k + 1:   
                dq.popleft()

            # Remove all elements smaller than the currently being added element
            # If the current element arr[i] is greater than or equal to elements at the back of dq, remove those elem's indices
            # if dq = [0, 1] with values pointed are arr = [12, 1], if arr[2] = 78 >= arr[dq[-1]] = arr[1] = 1, pop 1 fron dq, and repeat
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()

            # Add current element at the rear of deque
            dq.append(i)

            # If we have processed at least k elements, add to result
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result


solution = Solution()
arr = [12, 1, 78, 90, 57]
k = 3
result = solution.printMax(arr, k)

# Print the result
print(result)  # Output should be [78, 90, 90]
