import time

array2 = ['nemo' for i in range (1000000)]
#print(array2)

#### Time Complexity O(1) - Constant (constant number of statements)

def findNemo2 (array):
    t0 = time.time()
    print('Value = ', array[0] )     #O(1)
    print('Value = ', array[100] )   #O(1)
    t1 = time.time()
    print(f'Time taken = {t1-t0}')

findNemo2 (array2)   # O(2) --> O(1) - Constant (constant number of statements)