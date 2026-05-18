salaries = [55000.0, 72000.5, 48000.0, 91000.0, 63000.0,
            85000.5, 39000.0, 77000.0, 52000.0, 68000.0]
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
selection_sort(salaries)
print("Sorted Salaries:", salaries)
print("Top 5 Highest Salaries:", salaries[-5:][::-1])