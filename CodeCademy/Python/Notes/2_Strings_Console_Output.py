print("")
print("------ 2. Strings & Console Output ------")
print("------ 2.1. Strings ------")

print("")
print("------ 2.1.1. String ------")
# From notes :
name = "Ryan"
age = "19"
food = "cheese"
print(name, age, food)

# Exercise :
brian = "Hello life!"
print(brian)


print("")
print("------ 2.1.2. Practice ------")
caesar = "Graham"
praline = "John"
viking = "Teresa"

print(caesar)
print(praline)
print(viking)


print("")
print("------ 2.1.3. Escaping characters ------")
line = 'This isn\'t flying, this is falling with style!'
print(line)



print("")
print("------ 2.1.4. Access by Index ------")
# From notes :
c = "cats"[0]
n = "Ryan"[3]

print(c, n)

# Exercise :
fifth_letter = "MONTY"[4]
print(fifth_letter)


print("")
print("------ 2.1.5. String methods ------")
parrot = "Norwegian Blue"
print(parrot)
print(len(parrot))



print("")
print("------ 2.1.6. lower() ------")
parrot = "Norwegian Blue"
print(parrot)
print(parrot.lower())


print("")
print("------ 2.1.7. upper() ------")
parrot = "Norwegian Blue"
print(parrot)
print(parrot.upper())



print("")
print("------ 2.1.8. str() ------")
pi = 3.14
print(str(pi))


print("")
print("------ 2.1.9. Dot Notation ------")
ministry = "The Ministry of Silly Walks"
print(ministry)
print(len(ministry))
print(ministry.upper())



print("")
print("------ 2.1.10. Printing Strings ------")
print("Monty Python")


print("")
print("------ 2.1.11. Printing Variables ------")
the_machine_goes = "Ping!"
print(the_machine_goes)


print("")
print("------ 2.1.12. String Concatenation ------")
print("Life " + "of " + "Brian")
print("Spam " + "and " + "eggs")


print("")
print("------ 2.1.13. Explicit String Conversion ------")
print("The value of pi is around " + str(3.14))


print("")
print("------ 2.1.14. String Formatting with %, Part 1 ------")
name = "Mike"
print("Hello %s" % (name))

day = 6
print("03 - %s - 2019" %  (day))
print("03 - %02d - 2019" % (day))


string_1 = "Camelot"
string_2 = "place"
print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))



print("")
print("------ 2.1.15. String Formatting with %, Part 2 ------")
print("The %s who %s %s!" % ("Knights", "say", "Ni"))

name = input("What is your name? ")
quest = input("What is your quest? ")
color = input("What is your favorite color? ")
print("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))



print("")
print("------ 2.1.16. And Now, For Something Completely Familiar ------")
g = "Golf"
h = "Hotel"
print("%s, %s" % (g, h))

my_string = "Learning code is fun!"
print(len(my_string))
print(my_string.upper())



print("")
print("")
print("------ 2.2. Date and Time ------")

print("")
print("------ 2.2.2. Getting the Current Date and Time ------")
from datetime import datetime
print(datetime.now())

now = datetime.now()
print(now)



print("")
print("------ 2.2.3 Extracting Information ------")
from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

print(now)
print(current_year)
print(current_month)
print(current_day)


from datetime import datetime
now = datetime.now()
print(now.year)
print(now.month)
print(now.day)


print("")
print("------ 2.2.4 Hot Date ------")
from datetime import datetime
now = datetime.now()

print('%02d/%02d/%04d' % (now.month, now.day, now.year))
print('%02d/%02d/%04d' % (now.day, now.month, now.year))


print("")
print("------ 2.2.5 Pretty Date ------")
from datetime import datetime
now = datetime.now()
print('%02d:%02d:%04d' % (now.hour, now.minute, now.second))



print("")
print("------ 2.2.6 Grand Finale ------")
from datetime import datetime
now = datetime.now()
print('%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
