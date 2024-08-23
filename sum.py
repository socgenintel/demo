import sys
def add(num1,num2):
    return num1 + num2

num1=int(sys.argv[1])
num2=int(sys.argv[2])
sum=add(num1,num2)
print("The sum of 2 nos from inputted argument is:", sum)