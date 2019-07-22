print("============================================")
print("Python 3 Programming Specialization")
print("Course 3 : Data Collection and Processing with Python")
print("Week 1 : Nested Data and Nested Iteration")

print("")

print("============================================")
print("============ 1.1. Nested Lists =============")
print("--------------------------------------------")
nested1 = [["a", "b", "c"], ["d", "e"], ["f", "g", "h"]]
print(nested1[0])
print(len(nested1))
print(len(nested1[1]))
nested1.append(["i"])
for L in nested1:
	print(L)

print("")

nested1 = [["a", "b", "c"], ["d", "e"], ["f", "g", "h"]]
y = nested1[1]
print(y)
print(y[0])

print([10, 20, 30][1])
print(nested1[1][0])

print("")

nested1 = [["a", "b", "c"], ["d", "e"], ["f", "g", "h"], ["i"]]
print(nested1)
nested1[1] = [1, 2, 3]
print(nested1)
nested1[1][0] = 100
print(nested1)

print("")

nested2 = [{'a': 1, 'b': 3}, {'a': 5, 'c': 90, 5: 50}, {'b': 3, 'c': "yes"}]
print(nested2)
print(nested2[1])
print(nested2[1]["c"])
nested2[1]["c"] = 7
print(nested2[1])
print(nested2[2])
nested2[2]["c"] = "no"
print(nested2[2])
print(nested2)

print("")

def square(x):
	return x*x

L = [square, abs, lambda x: x+1]

print("***names***")
for f in L:
	print(f)

print("***call each of them***")
for f in L:
	print(f(-2))

print("***just the first one in the list***")
print(L[0])
print(L[0](3))


print("")

animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]
idx1 = animals[1][0]
print(idx1)


print("")

data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]

plant = data[7][0][0]
print(plant)

print("")

print("============================================")
print("========= 1.2. Nested Dictionaries =========")
print("--------------------------------------------")
info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }

color = info["personal_data"]["physical_features"]["color"]
print(color)

print("")

print("============================================")
print("=== 1.3. JSON Format and the JSON Module ===")
print("--------------------------------------------")
import json
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)

print("")

print(type(d))
print(d.keys())
print(d["resultCount"])
print(d)

print("")

def pretty(obj):
	return json.dumps(obj, indent=2)

d = {'key1': {'c': True, 'a': 90, 5: 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print("")
print(pretty(d))
