print("============================================")
print("Python 3 Programming Specialization")
print("Course 2 : Python Functions, Files, and Dictionaries")
print("Week 4 : More Iteration and Advanced Functions")
print("============================================")
print("========= 4.1. The While Statement =========")
print("--------------------------------------------")
def sumTo(aBound):
	"""Return the sum of 1+2+3 ... n"""
	theSum = 0
	aNumber = 1
	while aNumber <= aBound:
		theSum = theSum + aNumber
		aNumber = aNumber + 1
	return theSum

print(sumTo(4))
print(sumTo(1000))

print("")

eve_nums = []
counter = 0

while counter <= 15:
	if counter % 2 == 0:
		eve_nums.append(counter)
	counter += 1

print(eve_nums)

print("")

list1 = [8, 3, 4, 5, 6, 7, 9]
aNum = 0
accum = 0

while aNum < 10:
	if aNum in list1:
		accum += aNum
	aNum += 1

print(accum)

print("")

def stop_at_four(aList):
	ind = 0
	newList = []
	while ind < len(aList):
		if aList[ind] != 4:
			newList.append(aList[ind])
			ind += 1
		else:
			break
	return newList


blist = [1, 3, 6, 3, 7, 4, 8, 30]
clist = [0, 9, 4.5, 1, 7, 4, 8, 9, 3]
dlist = [4, 1, 2, 8]
elist = [4]
flist = [1,6,2,3,9]

print(stop_at_four(blist))
print(stop_at_four(clist))
print(stop_at_four(dlist))
print(stop_at_four(elist))
print(stop_at_four(flist))

print("")

print("============================================")
print("========== 4.2. The Listener Loop ==========")
print("--------------------------------------------")
theSum = 0
x = -1
while (x != 0):
	x = int(input("next number to add up (enter 0 if no more numbers): "))
	theSum = theSum + x

print(theSum)

print("")

def checkout():
	total = 0
	count = 0
	moreItems = True
	while moreItems:
		price = float(input("Enter price of item (0 when done): "))
		if price != 0:
			count = count + 1
			total = total + price
			print("Subtotal: $", total)
		else:
			moreItems = False
	average = total / count
	print("Total items: ", count)
	print("Total $", total)
	print("Average price per item: $", average)

checkout()

print("")

def get_yes_or_no(message):
	valid_input = False
	while not valid_input:
		answer = input(message)
		answer = answer.upper()
		if answer == "Y" or answer == "N":
			valid_input = True
		else:
			print("Please enter Y for yes or N for no.")
	return answer

response = get_yes_or_no("Do you like lima beans? Y)es or N)o: ")
if response == "Y":
	print("Great! They are very healthy!")
else:
	print("Too bad. If cooked right, they are quite tasty.")

print("")

print("============================================")
print("====== 4.3. Randomly Walking Turtles =======")
print("--------------------------------------------")
import random
import turtle


def isInScreen(w, t):
    if random.random() > 0.1:
        return True
    else:
        return False


t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn, t):
    coin = random.randrange(0, 2)
    if coin == 0:              # heads
        t.left(90)
    else:                      # tails
        t.right(90)

    t.forward(50)

wn.clear()


def IsInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while IsInScreen(wn,t):
    coin = random.randrange(0, 2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)

wn.clear()


print("")

print("============================================")
print("========= 4.4. Break and Continue ==========")
print("--------------------------------------------")
while True:
	print("This phrase will always print")
	break
	print("Does this phrase print?")

print("We are done with the while loop.")

print("")

x = 0

while x < 10:
	print("We are incrementing x")
	if x % 2 == 0:
		x += 3
		continue
	if x % 3 == 0:
		x += 5
	x += 1

print("Done with our loop! X has the value: " + str(x))

print("")

print("============================================")
print("========= 4.6. Optional Parameters =========")
print("--------------------------------------------")
print(int("100"))
print(int("100", 10))
print(int("100", 8))

print("")

initial = 7
def f(x, y = 3, z = initial):
	print("x, y, z, are: " + str(x) + "," + str(y) + "," + str(z))

f(2)
f(2, 5)
f(2, 5, 8)

initial = 10

f(2)

print("")

def f(a, L=[]):
	L.append(a)
	return L

print(f(1))
print(f(2))
print(f(3))
print(f(4, ["Hello"]))
print(f(5, ["Hello"]))

print("")

def f2(x = 0, y = 1):
	return x * y

print(f2())
print(f2(1))
print(f2(1,3))

print("")

def str_mult(x, y=3):
    return x * y

print(str_mult("ha"))
print(str_mult("ha", 9))
print(str_mult("hello "))

print("")

print("============================================")
print("========= 4.7. Keyword Parameters ==========")
print("--------------------------------------------")
def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
	print("-- This parrot wouldn't " + action,)
	print("if you put " + str(voltage) + " volts through it.")
	print("-- Lovely plumage, the " + type)
	print("-- It's " + state + "!")
	print("")

