from collections import deque
queue = deque()
def add_event(event):
    queue.append(event)
    print(f"Event added: '{event}'")
def process_event():
    if queue:
        print(f"Processing: '{queue.popleft()}'")
    else:
        print("No events to process.")
def display_events():
    print("Pending events:", list(queue) if queue else "None")
def cancel_event(event):
    if event in queue:
        queue.remove(event)
        print(f"Cancelled: '{event}'")
    else:
        print("Event not found.")
add_event("Login")
add_event("Purchase")
add_event("Logout")
display_events()
process_event()
cancel_event("Logout")
display_events()