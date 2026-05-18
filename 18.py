class Node:
    def __init__(self, val): self.val, self.left, self.right = val, None, None
class BST:
    def __init__(self): self.root = None
    def insert(self, val):
        def _ins(node, v):
            if not node: return Node(v)
            if v < node.val: node.left = _ins(node.left, v)
            elif v > node.val: node.right = _ins(node.right, v)
            return node
        self.root = _ins(self.root, val)
    def search(self, val):
        cur = self.root
        while cur:
            if val == cur.val: print(f"Found: {val}"); return
            cur = cur.left if val < cur.val else cur.right
        print(f"Not found: {val}")
    def delete(self, val):
        def _del(node, v):
            if not node: return None
            if v < node.val: node.left = _del(node.left, v)
            elif v > node.val: node.right = _del(node.right, v)
            else:
                if not node.left: return node.right
                if not node.right: return node.left
                cur = node.right
                while cur.left: cur = cur.left
                node.val = cur.val; node.right = _del(node.right, cur.val)
            return node
        self.root = _del(self.root, val)
    def inorder(self, node=None, first=True):
        if first: node = self.root
        if node: self.inorder(node.left, False); print(node.val, end=' '); self.inorder(node.right, False)
bst = BST()
for v in [50, 30, 70, 20, 40, 60, 80]: bst.insert(v)
print("Inorder:"); bst.inorder(); print()
bst.search(40); bst.delete(30); print("After delete 30:"); bst.inorder(); print()