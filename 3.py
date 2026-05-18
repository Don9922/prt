account_ids = [1021, 2045, 3078, 4012, 5099, 6034, 7088]
def linear_search(lst, target):
    for i, val in enumerate(lst):
        if val == target:
            return i
    return -1
target = int(input("Enter account ID to search: "))
result = linear_search(account_ids, target)
if result != -1:
    print(f"Account ID {target} found at index {result}.")
else:
    print(f"Account ID {target} not found.")