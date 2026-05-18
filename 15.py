SIZE = 10
table = [None] * SIZE
def h(key): return key % SIZE
def insert(key):
    idx = h(key)
    for _ in range(SIZE):
        if table[idx] is None or table[idx] == "DELETED":
            table[idx] = key; print(f"Inserted {key} at index {idx}"); return
        idx = (idx + 1) % SIZE
    print("Table full")
def search(key):
    idx = h(key)
    for _ in range(SIZE):
        if table[idx] is None: print("Not found"); return
        if table[idx] == key: print(f"Found {key} at index {idx}"); return
        idx = (idx + 1) % SIZE
    print("Not found")
def delete(key):
    idx = h(key)
    for _ in range(SIZE):
        if table[idx] is None: print("Not found"); return
        if table[idx] == key: table[idx] = "DELETED"; print(f"Deleted {key}"); return
        idx = (idx + 1) % SIZE
def display(): print("Table:", table)
insert(12); insert(22); insert(32); insert(5); insert(15)
display(); search(22); delete(22); display()