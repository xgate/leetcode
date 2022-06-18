class MinStack:

    def __init__(self):
        self.stack = list()
        self.size = 0

    def push(self, val: int) -> None:
        if not self.stack:
            # val, min val
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[self.size-1][1])))
        self.size += 1

    def pop(self) -> None:
        self.stack.pop()
        self.size -= 1

    def top(self) -> int:
        return self.stack[self.size-1][0]

    def getMin(self) -> int:
        return self.stack[self.size-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
