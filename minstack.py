class MinStack:

    def __init__(self):
        self.s=[]
        self.mins=[]

        
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.mins:
           
            # bascallyu dono value ko caompre kiye then minimum ko add kr diya
            val =min(val, self.mins[-1])

        self.mins.append(val)

        

    def pop(self) -> None:

        self.s.pop()
        self.mins.pop()


    def top(self) -> int:
        return self.s[-1]

        
        

    def getMin(self) -> int:
        return self.mins[-1]
        
