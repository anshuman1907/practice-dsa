class Node():
    def __init__(self,prev= None, val=None,next=None):
        self.prev= prev
        self.val= val
        self.next= next


class Dll():
    def __init__(self,head = None):
          self.head= head

    def at_start(self,data):
        temp= Node(data)
        

    
        if self.head is not None:
            l1= self.head
           
            temp.next = l1
            
            l1.prev = temp
            l1= temp
            
            

        else:
            self.head = temp
          


  

    def insert_after(self, data):
        curr = self.head

        count = 0
        while curr:
            count += 1
            curr = curr.next

        midnodeindex = count // 2
        curr = self.head
        for i in range(midnodeindex):
            curr = curr.next
        l1 = curr
        l2 = curr.next
        temp = Node(val=data)
        temp.next = l2

        temp.prev = l1
        l1.next= temp
        l2.prev= temp


    def at_end(self,data):

        temp= Node(data)
        l1= self.head
        
        while l1.next:
            l1= l1.next

          
        l1.next= temp
        temp.prev = l1



#####################################

class Node():
    def __init__(self,val= None,next=None):
        self.val= val
        self.next= next

class Sll():
    def __init__(self,head= None):
        self.head = head

    def at_start(self,data):
        temp = Node(data)
        l1= self.head
          
        temp.next = l1
        l1= temp
            
            
    def at_end(self,data):
        temp= Node(data)
        l1=self.head
        while l1.next:
            l1= l1.next

        l1.next= temp


    def at_mid(self,data):
        curr=self.head
        count= 0
        while curr:
            count+=1
            curr=curr.next

        midnodeindex= count//2

        curr= self.head

        for _ in range(midnodeindex):
            curr= curr.next

        temp = Node(data)
        # l1= self.curr
        temp.next =curr.next
        curr.next= temp