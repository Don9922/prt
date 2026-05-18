class Node:
    def __init__(self, roll, name, marks):
        self.roll, self.name, self.marks = roll, name, marks
        self.next = None
class StudentList:
    def __init__(self): self.head = None
    def add(self, roll, name, marks):
        node = Node(roll, name, marks)
        if not self.head: self.head = node; return
        cur = self.head
        while cur.next: cur = cur.next
        cur.next = node
    def sort_desc(self):
        nodes = []
        cur = self.head
        while cur: nodes.append(cur); cur = cur.next
        nodes.sort(key=lambda x: x.marks, reverse=True)
        for i in range(len(nodes)-1): nodes[i].next = nodes[i+1]
        if nodes: nodes[-1].next = None; self.head = nodes[0]
    def display(self):
        cur = self.head
        while cur: print(f"{cur.roll} | {cur.name} | {cur.marks}"); cur = cur.next
sl = StudentList()
sl.add(1,"Alice",88); sl.add(2,"Bob",76); sl.add(3,"Charlie",92); sl.add(4,"Diana",65)
sl.sort_desc()
print("Sorted (Descending):"); sl.display()