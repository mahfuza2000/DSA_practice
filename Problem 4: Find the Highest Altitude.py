'''
Problem Statement
A bike rider is going on a ride. The road contains n + 1 points at different altitudes. The rider starts from point 0 at an altitude of 0.

Given an array of integers gain of length n, where gain[i] represents the net gain in altitude between points i and i + 1 for all (0 <= i < n), return the highest altitude of a point.

Examples
Example 1
Input: gain = [-5, 1, 5, 0, -7]
Expected Output: 1
Justification: The altitude changes are [-5, -4, 1, 1, -6], where 1 is the highest altitude reached.
Example 2
Input: gain = [4, -3, 2, -1, -2]
Expected Output: 4
Justification: The altitude changes are [4, 1, 3, 2, 0], where 4 is the highest altitude reached.
Example 3
Input: gain = [2, 2, -3, -1, 2, 1, -5]
Expected Output: 4
Justification: The altitude changes are [2, 4, 1, 0, 2, 3, -2], where 4 is the highest altitude reached.
Constraints:

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100
'''

# My Solution 1:
class Solution:
    def largestAltitude(self, gain):
        max_altitude = 0  # To store the maximum altitude encountered
        for i in range(len(gain)):
            gain_sum = sum(gain[0:i+1])
            if  gain_sum > max_altitude:
                max_altitude = gain_sum
        return max_altitude

# My Solution 2:
class Solution:
    def largestAltitude(self, gain):
        max_altitude = 0  # To store the maximum altitude encountered
        current_altitude = 0
        for i in range(len(gain)):
            current_altitude += gain[i]
            if  current_altitude > max_altitude:
                max_altitude = current_altitude
        return max_altitude

# Given Solution:
'''
class Solution:
    def largestAltitude(self, gain):
        currentAltitude = 0  # To store the current altitude during iteration
        maxAltitude = 0  # To store the maximum altitude encountered

        # Iterate through the gain list, updating the current and max altitudes
        for i in gain:
            currentAltitude += i
            maxAltitude = max(currentAltitude, maxAltitude)

        return maxAltitude

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    print(solution.largestAltitude([-5, 1, 5, 0, -7]))  # Expected: 1

    # Example 2
    print(solution.largestAltitude([4, -3, 2, -1, -2]))  # Expected: 4
    
    # Example 3
    print(solution.largestAltitude([2, 2, -3, -1, 2, 1, -5]))  # Expected: 4
'''
