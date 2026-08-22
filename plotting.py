from pylab import *

# 1. Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

figure()
plot(x, y, marker='o')
title("Line Plot")
xlabel("X-axis")
ylabel("Y-axis")
grid(True)
show()


# 2. Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [25, 40, 30, 55]

figure()
bar(categories, values, color='skyblue')
title("Bar Chart")
xlabel("Categories")
ylabel("Values")
show()


# 3. Pie Chart
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [35, 25, 20, 20]

figure()
pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
title("Pie Chart")
axis('equal')
show()


# 4. Histogram
data = [22, 25, 30, 35, 40, 42, 45, 50, 55, 60, 22, 28, 33]

figure()
hist(data, bins=5, color='green', edgecolor='black')
title("Histogram")
xlabel("Value")
ylabel("Frequency")
show()


# 5. Scatter Plot
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78]

figure()
scatter(x, y, color='red')
title("Scatter Plot")
xlabel("X-axis")
ylabel("Y-axis")
show()
