class Node:
    def __init__(self, roll, name, marks):
        self.roll, self.name, self.marks = roll, name, marks
        self.next = None
class StudentList:
    def __init__(self): self.head = None
    def add(self, roll, name, marks):
        self.head = Node(roll, name, marks) if not self.head else self._append(Node(roll, name, marks))
    def _append(self, node):
        cur = self.head
        while cur.next: cur = cur.next
        cur.next = node; return self.head
    def delete(self, roll):
        cur, prev = self.head, None
        while cur:
            if cur.roll == roll:
                if prev: prev.next = cur.next
                else: self.head = cur.next
                print(f"Deleted roll {roll}"); return
            prev, cur = cur, cur.next
        print("Not found")
    def search(self, roll):
        cur = self.head
        while cur:
            if cur.roll == roll: print(f"Found: {cur.roll} {cur.name} {cur.marks}"); return
            cur = cur.next
        print("Not found")
    def update(self, roll, name, marks):
        cur = self.head
        while cur:
            if cur.roll == roll: cur.name, cur.marks = name, marks; print("Updated"); return
            cur = cur.next
        print("Not found")
    def display(self):
        cur = self.head
        while cur: print(f"{cur.roll} | {cur.name} | {cur.marks}"); cur = cur.next
sl = StudentList()
sl.add(1, "Alice", 88); sl.add(2, "Bob", 76); sl.add(3, "Charlie", 92)
sl.display(); sl.search(2); sl.update(2, "Bobby", 80); sl.delete(1); sl.display()