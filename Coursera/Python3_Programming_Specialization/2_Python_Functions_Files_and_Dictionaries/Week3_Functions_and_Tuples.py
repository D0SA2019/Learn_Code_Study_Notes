print("============================================")
print("Python 3 Programming Specialization")
print("Course 2 : Python Functions, Files, and Dictionaries")
print("Week 3 : Functions and Tuples")
print("============================================")
print("========= 3.1. Defining Functions ==========")
print("--------------------------------------------")
import turtle

def drawSquare(t, sz):
	"""Make turtle t draw a square of with side sz."""

	for i in range(4):
		t.forward(sz)
		t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.speed(1)
drawSquare(alex, 50)

wn.exitonclick()

def hello():
	print("hello")
	print("Glad to meet you")

print(type(hello))
print(type("hello"))

hello()
print("Hey, that just printed two lines with one line of code!")
hello()

print("")

print("============================================")
print("========= 3.2. Function Parameters =========")
print("--------------------------------------------")
def hello2(s):
	print("Hello " + s)
	print("Glad to meet you")

hello2("Iman")
hello2("Jackie")

print("")

hello2("Iman" + " and Jackie")
hello2("Class " * 3)

print("")

def hello3(s, n):
	greeting = "Hello {} ".format(s)
	print(greeting * n)

hello3("Wei", 4)
hello3("", 1)
hello3("Kitty", 11)

print("")

print("============================================")
print("=========== 3.3. Returning Values ==========")
print("--------------------------------------------")
def square(x):
	y = x * x
	return y

toSquare = 10
result = square(toSquare)
print("The result of {} squared is {}.".format(toSquare, result))

def square(x):
	return x * x

toSquare = 10
result = square(toSquare)
print("The result of {} squared is {}.".format(toSquare, result))

def square(x):
	y = x * x
	print(y)

toSquare = 10
squareResult = square(toSquare)
print("The result of {} squared is {}.".format(toSquare, result))

print("")

def weird():
	print("here")
	return 5
	print("there")
	return 10

x = weird()
print(x)

print("")

def longer_than_five(list_of_names):
	for name in list_of_names:
		if len(name) > 5:
			return True
	return False

list1 = ["Sam","Tera","Sal","Amita"]
list2 = ["Rey","Ayo","Lauren","Natalie"]

print(longer_than_five(list1))
print(longer_than_five(list2))

print("")

def square(x):
	y = x * x
	return y

print(square(5) + square(5))


def square(x):
	y = x * x
	return y

print(square(square(2)))


def cyu2(s1, s2):
	x = len(s1)
	y = len(s2)
	return x - y

z = cyu2("Yes", "no")

if z > 0:
	print("First one was longer")
else:
	print("Second one was at least as long")

def square(x):
	print("square")
	return x*x

def g(y):
	print("g")
	return y + 3

print(square(g(2)))


def show_me_numbers(list_of_ints):
	print(10)
	print("Next we'll accumulate the sum")
	accum = 0
	for num in list_of_ints:
		accum = accum + num
	return accum
	print("All done with accumulation!")

show_me_numbers([4,2,3])


print("")

def same(str):
	return str

print(same("some string here"))

def same_thing(thing):
	return thing

print(same_thing(45))
print(same_thing("another string here"))

def subtract_three(num):
	return num - 3

print(subtract_three(4))

def change(num):
	return num + 7

print(change(7))
print(change(-4))

def intro(str):
	return "Hello, my name is {} and I love SI 106.".format(str)

print(intro("Becky"))

def s_change(str):
	return str + " for fun."

print(s_change("Coding"))

def decision(str):
	if len(str) > 17:
		return "This is a long string"
	else:
		return "This is a short string"

print(decision("Write a function called decision"))
print(decision("it has"))

print("")

print("============================================")
print("===== 3.5. A Function that Accumulates =====")
print("--------------------------------------------")
def mylen(seq):
	c = 0
	for _ in seq:
		c = c + 1
	return c

print(mylen("hello"))
print(mylen([1, 2, 7]))

print("")

def total(alist):
	tot = 0
	for number in alist:
		tot += number
	return tot

list_a = [1, 4, 2, 8, 30]
list_b = [3, 2, 9, 7]

print(total(list_a))
print(total(list_b))

print("")

def count(alist):
	co = 0
	for number in alist:
		co += 1
	return co

list_a = [1, 4, 2, 8, 30]
list_b = [3, 2, 9, 7]

print(count(list_a))
print(count(list_b))

print("")

print("============================================")
print("===== 3.6. Local and Global Variables ======")
print("--------------------------------------------")
numbers = [1, 12, 13, 4]
def foo(bar):
	aug = str(bar) + "street"
	return aug

addresses = []
for item in numbers:
	addresses.append(foo(item))

print(addresses)

print("")

def badsquare(x):
	y = x ** power
	return y

power = 2
result = badsquare(10)
print(result)

print("")

def powerof(x,p):
	power = p
	y = x ** power
	return y

power = 3
result = powerof(10, 2)
print(result)

print("")

def powerof(x,p):
	global power
	power = p
	y = x ** power
	return y

power = 3
result = powerof(10, 2)
print(result)
print(power)

print("")

def square(x):
	y = x * x
	x = 0
	return y

x = 2
z = square(x)
print(z)
