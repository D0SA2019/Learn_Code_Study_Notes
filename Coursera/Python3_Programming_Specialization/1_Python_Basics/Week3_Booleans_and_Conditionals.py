print("============================================")
print("Python 3 Programming Specialization")
print("Course 1 : Python Basics")
print("Week 3 : Booleans and Conditionals")
print("============================================")
print("========= 3.1. Boolean Expressions =========")
print("--------------------------------------------")
print(True)
print(type(True))
print(type(False))

print("")

print(type(True))
print(type("True"))

print("")

print(5 == 5)
print(5 == 6)

print("============================================")
print("========== 3.2. Logical Operators ==========")
print("--------------------------------------------")
x = 5
print(x>0 and x<10)

n = 25
print(n%2 == 0 or n%3 == 0)

print("============================================")
print("===== 3.3. The in and not in Operators =====")
print("--------------------------------------------")
print("p" in "apple")
print("i" in "apple")
print("ap" in "apple")
print("pa" in "apple")

print("")

print("a" in "a")
print("apple" in "apple")
print("" in "a")
print("" in "apple")

print("")

print("x" not in "apple")

print("")

print("a" in ["a", "b", "c", "d"])
print(9 in [3, 2, 9, 10, 9.0])
print("wow" not in ["gee wiz", "gosh golly", "wow", "amazing"])

print("")

print("a" in ["apple", "absolutely", "application", "nope"])

print("============================================")
print("======== 3.5. Conditional Execution ========")
print("--------------------------------------------")
x = 15

if x % 2 == 0:
	print(x, "is even")
else:
	print(x, "is odd")

print("")

courses = ["ENGR 101", "SI 110", "ENG 125", "SI 106", "CHEM 130"]

if "SI 106" in courses:
    output = "You can apply to SI!"
else :
    output = "Take SI 106!"
print(output)

print("")

a = 20
b = 15

if b > a :
	a = a * 2
else:
	pass

c = a + b
print(c)

print("============================================")
print("=========== 3.6. Unary Selection ===========")
print("--------------------------------------------")
x = 10
if x < 0:
	print("The negative number ", x, " is not valid here.")
print("This is always printed.")

x = -10
if x < 0:
	print("The negative number ", x, " is not valid here.")
print("This is always printed.")

print("============================================")
print("========= 3.7. Nested conditionals =========")
print("--------------------------------------------")
x = 10
y = 10

if x < y:
    print("x is less than y")
else:
    if x > y:
        print("x is greater than y")
    else:
        print("x and y must be equal")

print("============================================")
print("======== 3.8. Chained conditionals =========")
print("--------------------------------------------")
x = 10
y = 10

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")


print("")

x = 3
y = 5
z = 2

if x < y and x < z:
    print("a")
elif y < x and y < z:
    print("b")
else:
    print("c")

print("")

str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"

if "false" in str1:
    output = "False. You aren’t you?"
elif "true" in str1:
	output = "True! You are you!"
else:
	output = "Neither true nor false!"
print(output)

print("")

percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = []

for rain in percent_rain:
	if rain > 90:
		resps.append("Bring an umbrella.")
	elif rain > 80:
		resps.append("Good for the flowers?")
	elif rain > 50:
		resps.append("Watch out for clouds!")
	else:
		resps.append("Nice day!")
print(resps)


print("")

x = 64
output = []

if x > 63:
    output.append(True)
elif x > 55:
    output.append(False)
else:
    output.append("Neither")

if x > 67:
    output.append(True)
else:
    output.append(None)
print(output)


print("============================================")
print("====== 3.10. The Accumulator Pattern =======")
print("============ with Conditionals =============")
print("--------------------------------------------")
phrase = "What a wonderful day to program"
tot = 0

for char in phrase:
	if char != " ":
		tot = tot + 1

print(tot)

s = "what if we went to the zoo"
x = 0

for i in s:
	if i in ["a", "e", "i", "o", "u"]:
		x += 1

print(x)


nums = [9, 3, 8, 11, 5, 29, 2]
best_num = 0

for n in nums:
	if n > best_num:
		best_num = n

print(best_num)

nums = [9, 3, 8, 11, 5, 29, 2]
best_num = nums[0]

for n in nums:
	if n > best_num:
		best_num = n

print(best_num)

nums = [-9, -3, -8, -11, -5, -29, -2]
best_num = nums[0]

for n in nums:
	if n > best_num:
		best_num = n

