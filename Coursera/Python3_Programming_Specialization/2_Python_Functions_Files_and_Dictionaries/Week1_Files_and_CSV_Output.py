print("============================================")
print("Python 3 Programming Specialization")
print("Course 2 : Python Functions, Files, and Dictionaries")
print("Week 1 : Files and CSV Output")
print("============================================")
print("=========== 1.2. Reading a File ============")
print("--------------------------------------------")
ol_file = open("olympics.txt", "r")
print(ol_file)

contents_full = ol_file.read()
print(contents_full)
ol_file.close()

print("")

ol_file = open("olympics.txt", "r")
contents_100 = ol_file.read(100)
print(contents_100)
ol_file.close()

print("")

ol_file = open("olympics.txt", "r")
contents_line = ol_file.readline()
print(contents_line)
ol_file.close()


ol_file = open("olympics.txt", "r")
contents_line_5 = ol_file.readline(5)
print(contents_line_5)
ol_file.close()


print("")

ol_file = open("olympics.txt", "r")
contents_lines = ol_file.readlines()
print(contents_lines)
ol_file.close()

print("")

ol_file = open("olympics.txt", "r")
contents_lines_5 = ol_file.readlines(100)
print(contents_lines_5)
ol_file.close()

print("")

sc_file = open("school_prompt2.txt", "r")
num_char = len(sc_file.read())
print(num_char)
sc_file.close()

print("")


tr_file = open("travel_plans2.txt", "r")
num_lines = len(tr_file.readlines())
print(num_lines)

print("")

em_file = open("emotion_words2.txt", "r")
first_forty = em_file.read(40)
print(first_forty)

print("")

olympicsfile = open("olympics.txt","r")
for aline in olympicsfile.readlines():
  values = aline.split(",")
  print(values[0], "is from", values[3], "and is on the roster for", values[4])
olympicsfile.close()

print("")

olympicsfile = open("olympics.txt","r")

for aline in olympicsfile:
  values = aline.split(",")
  print(values[0], "is from", values[3], "and is on the roster for", values[4])
olympicsfile.close()

print("")

em_file = open("emotion_words.txt", "r")

num_lines = 0

for line in em_file:
    num_lines +=1
print(num_lines)

print("")

print("============================================")
print("========== 1.4. Writing to a File ==========")
print("--------------------------------------------")
for number in range(13):
	square = number * number
	print(square)

print("")

filename = "squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1, 13):
	square = number * number
	outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read())

print("")

print("============================================")
print("====== 1.5. Using With to Open Files =======")
print("--------------------------------------------")

with open("mydata.txt", "r") as md:
	for line in md:
		print(line)

print("")

md = open("mydata.txt", "r")
for line in md:
	print(line)
md.close()

print("")

print("============================================")
print("========= 1.6. Reading a .csv File =========")
print("--------------------------------------------")

fileconnection = open("olympics.txt", "r")
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(",")
print(field_names)

for row in lines[1:]:
	vals = row.strip().split(",")
	if vals[5] != "NA":
		print("{}: {}; {}".format(
					vals[0],
					vals[4],
					vals[5]))

print("")

print("============================================")
print("===== 1.7. Writing Data to a .csv File =====")
print("--------------------------------------------")
olympians = [("John Aalberg", 31, "Cross Country Skiing"),
            ("Minna Maarit Aalto", 30, "Sailing"),
            ("Win Valdemar Aaltonen", 54, "Art Competitions"),
            ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
outfile.write("Name,Age,Sport")
outfile.write("\n")

for olympian in olympians:
	row_string = "{},{},{}".format(olympian[0], olympian[1], olympian[2])
	outfile.write(row_string)
	outfile.write("\n")

outfile.close()

oly_file = open("reduced_olympics.csv", "r")
print(oly_file.read())
oly_file.close()


olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
            ("Minna Maarit Aalto", 30, "Sailing"),
            ("Win Valdemar Aaltonen", 54, "Art Competitions"),
            ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics2.csv","w")
# output the header row
outfile.write('"Name","Age","Sport"')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()


oly_file2 = open("reduced_olympics2.csv", "r")
print(oly_file2.read())
oly_file2.close()

print("")

print("============================================")
print("======= 1.9. Assessments & Exercises =======")
print("--------------------------------------------")

stu_file = open("studentdata.txt", "r")

for student in stu_file.readlines():
    student = student.strip().split()
    if len(student) > 7:
        print(student[0])
stu_file.close()

print("")

tr_file = open("travel_plans.txt", "r")
destination = []

for line in tr_file.readlines():
    line = line.strip()
    if ":" in line:
        destination.append(line)
print(destination)
tr_file.close()

print("")

emo_file = open("emotion_words.txt", "r")
emo_content = emo_file.read().split()
j_emotions = []

for emo in emo_content:
    if emo[0] == "j":
        j_emotions.append(emo)

print(j_emotions)
emo_file.close()

print("")

tr_file = open("travel_plans.txt", "r").read()
num = 0

for char in tr_file:
    num += 1

print(num)


print("")

emo_file = open("emotion_words.txt", "r").read()
num_words = len(emo_file.split())
print(num_words)

print("")

sc_file = open("school_prompt.txt", "r").readlines()
num_lines = 0

for line in sc_file:
    num_lines += 1

print(num_lines)

print("")

beginning_chars = open("school_prompt.txt", "r").read(30)
print(beginning_chars)

print("")

sch_file = open("school_prompt.txt", "r").readlines()
three = []

for line in sch_file:
    line = line.strip().split()
    three.append(line[2])

print(three)

print("")

emo_file = open("emotion_words.txt", "r").readlines()
emotions = []

for line in emo_file:
    line = line.strip().split()
    emotions.append(line[0])

print(emotions)

print("")

first_chars = open("travel_plans.txt", "r").read(33)
print(first_chars)

print("")

sc_file = open("school_prompt.txt", "r").read()

words = sc_file.split()
p_words = []

for word in words:
    if "p" in word:
        p_words.append(word)
print(p_words)
