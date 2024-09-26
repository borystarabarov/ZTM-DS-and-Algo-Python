# [1,2,3,4,5,6] , 7 -> true
# [1,2,3,4,5,6] , 8 -> true
# [1,2,3,4,5,5] , 11 -> false


# Loop over the array and pick an item
 # For each item loop over same array and check if item + item = sum
# Time O(n^2)
# Space O(1)

def hasPairWithSum(array, sum):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i]+array[j] == sum:
                return True
    return False

arr1 = [1,2,3,4,5,6]

x = hasPairWithSum(arr1, 10)

print(x)


# Loop over the array and put values into a hash table
# loop over the array and check for current item if (sum - item) is in table
# Time O(2n) -> O(n)
# Space O(n)

# [1,2,3,4,5,6] , 7
#0 [] 
#1 1 -> 6 -> [1]
#2 2 -> 5 -> [1,2]
#3 3 -> 4 -> [1,2,3]
#4 4 -> 3 -> [1,2,3] - true

def hasPairWithSum2(array, sum):
    hashtable = dict()

    for item in array:
        hashtable[item] = True

    print(hashtable)


arr1 = [1,2,3,4,5,6]

hasPairWithSum2(arr1, 10)





