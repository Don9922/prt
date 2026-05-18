borrow_counts = {'Alice': 5, 'Bob': 0, 'Charlie': 8, 'Diana': 0, 'Eve': 7, 'Frank': 5}
zero_members = [m for m, c in borrow_counts.items() if c == 0]
print(f"Members with no borrowings: {len(zero_members)} -> {zero_members}")
from collections import Counter
counts = list(borrow_counts.values())
mode_val = Counter(counts).most_common(1)[0][0]
mode_members = [m for m, c in borrow_counts.items() if c == mode_val]
print(f"Most frequent borrow count (mode): {mode_val} -> {mode_members}")