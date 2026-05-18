salaries = [55000.0, 72000.5, 48000.0, 91000.0, 63000.0,
            85000.5, 39000.0, 77000.0, 52000.0, 68000.0]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
bubble_sort(salaries)
print("Sorted Salaries:", salaries)
print("Top 5 Highest Salaries:", salaries[-5:][::-1])