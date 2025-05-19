#if,elif,else

# syntex

if condition:
    code_block
elif condition:
    code_block
else:
    code_block

#if
age=16
if age>=18:
    print("eligible")

#if else
age=16
if age>=18:
    print("eligible")
else:
    print("not eligible")


# if elif else

marks=85
if marks>=90:
    print("A+")
elif marks>=80:
    print("A")
elif marks>=70:
    print("B")
else:
    print("fail")

#using logical operators

# and: দুটি শর্তই সত্য হলে সত্য।
# or: যেকোনো একটি শর্ত সত্য হলে সত্য।
# not: শর্তের উল্টো মান দেয়।

# and_operator

age=19
has_id=True
if age>=18 and has_id:
    print("eligible")
else:
    print("not eligible")

# or_operator
day="friday"

if day=="saturday" or day=="sunday":
    print("holiday")
else:
    print("not holiday")

# not_operator
age=19
if not age>18:
    print("not eligible")
else:
    print("eligible")

#nested if
num=51
if num>0:
    print("positive")
    if num%2==0:
        print("even")
    else:
        print("odd")
else:
    print("negative")

#question

#write a prog to check even or odd
num=int(input("enter a number"))
if num%2==0:
    print("even")
else:
    print("odd")

#grade calculator

marks=int(input("enter your marks"))

if marks>=90:
    print("A+")
elif marks>=80:
    print("A")
elif marks>=70:
    print("B")
else:
    print("fail")

#leap year

year=int(input("enter a year"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("leap year")
else:
    print("not leap year")
