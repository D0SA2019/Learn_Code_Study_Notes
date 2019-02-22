print("")
print("------ 5. Python Lists and Dictionaries ------")

print("")
print("------ 5.1. Introduction to Lists ------")
zoo_animals = ["pangolin", "cassowary", "sloth", "panda" ]

if len(zoo_animals) > 3:
  print("The first animal at the zoo is the " + zoo_animals[0])
  print("The second animal at the zoo is the " + zoo_animals[1])
  print("The third animal at the zoo is the " + zoo_animals[2])
  print("The fourth animal at the zoo is the " + zoo_animals[3])



print("")
print("------ 5.2. Access by Index ------")
numbers = [5, 6, 7, 8]
print("Adding the numbers at indices 0 and 2...")
print(numbers[0] + numbers[2])
print("Adding the numbers at indices 1 and 3...")
print(numbers[1] + numbers[3])



print("")
print("------ 5.3. New Neighbors ------")
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
print(zoo_animals)
zoo_animals[2] = "hyena"
print(zoo_animals)
zoo_animals[3] = "panda"
print(zoo_animals)



print("")
print("------ 5.4. Late Arrivals & List Length ------")
letters = ["a", "b", "c"]
print(len(letters))
print(letters)
letters.append("d")
print(len(letters))
print(letters)

print("")
suitcase = []
suitcase.append("sunglasses")
suitcase.append("lotion")
suitcase.append("book")
suitcase.append("map")

list_length = len(suitcase)
print("There are %d items in the suitcase." % (list_length))
print(suitcase)


print("")
print("------ 5.5. List Slicing ------")
letters = ["a", "b", "c", "d", "e"]
slice = letters[1:3]
print(slice)
print(letters)

print("")
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
first = suitcase[0:2]
middle = suitcase[2:4]
last =  suitcase [4:]
print(middle)
print(last)
print(suitcase)


print("")
print("------ 5.6. Slicing Lists and Strings ------")
animals = "catdogfrog"
cat = animals[:3]
dog = animals[3:6]
frog = animals[6:]
print(cat)
print(dog)
print(frog)
print(animals)



print("")
print("------ 5.7. Maintaining Order ------")
animals = ["ant", "bat", "cat"]
print(animals.index("bat"))

animals.insert(1, "dog")
print(animals)

print("")
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
animals.insert(duck_index, "cobra")
print(animals)



print("")
print("------ 5.8. For One and All ------")
my_list = [1,9,3,8,5,7]

for number in my_list:
  print(number * 2)



print("")
print("------ 5.9. More with `for` ------")
animals = ["cat", "ant", "bat"]
animals.sort()
print(animals)
for animal in animals:
  print(animal)

print("")
start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
  square_list.append(number ** 2)

print(square_list)
square_list.sort()
print(square_list)



print("")
print("------ 5.10. This Next Part is Key ------")
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print(residents['Puffin'])
print(residents["Sloth"])
print(residents["Burmese Python"])



print("")
print("------ 5.11. New Entries ------")
menu = {}
menu['Chicken Alfredo'] = 14.50
print(menu['Chicken Alfredo'])

menu["Onion Soup"] = 6.70
menu["French Fries"] = 3.40
menu["Tiramisu"] = 7.50

print("There are " + str(len(menu)) + " items on the menu.")
print(menu)



print("")
print("------ 5.12. Changing Your Mind ------")
zoo_animals = { 'Unicorn' : 'Cotton Candy House', 'Sloth' : 'Rainforest Exhibit', 'Bengal Tiger' : 'Jungle House', 'Atlantic Puffin' : 'Arctic Exhibit', 'Rockhopper Penguin' : 'Arctic Exhibit'}

del zoo_animals['Unicorn']
del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]
zoo_animals["Rockhopper Penguin"] = "Desert Exhibit"

print(zoo_animals)



print("")
print("------ 5.13. Remove a Few Things ------")
beatles = ["john", "paul", "george", "ringo", "stuart"]
beatles.remove("stuart")
print(beatles)

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove("dagger")
print(backpack)


print("")
print("------ 5.14. It's Dangerous to Go Alone! Take This ------")

my_dict = {
  "fish" : ["c", "a", "r", "p"],
  "cash" : -4483,
  "luck" : "good"
}

print(my_dict["fish"][0])

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pouch'].sort()
inventory["pocket"] = ["seashell", "strange berry", "lint"]
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
inventory["gold"] += 50

print(inventory)


print("")
print("---------------------------------------------------------")
print("------ A Day At The Supermarket ------")
print("---------------------------------------------------------")
print("------ 5.1. BeFOR We Begin ------")
for item in [1, 3, 21]:
  print(item)

names = ["Adam","Alex","Mariah","Martine","Columbus"]
for name in names :
  print(name)


print("")
print("------ 5.2. This is KEY! ------")
d = {"foo" : "bar"}

for key in d:
  print(d[key])

webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}
for item in webster:
  print(webster[item])



print("")
print("------ 5.3. Control Flow and Looping ------")
numbers = [1, 3, 4, 7]
for number in numbers:
  if number > 6:
    print(number)
print("We printed 7.")

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for item in a :
  if item % 2 == 0:
    print(item)



print("")
print("------ 5.4. Lists + Functions ------")
def count_small(numbers):
  total = 0
  for n in numbers:
    if n < 10:
      total = total + 1
  return total

lotto = [4, 8, 15, 16, 23, 42]
small = count_small(lotto)
print(small)


def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count += 1
  return count


print(fizz_count(["fizz", "cat", "fizz"]))



print("")
print("------ 5.5. String Looping ------")
for letter in "Codecademy":
  print(letter)

print("")
print("")

word = "Programming is fun!"

for letter in word:
  if letter == "i":
    print(letter)



print("")
print("------ 5.6. Your Own Store ------")
shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

def compute_bill():
  total = 0
  for item in shopping_list:
    if stock[item] > 0 :
      total += prices[item]
      stock[item] -=1
  return total
  print(total)

print(compute_bill())
