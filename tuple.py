# immutable

fruits=("Appple","Banana","Cherry")
num=(1,2,3)

#tuple ordered
#tupple immutable
#every item in tupple is in indexing order which start from 0
#double item is accepted in tupple

fruits=("Appple","Banana","Apple")
print(fruits)

#tuple creating and indexing
fruits=("apple","banana","cherry")
print(fruits[0])
print(fruits[-1])

#try to add item in tupple

# fruits[0]="grape" this will give error because tupple is immutable

#tuple slicing
numbers=(1,2,3,4,5,6,7,8,9)
print(numbers[2:5]) 
print(numbers[:5])
print(numbers[1:])
print(numbers[::2])
print(numbers[::-1])

#tuple operations
#concatination
# num1=(1,2,3)
# num2=(4,5,6)
# num3=num1+num2
# print(num3)

#repetition
# num1=(1,2,3)
# print(num1*2)

#check item in tupple
numbers=(1,2,3,4,5,6,7,6,7,4,21,6,6,6,8,9)
print(2 in numbers)
print(len(numbers))

#methods
#count
print(numbers.count(6))
#index
print(numbers.index(21))

#tuple unpacking
numbers=(1,2,3,4,5)
a,b,c,d,e=numbers
print(a)

#question
#print something from a tuple
fruits=("apple","banana","cherry")
print(fruits[0])

#numbers=(1,2,3,4,5,6,7,8,9) ,output=(3,4,5)

numbers=(1,2,3,4,5,6,7,8,9)
print(numbers[2:5])

#given number is 3,4 ,assign the items of the variable to a tuple

numbers=(3,4)
x,y=numbers
print(f"x={x},y={y}")

#count tuple items
items=(1,2,3,4,5,6,7,8,9)
print(items.count(3))
