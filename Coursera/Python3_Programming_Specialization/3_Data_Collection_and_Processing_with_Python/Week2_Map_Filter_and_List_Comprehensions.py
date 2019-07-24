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
