SIZE = 10
table = [[] for _ in range(SIZE)]
def h(key): return key % SIZE
def insert(key, val):
    bucket = table[h(key)]
    for i, (k, v) in enumerate(bucket):
        if k == key: bucket[i] = (key, val); return
    bucket.append((key, val))
def search(key):
    for k, v in table[h(key)]:
        if k == key: print(f"Found: key={key}, value={v}"); return
    print(f"Key {key} not found")
def delete(key):
    bucket = table[h(key)]
    for i, (k, v) in enumerate(bucket):
        if k == key: bucket.pop(i); print(f"Deleted key {key}"); return
    print(f"Key {key} not found")
def display():
    for i, bucket in enumerate(table):
        if bucket: print(f"  [{i}] -> {bucket}")
insert(12, "Alice"); insert(22, "Bob"); insert(32, "Charlie"); insert(5, "Diana")
print("Hash Table:"); display()
search(22); delete(22); display()