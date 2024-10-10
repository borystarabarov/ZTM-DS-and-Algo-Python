
# Basic approach # Time comp O(n)  Space comp O(n) 
def reverse(string):

   # check the input
   if isinstance(string, str) and len(string) > 0:
        
        result = []
        for i in range(0, len(string)):                               # Time comp O(n)  # Space comp O(n) because we create a new array 
            result.append(string[len(string) - 1 - i])
        return ''.join(result)
   else:
       print('Incorrect string')
       return None
   
print(reverse('ABCDE'))
print(reverse(''))
print(reverse(18))

# More efficient way is to go through a half of array and do a swap of first and last, then second and one defore last and so on
def reverse_opt(string):
    result = list(string)
    for i in range(0, len(result)//2):
        temp = result[i]
        result[i] = result[len(result) - 1 - i]
        result[len(result) - 1 - i] = temp
    return result
print('---------------')
print(''.join(reverse_opt('ABCDE')))

#In the context of reversing a string, the time complexity of \(O(n)\) is the lower bound on the operation because every character in the string 
# must be examined and rearranged in order to create the reversed string. 
# This means that every valid algorithm for reversing a string necessarily has a time complexity of \(O(n)\), where \(n\) is the length of the string.



#Swapping elements from either end of the string to reverse it is a clever approach commonly used for in-place reversal of mutable sequences like arrays or lists. However, in terms of time complexity, it still remains \(O(n)\) despite requiring only half the iterations.
### Why It Remains \(O(n)\)

# **Iteration Count**: While you indeed perform half as many swaps as there are elements (because each swap operation involves two elements), each swap operation still involves visiting every element at least once. Therefore, the total number of operations is still proportional to the number of elements \(n\).
# **Time Complexity Definition**: Time complexity measures how the execution time grows with input size. Because all \(n\) characters are involved in the swaps, the execution time grows linearly with \(n\).

### Swapping Elements Example
#Although this cannot be applied directly to immutable strings in Python, the concept is efficient for lists:

def reverse_in_place(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

# Example usage with a list
mutable_list = ['A', 'B', 'C', 'D', 'E']
print(reverse_in_place(mutable_list))  # Output: ['E', 'D', 'C', 'B', 'A']



# Other ways to do it with a Python built in functions

### 1. Slicing
def reverse1(string):
    return str(string)[::-1]

print(reverse1('ABCDE'))

### 2. `reversed()` Function
def reverse2(string):
    return ''.join(reversed(string))       # reversed is an iterable function

print(reverse2('ABCDE'))





    