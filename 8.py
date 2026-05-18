stack = []
def push(val):
    stack.append(val)
    print(f"Pushed: {val}")
def pop():
    if stack:
        print(f"Popped: {stack.pop()}")
    else:
        print("Stack is empty!")
def display():
    print("Stack (top->bottom):", stack[::-1] if stack else "Empty")
while True:
    print("\n1.Push  2.Pop  3.Display  4.Exit")
    ch = input("Choice: ")
    if ch == '1':   push(input("Enter value: "))
    elif ch == '2': pop()
    elif ch == '3': display()
    elif ch == '4': break
    else: print("Invalid choice")