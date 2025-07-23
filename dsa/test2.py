class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Dll:
    def __init__(self, head=None):
        self.head = head
        

    def at_start(self, data):
        self.head = self._insert_a_node(data, None, self.head)

    def at_end(self, val):
        cur = self.head
        while cur and cur.next:
            cur = cur.next

        l1 = cur
        self._insert_a_node(val, l1, None)

    def insert(self, tar, val):
        curr = self.head
        while curr:
            if curr.val == tar:
                self._insert_a_node(val, l1=curr, l2=curr.next)
            curr = curr.next

    def inser_after(self, tar, val):
        curr = self.head
        while curr:
            if curr.val == tar:
                self._insert_a_node(val,curr,curr.next)
            curr = curr.next

    def inser_before(self, tar, val):
        curr = self.head
        while curr:
            if  curr.val==tar:
                self._insert_a_node(val, curr.prev, curr)
            curr = curr.next


    def _insert_a_node(self, val, l1, l2):
        temp = Node(val)
        temp.next = l2
        temp.prev = l1

        if l1:
            l1.next = temp
        else:
            self.head = temp

        if l2:
            l2.prev = temp
        return temp
    

    def print1(self):
        curr = self.head
        while curr:
            print(curr.val,end='<--->')
            curr = curr.next
        print(" ")


s = Dll()

s.at_start(23)
s.at_start(4)
s.at_start(244)
s.at_start(33)
s.at_start(4)
s.at_start(33)
s.at_start(65)
s.at_start(33)
s.at_start(45)
s.at_start(222)

s.print1()

               

s.inser_before(4 ,2)



s.print1()
print("chnage")

s.inser_after(33,1111)
s.print1()