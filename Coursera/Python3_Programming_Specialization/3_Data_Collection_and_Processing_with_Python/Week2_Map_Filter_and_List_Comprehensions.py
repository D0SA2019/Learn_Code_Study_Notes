print("============================================")
print("Python 3 Programming Specialization")
print("Course 3 : Data Collection and Processing with Python")
print("Week 2 : Map, Filter, and List Comprehensions")

print("")

print("============================================")
print("================= 2.1. Map =================")
print("--------------------------------------------")
def doubleStuff(a_list):
	"""Return a new list in which contains doubles of the elements in a_list. """
	new_list = []
	for value in a_list:
		new_elem = 2 * value
		new_list.append(new_elem)
	return new_list

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)

print("")

def triple(value):
	return 3*value

def tripleStuff(a_list):
	new_seq = map(triple, a_list)
	return list(new_seq)

def quadrupleStuff(a_list):
	new_seq = map(lambda value: 4*value, a_list)
	return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)

things4 = quadrupleStuff(things)
print(things4)

print("")

things = [2, 5, 9]

things4 = list(map(lambda value: 4*value, things))
print(things4)

print(list(map(lambda value: 5*value, [1, 2, 3])))

print("")

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

greeting_doubled = list(map(lambda x: x*2, lst))
print(greeting_doubled)

print("")

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

abbrevs_upper = list(map(lambda x: x.upper(), abbrevs))
print(abbrevs_upper)

print("")

print("============================================")
print("=============== 2.2. Filter ================")
print("--------------------------------------------")
def keep_evens(nums):
	new_list = []
	for num in nums:
		if num % 2 == 0:
			new_list.append(num)
	return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

print("")

def keep_evens_filter(nums):
	new_seq = filter(lambda num: num % 2 == 0, nums)
	return list(new_seq)

print(keep_evens_filter([3, 4, 6, 7, 0, 1]))

print("")

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing = list(filter(lambda x: "w" in x, lst_check))
print(filter_testing)

print("")

lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]

lst2 = list(filter(lambda x: "o" in x, lst))
print(lst2)


print("")

print("============================================")
print("========= 2.3. List Comprehensions =========")
print("--------------------------------------------")
things = [2, 5, 9]
yourlist = [value * 2 for value in things]
print(yourlist)

print("")

def keep_evens_comp(nums):
	new_list = [num for num in nums if num % 2 == 0]
	return new_list

print(keep_evens_comp([3, 4, 6, 7, 0, 1]))

print("")

things = [3, 4, 6, 7, 0, 1]

print(list(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things))))

print([x * 2 for x in things if x % 2 == 0])

print("")

alist = [4,2,8,6,5]
blist = [num*2 for num in alist if num%2==1]
print(blist)

print("")

L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)

lst2 = [x for x in L if x > 10]
print(lst2)

print("")

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

compri = [x["name"] for x in tester["info"]]
print(compri)


print("")

print("============================================")
print("================= 2.4. Zip =================")
print("--------------------------------------------")
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []

for i in range(len(L1)):
	L3.append(L1[i] + L2[i])

print(L3)

L4 = list(zip(L1, L2))
print(L4)

L5 = []
for (x1, x2) in L4:
	L5.append(x1 + x2)
print(L5)


L6 = [x1 + x2 for (x1,x2) in list(zip(L1,L2))]
print(L6)


L7 = list(map(lambda x: x[0] + x[1], zip(L1, L2)))
print(L7)

print("")

def possible(word, blanked, guesses_made):
	if len(word) != len(blanked):
		return False

	for i in range(len(word)):
		bc = blanked[i]
		wc = word[i]
		if bc == "_" and wc in guesses_made:
			return False
		elif bc != "_" and bc!= wc:
			return False
	return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))

print("")

def possible1(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for (bc, wc) in zip(blanked, word):
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible1("wonderwall", "_on__r__ll", "otnqurl"))
print(possible1("wonderwall", "_on__r__ll", "wotnqurl"))

print("")

L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [(x+y) for (x,y) in list(zip(L1,L2)) if x>10 and y<5]
print(L3)


print("")

print("============================================")
print("======= 2.5. Assessments & Exercises =======")
print("--------------------------------------------")
things = [3, 5, -4, 7]

accum = []
for thing in things:
    accum.append(thing+1)
print(accum)

test = list(map(lambda x: x+1, things))
print(test)


print("")

def lengths_accum(strings):
	len_list = []
	for word in strings:
		accum = 0
		for char in word:
			accum += 1
		len_list.append(accum)
	return len_list

print(lengths_accum(["happy", "fun", "bless"]))


def lengths_map(strings):
	fun = list(map(lambda x: len(x), strings))
	return fun

