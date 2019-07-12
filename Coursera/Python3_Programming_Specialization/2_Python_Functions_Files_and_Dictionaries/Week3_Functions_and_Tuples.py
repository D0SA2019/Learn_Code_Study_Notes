print("============================================")
print("Python 3 Programming Specialization")
print("Course 2 : Python Functions, Files, and Dictionaries")
print("Week 3 : Functions and Tuples")
print("============================================")
print("========= 3.1. Defining Functions ==========")
print("--------------------------------------------")
'''
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


print("")

print("============================================")
print("======== 3.7. Function Composition =========")
print("--------------------------------------------")
def square(x):
	y = x * x
	return y

def sum_of_squares(x, y, z):
	a = square(x)
	b = square(y)
	c = square(z)

	return a + b + c

a = -5
b = 2
c = 10

result = sum_of_squares(a, b, c)
print(result)

def most_common_letter(s):
	frequencies = count_freqs(s)
	return best_key(frequencies)

def count_freqs(st):
	d = {}
	for c in st:
		if c not in d:
			d[c] = 0
		d[c] = d[c] + 1

	return d

def best_key(dictionary):
	ks = dictionary.keys()
	best_key_so_far = list(ks)[0]
	for k in ks:
		if dictionary[k] > dictionary[best_key_so_far]:
			best_key_so_far = k
	return best_key_so_far

print(most_common_letter("abbbbbbbbbbbbbbcccddddd"))

def addit(n):
	return n + 5

def mult(s):
	return s * addit(s)

print(mult(7))

def pow(b, p):
	y = b ** p
	return y

def square(x):
	a = pow(x, 2)
	return a

n = 5
result = square(n)
print(result)

print("")

print("============================================")
print("========== 3.8. Print vs. return ===========")
print("--------------------------------------------")
def square(x):
	return x * x

def g(y):
	return y + 3

def h(y):
	return square(y) + 3

print(h(2))
print(g(h(2)))

print("")

print("============================================")
print("=== 3.9.Mutable Objects and Side Effects ===")
print("--------------------------------------------")
def double(y):
	y = 2 * y

def changeit(lst):
	lst[0] = "Michigan"
	lst[1] = "Wolverines"

y = 5
double(y)
print(y)

mylst = ["our", "students", "are", "awesome"]
print(mylst)
changeit(mylst)
print(mylst)

print("")

def double(n):
	global y
	y = 2 * n

y = 5
print(y)

double(y)
print(y)

def double(n):
	return 2 * n

y = 5
print(y)

y = double(y)
print(y)

print("")

def change_it(alist):
	blist = alist[:]
	blist[0] = "Michigan"
	blist[1] = "Wolverines"
	return blist

my_list = ["106", "students", "are", "awesome"]
new_list = change_it(my_list)
print(my_list)
print(new_list)

print("")

print("============================================")
print("=========== 3.10. Tuple Packing ============")
print("--------------------------------------------")
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
print(julia[4])
print(julia[-1])

def circleInfo(r):
	"""Return (circumference, area) of a circle of radius r"""
	c = 2 * 3.14159 * r
	a = 3.14159 * r * r
	return c,a

print(circleInfo(10))

print("")
practice = ("y", "h", "z", "x")
print(practice)

tup1 = ("a", "b", "c")
print(tup1)

print("")

lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
t_check = []

for tup in lst_tups:
	t_check.append(tup[2])

print(t_check)


tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]

seconds = []

for tup in tups:
	seconds.append(tup[1])

print(seconds)

print("")

def information(name, birth_year, fav_color, hometown):
	return name, birth_year, fav_color, hometown

print(information("Alex", 1979, "yellow", "Georgia"))

print("")

print("============================================")
print("== 3.11. Tuple Assignment with Unpacking ===")
print("--------------------------------------------")
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"

name, surname, birth_year, movie, movie_year, profession, birth_place = julia

print(name, surname, birth_year, profession)
print(movie, movie_year)

print("")

a = 1
b = 2
temp = a
a = b
b = temp
print(a, b, temp)

a = 1
b = 2
(a,b) = (b,a)
print(a,b)

print("")

def circle_info(r):
	"""Return (circumference, area) of a circle of radius r"""
	c = 2 * 3.14159 * r
	a = 3.14159 * r * r
	return c, a

print(circle_info(10))

circumference, area = circle_info(10)
print(circumference)
print(area)

circumference_two, area_two = circle_info(45)
print(circumference_two)
print(area_two)

print("")

def add(x, y):
	return x + y

print(add(3,4))

z = (5,4)
print(add(*z))

print("")

d = {"k1": 3, "k2": 7, "k3": "some other value"}

for p in d.items():
	print("key: {}, value: {}".format(p[0], p[1]))

print("")

for k, v in d.items():
	print("key: {}, value: {}".format(k, v))

print("")

water, fire, electric, grass = "Squirtle", "Charmander", "Pikachu", "Bulbasaur"
print(water)
print(grass)

print("")

v1, v2, v3, v4 = 1, 2, 3, 4

print(v1)
print(v3)

print("")

pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}

p_names = []
p_number = []

for k, v in pokemon.items():
	p_names.append(k)
	p_number.append(v)

print(p_names)
print(p_number)

print("")

track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}

track_events = []

for k, v in track_medal_counts.items():
	track_events.append(k)

print(track_events)

print("")
'''
print("============================================")
print("====== 3.12. Assessments & Exercises =======")
print("--------------------------------------------")
def num_test(n):
	if n > 10:
		return "Greater than 10."
	elif n < 10:
		return "Less than 10."
	else:
		return "Equal to 10."

print(num_test(int(input("Enter a number: "))))

print("")

