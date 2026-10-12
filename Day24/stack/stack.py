class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x) # O(1)

    def pop(self):
        if self.is_empty():
            return "Stack Empty"
        return self.stack.pop() # O(1)

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)

s = Stack()
s.push(10); s.push(20); s.push(30)
s.display() # [10, 20, 30]
print(s.pop()) # 30
print(s.peek()) # 20