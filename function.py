#syntex
def hello_world():
    print("hello world")

hello_world()

#function reusable
#function moduler
#function can take perameter as input
#function can return value

#parameter and argument

def add(a,b):
    print(a+b)

add(10,20)


def square(num):
    return num*num

print(square(10))

#default parameter
def greet(name="noushad"):
    print(f"hello {name}") 

greet()
greet("shadman")


 # keyword argument
def student_info(name,age,grade): 
    print(f"hello {name} your age is {age} your grade: {grade}" )

student_info(name="shadman",age=20,grade="A")
student_info(grade="A",name="alif",age=20)

#variable length argument
#when we dont know how many arguments we will pass to the function then we can use *args

def sum(*args):
    total=0
    for num in args:
        total+=num
    return total

print(sum(10,20,30,40,50))
print(sum(10,20,30))

#recursive function
#the function which calls itself is called recursive function

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1) #recursive call
print(factorial(5))

#questions

# 1. Write a function to calculate the sum 
def add(a,b):
    return a+b
print(add(10,20))

#2.check prime number

def is_prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

print(is_prime(10))
   
#recursive factorial

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

#write a function which prints name and city ,take city="dhaka" as a default parameter

def print_name(name,city="dhaka"):
    print(f"hello {name} your city is {city}")
print_name("shadman")
print_name("alif","chittagong")
