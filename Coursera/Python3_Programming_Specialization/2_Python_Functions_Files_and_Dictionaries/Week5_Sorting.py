print("============================================")
print("Python 3 Programming Specialization")
print("Course 2 : Python Functions, Files, and Dictionaries")
print("Week 5 : Sorting")
print("============================================")
print("====== 5.1. Invoking .sort and sorted ======")
print("--------------------------------------------")
L1 = [1, 7, 4, -2, 3]
L2 = ["Cherry", "Apple", "Blueberry"]

L1.sort()
print(L1)
L2.sort()
print(L2)

print("")

L2 = ["Cherry", "Apple", "Blueberry"]

L3 = sorted(L2)
print(L3)
print(sorted(L2))
print(L2)

print("")

L2.sort()
print(L2)
print(L2.sort())

print("")

print("============================================")
print("===== 5.2. Optional Reverse Parameter ======")
print("--------------------------------------------")
L2 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L2, reverse=True))

print("")
lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted = sorted(lst, reverse=True)
print(lst)
print(lst_sorted)

print("")

print("============================================")
print("======= 5.3. Optional Key Parameter ========")
print("--------------------------------------------")
L1 = [1, 7, 4, -2, 3]

def absolute(x):
	if x >= 0:
		return x
	else:
		return -x

print(absolute(3))
print(absolute(-119))

for y in L1:
	print(absolute(y))

print("")

L2 = sorted(L1, key=absolute)
print(L2)

print(sorted(L1, reverse=True, key=absolute))

print("")

L1 = [1, 7, 4, -2, 3]

def absolute(x):
    print("--- figuring out what to write on the post-it note for " + str(x))
    if x >= 0:
        return x
    else:
        return -x

print("About to call sorted")
L2 = sorted(L1, key=absolute)
print("Finished execution of sorted")
print(L2)

print("")

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

def second_let(somestr):
	return somestr[1]

func_sort = sorted(ex_lst, key=second_let)
print(func_sort)

print("")

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(astring):
	return astring[-1]

nums_sorted = sorted(nums, reverse=True, key=last_char)
print(nums_sorted)

print("")

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums_sorted_lambda = sorted(nums, reverse=True, key=lambda x: x[-1])
print(nums_sorted_lambda)

print("")

print("============================================")
print("===== 5.4. Sorting A Dictionary's Keys =====")
print("--------------------------------------------")
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}

for x in L:
	if x in d:
		d[x] = d[x] + 1
	else:
		d[x] = 1

print(d)

for x in d.keys():
	print("{} appears {} times".format(x, d[x]))

print("")

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}

for x in L:
	if x in d:
		d[x] += 1
	else:
		d[x] = 1

y = sorted(d.keys())

for k in y:
	print("{} appears {} times".format(k, d[k]))

print("")

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}

for x in L:
	if x in d:
		d[x] += 1
	else:
		d[x] = 1

y = sorted(d.keys(), key=lambda k: d[k], reverse=True)

for k in y:
    print("{} appears {} times".format(k, d[k]))

print("")

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

def g(k):
    return d[k]

y =(sorted(d.keys(), key=g, reverse=True))

for k in y:
    print("{} appears {} times".format(k, d[k]))

print("")

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

for k in sorted(d, key=lambda k: d[k], reverse=True):
      print("{} appears {} times".format(k, d[k]))

print("")

L = [4, 5, 1, 0, 3, 8, 8, 2, 1, 0, 3, 3, 4, 3]

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

def g(k, d):
    return d[k]

ks = d.keys()
print(sorted(ks, key=lambda x: d[x]))
print(sorted(ks, key=lambda x: g(x, d)))

print("")

dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_keys = sorted(dictionary)
print(sorted_keys)

print("")

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

grocery_keys_sorted = sorted(groceries)
print(grocery_keys_sorted)

print("")

dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_values = sorted(dictionary, key=lambda k: dictionary[k], reverse=True)
print(sorted_values)

print("")

print("============================================")
print("============ 5.5. Breaking Ties ============")
print("--------------------------------------------")
tups = [('A', 3, 2),
        ('C', 1, 4),
        ('B', 3, 1),
        ('A', 2, 4),
        ('C', 1, 2)]

for tup in sorted(tups):
	print(tup)

print("")

fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']

new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))

for fruit in new_order:
  print(fruit)

print("")

fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']

new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name), reverse=True)

for fruit in new_order:
  print(fruit)


print("")

fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']

new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)


print("")

weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

sorted_weather = sorted(weather, key=lambda w: (w, weather[w]['temp']))
print(sorted_weather)

sorted_weather = sorted(weather, key=lambda w: (w, -weather[w]['temp']), reverse=True)
print(sorted_weather)

print("")

print("============================================")
print("=== 5.6. When to Use a Lambda Expression ===")
print("--------------------------------------------")
states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: len(states[state][0])))

print("")

def s_cities_count(city_list):
  ct = 0
  for city in city_list:
    if city[0] == "S":
      ct += 1
  return ct


states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
            "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
            "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: s_cities_count(states[state])))
