print("")
print("------ 7. Lists and Functions ------")

print("")
print("------ 7.1. List accessing  ------")
n = [1, 3, 5]
print(n[1])


print("")
print("------ 7.2. List element modification  ------")
n = [1, 3, 5]
second = n[1] * 5
n[1]=second
print(n)

n = [1, 3, 5]
n[1] = n[1] * 5
print(n)



print("")
print("------ 7.3. Appending to a list ------")
n = [1, 3, 5]
n.append(4)
print(n)



print("")
print("------ 7.4. Removing elements from lists ------")
n = [1, 3, 5]
n.pop(1)
print(n)

n = [1, 3, 5]
n.remove(1)
print(n)

n = [1, 3, 5]
del(n[1])
print(n)



print("")
print("------ 7.5. Changing the functionality of a function ------")
number = 5

def my_function(x):
  return x + 3

print(my_function(number))


number = 5

def my_function(x):
  return x * 3

print(my_function(number))



print("")
print("------ 7.6. More than one argument ------")
m = 5
n = 13

def add_function(x,y):
  return x + y

print(add_function(m, n))



print("")
print("------ 7.7. Strings in functions ------")
n = "Hello"

def string_function(s):
  return s + 'world'

print(string_function(n))



print("")
print("------ 7.8. Passing a list to a function ------")
def list_function(x):
  return x

n = [3, 5, 7]
print(list_function(n))




print("")
print("------ 7.9. Using an element from a list in a function ------")
def first_item(items):
  print(items[0])

numbers = [2, 7, 9]
first_item(numbers)


def list_function(x):
  return x[1]

n = [3, 5, 7]
print(list_function(n))




print("")
print("------ 7.10. Modifying an element of a list in a function ------")
def double_first(n):
  n[0] = n[0] * 2

numbers = [1, 2, 3, 4]
double_first(numbers)
print(numbers)


numbers = [1, 2, 3, 4]
def repeat_first(n):
  return n.insert(n[0], n[0] * 1)

repeat_first(numbers)
print(numbers)


def list_function(x):
  x[1] = x[1] + 3
  return x

n = [3, 5, 7]
print(list_function(n))




print("")
print("------ 7.11. List manipulation in functions ------")
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

n = [3, 5, 7]

def list_extender(lst):
  lst.append(9)
  return lst

print(list_extender(n))




print("")
print("------ 7.12. Printing out a list item by item in a function ------")
n = [3, 5, 7]

def print_list(x):
  for i in range(0, len(x)):
    print(x[i])

print_list(n)




print("")
print("------ 7.13. Modifying each element in a list in a function ------")
n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x

print(double_list(n))




print("")
print("------ 7.14. Passing a range into a function ------")
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print(my_function(list(range(3))))




print("")
print("------ 7.15. Iterating over a list in a function ------")
n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in numbers:
    result += i
  return result

print(total(n))




print("")
print("------ 7.16. Using strings in lists in functions ------")
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ""
  for word in words:
    result += word
  return result

print(join_strings(n))




print("")
print("------ 7.17. Using two lists as two arguments in a function ------")
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x,y):
  return x + y

print(join_lists(m, n))




print("")
print("------ 7.18. Using a list of lists in a function ------")
list_of_lists = [[1, 2, 3], [4, 5, 6]]

for lst in list_of_lists:
  for item in lst:
    print(item)

print("")

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists):
  results = list()
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results


print(flatten(n))
