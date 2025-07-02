# class Node():
#     def __init__(self,prev= None, val=None,next=None):
#         self.prev= prev
#         self.val= val
#         self.next= next


# class Dll():
#     def __init__(self,head = None):
#           self.head= head

#     def at_start(self,data):
#         temp= Node(data)
        

    
#         if self.head is not None:
#             l1= self.head
           
#             temp.next = l1
            
#             l1.prev = temp
#             l1= temp
            
            

#         else:
#             self.head = temp
          


  

#     def insert_after(self, data):
#         curr = self.head

#         count = 0
#         while curr:
#             count += 1
#             curr = curr.next

#         midnodeindex = count // 2
#         curr = self.head
#         for i in range(midnodeindex):
#             curr = curr.next
#         l1 = curr
#         l2 = curr.next
#         temp = Node(val=data)
#         temp.next = l2

#         temp.prev = l1
#         l1.next= temp
#         l2.prev= temp


#     def at_end(self,data):

#         temp= Node(data)
#         l1= self.head
        
#         while l1.next:
#             l1= l1.next

          
#         l1.next= temp
#         temp.prev = l1



# #####################################

# class Node():
#     def __init__(self,val= None,next=None):
#         self.val= val
#         self.next= next

# class Sll():
#     def __init__(self,head= None):
#         self.head = head

#     def at_start(self,data):
#         temp = Node(data)
#         l1= self.head
          
#         temp.next = l1
#         l1= temp
            
            
#     def at_end(self,data):
#         temp= Node(data)
#         l1=self.head
#         while l1.next:
#             l1= l1.next

#         l1.next= temp


#     def at_mid(self,data):
#         curr=self.head
#         count= 0
#         while curr:
#             count+=1
#             curr=curr.next

#         midnodeindex= count//2

#         curr= self.head

#         for _ in range(midnodeindex):
#             curr= curr.next

#         temp = Node(data)
#         # l1= self.curr
#         temp.next =curr.next
#         curr.next= temp






class Node:
    def __init__(self,val= None,next=None):
        self.val= val
        self.next= next

class Sll():
    def __init__(self,head= None):
        self.head = head

    def at_start(self,data):
        self.head = self._insert_a_node(data, None, self.head)

        # temp = Node(data)
        # temp.next = self.head
        # self.head = temp

    def at_end(self, val):
        # get las
        cur = self.head
        while cur and cur.next:
            cur = cur.next

        l1 = cur
        self._insert_a_node(val, l1,  None)
 
    def insert(self,tar, val):
        curr= self.head
        while curr: 
            if curr.val==tar:
                self._insert_a_node(val, l1=curr,l2=curr.next)
            curr= curr.next

    def inser_after(self,tar, val):
        curr= self.head
      
        while curr: 
            if curr.val==tar:
                # self._insert_a_node(val, l1=curr,l2=curr.next)

                temp =Node(val)

                l1= curr
                l2= curr.next            

                temp.next= l2
                l1.next = temp

                # point farword
                curr = temp
            curr= curr.next

            
    def _insert_a_node(self, val, l1, l2):
        # step 1
        temp = Node(val)
        # step 2:
        temp.next = l2

        # step 3:
        if l1:
            l1.next = temp

        return temp


    def print1(self):
        curr= self.head 
        while curr:
            print(curr.val, end='->')
            curr= curr.next
        print("")


s= Sll()

s.at_start(23)
s.at_start(4)

s.at_start(244)
s.at_start(33)
s.at_start(4)
s.at_start(255)
s.print1()

s.inser_after(4,3)


s.print1()

# s.insert(4,23)
# print(s.insert(4,3))



            
