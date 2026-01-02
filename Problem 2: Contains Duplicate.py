'''
Problem Statement
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums= [1, 2, 3, 4]
Output: false  
Explanation: There are no duplicates in the given array.

Example 2:
Input: nums= [1, 2, 3, 1]
Output: true  
Explanation: '1' is repeating.
'''

# My Solution:
class Solution:
    def containsDuplicate(self, nums):
      values_seen = []
      for i in range(len(nums)):
        if nums[i] not in values_seen:
          values_seen.append(nums[i])
        else:
          return True
      return False


# Given Solution:
'''
class Solution:
  def containsDuplicate(self, nums) -> bool:
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]: # if any two elements are the same, return true
          return True
    return False 

if __name__ == '__main__':
  sol = Solution()
  nums1 = [1, 2, 3, 4]
  print(sol.containsDuplicate(nums1)) # Expected output: False

  nums2 = [1, 2, 3, 1]
  print(sol.containsDuplicate(nums2)) # Expected output: True

  nums3 = []
  print(sol.containsDuplicate(nums3)) # Expected output: False

  nums4 = [3, 2, 6, -1, 2, 1]
  print(sol.containsDuplicate(nums4)) # Expected output: True
'''

# Given Soultion 2 (Hash Set):
'''
class Solution:
  def contains_duplicate(self, nums):
    unique_set = set() # Use set to store unique elements
    
    for x in nums:
      if x in unique_set: # If the set already contains the current element, return True
        return True
      unique_set.add(x) # Add the current element to the set

    return False 
'''

# Given Solution 3 (Sorting):
'''
class Solution:
  def contains_duplicate(self, nums) -> bool:
    nums.sort() # sort the array
    # use a loop to compare each element with its next element
    for i in range(len(nums) - 1):
      if nums[i] == nums[i + 1]: # if any two elements are the same, return true
        return True
    return False 
'''
