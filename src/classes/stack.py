class Stack:
    def __init__(self):
        self.items = []

    def is_blank(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def look_top(self):
        return self.items[0]
