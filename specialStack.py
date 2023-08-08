class SpecialStack:
    def __init__(self):
        self.min_stack = []
        self.stack = []

    def min(self):
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        else:
            return -1
        
    def push(self, number):
        self.stack.append(number)
        if len(self.min_stack) == 0 or number < self.min_stack[-1]:
            self.min_stack.append(number)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        
        return self.stack.pop()
    

