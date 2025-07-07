class Node:
    def __init__(self,prev= None,item =None,next= None):
        self.prev= prev
        self.item= item
        self.next = next 
        

class Dll:
    def __init__(self ,start=None):
        self.start= start



    def is_empty(self):
        return self.start is  None
    
    def add_start(self,data):
        n= Node(None,data,self.start)
        if not self.is_empty():

            self.start.prev=n 
        self.start= n
        

    def at_last(self,data ):
        temp =self.start
        if self.start is not None:
           
            while temp.next != None:
                temp = temp.next
        
        n= Node(temp,data,None)
        if temp is None:
            self.start = n
        else:
            temp.next=n
            
    def search(self ,data):
        temp = self.start
        while temp is not None:
            if temp.item== data:
                return temp
            temp= temp.next
        return None
    
    def after_insert(self,temp,data):
        if temp is not None:
            n= Node(temp,data, temp.next)
            if temp.next is not None:
                 temp.next.prev= n

            temp.next=n
    

    def print_list(self):
        temp = self.start
        while temp is not None:
            
            print(temp.item,end=' ') 
            temp = temp.next

    def delete_start(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev= None


    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is  None:
            self.start= None
            
        else:
            temp = self.start
            while temp.next is not None:
                temp= temp.next

            temp.prev.next = None
            
    def delete_item(self,data):
        if self.start is None:

            pass
       
        else:
            temp = self.start
           

            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp .next.prev= temp.prev
                    if temp.prev is not None:
                        temp.prev.next= temp.next
                    else:
                        self.start= temp.next
                    break

                temp= temp.next

    def __iter__(self):
        return DllIterator(self.start)
    
    
class DllIterator:
    def __init__(self,start):
            self.current= start

    def __iter__(self):
            return self
        
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current= self.current.next
        return data


myl= Dll()
myl.add_start(23)
myl.at_last(45)
myl.after_insert(myl.search(23),65)

myl.print_list()
# for x in myl:
#     print(x, end=' ')
print()


myl.delete_item(45)


for x in myl:
    print(x, end=' ')


print()


myl.delete_last()
myl.print_list()


print()