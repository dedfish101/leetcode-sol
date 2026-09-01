class MinStack:

    def __init__(self):
        from collections import deque
        self.minstack = deque()
        self.mainstack = deque()
        
        
        

        

    def push(self, value: int) -> None:
        
        if not self.mainstack:
            self.mainstack.append(value)
            self.minstack.append(value)
        else:
            minval = self.getMin()
            self.mainstack.append(value)
            if value <= minval:
                self.minstack.append(value)
            
        

    def pop(self) -> None:
        
        if not self.mainstack:
            return False 
        
        else:
            minval = self.getMin()
            popped_val = self.mainstack.pop()
        
            if popped_val == minval:
                self.minstack.pop()

        

    def top(self) -> int:
        self.topmain = self.mainstack[-1]
        return self.topmain
        

    def getMin(self) -> int:
        self.topmin = self.minstack[-1]
        return self.topmin
        


# Your self.minstack object will be instantiated and called as such:
# obj = self.minstack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
