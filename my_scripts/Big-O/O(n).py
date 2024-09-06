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

findNemo (array2)   

#### Time Complexity O(n) - Linear (One Loop)
#### Space Complexity O(3) -> O(1) -> Constant - we're keeping in memory only the current variable i + t0 + t1


#### Time Complexity O(n) - Linear (One Loop)

def findNemo (array):

    a = 10      # O(1)
    b = a * 5   # O(1)
    c = b + a   # O(1)

    for i in range(len(array)):   #if we extend logic of for loop it will be for i = 0; i <= len; i++ -> 1 + (1+1)*n -> 1 + 2n
        if array[i] == 'nemo':    # n*O(1)
            print('Found Nemo')   # n*O(1)
            w = a + b + c         # n*O(1)

    a = 0     # O(1)
    b = a + b + c     # O(1)
    print('Something')  # O(1)

findNemo (array2)   

#### Time Complexity  O( 1 + 1 + 1 + 1 + 2n + n + n + n + 1 + 1 + 1) -> O(7 + 5n) -> O(5n) -> O(n) - Linear (One Loop)
#### Space Complexity O(4) -> O(1) -> Constant - we're keeping in memory only the current variable i + a,b,c


def findNemo (array):

    for i in range(len(array)):   # O(n)
        if array[i] == 'nemo':    # O(n)
            print('Found Nemo')   # O(n)
            w = 1 + 3 + 5         # O(n)

    for i in range(len(array) - 5):   # O(n)
        print('Found Nemo')   # O(n)
        w = w + 3         # O(n)
        w = w +1         # O(n)

    a = 0     # O(1)
    b = w + a     # O(1)

findNemo (array2)   


# Time Complexity  O(n + n + n + n + n + + n + n + n + 1 + 1) -> O(8n + 2) -> O(8n) -> O(n) - Linear (One Loop)
# Space Complexity O(1)

def createarray(n):
    array = []                 # O(1)
    for i in range(n):         # O(n)
        array.append('Hi')     # n*O(1)

    print(array)               # O(1)

createarray(10)

# Time Complexity  O(n)
# Space Complexity O(n) as space allocated is dependent on n