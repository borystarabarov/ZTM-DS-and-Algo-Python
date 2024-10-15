# We re using a two-pointer logic where we in j we track the position where we should place next non zero element and in i we're iterating over an array

# Both solutions are of O(n) time comp and 1(n) space comp

def moveZeroes(nums):
    j = 0
    for i in range(0, len(nums)):
        print(nums)
        if nums[i] != 0:
            if i > j:
                nums[j] = nums[i]
                nums[i] = 0
            j+=1
        
    return nums



def moveZeroes2(nums):
    j = 0
    for i in range(0, len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j+=1     
    return nums


print(moveZeroes2([0,1,0,3,12]))

print(moveZeroes2([1]))

print(moveZeroes2([0]))
