print("============================================")
print("Python 3 Programming Specialization")
print("Course 1 : Python Basics")
print("Week 4 : Sequence Mutation and Accumulation Patterns")
print("============================================")
print("============= 4.1. Mutability ==============")
print("--------------------------------------------")
fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)

print("")

alist = ["a", "b", "c", "d", "e", "f"]
alist[1:3] = ["x", "y"]
print(alist)

print("")

alist = ["a", "b", "c", "d", "e", "f"]
alist[1:3] = []
print(alist)

print("")

alist = ["a", "d", "f"]
alist[1:1] = ["b", "c"]
print(alist)

alist[4:4] = ["e"]
print(alist)

print("")

greeting = "Hello, world!"
newGreeting = "J" + greeting[1:]
print(newGreeting)
print(greeting)

print("")

phrase = "many moons"
print(phrase)
phrase_expanded = phrase + " and many stars"
print(phrase_expanded)
phrase_larger = phrase_expanded + " litter"
print(phrase_larger)
phrase_complete = "M" + phrase_larger[1:] + " the night sky."
print(phrase_complete)
excited_phrase_complete = phrase_complete[:-1] + "!"
print(excited_phrase_complete)

print("")

alist = [4, 2, 8, 6, 5]
alist[2] = True
print(alist)

print("============================================")
print("======= 4.2. List Element Deletion =========")
print("--------------------------------------------")
a = ["one", "two", "three"]
del a[1]
print(a)

alist = ["a", "b", "c", "d", "d", "f"]
del alist[1:5]
print(alist)

alist = ["a", "b", "c", "d", "d", "f"]
alist.remove("b")
print(alist)


print("============================================")
print("======= 4.3. Objects and References ========")
print("--------------------------------------------")
a = "banana"
b = "banana"

print(a is b)
print(id(a))
print(id(b))

print("")

a = [81, 82, 83]
b = [81, 82, 83]

print(a is b)

print(a == b)

print(id(a))
print(id(b))

print("============================================")
print("============== 4.4. Aliasing ===============")
print("--------------------------------------------")
a = [81, 82, 83]
b = a

print(a is b)

print("")

a = [81, 82, 83]
b = [81, 82, 83]

print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)

print("============================================")
print("=========== 4.5. Cloning Lists =============")
print("--------------------------------------------")
a = [81, 82, 83]

b = a[:]
print(a == b)
print(a is b)

b[0] = 5
print(a)
print(b)

alist = [4, 2, 8, 6, 5]
blist = alist * 2
blist[3] = 999
print(alist)


print("============================================")
print("========= 4.6. Methods on Lists ============")
print("--------------------------------------------")
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)

print(mylist.count(12))
print(mylist.count(5))

print(mylist.index(3))
print(mylist.index(27))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)

mylist.pop(0)
print(mylist)


print("============================================")
print("====== 4.7. Append vs. Concatenate =========")
print("--------------------------------------------")
origlist = [45, 32, 88]
origlist.append("cat")
print(origlist)

origlist = origlist + ["cat"]
print(origlist)

print("")

origlist = [45, 32, 88]
print("origlist:", origlist)
print("the identifier:", id(origlist))
newlist = origlist + ["cat"]
print("newlist:", newlist)
print("the identifier:", id(newlist))
origlist.append("cat")
print("origlist:", origlist)
print("the identifier:", id(origlist))

print("")

st = "Warmth"
a = []
b = a + [st[0]]
c = b + [st[1]]
d = c + [st[2]]
e = d + [st[3]]
f = e + [st[4]]
g = f + [st[5]]
print(g)

st = "Warmth"
a = []
a.append(st[0])
a.append(st[1])
a.append(st[2])
a.append(st[3])
a.append(st[4])
a.append(st[5])
print(a)

print("")


print("============================================")
print("=== 4.8. Non-Mutating Methods on Strings ===")
print("--------------------------------------------")
ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)
print(ss)

print("")

ss = "     Hello, World     "

els = ss.count("l")
print(els)

print("***" + ss.strip() + "***")

news = ss.replace("o", "***")
print(news)

print("")

food = "banana bread"
print(food.upper())

print("============================================")
print("======== 4.9. String Format Method =========")
print("--------------------------------------------")

name = "Rodney Dangerfield"
score = -1    # No respect!
print("Hello " + name + ". Your score is " + str(score))

scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]

for person in scores:
  name = person[0]
  score = person[1]
  print("Hello " + name + ". Your score is " + str(score))

scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]

for person in scores:
  name = person[0]
  score = person[1]
  print("Hello {}. Your score is {}.".format(name, score))


person = input("Your name: ")
greeting = "Hello {}!".format(person)
print(greeting)

person = input("Enter your name: ")
print("Hello {}!".format(person))

origPrice = float(input("Enter the original price: $"))
discount = float(input("Enter discount percentage: "))
newPrice = (1 - discount/100)*origPrice
calculation = "${} discounted by {}% is ${}.".format(origPrice, discount, newPrice)
print(calculation)


origPrice = float(input("Enter the original price: $"))
discount = float(input("Enter discount percentage: "))
newPrice = (1 - discount/100)*origPrice
calculation = "${:.2f} discounted by {}% is ${:.2f}.".format(origPrice, discount, newPrice)
print(calculation)

print("")

name = "Sally"
greeting = "Nice to meet you"
s = "Hello, {}. {}."

print(s.format(name, greeting))
print(s.format(greeting, name))

print("")

a = 5
b = 9
setStr = "The set is {{{}, {}}}.".format(a, b)
print(setStr)

print("")

x = 2
y = 6
print("sum of {} and {} is {}; product: {}.".format(x, y, x+y, x*y))

v = 2.34567
print("{:.1f} {:.2f} {:.7f}".format(v, v, v))