def numDigits(n):
	len_n = len(str(n))
	return len_n

print(numDigits(200))
print(numDigits(3))
print(numDigits(209903))

print("")

def reverse(astring):
	return astring[::-1]

print(reverse("something happened"))
print(reverse("is it reversed?"))

print("")

def mirror(mystr):
	rev_mystr = mystr[::-1]
	return mystr + rev_mystr

print(mirror("something"))
print(mirror("let's get a mirror effect"))

print("")

def remove_letter(theLetter,theString):
	letterless = theString.split(theLetter)
	new_str = "".join(letterless)
	return new_str

print(remove_letter("a", "it's gonna disappear"))
print(remove_letter("c", "could you come over please?"))

print("")

def count(thing, alist):
	c = 0
	for item in alist:
		if item == thing:
			c += 1
	return c

def is_in(thing, alist):
	for item in alist:
		if item == thing:
			return True
	return False

def reverse(alist):
	blist = []
	for item in alist:
		blist.insert(0, item)
	return blist

def index(thing, alist):
	c = 0
	for item in alist:
		if item == thing:
			return c
		else:
			c += 1
	return c

def insert(thing, index, alist):
	blist = []
	for ind in range(len(alist)):
		if ind == index:
			blist.append(thing)
		else:
			blist.append(alist[ind])
	return blist

lst = ["something", "is", "here", "lets", "find", "out", "the", "functions", "works", "something"]

print(count("something", lst))
print(is_in("here", lst))
print(reverse(lst))
print(index("lets", lst))
print(insert("what", 5, lst))

print("")

def replace(s, old, new):
	lst = s.split(old)
	new_s = new.join(lst)
	return new_s

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'

print(replace(s, "om", "am"))
print(replace(s, "o", "a"))
print(replace("Mississippi", "i", "I"))

print("")

import random

def random_max(alist):
	max = None

	for num in num_list:
		if max == None:
			max = num
		else:
			if num > max:
				max = num
	return max

num_list = []

for n in range(100):
	n = random.randint(0,1000)
	num_list.append(n)

print(num_list)
print(random_max(num_list))

print("")

def square(num):
	return num * num

def sum_of_squares(xs):
	tot = 0
	for n in xs:
		tot += square(n)
	return tot

somelist = [2, 3, 4]
print(sum_of_squares(somelist))

print("")

def countOdd(lst):
	c = 0
	for num in lst:
		if num % 2 != 0:
			c += 1
	return c

clist = [2, 5, 6, 3, 9, 49, 4, 90]
print(countOdd(clist))

print("")

def sumEven(lst):
	tot = 0
	for num in lst:
		if num % 2 == 0:
			tot += num
	return tot

clist = [2, 5, 6, 3, 9, 49, 4, 90]
print(sumEven(clist))

def sumNegatives(lst):
	tot = 0
	for num in lst:
		if num < 0 :
			tot += num
	return tot

dlist = [-1,-2,-3,-4,-5]
print(sumNegatives(dlist))

print("")

def findHypot(a,b):
	return ((a * a) + (b * b)) ** 0.5

print(findHypot(3,6))

print("")

def is_even(n):
	if n % 2 == 0:
		return True
	else:
		return False

print(is_even(8))
print(is_even(5))

print("")

def is_odd(n):
	if n % 2 != 0:
		return True
	else:
		return False

print(is_odd(8))
print(is_odd(5))

print("")


def is_rightangled(a, b, c):
	if int(a) == int(((b * b) + (c * c)) ** 0.5):
		return True
	elif int(b) == int(((a * a) + (c * c)) ** 0.5):
		return True
	elif int(c) == int(((b * b) + (a * a)) ** 0.5):
		return True
	else:
		return False

print(is_rightangled(3,4,5))
print(is_rightangled(4.1,8.2,9.16787))

print("")

def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

circ, area = circleInfo(10)
print("area is " + str(area))
print("circumference is " + str(circ))

print("")

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
claude = ("Claude", "Shannon", 1916, "A Mathematical Theory of Communication", 1948, "Mathematician", "Petoskey, Michigan")
alan = ("Alan", "Turing", 1912, "Computing machinery and intelligence", 1950, "Mathematician", "London, England")

people = [julia, claude, alan]

for person in people:
	name, surname, year_of_birth, movie, movie_year, profession, city = person
	print(name, surname, year_of_birth, city)

print("")

olympics = ("Beijing", "London", "Rio", "Tokyo")
print(olympics)

print("")

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]

country = []

for tup in tuples_lst:
	second = tup[1]
	country.append(second)

print(country)


print("")

olymp = ('Rio', 'Brazil', 2016)

city, country, year = olymp
print(city)
print(country)
print(year)

print("")

def info(name, gender, age, bday_month, hometown):
	atuple = (name, gender, age, bday_month, hometown)
	return atuple

print(info("Steven", "Male", 29, "April", "LA"))

print("")

gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}

num_medals = []

for k,v in gold.items():
	num_medals.append(v)

print(num_medals)

print("")

def int_return(n):
	return n

print(int_return(int(input("Enter a number: "))))

print("")

def add(n):
	return n + 2

print(add(int(input("Enter a number: "))))

print("")

def change(astr):
    return astr + "Nice to meet you!"

print(change("Steven"))

print("")

def accum(alist):
	tot = 0
	for num in alist:
		tot += num
	return tot

lst = [2, 5, 6, 6, 5]

print(accum(lst))

print("")

def length(alist):
	if len(alist) >= 5:
		return "Longer than 4"
	else:
		return "Less than 5"

lst = [2, 5, 6, 6, 5]

print(length(lst))

print("")

def divide(num):
	return num / 2

def sum(num):
	return divide(num) + 6

print(sum(40))
