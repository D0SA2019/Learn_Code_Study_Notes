print("")
print("------ 8. Loops ------")

print("")
print("------ 8.1. While you're here  ------")
count = 0

if count < 5:
  print("Hello, I am an if statement and count is", count)

while count < 10:
  print("Hello, I am a while and count is", count)
  count += 1



print("")
print("------ 8.2. Condition  ------")
loop_condition = True

while loop_condition:
  print("I am a loop")
  loop_condition = False




print("")
print("------ 8.3. While you're at it ------")
num = 1

while num < 11:
  print(num ** 2)
  num += 1




print("")
print("------ 8.4. Simple errors ------")
choice = input('Enjoying the course? (y/n)')

while choice != "y" and choice != "n" :
  choice = input("Sorry, I didn't catch that. Enter again: ")




print("")
print("------ 8.5. Infinite loops ------")
count = 0

while count < 10:
  print(count)
  count += 1




print("")
print("------ 8.6. Break ------")
count = 0

while True:
  print(count)
  count += 1
  if count >= 10:
    break

print("")

count = 0

while True:
  print(count)
  count += 1
  if count == 4:
    break



print("")
print("------ 8.7. While / else ------")
import random

print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")

count = 0
while count < 3:
  num = random.randint(1, 6)
  print(num)
  if num == 5:
    print("Sorry, you lose!")
    break
  count += 1
else:
  print("You win!")




print("")
print("------ 8.8. Your own while / else ------")
from random import randint

random_number = randint(1, 10)

guesses_left = 3
while guesses_left > 0 :
  guess = int(input("Make a guess! "))
  if guess == random_number:
    print("You win!")
    break
  guesses_left -= 1
else:
  print("You lose.")



print("")
print("------ 8.9. For your health ------")
print("Counting...")

for i in range(20):
  print(i)




print("")
print("------ 8.9. For your health ------")
hobbies = []

for i in range(3):
    hobby = input("Enter one of your hobbies: ")
    hobbies.append(hobby)
print(hobbies)




print("")
print("------ 8.11. For your strings ------")
thing = "spam!"
for c in thing:
  print(c)

word = "eggs!"
for letter in word:
  print(letter)




print("")
print("------ 8.12. For your A ------")
word = "Marble"
for char in word:
  print(char, end =" ")

print("")

phrase = "A bird in the hand..."
for char in phrase:
  if char == "A" or char == "a":
    print("X", end=" ")
  else:
    print(char, end=" ")



print("")
print("")
print("------ 8.13. For your lists ------")

numbers  = [7, 9, 12, 54, 99]

print("This list contains: ")

for num in numbers:
  print(num)

for num in numbers:
  print(num**2)




print("")
print("------ 8.14. Looping over a dictionary ------")
d = {'x': 9, 'y': 10, 'z': 20}
for key in d:
  if d[key] == 10:
    print("This dictionary has the value 10!")


d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  print(key, d[key])




print("")
print("------ 8.15. Counting as you go ------")
choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
for index, item in enumerate(choices):
  print(index + 1, item)




print("")
print("------ 8.16. Multiple lists ------")
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  if a > b:
    print(a)
  else:
    print(b)




print("")
print("------ 8.17. For / else ------")
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
  if f == 'tomato':
    print('A tomato is not a fruit!')
    break
  print('A', f)
else:
  print('A fine selection of fruits!')




print("")
print("------ 8.18. Change it up ------")
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
  if f == 'tomato':
    print('A tomato is not a fruit!') # (It actually is.)
    continue
  print('A', f)
else:
  print('A fine selection of fruits!')




print("")
print("------ 8.19. Create your own ------")
breakfast_order = ["coffee", "tea", "beer", "chocolate", "cheese", "pancake", "egg"]

for i in breakfast_order:
  if i == "beer":
    print("A", i, end=" ")
    print("Not a good choice for breakfast! I won't give you it.")
    continue
  else:
    print("A", i)
else :
  print("Good choice! It'll be perfect Sunday breakfast!")
