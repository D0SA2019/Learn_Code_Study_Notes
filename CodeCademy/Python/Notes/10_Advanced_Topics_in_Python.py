print("")
print("------ 10. Advanced Topics in Python ------")

print("")
print("------ 10.1. Iterators for Dictionaries ------")
d = {
	"Name": "Guidio",
	"Age": 56,
	"BDFL": True
}

print(d)
print(d.items())

print("")

my_dict = {
	"Drink" : "Coffee",
	"Eat" : "Cake",
	"Think" : "Today's to-dos",
	"Learn" : "Python",
	"Develop" : "Project"
}

print(my_dict.items())



print("")
print("------ 10.2. keys() and values() ------")
my_dict = {
	"Drink" : "Coffee",
	"Eat" : "Cake",
	"Think" : "Today's to-dos",
	"Learn" : "Python",
	"Develop" : "Project"
}


print(my_dict.keys())
print(my_dict.values())




print("")
print("------ 10.3. The 'in' Operator ------")
for number in range(5):
	print(number, end=" ")


d = {
	"name": "Eric",
	"age": 26
}

for key in d:
	print(key, d[key], end=" ")

for letter in "Eric":
	print(letter, end=" ")

print("")


my_dict = {
	"Drink" : "Coffee",
	"Eat" : "Cake",
	"Think" : "Today's to-dos",
	"Learn" : "Python",
	"Develop" : "Project"
}

print(my_dict.keys())
print(my_dict.values())


for key in my_dict:
	print(key, my_dict[key])




print("")
print("------ 10.4. Building Lists ------")
my_list = range(51)
print(my_list)

my_list = list(range(51))
print(my_list)

print("")

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)




print("")
print("------ 10.5. List Comprehension Syntax ------")
new_list = [x for x in range(1,6)]
print(new_list)

doubles = [x * 2 for x in range(1,6)]
print(doubles)

doubles_by_3 = [x * 2 for x in range (1,6) if (x * 2) % 3 == 0]
print(doubles_by_3)


even_squares = [x**2 for x in range (1,11) if (x ** 2) % 2 == 0]
print(even_squares)




print("")
print("------ 10.6. Now You Try! ------")
c = ['C' for x in range(5) if x < 3]
print(c)

cubes_by_four = [x ** 3 for x in range(1,11) if (x ** 3) % 4 == 0]
print(cubes_by_four)




print("")
print("------ 10.7. List Slicing Syntax ------")
l = [i ** 2 for i in range(1, 11)]
print(l)
print(l[2:9:2])




print("")
print("------ 10.8. Omitting Indices ------")
to_five = ['A', 'B', 'C', 'D', 'E']

print(to_five[3:])
print(to_five[:2])
print(to_five[::2])

my_list = list(range(1, 11))
print(my_list[::2])




print("")
print("------ 10.9. Reversing a List ------")
letters = ['A', 'B', 'C', 'D', 'E']
print(letters[::-1])

my_list = list(range(1, 11))
backwards = my_list[::-1]

print(my_list)
print(backwards)




print("")
print("------ 10.10. Stride Length ------")
to_one_hundred = list(range(101))

backwards_by_tens = to_one_hundred[::-10]
print(backwards_by_tens)




print("")
print("------ 10.11. Practice Makes Perfect ------")

to_21 = list(range(1,22))
odds = to_21[::2]
middle_third = to_21[7:14]

print(to_21)
print(odds)
print(middle_third)




print("")
print("------ 10.12. Anonymous Functions ------")
my_list = list(range(16))
filtered = list((filter(lambda x: x % 3 == 0, my_list)))
print(filtered)




print("")
print("------ 10.13. Lambda Syntax ------")
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(list(filter(lambda x: x == "Python", languages)))




print("")
print("------ 10.14. Try It! ------")
squares = [x **2 for x in range(1,11)]
print(list(filter(lambda x: 30 <= x <= 70, squares)))




print("")
print("------ 10.15. Iterating Over Dictionaries ------")
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}

print(list(movies.items()))




print("")
print("------ 10.16. Comprehending Comprehensions ------")
threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
print(threes_and_fives)




print("")
print("------ 10.17. List Slicing ------")
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]
print(message)




print("")
print("------ 10.18. Lambda Expressions ------")
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = "".join(filter(lambda x : x != "X", garbled))
print(message)
