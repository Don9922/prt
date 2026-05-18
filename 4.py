account_ids = sorted([1021, 2045, 3078, 4012, 5099, 6034, 7088])
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
target = int(input("Enter account ID to search: "))
result = binary_search(account_ids, target)
if result != -1:
    print(f"Account ID {target} found at index {result}.")
else:
    print(f"Account ID {target} not found.")

