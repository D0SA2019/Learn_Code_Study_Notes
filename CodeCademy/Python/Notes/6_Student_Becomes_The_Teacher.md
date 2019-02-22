# 6. 6. Student Becomes The Teacher
### 6.1. Lesson Number One

Welcome to this "Challenge Course". Until now we've been leading you by the hand and working on some short and relatively easy projects. This is a **challenge** so be ready. We have faith in you!

We're going to switch it up a bir and allow you to be the teacher of your own class. Make a gradebook for all of your students.

```python
animal = {
	"name": "Mr. Fluffles",
	"sounds": ["meow", "purr"]
}
print(animal["name"])


# Output
Mr. Fluffles
```
The example above is just to remind you how to create a dictionary and then to access the item stored by the `"name"` key.

##### Instructions
Create three dictionaries : `lloyd`, `alice` and `tyler`.

Give each dictionary the keys `"name"`, `"homework"`, `"quizzes"` and `"tests"`.

Have the "name" key be the name of the student (that is, `llyod`'s name shoud be `"Lloyd"`) and the other keys should be an empty list (We'll fill in these lists soon!)


```Python
# SOLUTION
lloyd = {
  "name" : "Lloyd",
  "homework" : [],
  "quizzes" : [],
  "tests" : []
}

alice = {
  "name" : "Alice",
  "homework" : [],
  "quizzes" : [],
  "tests" : []
}

tyler = {
  "name" : "Tyler",
  "homework" : [],
  "quizzes" : [],
  "tests" : []
}
```


### 6.2. What's the Score?
Great work!


##### Instructions
Now fill out your `lloyd` dictionary with the appropriate scores. To save you some time, we've filled out the rest of you.

Homework: 90.0, 97.0, 75.0, 92.0

Quizzes: 88.0, 40.0, 94.0

Test Scores: 75.0, 90.0

**Make sure to include the decimal points so your grades are stored as floats!** This will be important later.

```Python
#GIVEN
lloyd = {
  "name": "Lloyd",
  "homework": [],
  "quizzes": [],
  "tests": []
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# SOLUTION
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
```


### 6.3. Put It Together
Now lets put the three dictionaries in a list together.

```Python
my_list = [1, 2, 3]
```
The above example is just a reminder on how to create a list. Afterwards, `my_list` contains `1`, `2` and `3`.

##### Instructions
Below your code, create a list called `students` that contains `lloyd`, `alice` and `tyler`.

```Python
#GIVEN
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}


# SOLUTION
# add
students = [lloyd, alice, tyler]
```



### 6.4. For the Record
Excellent. Now you need a hard copy document with all of your students' grades.

```Python
animal_sounds : {
	"cat": ["meow", "purr"],
	"dog": ["woof", "bark"],
	"fox": [],
}

print(animal_sounds["cat"])


# Output
['meow', 'purr']
```
The example above is just to remind you how to create a dictionary and then to access the item stored by the `"cat"` key.

##### Instructions
`for` each `student` in your `students` list, print out that `student`'s data, as follows :

* `print` the `student`'s `name`
* `print` the `student`'s `homework`
* `print` the `student`'s `quizzes`
* `print` the `student`'s `tests`


```Python
#GIVEN
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]


# SOLUTION
# add
for student in students:
  print(student["name"])
  print(student["homework"])
  print(student["quizzes"])
  print(student["tests"])


# OUTPUT
Lloyd
[90.0, 97.0, 75.0, 92.0]
[88.0, 40.0, 94.0]
[75.0, 90.0]
Alice
[100.0, 92.0, 98.0, 100.0]
[82.0, 83.0, 91.0]
[89.0, 97.0]
Tyler
[0.0, 87.0, 75.0, 22.0]
[0.0, 75.0, 78.0]
[100.0, 100.0]
```


### 6.5. It's Okay to be Average
When teaching a class, it's important to take the student's averages in order to assign grades.

```Python
5 / 2
# 2

5.0 / 2
# 2.5

float(5) / 2
# 2.5
```
The above example is a reminder of how division works in Python.

* When you divide an integer by another integer, the result is always an integer (rounded down, if needed).
* When you divide a float by an integer, the result is always a float.
* To divide two integers and end up with a float, you must first use `float()` to convert one of the integers to a float.


##### Instructions
Write a function `average` that takes a list of numbers and returns the average.

* Define a function called `average` that has one argument `numbers`.
* Inside that function, call the built-in `sum()` function with the `numbers` list as a parameter. Store the result in a variable called `total`.
* Like the example above, use `float()` to convert `total` and store the result in `total`.
* Divide `total` by the lenght of the `numbers` list. Use the built-in `len()` function to calculate that.
* Return that result.


```Python
#GIVEN
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}


# SOLUTION
# add
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)
```


### 6.6. Just Weight and See
Great! Now we need to compute a student's average using wighted averages.

