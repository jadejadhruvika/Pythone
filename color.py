color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

result = [x for i, x in enumerate(color) if i not in (0, 2, 3, 5)]

print("Original List:", color)
print("New List:", result)

