import time

array1 = ['nemo' for i in range (100)]
array2 = ['nemo' for i in range (10000)]
#print(array2)

#### Time Complexity O(n) - Linear (One Loop)

def findNemo (array):
    t0 = time.time()
    for i in range(len(array)):
        if array[i] == 'nemo':
            print('Found Nemo')
            #break
    t1 = time.time()
    print(f'Time taken = {t1-t0}')

findNemo (array2)   # Time Complexity O(n) - Linear (One Loop)


#### Time Complexity O(n) - Linear (One Loop)

def findNemo (array):

    a = 10      # O(1)
    b = a * 5   # O(1)
    c = b + a   # O(1)

    for i in range(len(array)):   
        if array[i] == 'nemo':
            print('Found Nemo')   # O(n)
            w = a + b + c         # O(n)

    a = 0     # O(1)
    b = a + b + c     # O(1)
    print('Something')  # O(1)

findNemo (array2)   # Time Complexity  O( 1 + 1 + 1 + n + n + 1 + 1) -> O(5 + 2n) -> O(2n) -> O(n) - Linear (One Loop)



def findNemo (array):

    for i in range(len(array)):   
        if array[i] == 'nemo':
            print('Found Nemo')   # O(n)
            w = a + b + c         # O(n)

    for i in range(len(array) - 5):   
        print('Found Nemo')   # O(n)
        w = a + b + c         # O(n)
        w = a + b + c         # O(n)

    a = 0     # O(1)
    b = a + b + c     # O(1)

findNemo (array2)   # Time Complexity  O(n + n + n + n + n + 1 + 1) -> O(5n + 2) -> O(5n) -> O(n) - Linear (One Loop)