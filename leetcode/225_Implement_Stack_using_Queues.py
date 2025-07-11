class MyStack:

    def __init__(self):
        self.s=[]

    def push(self, x: int) -> None:
        return self.s.append(x)

    def pop(self) -> int:
        return self.s.pop(-1)
        

    def top(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        if self.s:
            return False
        return True

