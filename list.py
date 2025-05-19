# Syntex: list[start:end:step]
# start: শুরুর ইনডেক্স (অন্তর্ভুক্ত)
# end: শেষের ইনডেক্স (বাদ যায়)
# step: কত ধাপ এগিয়ে যাবে।

fruits=["apple","banana","orrange"]
print(fruits)
print(fruits[0]) #accessing first element
print(fruits[-1]) #accessing last element

# list slicing

numbers=[1,2,3,4,5]
print(numbers[1:3])
print(numbers[1:])
print(numbers[:3])
print(numbers[-3:-1])
print(numbers[::2])
print(numbers[::-1])

# list methods

# মেথড	            কাজ	                                             উদাহরণ
# append(x)	  লিস্টের শেষে নতুন আইটেম যোগ করে 	               fruits.append("mango")
# extend(list)	অন্য লিস্টের আইটেম যোগ করে	                   fruits.extend(["grape", "pear"])
# insert(i, x)	নির্দিষ্ট ইনডেক্সে আইটেম যোগ করে	               fruits.insert(1, "kiwi")
# remove(x)	    প্রথম মিলে যাওয়া আইটেম মুছে ফেলে	                  fruits.remove("banana")
# pop(i)	নির্দিষ্ট ইনডেক্সের আইটেম মুছে ফেলে এবং রিটার্ন করে	       fruits.pop(0)
# clear()	লিস্টের সব আইটেম মুছে ফেলে	                          fruits.clear()
# index(x)	আইটেমের ইনডেক্স রিটার্ন করে	                           fruits.index("apple")
# count(x)	আইটেম কতবার আছে গণনা করে	                      fruits.count("apple")
# sort()	লিস্ট সাজায় (আলফাবেটিক্যালি বা নিউমেরিক্যালি)             	fruits.sort()
# reverse()	লিস্টের ক্রম উল্টিয়ে দেয়	                                fruits.reverse()

fruits=["apple","banana","orrange","banana"]

fruits.append("mango")
print(fruits)

fruits.extend(["grape", "pear"])
print(fruits)

fruits.insert(1,"lichi")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.pop(0)
print(fruits)

print(fruits.index("mango"))
print(fruits.count("lichi"))
print(fruits.sort())
print(fruits.reverse())
print(fruits.clear())

print(fruits)

# list operations

# concatenation

list1=[1,2,3]
list2=[4,5,6]
list3=list1+list2
print(list3)

#repetition

list4=list1*3
print(list4)

#check
print(2 in list1)
print(len(list4))

# prac question:

# ইনপুট থেকে লিস্ট তৈরি: ব্যবহারকারীর কাছ থেকে ৫টি সংখ্যা নিয়ে একটি লিস্ট তৈরি করো এবং এর যোগফল প্রিন্ট করো।

numbers=[]
for i in range(5):
    num=int(input("enter a number:"))
    numbers.append(num)
print(sum(numbers))

# লিস্ট রিভার্স করা: একটি লিস্ট নিয়ে এটি রিভার্স করো (স্লাইসিং বা reverse() ব্যবহার করে)।
name=["alif","hasan","shadman"]
name.reverse()
print(name)

# জোড় সংখ্যা ফিল্টার করা: একটি লিস্ট থেকে শুধু জোড় সংখ্যাগুলো বের করো।

numbers=[1,2,3,4,5,6,7,8,9]
even=[x for x in numbers if x%2==0]
print(even)

# লিস্ট সর্টিং: একটি লিস্টকে ছোট থেকে বড় বা বড় থেকে ছোট ক্রমে সাজাও।

numbers=[5,2,9,1,5,6]
numbers.sort()#ascending order
print(numbers)
numbers.sort(reverse=True) #descending order
print(numbers)

