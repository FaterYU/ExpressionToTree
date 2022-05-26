class Stack:
    # init a list to store the elements
    def __init__(self):
        self.items = []
    # push an element to the top of the stack
    def push(self, item):
        self.items.append(item)
    # return the top element of the stack
    def top(self):
        if(self.size() == 0):
            return None
        else:
            return self.items[-1]
    # pop the top element of the stack
    def pop(self):
        top = self.items[-1]
        self.items.pop()
        return top
    # return the size of the stack
    def size(self):
        return len(self.items)