#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

#Input: nums = [1,2,3,4,5,6,7], k = 3
#Output: [5,6,7,1,2,3,4]
#Explanation:
#rotate 1 steps to the right: [7,1,2,3,4,5,6]
#rotate 2 steps to the right: [6,7,1,2,3,4,5]
#rotate 3 steps to the right: [5,6,7,1,2,3,4]


#Naive approach with O(n2) tc and O(1) sc

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        
        i = 1
        while i <= k:
            nums.insert(0, nums[len(nums)-1])
            nums.pop()
            i+=1
        return nums
    
a = Solution()

print(a.rotate([1,2,3,4,5,6,7], 3))


print('--------------------------')
#Time optymized approach with O(n) tc but also O(n) sc
class Solution2:
    def rotate(self, nums: list[int], k: int) -> None:
        
        nums2 = list()

        for i in range(len(nums)):

            nums2.append(nums[i-k])

        return nums2


a = Solution2()

print(a.rotate([1,2,3,4,5,6,7], 3))


print('--------------------------')
#More Pythonic approach using a List Comprehension with O(n) and also O(n) sc

class Solution3:
    def rotate(self, nums: list[int], k: int) -> None:
        
        nums2 = [nums[i-k] for i in range(len(nums))]

        return nums2


a = Solution3()

print(a.rotate([1,2,3,4,5,6,7], 3))


print('--------------------------')
#Another simple O(n) tc approach and also O(n) sc

class Solution4:
    def rotate(self, nums: list[int], k: int) -> list[int]:
        new = list()

        for i in range(-k, 0, 1):
            new.append(nums[i])       
        for i in range( len(nums) - k ):
            new.append(nums[i])
        return new
    
a = Solution4()

print(a.rotate([1,2,3,4,5,6,7], 3))


print('--------------------------')

#Swapping/reversing approach with O(n) tc and O(1) sc


# 3 rotation steps required
# 1-st: rotate whole array - rotate(0, len())
# 2-nd: rotate part of array from previous step from begginning till k - rotate(0, k)
# 3-rd: rotate part of array from previous step from k till the end - rotate(k, end)

class Solution5:
    def rotate(self, nums: list[int], k: int) -> list[int]:
        length = len(nums)
        k = k%length
        def reverse(array, beg_indx, end_indx):
            while beg_indx < end_indx:
                array[beg_indx], array[end_indx] = array[end_indx], array[beg_indx]
                beg_indx +=1
                end_indx -=1
            
            return array
        reverse(nums,0,length-1)
        reverse(nums,0,k-1)
        reverse(nums,k,length-1)
        return nums
    
a = Solution5()

print(a.rotate([1,2,3,4,5,6,7], 3))