print(best_num)


print("")

words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0

for word in words:
    len_word = len(word)
    if len_word > 3:
        num_words += 1

print(num_words)

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = list()

for word in words:
    if word[-1] == "e":
        word = word + "d"
        past_tense.append(word)
    else:
        word = word + "ed"
        past_tense.append(word)

print(past_tense)

print("============================================")
print("====== 3.11. Assessments & Exercises =======")
print("--------------------------------------------")

score = int(input("Enter the score: "))

if score >= 90:
	grade = "A"
elif 80 <= score < 90:
	grade = "B"
elif 70 <= score < 80:
	grade = "C"
elif 60 <= score < 70:
	grade = "D"
else:
	grade = "F"

print(grade)

year = int(input("Enter the year: "))

if year % 100 == 0:
	if year % 400 == 0:
		is_leap = True
	else:
		is_leap = False
elif year % 4 == 0:
	is_leap = True
else:
	is_leap = False

print(is_leap)

print("")

print(3 == 3)
print(3 != 3)
print(3 >= 4)
print(not (3 < 4))

print("")

side1 = 3
side2 = 4


hypo_len = ((side1 ** 2) + (side2 ** 2)) ** 0.5
print(hypo_len)


num_lst = [3, 20, -1, 9, 10]
is_even = list()

for num in num_lst:
    if num % 2 == 0 :
        num_even = True
        is_even.append(num_even)
    else:
        num_even = False
        is_even.append(num_even)

print(is_even)


num_lst = [3, 20, -1, 9, 10]
is_odd = list()

for num in num_lst:
	if num % 2 != 0:
		num_odd = True
		is_odd.append(num_odd)
	else:
		num_odd = False
		is_odd.append(num_odd)

print(is_odd)

a = 5
b = 6
c = 8

if (((b**2) + (c**2)) ** 0,5) == a:
	is_rightangled = True
elif (((a**2) + (c**2)) ** 0,5) == b:
	is_rightangled = True
elif (((a**2) + (b**2)) ** 0,5) == c:
	is_rightangled = True
else:
	is_rightangled = False

print(is_rightangled)



year = int(input("Enter the year between 1900-2099: "))

if year not in list(range(1900, 2100)):
	print("The year isnt'n between 1900-2099")
else:
	a = year % 19
	b = year % 4
	c = year % 7
	d = (19 * a + 24) % 30
	e = (2 * b + 4 * c + 6 * d + 5) % 7
	dateofeaster = 22 + d + e

	if year in [1954, 1981, 2049, 2076]:
		dateofeaster -= 7
	if dateofeaster > 31:
		print("April", dateofeaster - 31)
	else:
		print("March", dateofeaster)


text = input("Enter a word or text: ")
count = 0

for char in text:
	ind = text.find(char)
	if char == text[(-ind)-1]:
		count += 1

if count >= 2:
	is_pal = True
else :
	is_pal = False

print(is_pal)


print("")

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rains = rainfall_mi.split(",")
num_rainy_months = 0
for rain in rains:
    if float(rain) > 3.0 :
        num_rainy_months += 1

print(num_rainy_months)


sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
sliced = sentence.split()
same_letter_count = 0

for word in sliced:
	if word[0] == word[-1]:
		same_letter_count += 1

print(same_letter_count)



items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0

for item in items:
	w_num = item.count("w")
	if w_num > 0:
		acc_num +=1
print(acc_num)



sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
sliced = sentence.split()
num_a_or_e = 0

for word in sliced:
    num_a = word.count("a")
    num_e = word.count("e")

    if num_a > 0 or num_e > 0:
        num_a_or_e += 1

print(num_a_or_e)


s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

num_vowels = 0
sliced = s.split()

for word in sliced:
    for letter in word:
        if letter in vowels:
            num_vowels += 1

print(num_vowels)


schedule = ["SI 106", "STATS 250", "SI 110", "ENGLISH 124/125"]
if "STATS 250" in schedule:
    resp = "You could be in Information Science!"
else:
    resp = "That's too bad."

print(resp)


y = 22
z = 30

if z > y:
    y += 5

x = z * y
print(x)

wrd_lst = ["Hello", "activecode", "Java", "C#", "Python", "HTML and CSS", "Javascript", "Swift", "php"]
accum = 0

for word in wrd_lst:
    len_word = len(word)

    if len_word < 6:
        accum += 1

print(accum)
