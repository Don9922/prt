undo_stack = []
redo_stack = []
document = ""
def make_change(new_text):
    global document
    undo_stack.append(document)
    redo_stack.clear()
    document = new_text
    print(f"Document: '{document}'")
def undo():
    global document
    if undo_stack:
        redo_stack.append(document)
        document = undo_stack.pop()
        print(f"Undo -> Document: '{document}'")
    else:
        print("Nothing to undo.")
def redo():
    global document
    if redo_stack:
        undo_stack.append(document)
        document = redo_stack.pop()
        print(f"Redo -> Document: '{document}'")
    else:
        print("Nothing to redo.")
make_change("Hello")
make_change("Hello World")
make_change("Hello World!")
undo()
undo()
redo()