class MinStack:

    def __init__(self):
        self.arr = []
        self.minarr = []
        self.len = 0


    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.minarr) == 0:
            self.minarr.append(val)
        else:
            self.minarr.append(min(self.getMin(), val))
        self.len +=1 

    def pop(self) -> None:
        self.arr.pop()
        self.minarr.pop()
        self.len -= 1

    def top(self) -> int:
        return self.arr[self.len -1]

    def getMin(self) -> int:
        return self.minarr[self.len-1]
