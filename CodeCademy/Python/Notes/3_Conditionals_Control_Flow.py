print("")
print("------ 3. Conditionals & Control Flow ------")

print("")
print("------ 3.1. Go With the Flow ------")
# From notes :
def clinic():
    print("You've just entered the clinic!")
    print("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
      print("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
      print("Of course this is the Argument Room, I've told you that already!")
    else:
      print("You didn't pick left or right! Try again.")
      clinic()

clinic()



print("")
print("------ 3.4. How the Tables Have Turned ------")
# From notes :
bool_one = 3 < 5
print(bool_one)

# Exercise :
bool_one = 3 < 5
bool_two = 2 != 2
bool_three = 2 == 2
bool_four = 2 < 2
bool_five = 2 <= 2
print(bool_one)
print(bool_two)
print(bool_three)
print(bool_four)
print(bool_five)



print("")
print("------ 3.6. And ------")

# From notes
b1 = -(-(-(-2))) == -2
b2 = 4 >= 16 ** 0.5
b3 = 19 % 4 != 300 / 10 / 10
b4 = -(1 ** 2) < 2 ** 0
b5 = 10 % 10 <= 20 - 10 * 2

print(b1)
print(b2)
print(b3)
print(b4)
print(b5)

# Exercise
bool_one = 2 != 2 and 2 >= 5
bool_two = 2 > 5 and 2 < 5
bool_three = 1 == -1 and 1 <= -1
bool_four = 1 != -1 and 1 >= -1
bool_five = 3 == 3 and 5 >= 5

print(bool_one)
print(bool_two)
print(bool_three)
print(bool_four)
print(bool_five)


print("")
print("------ 3.7. Or ------")

# From notes
b1 = 2 ** 3 == 108 % 100
b2 = 'Cleese' == 'King Arthur'
b3 = 100 ** 0.5 >= 50
b4 = 1 ** 100 == 100 ** 1
b5 = 3 * 2 * 1 != 3 + 2 + 1

print(b1)
print(b2)
print(b3)
print(b4)
print(b5)

print("")
# Exercise
bool_one = 1 == 1 or 1 == -1
bool_two = 1 > -1 or 1 < -1
bool_three = 1 == -1 or 1 < -1
bool_four = 1 == 1 or 1 > -1
bool_five = 3 != 3 or 3 == -3

print(bool_one)
print(bool_two)
print(bool_three)
print(bool_four)
print(bool_five)


print("")
print("------ 3.8. Not ------")

# From notes
b1 = not True
b2 = not 3 ** 4 < 4 ** 3
b3 = not 10 % 3 <= 10 % 2
b4 = not 3 ** 2 + 4 ** 2 != 5 ** 2
b5 = not not False

print(b1)
print(b2)
print(b3)
print(b4)
print(b5)


print("")
print("------ 3.9. This and That (or This, But Not That!) ------")
b1 = True or not False and False
b2 = not False or True and False
b3 = False and True or not False
b4 = (True or not False) and False


print(b1)
print(b2)
print(b3)
print(b4)

print("")
b1 = False or not True and True
b2 = False and not True or True
b3 = True and not (False or False)
b4 = not not True or False and not True
b5 = False or not (True and True)

print(b1)
print(b2)
print(b3)
print(b4)
print(b5)


print("")
print("------ 3.10. Mix 'n' Match ------")
# From notes
bool_one = (2 <= 2) and "Alpha" == "Bravo"
print(bool_one)

print("")
# Exercise
bool_one = (2 <= 2) and "Alpha" == "Bravo"
bool_two = 1 != -1 or 1 < -1
bool_three = not 1 > -1
bool_four = not -1 > 1
bool_five = 1 == 1 and -1 != 1

print(bool_one)
print(bool_two)
print(bool_three)
print(bool_four)
print(bool_five)


print("")
print("------ 3.11. Conditional Statement Syntax ------")
# From notes
if 8 < 9:
  print("Eight is less than nine!")

# Exercise
answer = "Left"
if answer == "Left":
    print("This is the Verbal Abuse Room, you heap of parrot droppings!")



print("")
print("------ 3.12. If You're Having... ------")
def using_control_once():
    if "Blue" != "blue":
        return "Success #1"

def using_control_again():
    if 1**1 == 1:
        return "Success #2"
print(using_control_once())
print(using_control_again())


print("")
print("------ 3.13. Else Problems, I Feel Bad for You, Son... ------")
# From notes
if 8 > 9:
  print("I don't printed!")
else:
  print("I get printed!")




print("")
print("------ 3.14. I Got 99 Problems, But a Switch Ain't One ------")
if 8 > 9:
  print("I don't get printed!")
elif 8 < 9:
  print("I get printed!")
else:
  print("I also don't get printed!")

print("")
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0

print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))


print("")
print("------ 3.15. The Big If ------")
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80 and grade <= 89:
        return "B"
    elif grade >= 70 and grade <= 79:
        return "C"
    elif grade >= 65 and grade <= 69:
        return "D"
    else:
        return "F"

print(grade_converter(92))
print(grade_converter(70))
print(grade_converter(61))



print("")
print("------ PygLatin ------")

pyg = 'ay'

print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")

if len(original) > 0 and original.isalpha():
  print(original)
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print(new_word)
else:
  print("empty")
