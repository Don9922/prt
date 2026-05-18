from collections import deque
queue = deque()
def enqueue(val):
    queue.append(val)
    print(f"Enqueued: {val}")
def dequeue():
    if queue:
        print(f"Dequeued: {queue.popleft()}")
    else:
        print("Queue is empty!")
def display():
    print("Queue (front->rear):", list(queue) if queue else "Empty")
while True:
    print("\n1.Enqueue  2.Dequeue  3.Display  4.Exit")
    ch = input("Choice: ")
    if ch == '1':   enqueue(input("Enter value: "))
    elif ch == '2': dequeue()
    elif ch == '3': display()
    elif ch == '4': break
    else: print("Invalid choice")