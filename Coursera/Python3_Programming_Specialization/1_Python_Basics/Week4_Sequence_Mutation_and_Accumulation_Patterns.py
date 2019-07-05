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

print("============================================")
print("====== 4.10. The Accumulator Pattern =======")
print("================ with Lists ================")
print("--------------------------------------------")
nums = [3, 5, 8]
accum = []
for w in nums:
	x = w ** 2
	accum.append(x)
print(accum)

print("")

alist = [4, 2, 8, 6, 5]
blist = []
for item in alist:
	blist.append(item+5)
print(blist)

lst = [3, 0, 9, 4, 1, 7]
new_list = []
for i in range(len(lst)):
	new_list.append(lst[i]+5)
print(new_list)

print("")

verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []
for word in verbs:
    word = word + "ing"
    ing.append(word)
print(ing)


numbs = [5, 10, 15, 20, 25]
newlist = []

for num in numbs:
    num += 5
    newlist.append(num)
print(newlist)


lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]
larger_nums = []
for number in lst_nums:
    number = number * 2
    larger_nums.append(number)
print(larger_nums)

print("============================================")
print("====== 4.11. The Accumulator Pattern =======")
print("=============== with Strings ===============")
print("--------------------------------------------")

s = input("Enter some text: ")
ac = ""

for c in s:
	ac = ac + c + "-" + c + "-"
print(ac)


s = "ball"
r = ""

for item in s:
	r = item.upper() + r

print(r)


str1 = "I love python"
chars = []
for char in str1:
    chars.append(char)
print(chars)


output = ""
for a in range(35):
    output = output + "a"
print(output)

print("============================================")
print("======== 4.13. Don’t Mutate A List =========")
print("===== That You Are Iterating Through =======")
print("--------------------------------------------")
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

for color in colors:
	print(color)

print("")

colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
initials = []

for color in colors:
	initials.append(color[0])

print(initials)

print("")

print("============================================")
print("====== 4.14. Assessments & Exercises =======")
print("--------------------------------------------")
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
len_verbs = len(verbs)
for i in range(len_verbs):
    verbing = verbs[i] + "ing"
    verbs.append(verbing)
del verbs[:len_verbs]
print(verbs)

print("")

classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]

upper = []
lower = []

for clas in classes:
    cls = clas.split()
    if cls[0] == "MATH":
        if int(cls[1]) >= 300 :
            upper.append(clas)
        else:
            lower.append(clas)
    elif cls[0] == "ENG":
        if int(cls[1]) >= 200 :
            upper.append(clas)
        else:
            lower.append(clas)
    elif cls[0] == "PSYCH":
        if int(cls[1]) >= 400 :
            upper.append(clas)
        else:
            lower.append(clas)
print(upper)
print(lower)

print("")

myList = [76, 92.3, 'hello', True, 4, 76]
myList.append("apple")
myList.append(76)
myList.insert(3, "cat")
myList.insert(0, 99)
print(myList.index("hello"))
print(myList.count(76))
myList.remove(76)
myList.pop(myList.index(True))
print(myList)

print("")

import keyword
test = ["else", "integer", "except", "elif"]
keyword_test = []

for word in test:
    val = keyword.iskeyword(word)
    keyword_test.append(val)

print(keyword_test)

print("")

import string
chars = ['h', '1', 'C', 'i', '9', 'True', '3.1', '8', 'F', '4', 'j']

nums = string.digits
is_num = []

for char in chars:
    if char in nums:
        v = True
    else:
        v = False
    is_num.append((char, v))

print(is_num)

print("")

sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

sports.insert(2, "horseback riding")
print(sports)

print("")

trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
del trav_dest[trav_dest.index("London")]
print(trav_dest)

print("")

trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']

trav_dest.append("Guadalajara")
print(trav_dest)

print("")

a = ["holiday", "celebrate!"]
quiet = a
quiet.append("company")
print(a)

print("")

b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)

print("")

sent = "Holidays can be a fun time when you have good company!"
phrase = sent
phrase = phrase + " Holidays can also be fun on your own!"
print(sent)
print(phrase)

print("")

sent = "The mall has excellent sales right now."
wrds = sent.split()
wrds[1] = 'store'
new_sent = " ".join(wrds)
print(sent)
print(wrds)
print(new_sent)

print("")

awards = ['Emmy', 'Tony', 'Academy', 'Grammy']
pos = awards.index("Tony")
print(pos)

print("")

str1 = "I love python"
chars = []

for char in str1:
    chars.append(char)
print(chars)

print("")

ael = "python!"
app = []

for char in ael:
    app.append(char)
print(app)

print("")

wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []

for word in wrds:
    word = word + "ed"
    past_wrds.append(word)
print(past_wrds)

print("")

original_str = "The quick brown rhino jumped over the extremely lazy fox"
num_words_list = []
list_str = original_str.split()

for word in list_str:
    num_words_list.append(len(word))

print(num_words_list)

print("")

lett = ""

for b in range(7):
    lett = lett + "b"

print(lett)

print("")

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

scores = scores.split()
a_scores = 0

for score in scores:
    if int(score) >= 90:
        a_scores += 1
print(a_scores)

print("")

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = ""

org_list = org.split()

for word in org_list:
    if word.lower() in stopwords:
        pass
    else:
        acro_word = word[0].upper()
        acro = acro + acro_word
print(acro)

print("")

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ""
sent_list = sent.split()

for word in sent_list:
    if word.lower() in stopwords:
        pass
    elif word == sent_list[-1]:
        acro_word = word[:2].upper()
        acro = acro + acro_word
    else:
        acro_word = word[:2].upper()
        acro = acro + acro_word + ". "
print(acro)

print("")

p_phrase = "was it a car or a cat I saw"
r_phrase = []
lst = p_phrase.split()

for word in lst:
    r_phrase.append(word[::-1])

r_phrase.reverse()
r_phrase = " ".join(r_phrase)
print(r_phrase)

print("")

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for items in inventory:
    item, number, price = items.split(",")
    print("The store has {} {}, each for {} USD.".format(number.strip(), item, price.strip()))
