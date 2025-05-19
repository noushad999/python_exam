#never store duplicate data
#unordered

fruits={"apple", "banana", "cherry"}
numbers={1, 2, 3, 4, 5}
empty_set=set()

#unorded
#no duplicates
#mutable
#fast operations
#no indexing and slicing


num={1,2,3,4,5}
print(num)

fruits={"apple", "banana", "cherry"}
print(fruits)


#accessing with loops
for fruit in fruits:
    print(fruit)

#checking if an item exists
print("banana" in fruits)

# print(fruits[0]) -->> this will give an error because set is unordered and does not support indexing

#methods in set
# মেথড	                     কাজ	                                     উদাহরণ
# add(x)	            সেটে একটি আইটেম যোগ করে	                        fruits.add("mango")
# update(iterable)	একাধিক আইটেম যোগ করে	                        fruits.update(["grape", "pear"])
# remove(x)	        নির্দিষ্ট আইটেম মুছে ফেলে (না থাকলে এরর দেয়)	       fruits.remove("banana")
# discard(x)	        নির্দিষ্ট আইটেম মুছে ফেলে (না থাকলে এরর দেয় না)	   fruits.discard("banana")
# pop()	            র‍্যান্ডম আইটেম মুছে ফেলে এবং রিটার্ন করে	            fruits.pop()
# clear()	            সেটের সব আইটেম মুছে ফেলে	                      fruits.clear()
# copy()	            সেটের কপি তৈরি করে	                            set1.copy()


fruits={"apple", "banana", "cherry"}

fruits.add("mango")
print(fruits)

fruits.update(["grape", "pear"])
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.discard("cherry")
print(fruits)

print(fruits.pop())
print(fruits)

print(fruits.clear())
print(fruits)

#set operations
# অপারেশন           	অপারেটর	                    মেথড	                        কাজ
# Union	                 `     	                  union()
# Intersection	         &	                      intersection()        	দুটি সেটের মধ্যে কমন আইটেম
# Difference	             -	                      difference()	            একটি সেটে থাকা আইটেম যা অন্যটিতে নেই
# Symmetric Difference	 ^	                      symmetric_difference()	কমন আইটেম বাদে বাকি আইটেম
# Subset               	<=	                      issubset()	            একটি সেট অন্যটির সাবসেট কিনা
# Superset            	>=	                      issuperset()	            একটি সেট অন্যটির সুপারসেট কিনা

set1={1,2,3,4,5}
set2={3,4,5,6,7}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

#questions
#take 5 numbers from user and make a set 
num=set()
for i in range(5):
    num1=int(input("enter a number"))
    num.add(num1)
print(num)

#find the union and intersections  from two sets
set1={1,3,4,5,6}
set2={4,5,6,7,8}

# print(set1.intersection(set2))
print(set1.union(set2))

#remove duplicates from a list
list1=[1,2,3,4,5,6,7,8,9,10,1,2,3]
set1=set(list1)
print(set1) 

#REMOVE ITEM FROM A SET
set1={1,2,3,4,5}
set1.remove(3)
print(set1)
