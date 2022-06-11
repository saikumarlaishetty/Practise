# Queue is a linear data structure
# Queue is opened at both the ends
# insertion - back/tail/rear
# removed - head/front
# Queue follows LILO /FIFO methods
# stack follows - LIFO

# Process of adding is called enqueue
# Process of removing is called dequeue

# Operations of Queue is enqueue and dequeue or isFull or isEmpty
# Queues are used in printing documents

# Implementation of Queue 1) List 2) modules

# 1) lists
# enqueue - append
# dequeue - pop  # this we need to remove from other end so we mention the index
# like list.pop(0)

queue = []
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)

queue.pop(0)   # if queue.pop() it is stack here we are giving index hence it is queue
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)

# To see the queue model of LILO
queue = []
queue.insert(0,10)
queue.insert(0,20)
queue.insert(0,30)
print(queue)

queue.pop()
print(queue)
queue.pop()
print(queue)
queue.pop()
print(queue)

# To check if queue is empty
queue = []
print(not queue)

queue.append(10)
queue.append(20)
queue.append(30)
print(queue[-1])

# Complete implementation of Queue
queue = []
def enqueue():
    element = input("Enter the element")
    queue.append(element)
    print(element,"is added to queue!")

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        e = queue.pop(0)
        print("removed element:",e)

def display():
    print(queue)


while True:
    print("Select the operation 1.add 2.remove 3.show 4.quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter the correct operation")

