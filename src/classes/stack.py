class Stack:
    def __init__(self):
        self.elements = []

    def push(self, elem):
        self.elements.insert(0, elem)

    def pop(self):
        return self.elements.pop(0)

    def look_top(self):
        return self.elements[0]

    def is_blank(self):
        return self.elements == []
