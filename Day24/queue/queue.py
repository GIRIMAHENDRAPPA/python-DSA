class QueueList:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not self.queue:
            return "Queue Empty"
        return self.queue.pop(0) # O(n) - SLOW!

    def front(self):
        return self.queue[0] if self.queue else None
print("QueueList:")
q = QueueList()
print(q.enqueue(10))
print(q.enqueue(20))
print(q.front())
print(q.dequeue())
print(q.front())