print(lengths_map(["happy", "fun", "bless"]))



def lengths_list(strings):
	fun = [len(word) for word in strings]
	return fun

print(lengths_list(["happy", "fun", "bless"]))


print("")


things = [3, 5, -4, 7]

def positives_Acc(alist):
	new_list = []
	for num in alist:
		if num > 0:
			new_list.append(num)
	return new_list

print(positives_Acc(things))

def positives_Fil(alist):
	new_list = list(filter(lambda x: x > 0, alist))
	return new_list

print(positives_Fil(things))

def positives_Li_Com(alist):
	new_list = [num for num in alist if num > 0]
	return new_list

print(positives_Li_Com(things))


print("")

def longwords(strings):
	new_list = []
	for word in strings:
		if len(word) > 4:
			new_list.append(word)
	return new_list

print(longwords(["smile", "joy", "furniture", "camera", "ring"]))

def longwords_Fil(strings):
	new_list = list(filter(lambda x: len(x) > 4, strings))
	return new_list

print(longwords_Fil(["smile", "joy", "furniture", "camera", "ring"]))

def longwords_Li_Comp(strings):
	new_list = [word for word in strings if len(word) > 4]
	return new_list

print(longwords_Li_Comp(["smile", "joy", "furniture", "camera", "ring"]))

print("")


def longlengths(strings):
	new_list = [len(word) for word in strings if len(word) >= 4]
	return new_list

print(longlengths(["smile", "joy", "furniture", "camera", "ring"]))


def longlengths_filter(strings):
	new_list = list(filter(lambda x: x >= 4, list(map(lambda x: len(x), strings))))
	return new_list

print(longlengths_filter(["smile", "joy", "furniture", "camera", "ring"]))


print("")

nums = [3, 2, 2, -1, 1]

def sumSquares(L):
	accum = 0
	for num in L:
		accum += (num*num)
	return accum

print(sumSquares(nums))


def sumSquares_map(L):
	accum = sum(list(map(lambda x: x*x, L)))
	return accum

print(sumSquares_map(nums))


print("")

L1 = [1, 2, 3, 4]
L2 = [4, 3, 2, 3]
L3 = [0, 5, 0, 5]

tups = list(zip(L1,L2,L3))
print(tups)

print("")

L1 = [1, 2, 3, 4]
L2 = [4, 3, 2, 3]
L3 = [0, 5, 0, 5]

maxs = [max(num) for num in list(zip(L1,L2,L3))]
print(maxs)


print("")


tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}


compri_sample = [i["name"] for i in tester["info"] for t in i.keys() if i[t] == "Junior"]
print(compri_sample)


print("")

def onelist(lst):
    result = []
    for each_list in lst:
        for item in each_list:
            result.append(item)
    return result

L = [["hi", "bye"], ["hello", "goodbye"], ["hola", "adios", "bonjour", "au revoir"]]

result2 = [item for items in L for item in items]
print(result2)


print("")

tester = {'info': [
         {"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science", 'important classes': ['SI 106', 'ENGLISH 125', 'SI 110', 'AMCULT 202']},
         {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science', "important classes": ['SI 106', 'SI 410', 'PSYCH 111']},
         {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology', 'important classes': ['WOMENSTD 220', 'SOC 101', 'ENS 384']},
         {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science', "important classes": ['SOC 101', 'AMCULT 334', 'EECS 281']},
         {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History', 'important classes': ['ENGLISH 125', 'HIST 259', 'ENGLISH 130']},
         {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior', 'important classes': ['PIANO 101', 'STUDIO 300', 'THEORY 229', 'MUSC 356']}]}


class_sched = [t for i in tester["info"] for t in i["important classes"]]
print(class_sched)


print("")

nums = [[4, 3, 12, 10], [8, 7, 6], [5, 18, 15, 7, 11], [9, 4], [24, 20, 17], [3, 5]]

threes = [num for nlist in nums for num in nlist if num % 3 == 0]
print(threes)


print("")


lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing = list(map(lambda a : "Fruit: {}".format(a), lst_check))
print(map_testing)


print("")

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries = list(filter(lambda x: x[0] == "B", countries))
print(b_countries)


print("")

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

first_names = [name[1] for name in people]
print(first_names)

print("")

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst2 = [i*2 for i in lst]
print(lst2)


print("")


students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed = [i[0] for i in students if i[1] >= 70]
print(passed)


print("")

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']


opposites = list(filter(lambda x: len(x[0]) > 3 and len(x[1]) > 3, list(zip(l1,l2))))
print(opposites)


print("")


species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]


pop_info = list(zip(species, population))
endangered = [x[0] for x in pop_info if x[1] < 2500]
print(endangered)
