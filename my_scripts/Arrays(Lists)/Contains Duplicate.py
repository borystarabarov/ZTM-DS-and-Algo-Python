# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
#Input: nums = [1,2,3,1]
#Output: true
#Explanation:
#The element 1 occurs at the indices 0 and 3.


# Optimal from the time complexity O(n) but also O(n) from space complexity
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        map = {}

        for i in nums:
            if i in map:
                return True
            else:
                map[i] = True
        return False
    

#Another approach could be to do a space complexity optymization to O(1):

class Solution2:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()                       #sort is O(nlog(n)) tc
        for i in range(1, len(nums)):      # O(n) tc 
            if nums[i] == nums[i - 1]:    # but we have O(1) sc
                return True
        return False
    
a = Solution2()

print(a.containsDuplicate([1,2,3,4]))

