# while simple
i =0
while i<10:
    print(i )
    i += 1

# # infinite loop with break 
while True:
    print("hello world")
    break

# # list 
fruits = ["apple", "banana", "cherry"]
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1
# # append 
numbers = []
i = 1

while i <= 5:
    numbers.append(i)
    i += 1

print(numbers)

# even
i =2
while i<=20:
    print(i)
    i +=2


# tuple 
colors = ("red", "green", "blue")
i = 0

while i < len(colors):
    print(colors[i])
    i += 1

# fibonacci series
n =9
a,b = 0,1
i=0
while i< n:
    print(a, end=" ")
    a,b = b, a+b
    i +=1 


# factorial
num =6
factorial =1
i=1
while i <= num:
    factorial *= i
    i +=1
    print(factorial)
print(f"the factorial of {num} is {factorial}")


# factorial using function and while loop
def factorial(n):
    
    result =1
    i =1
    while i<= n:
        result *= i
        i +=1
    return result
num = int(input("enter number:- "))
print(f"the factorial of {num} is {factorial(num)}")

# password validation 
correct_password = input("set your password:- ")
password =""
while password !=correct_password:
    password = input("enter your password:- ")
    print("access granted")

# while else
i = 0
while i <5:
    print(i)
    i +=1
else:
    print("loop ended")


# break in while 
i = 0
while i<0:
    print(i)
    if i ==3:
        break
    i +=1
else:
    print("loop ended")

# contine in while 
i =0
while i <5:
    i +=1
    if i ==3:
        continue
    print(i)
else:
    print("loop ended")

# while True
while True:
    print("hello")
    break

# count 
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Done!")

countdown(2)

# formula

n= int(input("enter number:-"))
total = n*(n+1)//2
print("sum =", total)

# digits in a numbers

num= 9813763
count = 0

while num > 0:
    num //= 10
    count += 1

print("Digits: ", count)

# f.series
n= 9
a,b= 0,1
i=0

while i < n:
    print(a )
    a, b=b, a+b
    i += 1

n =5
total = n*(n+1)//2
print("sum =",total) 

def factorial(n):
    
    result =1
    i =1
    while i<= n:
        result *= i
        i +=1
    return result
num = int(input("enter number:- "))
print(f"the factorial of {num} is {factorial(num)}")

# key while loop
student ={
    "name" :"aryan",
    "age" : 21
}

keys =list(student.keys())
i = 0

while i< len(keys):
    key = keys[i]
    print(key,":",student[key])
    i += 1
