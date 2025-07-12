MAX = 5
queue = [None] * MAX
front = -1
rear = -1

def enqueue(val):
    global front, rear
    if rear == MAX - 1:
        print("Queue Overflow")
    else:
        if front == -1:
            front = 0
        rear += 1
        queue[rear] = val

def dequeue():
    global front, rear
    if front == -1 or front > rear:
        print("Queue Underflow")
    else:
        print(f"Dequeued element: {queue[front]}")
        front += 1

def display():
    global front, rear
    if front == -1 or front > rear:
        print("Queue is empty")
    else:
        print("Queue elements:", end=' ')
        for i in range(front, rear + 1):
            print(queue[i], end=' ')
        print()


enqueue(10)
enqueue(20)
enqueue(30)
display()
dequeue()
display()
