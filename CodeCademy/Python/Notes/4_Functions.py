print("")
print("------ 4. Functions ------")

print("")
print("------ 4.1. What Good are Functions? ------")
# From notes :
def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print("With tax: %f" % bill)
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print("With tip: %f" % bill)
  return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)



print("")
print("------ 4.2. Function Junction ------")
def hello_world():
  """Prints 'Hello World!' to the console."""
  print("Hello World!")

hello_world()

print("")
def spam():
  """Let's print some eggs!"""
  print("Eggs!")

spam()



print("")
print("------ 4.3. Call and Response ------")
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print("%d squared is %d." % (n, squared))
  return squared

square(10)



print("")
print("------ 4.4. Parameters and Arguments ------")
def power(base, exponent):
  result = base ** exponent
  print("%d to the power of %d is %d." % (base, exponent, result))

power(37, 4)




print("")
print("------ 4.5. Functions Calling Functions ------")
def one_good_turn(n):
  return n + 1

def deserves_another(n):
  return one_good_turn(n) + 2

print(one_good_turn(5))
print(deserves_another(5))


print("")
print("------ 4.6. Practice Makes Perfect ------")
def shout(phrase):
  if phrase == phrase.upper():
    return "YOU'RE SHOUTING!"
  else:
    return "Can you speak up?"

print(shout("I'M INTERESTED IN SHOUTING"))
print(shout("I'm interested in shouting"))

print("")
def cube(number):
  return number ** 3

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False

print(cube(2))
print(by_three(2))

print(cube(3))
print(by_three(3))



print("")
print("------ 4.8. Generic Imports ------")
import math
print(math.sqrt(25))



print("")
print("------ 4.11. Here Be Dragons ------")
import math
everything = dir(math)
print(everything)



print("")
print("------ 4.12. On Beyond Strings ------")
def biggest_number(*args):
  print(max(args))
  return max(args)

def smallest_number(*args):
  print(min(args))
  return min(args)

def distance_from_zero(arg):
  print(abs(arg))
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)



print("")
print("------ 4.13. max() ------")
maximum = max(38,93,1,20,40)
print(maximum)

maximum = max(38,-93,1,20,40)
print(maximum)




print("")
print("------ 4.14. min() ------")
minimum = min(38,93,1,20,40)
print(minimum)

minimum = min(38,-93,1,20,40)
print(minimum)



print("")
print("------ 4.15. abs() ------")
absolute = abs(-42)
print(absolute)



print("")
print("------ 4.16. type() ------")
print(type(42))
print(type(4.2))
print(type("spam"))

print("")
print(type(-23))
print(type(32.98))
print(type("Babe!"))



print("")
print("------ 4.17. Review: Functions ------")
def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"

print(shut_down("yes"))
print(shut_down("no"))
print(shut_down("what"))


print("")
print("------ 4.18. Review: Modules ------")
import math
print(math.sqrt(13689))

from math import sqrt
print(sqrt(13689))



print("")
print("------ 4.19. Review: Built-in Functions ------")
def distance_from_zero(value):
  if type(value) == int or type(value) == float:
    return abs(value)
  else:
    return "Nope"

print(distance_from_zero(89))
print(distance_from_zero(89.98))
print(distance_from_zero("89"))
