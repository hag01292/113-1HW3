class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1
        self.max_size = size

    def push(self, item):
        if self.isFull():
            print("Stack is full,can't push")
            return
        self.top += 1
        self.stack[self.top] = item
        print(f"Pushed: {item}")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty,can't pop")
            return None
        popped_item = self.stack[self.top]
        self.top -= 1
        print(f"Popped: {popped_item}")
        return popped_item

    def isFull(self):
        return self.top == self.max_size - 1

    def isEmpty(self):
        return self.top == -1

#test
stack = Stack(3)
stack.push('A')
stack.push('B')
stack.push('C')
stack.push('C')
stack.pop()
stack.push('D')
stack.pop()
stack.pop()
stack.pop()
stack.pop()
