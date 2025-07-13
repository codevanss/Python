MAX = 5
stack = []
top = -1

def push(val):
    global top
    if top == MAX - 1:
        print("Stack Overflow")
    else:
        stack.append(val)
        top += 1

def pop():
    global top
    if top == -1:
        print("Stack Underflow")
    else:
        print(f"Popped element: {stack[top]}")
        stack.pop()
        top -= 1

def display():
    if top == -1:
        print("Stack is empty")
    else:
        print("Stack elements:", end=' ')
        for i in range(top + 1):
            print(stack[i], end=' ')
        print()

push(10)
push(20)
push(30)
display()
pop()
display()
