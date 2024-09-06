import time

array1 = [1,2,3,4,5]


def find_pairs(array):

    t0 = time.time() #O(1)

    for i in range(len(array)): #O(m)
        for j in range(len(array)): #O(m)
            print(f"{array[i]} and {array[j]}") #O(1)

    t1 = time.time()  #O(1)
    print(f'The search took {t1-t0} seconds.')  #O(1)


find_pairs(array1)

#O(3 + m*(m+1)) -> O(m^2) -> O(m^2)


new_array = [1,2,3,4,5]
def print_numbers_then_pairs(array):

    print("The numbers are : ") #O(1)
    for i in range(len(array)): #O(n)
        print(array[i])         #O(1)

    print("The pairs are :") #O(1)
    for i in range(len(array)): #O(n)
        for j in range(len(array)): #O(n)
            print(array[i], array[j]) #O(1)

print_numbers_then_pairs(new_array)

#O(1 + n+1 + n*(n+1)) -> O(n + n^2) -> O(n^2)