parrot(1000)	# 1 positional argument
parrot(voltage=1000)	# 1 keyword argument
parrot(voltage=1000000, action="VOOOOOM") # 2 keyword arguments
parrot(action="VOOOOOM", voltage=1000000)	# 2 keyword arguments
parrot("a million", "bereft of life", "jump")	# 3 positional arguments
parrot("a thousand", state="pushing up the daisies") # 1 positional, 1 keyword arguments

print("")

names_scores = [("Jack", [67, 89, 91]), ("Emily", [72, 95, 42]), ("Taylor", [83, 92, 86])]
for name, scores in names_scores:
	print("The scores {nm} gor were: {s1}, {s2}, {s3}".format(nm=name, s1=scores[0], s2=scores[1], s3=scores[2]))

print("")


# this works
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello"))

print("")

# but this also works!
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello"))

print("")

names = ["Alexey", "Catalina", "Mitsuki", "Pablo"]
print("'{first}!' she yelled. 'Come here, {first}! {f_one}, {f_two}, and {f_three} are here!'".format(first = names[1], f_one = names[0], f_two = names[2], f_three = names[3]))

print("")

def multiply(str, mult_int=10):
    return str * mult_int

print(multiply("hello "))
print(multiply("ha"))
print(multiply("Hello ", 3))

print("")

def waste(mar, var = "Water", marble = "type"):
    final_string = var + " " + marble + " " + mar
    return final_string

print(waste("Pokemon"))


print("")

print("============================================")
print("========= 4.8. Anonymous Functions =========")
print("========== with Lambda Expressions =========")
print("--------------------------------------------")
def f(x):
	return x -1

print(f)
print(type(f))
print(f(3))

print(lambda x: x-2)
print(type(lambda x: x-2))
print((lambda x: x-2)(6))

print("")

def last_char(s):
	return s[-1]

print(last_char("hello there"))

last_char = lambda s: s[-1]
print(last_char("hello there"))

print("")

print("============================================")
print("========= 4.9. Method Invocations ==========")
print("--------------------------------------------")
y = "This is a sentence"
z = y.split()
print(type(z))
print(len(z))
print(z)
for w in z:
	print(w)

print("")

print("This is a sentence".replace("s", "").replace("t", ""))

print("")

print("============================================")
print("====== 4.10. Assessments & Exercises =======")
print("--------------------------------------------")
counter = 0
numbers = []

while counter < 36:
	numbers.append(counter)
	counter += 1

print(counter)
print(numbers)

print("")

counter = 0
L = []

while counter < 11:
	L.append(counter)
	counter += 1

print(L)

print("")

counter = 0
nums = []

while counter < 21:
	nums.append(counter)
	counter += 1

print(nums)

print("")


import random
import turtle

sc = turtle.Screen()
steve = turtle.Turtle()
steve.speed(1)

step = 0

while step < 11:
    step += 1
    coin = random.randrange(0,2)
    angle = random.randrange(0, 360)
    if coin == 1:
        steve.left(angle)
        steve.forward(50)
    elif coin == 2:
        steve.right(angle)
        steve.forward(50)
    else:
        pass

sc.clear()

def moveRandom(wn, t):
    coin = random.randrange(0,2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)

def areColliding(t1, t2):
    if t1.distance(t2) < 2:
        return True
    else:
        return False

def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False
    return stillIn

t1 = turtle.Turtle()
t2 = turtle.Turtle()
wn = turtle.Screen()

t1.shape('turtle')
t2.shape('circle')

leftBound = -wn.window_width() / 2
rightBound = wn.window_width() / 2
topBound = wn.window_height() / 2
bottomBound = -wn.window_height() / 2

t1.up()
t1.goto(random.randrange(leftBound, rightBound),
        random.randrange(bottomBound, topBound))
t1.setheading(random.randrange(0, 360))
t1.down()

t2.up()
t2.goto(random.randrange(leftBound, rightBound),
        random.randrange(bottomBound, topBound))
t2.setheading(random.randrange(0, 360))
t2.down()


while isInScreen(wn, t1) and isInScreen(wn, t2):
    moveRandom(wn, t1)
    moveRandom(wn, t2)

wn.exitonclick()

print("")

counter = 0
tens = []

while counter < 51:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print(counter)
print(tens)

print("")

counter = 0
three_nums = []

while counter < 36:
    if counter % 3 == 0:
        three_nums.append(counter)
    counter += 1

print(three_nums)


print("")

def sublist(alist):
	n = 0
	sub_alist = []

	while n < len(alist):
		if alist[n] != 5:
			sub_alist.append(alist[n])
			n += 1
		else:
			break
	return sub_alist

