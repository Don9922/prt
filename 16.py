class Bucket:
    def __init__(self, depth, size=3):
        self.depth, self.size = depth, size
        self.keys = []
    def is_full(self): return len(self.keys) >= self.size
class ExtendibleHash:
    def __init__(self):
        self.global_depth = 1
        self.buckets = [Bucket(1), Bucket(1)]
        self.directory = [0, 1]
    def _hash(self, key): return key % (2 ** self.global_depth)
    def insert(self, key):
        idx = self._hash(key)
        bkt = self.buckets[self.directory[idx]]
        if not bkt.is_full():
            bkt.keys.append(key); print(f"Inserted {key}")
        else:
            self.global_depth += 1
            new_buckets = [Bucket(self.global_depth) for _ in range(2 ** self.global_depth)]
            self.directory = list(range(2 ** self.global_depth))
            self.buckets = new_buckets
            for b in [bkt] + [self.buckets[i] for i in range(len(new_buckets))]:
                for k in getattr(b,'keys',[]):
                    ni = k % (2 ** self.global_depth)
                    self.buckets[ni].keys.append(k)
            self.buckets[key % (2**self.global_depth)].keys.append(key)
            print(f"Split & inserted {key}")
    def search(self, key):
        bkt = self.buckets[self.directory[self._hash(key)]]
        print(f"{'Found' if key in bkt.keys else 'Not found'}: {key}")
    def delete(self, key):
        bkt = self.buckets[self.directory[self._hash(key)]]
        if key in bkt.keys: bkt.keys.remove(key); print(f"Deleted {key}")
        else: print(f"Key {key} not found")
    def display(self):
        for i, bkt in enumerate(self.buckets):
            if bkt.keys: print(f"  Bucket {i}: {bkt.keys}")
eh = ExtendibleHash()
for k in [10, 20, 5, 15, 25, 35]: eh.insert(k)
print("Hash Table:"); eh.display()
eh.search(15); eh.delete(20); eh.display()