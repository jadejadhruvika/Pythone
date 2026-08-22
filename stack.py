# Stack using List

class Stack:
    def __init__(self):
        self.stack = []

    # Push operation
    def push(self, item):
        self.stack.append(item)
        print(item, "pushed into stack")

    # Pop operation
    def pop(self):
        if len(self.stack) == 0:
            return "Stack is Empty"
        return self.stack.pop()

    # Peek operation
    def peek(self):
        if len(self.stack) == 0:
            return "Stack is Empty"
        return self.stack[-1]

    # Check if stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # Size of stack
    def size(self):
        return len(self.stack)

    # Display stack
    def display(self):
        print("Stack:", self.stack)


# Driver Program
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Top Element:", s.peek())

print("Popped Element:", s.pop())

s.display()

print("Stack Size:", s.size())

print("Is Stack Empty?", s.isEmpty())
