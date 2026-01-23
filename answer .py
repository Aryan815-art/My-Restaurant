# 1
i =int(input("enter number :- "))

for i in range(6):
    print(i)

# 2
n=int(input("enter number:- "))

for i in range(2, n+1,2):
    print(i, end=" ")
    
# 3
n=int(input("enter number :-"))
total= 0

for i in range(1, n+1):
    total += 1

print("sum =",total)

# 4 multiplication table

n=int(input("enter number :-"))

for i in range(1, 11):
    print(f"{n} * {i} = {n *i}")
print("_"*21)

# 5 factorial using loop
# for
n=7
fact =1 
for i in range (1, n+1):
    fact *=i

print("Factorial =", fact)
print("_"*21)

# while
num=int(input("enter num:-"))

fact =1
i= 1

while i <= num:
    fact*=i
    i +=1
print("Factorial =", fact)

# 6 Reverse
n = int(input("Enter number: "))
rev = 0

while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10

print("Reversed =", rev)
print("_" *21)

# 7 prime
n=10

if n <=1:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, int(n** 0.5)+1 ):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

# 8.fibonaccie serice
# for
i = 7
a= 0
b=1

for i in range(i):
    print(a, end=" ")
    a, b=b, a+b

# while
n=int(input("enter number :-"))
a,b=0,1
i =1
while i< n :
    print(a, end=" ")
    a, b=b ,a +b
    i += 1

# 9.pattern priting

n= 6
for i in range(1, n+1):
    print("*"*i)
    
# 10.Number guessing game
number = 7

while True :
    guesse = int(input("enter number:- "))

    if guesse == number:
        print("you are coreect")
        break
    else :
        print("you are wrong")
        print("how many days in week ")
    