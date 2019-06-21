print("============================================")
print("Python 3 Programming Specialization")
print("Course 1 : Python Basics")
print("Week 2 : Sequences and Iteration")
print("============================================")
print("=============== 2.1. Strings ===============")
print("--------------------------------------------")
t = (5,)
print(type(t))

x = (5)
print(type(x))
print("============================================")
print("========== 2.2. The Index Operator =========")
print("--------------------------------------------")
school = "Luther College"
m = school[2]
print(m)

lastchar = school[-1]
print(lastchar)

print("")

numbers = [17, 123, 87, 34, 66, 8398, 44]
print(numbers[2])
print(numbers[9-8])
print(numbers[-2])

print("")

prices = [1.99, 2.00, 5.50, 20.95, 100.98]
print(prices[0])
print(prices[-1])
print(prices[3-5])

print("")

new_lst = ["NFLX", "AMZN", "GOOGL", "DIS", "XOM"]
part_of_new_lst = new_lst[0]
print(part_of_new_lst)

print("")

lst = [0]
n_lst = lst[0]

print(lst)
print(n_lst)

print("")

s = "python rocks"
print(s[3])

s = "python rocks"
print(s[2] + s[-4])

alist = [3, 67, "cat", [56, 57, "dog"], [], 3.14, False]
print(alist[5])

lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
output = lst[33]
print(output)

l = ("hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones")
checking = l[22]
print(checking)

lst = "Every chess or checkers game begins from the same position and has a finite number of moves that can be played. While the number of possible scenarios and moves is quite large, it is still possible for computers to calculate that number and even be programmed to respond well against a human player..."
output = lst[-1]
print(output)

print("============================================")
print("================ 2.3. Lenght ===============")
print("--------------------------------------------")
fruit = "Banana"
print(len(fruit))

fruit = "Banana"
sz = len(fruit)
last = fruit[sz-1]
print(last)

alist = ["hello", 2.0, 5]
print(len(alist))
print(len(alist[0]))

print("")

s = "python rocks"
print(len(s))

alist = [3, 67, "cat", 3.14, False]
print(len(alist))

L = [0.34, '6', 'SI106', 'Python', -2]
print(len(L[1:-1]))

lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
output = len(lst)
print(output)

print("============================================")
print("========== 2.4. The Slice Operator =========")
print("--------------------------------------------")
singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])

print("")

fruit = "banana"
print(fruit[:3])
print(fruit[3:])
print(fruit[:])

print("")

a_list = ["a", "b", "c", "d", "e", "f"]
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])

print("")

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])

print(len(julia))

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)

print("")

s = "python rocks"
print(s[3:8])

alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
print(alist[4:])

new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]
sub_lst = new_lst[8:12]
print(sub_lst)

print("============================================")
print("===== 2.5. Concatenation and Repetition=====")
print("--------------------------------------------")
fruit = ["apple", "orange", "banana", "cherry"]
print([1, 2] + [3, 4])
print(fruit + [6, 7, 8, 9])

print([0] * 4)
print([0, 1] * 4)
print(fruit * 4)
print((fruit + [1] )* 4)
print(fruit + [1] * 4)

print("")

alist = [1,3,5]
blist = [2,4,6]
print(alist + blist)

alist = [1,3,5]
print(alist * 3)

print("============================================")
print("=========== 2.6. Count and Index ===========")
print("--------------------------------------------")
a = "I have had an apple on my desk before!"
print(a.count("e"))
print(a.count("ha"))

print("")

z = ["atoms", 4, "neutron", 6, "proton", 4, "electron", 4, "electron", "atoms"]
print(z.count("4"))
print(z.count(4))
print(z.count("a"))
print(z.count("electron"))

print("")

music = "Pull out your music and dancing can begin"
bio = ["Metatarsal", "Metatarsal", "Fibula", [], "Tibia", "Tibia", 43, "Femur", "Occipital", "Metatarsal"]

print(music.index("m"))
print(music.index("your"))

print(bio.index("Metatarsal"))
print(bio.index([]))
print(bio.index(43))

print("============================================")
print("=========== 2.7. Split and Join ============")
print("--------------------------------------------")
song = "The rain in Spain..."
wds = song.split()
print(wds)

song = "The rain in Spain..."
wds = song.split("ai")
print(wds)

print("")

wds = ["red", "blue", "green"]
glue = ";"
s = glue.join(wds)
print(s)
print(wds)

print("***".join(wds))
print("".join(wds))

print("")

lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]

output = lst[5:13]
print(output)

str1 = "OH THE PLACES YOU'LL GO"
output = str1.split()
print(output)
print("============================================")
print("======= 2.8. Assessments & Exercises =======")
print("--------------------------------------------")
let = "z"
let_two = "p"
c = let_two + let
m = c * 5
print(m)

sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

last = sports[-3:]
print(last)

by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"

message = by + " " + az + io + ", " + qy
print(message)

ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
new = ls[2:4]
print(new)

l = ['w', '7', 0, 9]
m = l[1:2]
print(m)
print(type(m))

l = ['w', '7', 0, 9]
m = l[1]
print(m)
print(type(m))

b = "My, what a lovely day"
x = b.split(',')
print(x)
print(type(x))

b = "My, what a lovely day"
x = b.split(',')
z = "".join(x)
y = z.split()
a = "".join(y)
print(x)
print(z)
print(y)
print(a)
print(type(a))

nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
how_many = nums.count(9)
print(how_many)

nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
nums = nums[:4] + nums[5:]
print(nums)

lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]
end_elem = lst[-1]
print(end_elem)

lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]
num_lst = len(lst)
print(num_lst)

sent = "The bicentennial for our university was in 2017"
wrds = sent.split()
print(wrds)
