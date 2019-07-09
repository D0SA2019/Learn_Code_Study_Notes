print("============================================")
print("Python 3 Programming Specialization")
print("Course 2 : Python Functions, Files, and Dictionaries")
print("Week 2 : Dictionaries and Dictionary Accumulation")
print("============================================")
print("============ 2.1. Dictionaries =============")
print("--------------------------------------------")
eng2sp = {}
eng2sp["one"] = "uno"
eng2sp["two"] = "dos"
eng2sp["three"] = "tres"
print(eng2sp)

eng2sp = {"one" : "uno", "two" : "dos", "three" : "tres"}
print(eng2sp)

eng2sp = {"three" : "tres", "one" : "uno", "two" : "dos"}
value = eng2sp["two"]
print(value)
print(eng2sp["one"])

print("")

mydict = {"cat" : 12, "dog" : 6, "elephant" : 23}
print(mydict["dog"])

medals = {"gold": 33, "silver": 17, "bronze": 12}
print(medals)
print(medals["silver"])

olympics = {"gold" : 7,
						"silver" : 8,
						"bronze" : 6}
print(olympics)
print(olympics["gold"])
print("")

print("============================================")
print("======== 2.2. Dictionary Operations ========")
print("--------------------------------------------")
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(inventory)

del inventory["pears"]
print(inventory)

print("")

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(inventory)

inventory["pears"] = 0
print(inventory)

print("")

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(inventory)

inventory["bananas"] = inventory["bananas"] + 200
print(inventory)

numItems = len(inventory)
print(numItems)

print("")

mydict = {"cat": 12, "dog": 6, "elephant": 23}
mydict["mouse"] = mydict["cat"] + mydict["dog"]
print(mydict["mouse"])

print("")

swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
print(swimmers)
swimmers["Phelps"] = swimmers["Phelps"] + 5
print(swimmers)

print("")

print("============================================")
print("========= 2.3. Dictionary Methods ==========")
print("--------------------------------------------")
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

for akey in inventory.keys():
	print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)

print("")

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

for k in inventory:
	print("Got key", k)

print("")

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

print(list(inventory.values()))
print(list(inventory.items()))

for k in inventory:
	print("Got", k, "that maps to", inventory[k])

print("")

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

print("apples" in inventory)
print("cherries" in inventory)

if "bananas" in inventory:
	print(inventory["bananas"])
else:
	print("We have no bananas")

print("")

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))
print(inventory.get("cherries", 0))
print(inventory.get("cherries", 999))
print(inventory)

print("")

mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
answer = mydict.get("cat") // mydict.get("dog")
print(answer)

mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
print("dog" in mydict)

mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
print(23 in mydict)

print("")

places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}
print(places)
places["Brazil"] = 2016
print(places)

print("")

medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
events = list(medal_events.keys())
print(events)

print("")

print("============================================")
print("======== 2.4. Aliasing and Copying =========")
print("============ with Dictionaries =============")
print("--------------------------------------------")
opposites = {"up": "down", "right": "wrong", "true": "false"}
alias = opposites
print(alias is opposites)

alias["right"] = "left"
print(opposites["right"])

print("")

opposites = {"up": "down", "right": "wrong", "true": "false"}
alias = opposites
acopy = opposites.copy()
acopy["right"] = "left"
print(opposites)
print(acopy)

print("")

mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
yourdict = mydict
yourdict["elephant"] = 999
print(mydict["elephant"])

print("============================================")
print("====== 2.5. Dictionary Accumulation ========")
print("--------------------------------------------")
f = open("scarlet.txt", "r")
txt = f.read()

t_count = 0
for c in txt:
	if c == "t":
		t_count = t_count + 1
print("t: " + str(t_count) + " occurrences")
f.close()

print("")

f = open("scarlet.txt", "r")
txt = f.read()

t_count = 0
s_count = 0

for c in txt:
	if c == "t":
		t_count = t_count + 1
	elif c == "s":
		s_count = s_count + 1

print("t: " + str(t_count) + " occurrences")
print("s: " + str(s_count) + " occurrences")
f.close()

print("")

f = open("scarlet.txt", "r")
txt = f.read()

x = {}
x["t"] = 0
x["s"] = 0

for c in txt:
	if c == "t":
		x["t"] = x["t"] + 1
	elif c == "s":
		x["s"] = x["s"] + 1

print("t: " + str(x["t"]) + " occurrences")
print("s: " + str(x["s"]) + " occurrences")
f.close()

print("")

