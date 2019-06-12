print("============================================")
print("Python 3 Programming Specialization")
print("Course 1 : Python Basics")
print("Week 1 : Introduction to the Specialization")
print("============================================")
print("======== 1.2. Values and Data Types ========")
print("--------------------------------------------")
print(100)
print(3.14)
print("Hello world")

print("")

print(3.2)
print("Hello World!")
print("============================================")
print("======= 1.3. Operators and Operands ========")
print("--------------------------------------------")
print(100 + 200)
print(5 - 2)
print(2 * 4)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(4 ** 2)
print(10 + 20 / 2)
print((10 + 20) / 2)

print("")

print(20 + 32)
print(5 ** 2)
print((5 + 9) * (15 - 7))
print(9 / 5)
print(5 / 9)
print(9 // 5)
print(7.0 / 3.0)
print(7.0 // 3.0)
print(7 // 3)
print(7 % 3)
print(18 / 4)
print(18.0 // 4)
print(18 % 4)

print("")

print(2 * (3-1))
print((1+1)**(5-2))
print(2**1+1)
print(3*1**3)
print(2*3-1)
print(5-2*2)
print(6-3+2)
print(6-(3+2))

print("")

print(2 ** 3 ** 2)
print((2 ** 3) ** 2)
print(16 - 2 * 5 // 3 + 1)
print("============================================")
print("============ 1.4.Function Calls=============")
print("--------------------------------------------")
def square(num):
    return num * num

def sub(num1, num2):
    return num1 - num2

print(square(3))
square(4)
print(sub(6,4))
print(sub(5,9))

print("")

print(square(3) + 2)
print(sub(square(3), square(1 + 1)))

print("")

print(square)
print(square(3))
print("============================================")
print("============= 1.5.Data Types ===============")
print("--------------------------------------------")
print(type("Hello World!"))
print(type(17))
print(type(3.2))

print("")

print(type("17"))
print(type("3.2"))

print("")

print(type('This is a string.'))
print(type("And so it is."))
print(type("""and this."""))
print(type('''and even this.'''))

print("")

print("Bruce's beard")
print('She said "hi".')
print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')

print("")

print("""This message will span
several lines
of the text.""")

print("")

print('This is a string.')
print("""And so it is.""")

print("")

print(42,500)
print(42.500)
print(42500)

print("")

print(42, 17, 56, 34, 11, 4.35, 32)
print(3.4, "hello, 45")
print("============================================")
print("======= 1.6.Type Conversion Functions =======")
print("--------------------------------------------")
print(3.14, int(3.14))
print(3.9999, int(3.9999))
print(-3.9999, int(-3.9999))
print("2345", int("2345"))
print(17, int(17))
# print(int("23bottless")) Traceback error

print("")

print(float("123.45"))
print(type(float("123.45")))

print("")

print(str(17))
print(str(123.45))
print(type(str(123.45)))
print("============================================")
print("=============== 1.7.Variables ==============")
print("--------------------------------------------")
message = "What's up, Doc?"
n = 17
pi = 3.14159

print(message)
print(n)
print(pi)

print("")

print(type(message))
print(type(n))
print(type(pi))

print("")

bruce = 5
print(bruce)

bruce = 7
print(bruce)

print("")

a = 5
b = a
print(a, b)

a = 3
print(a, b)
print("============================================")
print("====== 1.8.Statements and Expressions ======")
print("--------------------------------------------")
print(1 + 1 + (2 * 3))
print(len("hello"))

print("")

y = 3.14
x = len("hello")
print(x)
print(y)

print("")

print(2 * len("hello") + len("goodbye"))

print("")

def square(x):
	return x * x

def sub(x, y):
	return x - y


x = 2
y = 1

print(square(y + 3))
print(square(y + square(x)))
print(sub(square(y), square(x)))
print("============================================")
print("========== 1.9.Updating Variables ==========")
print("--------------------------------------------")
x = 6
print(x)
x = x + 1
print(x)

print("")

x = 6
print(x)
x += 3
print(x)
x -= 1
print(x)

print("")

s = 1
print(s)
s = s + 2
print(s)
s = s + 3
print(s)
s = s + 4
print(s)
s = s + 5
print(s)
s = s + 6
print(s)
s = s + 7
print(s)
s = s + 8
print(s)
s = s + 9
print(s)
s = s + 10
print(s)
print("============================================")
print("================ 1.11.Input ================")
print("--------------------------------------------")
n = input("Please enter your name: ")
print("Hello", n)

print("")

str_seconds = input("Please enter the number of seconds you wish to convert: ")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)
print("============================================")
print("========= 1.12.Chapter Assessment ==========")
print("--------------------------------------------")
print(5 ** 2)
print(9 * 5)
print(15 / 12)
print(12 / 15)
print(15 // 12)
print(5 % 2)
print(9 % 5)
print(15 % 12)
print(12 % 15)
print(6 % 6)
print(0 % 7)

print("")

print(2 + (3 - 1) * 10 / 5 * (2 + 3))

print("")

time_now = int(input("What time now? "))
time_wait = int(input("How much time to wait? "))

clock = (time_now + time_wait) % 24
print(clock)

print("")

holiday_start = int(input("Day of starting your holiday? "))
holiday_stay = int(input("How many days stay on holiday? "))

return_day = (holiday_start + holiday_stay) % 7
print(return_day)

print("")

w1 = "All"
w2 = "work"
w3 = "and"
w4 = "no"
w5 = "play"
w6 = "makes"
w7 = "Jack"
w8 = "a"
w9 = "dull"
w10 = "boy."

print(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10)

print("")

print(6 * (1 - 2))

print("")

P = 10000
n = 12
r = 0.08
t = int(input("How many years? "))

A = P * ((1 + (r / n)) ** (n * t))
print(A)

print("")

r = int(input("Enter the radius: "))
pi = 3.14

A = pi * (r ** 2)
print("The area of the circle is ", A)

print("")

w = int(input("What's the width? "))
l = int(input("What's the lenght? "))

A = w * l
print("The area of the rectangle is", A)

print("")

driven_mile = int(input("Miles? "))
used_gallon = int(input("Gallon? "))

mpg = driven_mile / used_gallon
print("MPG of the car is", mpg)

print("")

c = int(input("What's the temperature on Celcius? "))
f = (((9 / 5)* c )+ 32)

print("It's", f, "Fahrenheit")

print("")

f = int(input("What's the temperature on Fahrenheit? "))
c = (5 / 9) * (f - 32)

print("It's", c, "Celcius")
print("============================================")
