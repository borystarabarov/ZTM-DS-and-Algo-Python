class cuboid:
    def __init__(self, l,b,h):
        self.length = l
        self.breadth = b
        self.hight = h
        self.volume_attr = self.length*self.breadth*self.hight
        print(id(self))
    
    def lidarea(self):
        return self.length*self.breadth
    
    def volume(self):
        print(id(self))
        return (self.length*self.breadth*self.hight)
    

c1 = cuboid(1,2,3)

print(c1.hight)
print(c1.volume())
print(c1.volume_attr)

print(id(c1))