class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

print('#1-------------------')
stack = Stack()

# 最初は空なのでTrue
print(stack.is_empty())

# 要素追加するとFalse
stack.push(1)
print(stack.is_empty())

# POPすると再びTrue
item = stack.pop()
print(item)
print(stack.is_empty())

for i in range(0, 6):
    stack.push(i)

print(stack.peek())
print(stack.size())


print('#2-------------------')
stack2 = Stack()

normal_s = input('文字を入力してください')

for c in normal_s:
    stack2.push(c)

reverse = ''

while stack2.size():
    reverse += str(stack2.pop())

print(reverse)



# 練習問題
s = Stack()

nl = [1, 2, 3, 4, 5]

for c in nl:
    s.push(c)

rl= []

while s.size():
    rl.append(s.pop())

print(rl)
