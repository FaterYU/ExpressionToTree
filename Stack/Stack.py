class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def top(self):
        if(self.size() == 0):
            return None
        else:
            return self.items[-1]

    def pop(self):
        top = self.items[-1]
        self.items.pop()
        return top

    def size(self):
        return len(self.items)