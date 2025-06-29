class Stack():
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item)==0
    
    def pus(self,data):
        self.item.append(data)


    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("stack is empty")
        

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        
        else:
            return self.item[-1]
        

    def size_of(self):
        return len(self.item)
        

s1= Stack()
s1.pus(10)
s1.pus(20)

print("top element",s1.peek())
print("removed element",s1.pop())
print("top element",s1.peek())
