class MyQueue:

    def __init__(self):
        self.queue=[]

    def push(self, x: int) -> None:
        return self.queue.insert(0,x)

    def pop(self) -> int:
        return self.queue.pop(-1)
        

    def peek(self) -> int:
        return self.queue[-1]        

    def empty(self) -> bool:
        if self.queue:
            return False
        return True
        


