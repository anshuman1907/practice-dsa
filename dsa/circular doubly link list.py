class Node():
    def __init__(self,prev= None, item= None,next= None):
        self.prev= prev
        self.item= item 
        self.next = next


class Cdll():
    def __init__(self,head = None):
        self.head = head

    def at_insert(self,data):
        n = Node(data)


        n.next = Node(data)


        
         