print(sublist([1, 2, 3, 4, 5, 6, 7, 8]))
print(sublist([5]))
print(sublist([8, 6, 5]))
print(sublist([1, 6, 2, 3, 9]))

print("")

def check_nums(alist):
    n = 0
    sevenless_list = []

    while n < len(alist):
        if alist[n] != 7:
            sevenless_list.append(alist[n])
            n += 1
        else:
            break
    return sevenless_list

print(check_nums([0,2,4,9,2,3,6,8,12,14,7,9,10,8,3]))
print(check_nums([9,302,4,62,78,97,10,7,8,23,53,1]))
print(check_nums([7,8,3,2,4,51]))
print(check_nums([1, 6, 2, 3, 9]))

print("")

def sublist_stop(alist):
	n = 0
	stopless = []

	while n < len(alist):
		if alist[n] != "STOP":
			stopless.append(alist[n])
			n += 1
		else:
			break
	return stopless

lst1 = ['bob', 'joe', 'lucy', 'STOP', 'carol', 'james']
lst2 = ['STOP']
lst3 = ['jackie', 'paul', 'STOP']

print(sublist_stop(lst1))
print(sublist_stop(lst2))
print(sublist_stop(lst3))

print("")

def stop_at_z(str):
	n = 0
	z_less = []

	while n < len(str):
		if str[n] != "z":
			z_less.append(str[n])
			n += 1
		else:
			break
	return z_less

print(stop_at_z(['c', 'b', 'd', 'zebra', 'h', 'r', 'z', 'm', 'a', 'k']))
print(stop_at_z(['zoo', 'zika', 'ozzie', 'pizzazz', 'z', 'pizza', 'zap', 'haze']))
print(stop_at_z(['z']))

print("")

sum1 = 0
lst = [65, 78, 21, 33]
for x in lst:
    sum1 = sum1 + x
print(sum1)

n = 0
sum2 = 0
while n < len(lst):
    sum2 += lst[n]
    n += 1
print(sum2)

print("")

def beginning(alist):
    n = 0
    first = []

    while n < len(alist):
        if alist[n] != "bye":
            first.append(alist[n])
            n += 1
        else:
            break
    return first[:10]

ls1 = ['water', 'phone', 'home', 'chapstick', 'market', 'headphones', 'bye', 'stickie notes', 'snapchat', 'facebook', 'social media']
ls2 = ['bye', 'no', 'yes', 'maybe', 'sorta']
ls3 = ['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup', 'see yah', 'toodel loo', 'night', 'until later', 'peace', 'bye', 'good-bye', 'g night']

print(beginning(ls1))
print(beginning(ls2))
print(beginning(ls3))

def g(x, y=4, z=0):
	return 2*x + y + z

print(g(3))
print(g(3, 2))
print(g(3, 2, 1))


print("")

def nums(x, mult_int = 5, switch = False):
	if switch == True:
		return -(x * mult_int)
	else:
		return x * mult_int

print(nums(5))
print(nums(2, mult_int=4))
print(nums(3, switch=True))
print(nums(4, mult_int=3, switch=True))
print(nums(0, switch=True))

print("")

def together(num, st, space= " "):
	return str(num) + space + st

print(together(12, 'cats'))
print(together(17.3, 'birthday cakes'))
print(together(3, 'dogs', ': '))
print(together(493.3, 'beans', 'lima'))

print("")

def mult(x, y=6):
	return x * y

print(mult(2))
print(mult(3, 5))
print(mult(4, "hello "))

print("")

def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

print("")

def sum(intx, intz=5):
    return intz + intx

print(sum(8,2))
print(sum(12))

print("")

def test(x, boo=True, dict1={2:3, 4:5, 6:8}):
	if boo == True:
		if x in dict1.keys():
			return dict1[x]
		else:
			return False
	else:
		return False

print(test(2))
print(test(4, False))
print(test(5, dict1 = {5:4, 2:1}))

print("")

def checkingIfIn(str1, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
	if direction == True:
		if str1 in d.keys():
			return True
		else:
			return False
	else:
		if str1 not in d.keys():
			return True
		else:
			return False


print(checkingIfIn('grapes'))
print(checkingIfIn('carrots'))
print(checkingIfIn('grapes', False))
print(checkingIfIn('carrots', False))
print(checkingIfIn('grapes', d = {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1}))
print(checkingIfIn('peas', d = {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1}))
print(checkingIfIn('peas', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1}))
print(checkingIfIn('apples', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1}))

print("")

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

c_false = checkingIfIn("beetroot")
print(c_false)
c_true = checkingIfIn("beetroot", False)
print(c_true)
fruit_ans = checkingIfIn("fruit")
print(fruit_ans)
param_check = checkingIfIn("apple", d = {'apple': 8, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7})
print(param_check)
