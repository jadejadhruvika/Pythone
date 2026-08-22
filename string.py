def find_length(data):
    count = 0
    for i in data:
        count += 1
    return count

# List
my_list = [10, 20, 30, 40, 50]
print("Length of List =", find_length(my_list))

# String
my_string = "Python"
print("Length of String =", find_length(my_string))
