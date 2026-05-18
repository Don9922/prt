borrow_counts = {'Alice': 5, 'Bob': 3, 'Charlie': 8, 'Diana': 2, 'Eve': 7}
books = {'Python Basics': 12, 'Data Structures': 8, 'Algorithms': 15, 'ML Guide': 5}
avg = sum(borrow_counts.values()) / len(borrow_counts)
print(f"Average books borrowed: {avg:.2f}")
max_book = max(books, key=books.get)
min_book = min(books, key=books.get)
print(f"Most borrowed book : {max_book} ({books[max_book]} times)")
print(f"Least borrowed book: {min_book} ({books[min_book]} times)")