f = open("scarlet.txt", "r")
txt = f.read()

x = {}
x['t'] = 0
x['s'] = 0
for c in txt:
    if c == 't':
        x[c] = x[c] + 1
    elif c == 's':
        x[c] = x[c] + 1

print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")
f.close()

print("")

f = open("scarlet.txt", "r")
txt = f.read()

x = {}
for c in txt:
	if c not in x:
		x[c] = 0

	x[c] = x[c] + 1

print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")
print(x)
f.close()

print("")

f = open('scarlet.txt', 'r')
txt = f.read()

letter_counts = {}
for c in txt:
	if c not in letter_counts:
		letter_counts[c] = 0
	letter_counts[c] = letter_counts[c] + 1

for c in letter_counts.keys():
	print(c + ": " + str(letter_counts[c]) + " occurrences")

f.close()

print("")

f = open("scarlet.txt", "r")
txt_lines = f.readlines()

print(len(txt_lines))
print(txt_lines[70:85])
f.close()

print("")

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
lst = sentence.split()
word_counts = {}

for word in lst:
	if word not in word_counts:
		word_counts[word] = 0
	word_counts[word] += 1

print(word_counts)

print("")

stri = "what can I do"
char_d = {}

for char in stri:
	if char not in char_d:
		char_d[char] = 0
	char_d[char] += 1

print(char_d)
print("")

print("============================================")
print("======== 2.6. Accumulating Results =========")
print("============ From a Dictionary =============")
print("--------------------------------------------")
f = open("scarlet.txt", "r")
txt = f.read()

x = {}
for c in txt:
	if c not in x:
		x[c] = 0
	x[c] = x[c] + 1

letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}

tot = 0
for y in x:
	if y in letter_values:
		tot = tot + letter_values[y] * x[y]

print(tot)

print("")

travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total = 0

for v in travel:
	total = total + travel[v]
print(total)

print("")

schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}

total_credits = 0

for k in schedule:
	total_credits += schedule[k]

print(total_credits)

print("")

d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = d.keys()
big_number = None
best_key_so_far = None
for k in ks:
	if big_number == None:
		big_number = d[k]
		best_key_so_far = k
	elif d[k] >= big_number :
		big_number = d[k]
		best_key_so_far = k
	else:
		pass

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))

print("")

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d = {}
min_val = None
min_value = None

for char in placement:
	if char not in d:
		d[char] = 0
	d[char] += 1

print(d)

for key in d:
	if min_val == None:
		min_val = d[key]
		min_value = key
	elif d[key] < min_val:
		min_val = d[key]
		min_value = key
	else:
		pass

print(min_value)

print("")

product = "iphone and android phones"
lett_d = {}
max_value = None
value = None

for char in product:
	if char not in lett_d:
		lett_d[char] = 0
	lett_d[char] += 1

print(lett_d)

for key in lett_d:
	if value == None:
		value = lett_d[key]
		max_value = key
	elif value <= lett_d[key]:
		value = lett_d[key]
		max_value = key
print(value)
print(max_value)

print("")

print("============================================")
print("====== 2.7. Assessments & Exercises ========")
print("--------------------------------------------")
d = {'apples': 15, 'grapes': 12, 'bananas': 35}
# print(d['banana'])
d['oranges'] = 20
print(len(d))
print('grapes' in d)
# print(d['pears'])
print(d.get('pears', 0))
fruits = d.keys()
print(fruits)
del d['apples']
print('apples' in d)

print("")

pirish = {
			"sir": "matey",
			"hotel": "fleabag inn",
			"student": "swabbie",
			"boy": "matey",
			"madam": "proud beauty",
			"professor": "foul blaggart",
			"restaurant": "galley",
			"your": "yer",
			"excuse": "arr",
			"students": "swabbies",
			"are": "be",
			"lawyer": "foul blaggart",
			"the": "th’",
			"restroom": "head",
			"my": "me",
			"hello": "avast",
			"is": "be",
			"man": "matey",
}

sentence = input("Enter a sentence : ").split()
translated = []

for word in sentence:
	if word in pirish:
		word = pirish[word]
	translated.append(word)

pirate_sentence = " ".join(translated)
print(pirate_sentence)

print("")

f = open('scarlet.txt', 'r')
text = f.read()
word_list = text.split()
words = {}
seven_letters = []
most_used = None

for word in word_list:
	if word not in words:
		words[word] = 0
	words[word] += 1

for wrd in words:
	if len(wrd) >= 7:
		seven_letters.append(wrd)

