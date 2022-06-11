import sys
# prepared the input file
f1 = open("data.txt", "w")
f1.write("25\n")
f1.write("30\n")
f1.close()
# we have re-directed input, output & error
sys.stdin  = open("data.txt", "r")
sys.stdout = open("out.txt", "w")
sys.stderr = open("err.txt", "w")
num1 = input()
num2 = input()
num1 = int(num1)
num2 = int(num2)
res = num1 + num2
print("Result = ",res)
res = int(num1) + str(num2)
