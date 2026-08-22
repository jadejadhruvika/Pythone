# Pattern 1
for i in range(1, 6):
    print(str(i) * i)

# Pattern 2 (Alphabets)
for i in range(5):
    for j in range(i+1):
        print(chr(65+j), end=" ")
print()

# Star Pattern
for i in range(5, 0, -1):
 print('*' * i)