for wd in seven_letters:
	if most_used == None:
		most_used = wd
	else :
		if words[wd] > words[most_used]:
			most_used = wd
		else:
			pass
#print(words)
#print(seven_letters)
print(most_used)
print(words[most_used])

print("")

sentence = input("Please enter a sentence: ").lower()
chars = {}

for char in sentence:
	if char not in chars:
		chars[char] = 0
	chars[char] += 1

ord_chars = list(chars.keys())
ord_chars.sort()

print(ord_chars)

for it in ord_chars:
	print("{} {}".format(it, chars[it]))

print("")

medal_count = {"United States": 70, "Great Britain": 38, "China": 45, "Russia": 30, "Germany": 17}
print(medal_count)

print("")

swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}
swimmers["Phelps"] = 23
print(swimmers)

print("")

sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2}
sports_periods["hockey"]=3
print(sports_periods)

print("")

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
golds["Spain"] += 2
print(golds["Spain"])

print("")

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
countries = list(golds.keys())
print(countries)

print("")

medal_count = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}
belarus = medal_count["Belarus"]
print(belarus)

print("")

total_golds = {"Italy": 114,
								"Germany": 782,
								"Pakistan": 10,
								"Sweden": 627,
								"USA": 2681,
								"Zimbabwe": 8,
								"Greece": 111,
								"Mongolia": 24,
								"Brazil": 108,
								"Croatia": 34,
								"Algeria": 15,
								"Switzerland": 323,
								"Yugoslavia": 87,
								"China": 526,
								"Egypt": 26,
								"Norway": 477,
								"Spain": 133,
								"Australia": 480,
								"Slovakia": 29,
								"Canada": 22,
								"New Zealand": 100,
								"Denmark": 180,
								"Chile": 13,
								"Argentina": 70,
								"Thailand": 24,
								"Cuba": 209,
								"Uganda": 7,
								"England": 806,
								"Denmark": 180,
								"Ukraine": 122,
								"Bahamas": 12}
chile_golds = total_golds["Chile"]
print(chile_golds)

print("")

US_medals = {"Swimming": 33,
							"Gymnastics": 6,
							"Track & Field": 6,
							"Tennis": 3,
							"Judo": 2,
							"Rowing": 2,
							"Shooting": 3,
							"Cycling - Road": 1,
							"Fencing": 4,
							"Diving": 2,
							"Archery": 2,
							"Cycling - Track": 1,
							"Equestrian": 2,
							"Golf": 1,
							"Weightlifting": 1}

fencing_value = US_medals["Fencing"]
print(fencing_value)

print("")

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0

for k in Junior:
    credits += Junior[k]
print(credits)

print("")

str1 = "peter piper picked a peck of pickled peppers"
freq = {}

for char in str1:
	if char not in freq:
		freq[char] = 0
	freq[char] += 1
print(freq)

print("")

s1 = "hello"
counts = {}

for char in s1:
	if char not in counts:
		counts[char] = 0
	counts[char] += 1

print(counts)

print("")

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}

for word in str1.split():
	if word not in freq_words:
		freq_words[word] = 0
	freq_words[word] += 1

print(freq_words)

print("")

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d = {}

for word in sent.split():
	if word not in wrd_d:
		wrd_d[word] = 0
	wrd_d[word] += 1
print(wrd_d)

print("")

sally = "sally sells sea shells by the sea shore"
characters = {}
best_char = None

for c in sally:
	if c not in characters:
		characters[c] = 0
	characters[c] += 1

for i in list(characters.keys()):
	if best_char == None:
		best_char = i
	else:
		if characters[i] >= characters[best_char]:
			best_char = i

print("The most frequent letter is", best_char, "and it appears", characters[best_char], "times")

print("")

sally = "sally sells sea shells by the sea shore"
characters = {}
worst_char = None

for c in sally:
	if c not in characters:
		characters[c] = 0
	characters[c] += 1

for i in list(characters.keys()):
	if worst_char == None:
		worst_char = i
	else:
		if characters[i] <= characters[worst_char]:
			worst_char = i

print("The least frequent letter is", worst_char, "and it appears", characters[worst_char], "times")

print("")

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."

letter_counts = {}

for c in string1.lower():
	if c not in letter_counts:
		letter_counts[c] = 0
	letter_counts[c] += 1

print(letter_counts)

print("")

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = {}

for c in p.lower():
	if c not in low_d:
		low_d[c] = 0
	low_d[c] += 1

print(low_d)
