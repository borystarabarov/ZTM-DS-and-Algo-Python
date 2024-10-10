class MyArray: 
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self,index):
        try:
            if index < self.length:
                return self.data[index]
            else:
                raise IndexError(f'Invalid Index: {index} is out of bounds for array of length {self.length}')
        except IndexError as e:
            print(e)
              
    def push(self, value):
        self.length += 1
        self.data[self.length - 1] = value
        return self.data
    
    def pop(self):
        self.length -= 1
        last_item = self.data[self.length]
        del self.data[self.length]
        return last_item 
    
    def insert(self, index, value):
        self.length += 1
        for i in range(self.length-1, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        return self.data
    
    def delete(self, index):
        self.length -= 1
        for i in range(index, self.length, 1):
            self.data[i] = self.data[i+1]
        del self.data[self.length]
        return self.data




arr = MyArray()

arr.push(6)
print(arr.data)
print(arr.get(0))

arr.push(16)
print(arr.data)
print(arr.get(1))

arr.push('Text')
print(arr.data)
print(arr.get(3))
print(arr.get(2))
arr.push(15)
print(arr.data)
print(arr.length)

arr.insert(2,10)
print(arr.data)
print(arr.length)

arr.delete(2)
print(arr.data)
print(arr.length)

arr.pop()
print(arr.data)
print(arr.length)
