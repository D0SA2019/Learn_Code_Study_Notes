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
