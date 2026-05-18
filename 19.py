class Node:
    def __init__(self, city, pop):
        self.city, self.pop, self.left, self.right = city, pop, None, None
class CityBST:
    def __init__(self): self.root = None
    def insert(self, city, pop):
        def _ins(node):
            if not node: return Node(city, pop)
            if city < node.city: node.left = _ins(node.left)
            elif city > node.city: node.right = _ins(node.right)
            else: node.pop = pop
            return node
        self.root = _ins(self.root)
    def delete(self, city):
        def _del(node):
            if not node: return None
            if city < node.city: node.left = _del(node.left)
            elif city > node.city: node.right = _del(node.right)
            else:
                if not node.left: return node.right
                if not node.right: return node.left
                cur = node.right
                while cur.left: cur = cur.left
                node.city, node.pop = cur.city, cur.pop
                node.right = _del(node.right)
            return node
        self.root = _del(self.root)
    def update(self, city, pop):
        cur = self.root
        while cur:
            if city == cur.city: cur.pop = pop; print(f"Updated {city}"); return
            cur = cur.left if city < cur.city else cur.right
        print("City not found")
    def display_asc(self, node='start'):
        if node == 'start': node = self.root
        if node:
            self.display_asc(node.left)
            print(f"  {node.city}: {node.pop}")
            self.display_asc(node.right)
    def display_desc(self, node='start'):
        if node == 'start': node = self.root
        if node:
            self.display_desc(node.right)
            print(f"  {node.city}: {node.pop}")
            self.display_desc(node.left)
    def search(self, city):
        cur, comps = self.root, 0
        while cur:
            comps += 1
            if city == cur.city:
                print(f"Found '{city}' in {comps} comparisons")
                return
            cur = cur.left if city < cur.city else cur.right
        print(f"'{city}' not found after {comps} comparisons")
bst = CityBST()
for city, pop in [("Mumbai",20),("Delhi",18),("Pune",5),("Nashik",2),("Nagpur",3)]:
    bst.insert(city, pop)
print("Ascending order:")
bst.display_asc()
print("Descending order:")
bst.display_desc()
bst.update("Pune", 6)
bst.delete("Delhi")
print("After update & delete (Ascending):")
bst.display_asc()
bst.search("Nashik")
bst.search("Delhi"