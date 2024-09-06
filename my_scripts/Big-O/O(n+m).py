import time

c_array1 = ['nemo' for i in range(100)]
c_array2 = ['nemo' for i in range(100000)]

def find_nemo(array1, array2):

    t0 = time.time() #O(1)
    for i in range(0,len(array1)): #O(m)
        if array1[i] == 'nemo':    #O(m)
            print("Found Nemo!!")  #O(m) 
    t1 = time.time() #O(1)
    print(f'The search took {t1-t0} seconds.') #O(1)

    t0 = time.time() #O(1)
    for i in range(0, len(array2)): #O(n)
        if array2[i] == 'nemo':     #O(n)
            print("Found Nemo!!")   #O(n)
    t1 = time.time() #O(1)
    print(f'The search took {t1 - t0} seconds.') #O(1)

find_nemo(c_array1, c_array2)

#O(1 + m + m + m + 1 + 1 + 1 + n + n + n + 1 + 1) = O(6 + 3m + 3n) -> O(m + n)