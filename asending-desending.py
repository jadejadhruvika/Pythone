d = {'A': 50, 'B': 10, 'C': 30, 'D': 20}

ascending = dict(sorted(d.items(), key=lambda item: item[1]))
descending = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

print("Ascending:", ascending)
print("Descending:", descending)

