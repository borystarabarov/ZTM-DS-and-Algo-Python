# [0,3,4,31] [4,6,30]
# []

def mergeSortedArrays(array1, array2):
    
    result = []
    i1 = 0
    i2 = 0
    i1_over_flag = False
    i2_over_flag = False

    while i1 < len(array1) or i2 < len(array2):       

        if i2 == len(array2):
            i2_over_flag = True
        
        if i1 == len(array1):
            i1_over_flag = True

        if i2_over_flag == True:
            result.append(array1[i1])
            i1 +=1
        elif i1_over_flag == True:
            result.append(array2[i2])
            i2 +=1
        elif array1[i1] <= array2[i2]:
            result.append(array1[i1])
            i1 +=1
        else:
            result.append(array2[i2])
            i2 +=1

    return result

print(mergeSortedArrays([0,1,2], [4,6,30,35,60]))

print(mergeSortedArrays([0,1,2], []))

print(mergeSortedArrays([], [4,6,30,35,60]))

# Time Complexity - O(n)
# Space Complexity - O(n)