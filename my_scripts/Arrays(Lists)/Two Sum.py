# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# Naive approach with O(n2) time comp
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]: 
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
    
a = Solution()

print(a.twoSum([2,7,11,15], 9))
print(a.twoSum([3,2,4], 6))
print(a.twoSum([3,3], 6))
print(a.twoSum([3,2], 6))
print(a.twoSum([], 6))


# more optimal approach O(n)
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        map = {}

        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in map:
                return [map[complement], i]
            map[nums[i]] = i


a = Solution2()

print(a.twoSum([2,7,11,15], 9))
print(a.twoSum([3,2,4], 6))
print(a.twoSum([3,3], 6))
print(a.twoSum([3,2], 6))
print(a.twoSum([], 6))