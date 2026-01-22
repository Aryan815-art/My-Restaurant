# for loop 
i = int(input("enter number:- "))
 
for i in range(i):
    print(i ,end=" ")

# even
for i in range(2,7,5):
    print(i)

# break
for i in range(1,10):
    if i == 5:
        break
    print(i)

# continue
for i in range(1,10):
    if i ==4:
        continue
    print(i)

# pass
for i in range(1,7):
    if i ==4:
        pass
    print(i)

# list 
fruits = [
    "apple","banana","cherry",1,2,3.5,True
    ]
for fruit in fruits:
    print(fruit)
# add
my_list = [1, 2, 3]

for i in range(4, 7):
    my_list.append(i)

print(my_list)


tuple
colors = ("red", "green", "blue")

for color in colors:
    print(color)

# Error
# my_tuple = (1, 2, 3)

# for i in range(len(my_tuple)):
#     my_tuple[i] = my_tuple[i] * 2   

# Count characters in a string
name = "aryan"
count = 0
for ch in name:
    count +=1
print("Length",count)

# loop over string
for letter in "Aryan":
    print(letter)

# fibonacci series
i = int(input("enter number:-"))

a=0
b=1

for i in range(i):
    print(a, end="")
    a, b=b , a+b

# table
num = int(input("number:- "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i} ")

enumerate
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# nested for loop
for i in range(3):
    for j in range(2):
        print(i,j)

# factorial for loop
num =5
factorial =1
for i in range(1, num+1):
    factorial *= i
    print(factorial)
print(f"the factorial of {num} is {factorial}")

# factorail using function and for loop

def function_factoridal(n):
    reslut =1
    for i in range(1, n+1):
        reslut *= i
    return reslut
num = int(input("enter number:-  "))
print("factorail =", function_factoridal(num))

# sum number ++

def sum_numbers(numbers):
    total =0
    for num in numbers :
        total +=num
    return total
result =sum_numbers([12,13,14,13])
print(result)

# add, subtraction,multipliction division 

a = int(input("enter number:- "))
b = int(input("enter number:- "))

operations = ["+", "-", "*", "/"]

for op in operations:
    if op == "+":
        print("Addition:", a + b)

    elif op == "-":
        print("Subtraction:", a - b)

    elif op == "*":
        print("Multiplication:", a * b)

    elif op == "/":
        if b != 0:
            print("Division:", a / b)
        else:
            print("-- cannot divide by zero --")

# for 
def check_apples(apples):
    for apple in apples:
        print("checking", apple)

check_apples(["red apple","green apple","yellow apple"])

list= [
    "aryan","meet","neet"
]

print(list)