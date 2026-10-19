# Day 25: Linked List Basics - Python Placement 60 Days
# Author: GIRIMAHENDRAPPA

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # O(1) - Insert at beginning
    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted at begin: {data}")
    
    # O(n) - Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(f"Inserted at end: {data}")
    
    # O(n) - Display
    def display(self):
        if not self.head:
            print("List Empty")
            return
        temp = self.head
        while temp:
            print(f"{temp.data} -> ", end="")
            temp = temp.next
        print("None")
    
    # O(n) - Delete by value
    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            print(f"Deleted: {key}")
            return
        
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        
        if not temp:
            print(f"{key} not found")
            return
        
        prev.next = temp.next
        print(f"Deleted: {key}")
    
    # O(n) - Length
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    # O(n) - Search
    def search(self, key):
        temp = self.head
        pos = 0
        while temp:
            if temp.data == key:
                return f"Found {key} at position {pos}"
            temp = temp.next
            pos += 1
        return f"{key} not found"

# ================= TESTING =================
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_begin(5)
    
    print("\nLinked List:")
    ll.display()
    print("Length:", ll.length())
    print(ll.search(20))
    
    ll.delete(20)
    print("\nAfter Deletion:")
    ll.display()
    
    # ============ INTERVIEW QUICK REVISION ============
    # Q1: Array vs Linked List?
    # Array: Contiguous memory, O(1) access, fixed size
    # Linked List: Non-contiguous, O(n) access, dynamic size, O(1) insert/delete at head
    
    # Q2: Types?
    # Singly, Doubly, Circular
    
    # Q3: Why head = None in init?
    # Empty list at start

# ============ MOST ASKED - REVERSE LINKED LIST ============
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev