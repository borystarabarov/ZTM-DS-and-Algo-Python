List1 = [ 1,2,3,4,5 ]
#List2 = list( ( 1,2,3,4,5 ) )
#List3 = list()

#print(List1)
#print(List2)
#print(List3)


# Access(Look-up) O(1)

#Any element of an array can be accessed by its index
# We're accessing a specific memory shelf(index) so it's a O(1)
print(List1[1])    # O(1)
print(List1[-1])   # O(1)
print(List1[-5])   # O(1)
print(len(List1))


# Push(Append)/Pop(Delete) O(1) in case of last element

#Push corresponds to pushing or adding an element at the end of the array.
#Similarly, pop corresponds to removing the element at the end of the array.
#Since the index of the end of the array is known, finding it and pushing or popping an element will only require O(1) time

List1.append('John')    # O(1)
List1.append('Bob')    # O(1)
print(List1)

List1.pop()       # O(1)
print(List1)


# Insert  # O(n)

#Insert operation inserts an element at the beginning of the array, or at any location specified.
#This is O(n) operation since after inserting the element at the desired location,
#The elements to the right of the array have to be updated with the correct index as they all have shifted by one place.
#This requires looping through the array. Hence, O(n) time.

List1.insert(0,50) #Inserts 50 at the beginning of the array and shifts all other elements one place towards right. O(n)
print(List1)
List1.insert(4,0) #inserts '0' at index '4', thus shifting all elements starting from index 4 one place towards right. O(n)
print(List1)


# Delete # O(n)

#Similar to insert, it deletes an element from the specified location in O(n) time
#The elements to the right of the deleted element have to shifted one space left, which requires looping over the entire array
#Hence, O(n) time complexity

List1.pop(0) #This pops the first element of the array, shifting the remaining elements of the array one place left. O(n)
print(List1)

del List1[2:4] #This command deletes elements from position 2 to position 4, again, in O(n) time
print(List1)

del List1[0] # O(n)
print(List1)


# Search # O(n)

#This command removes the first occurence of the element 17 in the array, for which it needs to traverse the entire array, which requires O(n) time

List1.remove('John') # O(n)
print(List1)