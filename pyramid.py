# main
row =int(input("enter row number:- "))

for i in range(1, row+1):
    print("*"*i)

# reverse 
row =int(input("enter row number:- "))
for i in range(row,0,-1):
    print("*"*i)

# even odd
num =(int(input("number:- ")))
if num %2 ==0:
    print("the number in even")
else:
    print("the number odd")

# number
n= 4
for i in range(1, n+1):
    print(""* (n-i),end="")
    for j in range(1, i+1):
        print(j, end="")
    for j in range(i -1,0,-1):
        print(j,end="")
    print()

# 2
row =int(input("number :-"))

for i in range(1, row+1):
    print(" "*(row -i),end="")
    for j in range(1, i+1):
        print("* ",end="")
    print()

# pattern printing

row =5
for i in range(1, row + 1):
    print("*"*i)

# diamond

rows= 5

for i in range(rows ):
    print(" " * (rows - i - 1) + "*" * (2*i +1))

for i in range(rows -2, -1,-1):
    print(" "*(rows -i -1)+ "*" * (2*i +1))