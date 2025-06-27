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
            