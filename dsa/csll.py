class Node:
    def __init__(self,item= None,next= None):
        self.item= item
        self.next= next


class CSLL:
    def __init__(self, tail= None):
        self.tail= tail


    def is_empty(self):
        return self.tail is None
    

    def insert_start(self,data):
        n= Node(data)

        if not self.is_empty():
            n.next=self.tail.next 
            next.temp.next= n 
            while self.next is not None:
                self.temp = n 
                n = self .next 
                if self.next.next == self.start:
                    n = self.item 
                    self.start.next = n 
                self.next.next = self.next

            self.next.item= n 
        
        
    def insert_at_end(self, temp,data  ):
        self.temp = temp 
        n = Node (data)
        if not  self.is_empty():
            self.start.next = n 
            self.item = n.next
            while self.next== n.next:
                n= self.start.next
                self.start= n

    def inser_after(self,data):
        temp = Node(data)
        if not self.is_empty():
            
            self.start.next = temp.next
            temp.next= temp

        elif self.start is not None:
            if self.start.next == data:
                self.start.next.next= temp
                temp.next= self.start
            temp.next = next
        else :
            self.temp.next = temp


    def search(self,data):
        if self.is_empty():
            return "cll is empty"

        if self.start == data:
            return data
        else:
            print("data not found is cll")   


    def  delete_at_start(self):
        if not self.is_empty():
            self.start = self.start.next
            
        else:
            self.start=self.start.next

    
    def delete_at_end(self):
        if not self.start.next== self.start.next:
            self.start.item = self.start
            self.start.item = self.start.next
            self.start = self.next
        elif self.start==self.start.next:
            self.start.next 