```Python
cost = {
	"apples": [3.5, 2.4, 2.3],
	"bananas": [1.2, 1.8],
}

return 0.9 * average(cost["apples"]) + \
0.1 * average(cost["bananas"])
```
1. In the above example, we create a dictionary called `cost` that contains the costs of some fruit.
2. Then, we calculate the average cost of apples and the average cost of bananas. Since we like apples much more than we like bananas, we weight the average cost of apples by 90% and the average cost of bananas by 10%.

The `\` character is contnuation chracter. The following line is considered a continuation of the current line.


##### Instructions
Write a function called `get_average` that takes a student dictionary (like `lloyd`, `alice` or `tyler`) as input and `return`s his/her weighted average.

* Define a function called `get_average` that takes one argument called `student`.
* Make a variable `homework` that stores the `average()` of `student["homework"]`.
* Repeat the above step for "quizzes" and "tests".
* Multiply the 3 averages by their weights and return the sum of those three. Homework is 10%, quizzes are 30% and tests are 60%.


```Python
#GIVEN
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)


# SOLUTION
# add
def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return (0.1 * homework) + (0.3 * quizzes) + (0.6 * tests)
```

### 6.7. Sending a Letter
Great work!

Now let's write a `get_letter_grade` function that takes a number `score` as input and returns a string with the letter grade that that student should receive.



##### Instructions
Define a new function called `get_letter_grade` that has one argument called `score`. Expect `score` to be a number.

Inside your function, test `score` using a chain of `if: / elif: / else:` statements like so :

* If score is 90 or above : `return "A"`
* Else if score is 80 or above : `return "B"`
* Else if score is 70 or above : `return "C"`
* Else if score is 60 or above : `return "D"`
* Otherwise : `return "F"`

Finally test your funtcion!

print the resulting letter grade with `print`. Call the `get_letter_grade` function and pass in `get_average(lloyd)`.


```Python
#GIVEN
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return (0.1 * homework) + (0.3 * quizzes) + (0.6 * tests)



# SOLUTION
# add
def get_letter_grade(score):
  if score >= 90 :
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

print(get_letter_grade(get_average(lloyd)))



# OUTPUT
B
```



### 6.6. Just Weight and See
Great! Now we need to compute a student's average using wighted averages.

```Python
cost = {
	"apples": [3.5, 2.4, 2.3],
	"bananas": [1.2, 1.8],
}

return 0.9 * average(cost["apples"]) + \
0.1 * average(cost["bananas"])
```
1. In the above example, we create a dictionary called `cost` that contains the costs of some fruit.
2. Then, we calculate the average cost of apples and the average cost of bananas. Since we like apples much more than we like bananas, we weight the average cost of apples by 90% and the average cost of bananas by 10%.

The `\` character is contnuation chracter. The following line is considered a continuation of the current line.


##### Instructions
Write a function called `get_average` that takes a student dictionary (like `lloyd`, `alice` or `tyler`) as input and `return`s his/her weighted average.

* Define a function called `get_average` that takes one argument called `student`.
* Make a variable `homework` that stores the `average()` of `student["homework"]`.
* Repeat the above step for "quizzes" and "tests".
* Multiply the 3 averages by their weights and return the sum of those three. Homework is 10%, quizzes are 30% and tests are 60%.


```Python
#GIVEN
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)


# SOLUTION
# add
def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return (0.1 * homework) + (0.3 * quizzes) + (0.6 * tests)
```

### 6.8. Part of the Whole
Good! Now let's calculate the class average.

You need to get the average for each student and then calculate the average of those averages.

##### Instructions
Define a function called `get_class_average` that has one argument `class_list`. You can expect `class_list` to be a list containing your three students.

First, make an empty list called `results`.

For each `student` item in the `class_list`, calculate `get_average(student)` and then call `results.append()` with result.

Finally, return the result of calling `average()` with `results`.


```Python
#GIVEN
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return (0.1 * homework) + (0.3 * quizzes) + (0.6 * tests)

def get_letter_grade(score):
  if score >= 90 :
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

print(get_letter_grade(get_average(lloyd)))



# SOLUTION
# add
def get_class_average(class_list):
  results = []
  for student in class_list:
    results.append(get_average(student))
  return average(results)

```


### 6.9. How is Everybody Doing?

Awesome! You're doing great. Now let's use the functions you've created to check the grade of the class overall.

##### Instructions
1. Create a list called `students` and fill it with the three students, `alice`, `lloyd`, and `tyler`.
2. Find the average grade of the class. Print this numerical grade to the terminal.
3. Finally, determine the letter grade for the class's average and print it to the terminal.

```Python
#GIVEN
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return (0.1 * homework) + (0.3 * quizzes) + (0.6 * tests)

def get_letter_grade(score):
  if score >= 90 :
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

print(get_letter_grade(get_average(lloyd)))

def get_class_average(class_list):
  results = []
  for student in class_list:
    results.append(get_average(student))
  return average(results)



# SOLUTION
# add

students = [alice, lloyd, tyler]
print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))



# OUTPUT
B
83.8666666667
B

```
