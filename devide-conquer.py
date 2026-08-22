def find_max(arr, low, high):
    # Base case: only one element
    if low == high:
        return arr[low]

    # Divide
    mid = (low + high) // 2

    # Conquer
    left_max = find_max(arr, low, mid)
    right_max = find_max(arr, mid + 1, high)

    # Combine
    return max(left_max, right_max)


# Testing
numbers = [12, 45, 67, 23, 89, 34, 11]

print("List:", numbers)
print(
    "Maximum element (using Divide & Conquer):",
    find_max(numbers, 0, len(numbers) - 1)
)
