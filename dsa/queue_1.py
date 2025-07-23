class Queue:
    def __init__(self):
        self.item= []

    def insert(self,data=None):
        self.item.append(data)

    def dequeue(self):
        self.item.pop(0)

    def peekfront(self):
        return self.item[0]
    
    def peekrear(self):
        return self.item[-1]
    
    def sizeof(self):
        return len(self.item)
    
s= Queue()
s.insert(23)
s.insert(24)

print(s.peekfront())
print(s.peekrear())
print(s.sizeof())
s.dequeue()
print(s.peekfront())
print(s.peekfront())
print(s.sizeof())

