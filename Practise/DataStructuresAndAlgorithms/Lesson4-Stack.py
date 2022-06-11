# LIFO or FIFO
# Basic operations on stack are Push,  pop , peap or top , isempty

# push and pop operations are most important one

# implementation of stack in python

# Stacks can be implemented using lists or modules

# 1) LIST
#  push --> append
#  pop  --> pop

stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

stack.pop()
stack.pop()
stack.pop()
print(stack)

# To check stack is empty or not
stack = []
print(len(stack) == 0)
print(not stack)


# A complete example of stack

stack = []
def push():
    element = input("Enter the element:")
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e = stack.pop()
        print("removed element:", e)
        print(stack)


while True:
    print("Select the operation 1.push 2.pop 3.quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct operation")



# Example 2 - where you set the limit of a stack

stack = []
def push():
    if len(stack)==n:
        print("list is full")
    else:
        element = input("Enter the element:")
        stack.append(element)
        print(stack)

def pop_element():
    if not stack:
        print("Stack is empty!")
    else:
        e = stack.pop()
        print("removed element:", e)
        print(stack)


n = int(input("Limit of stack:"))
while True:
    print("Select the operation 1.push 2.pop 3.quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct operation")

