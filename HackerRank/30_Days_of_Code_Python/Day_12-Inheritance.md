# Day 12: Inheritance
## Problem
#### Objective

Today, we're delving into Inheritance.

#### Task
You are given two classes, `Person` and `Student`, where `Person` is the base class and `Student` is the derived class. Completed code for `Person` and a declaration for `Student` are provided for you in the editor. Observe that `Student` inherits all the properties of `Person`.

Complete the `Student` class by writing the following:

* A `Student` class constructor, which has 4 parameters:
  - A string, `firstName`
  - A string, `lastName`
  - An integer, `id`
  - An integer array (or vector) of test scores, `scores`
* A char `calculate()` method that calculates a `Student` object's average and returns the grade character representative of their calculated average:

![](https://s3.amazonaws.com/hr-challenge-images/17165/1458142706-3073bc9143-Grading.png)


#### Input Format
The locked stub code in your editor calls your `Student` class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).

You are not responsible for reading the following inğut from stdin:

The first line contains `firstName`, `lastName`, and `id`, respectively. The second line contains the number of test scores. The third line of space-separated integers describes `scores`.

#### Constraints

* 1 <= |`firstName`|, |`lastName`| <= 9
* |`id`| ≡ 7
* 0 <= `score`, `average` <= 100


#### Output Format
This is handled by the locked stub code in your editor. Your output will be correct if your `Student` class constructor and `calculate()` method are properly implemented.


#### Sample Input

```
Heraldo Memelli 8135627
2
100 80
```

#### Sample Output

```
Name : Memelli, Heraldo
ID: 8135627
Grade: 0
```

#### Explanation
This student had 2 scores to average : 100 and 80. The student's averagre grade is (100 + 80)/2 = 90. An average grade of 90 corresponds to the letter grade `O`, so our `calculate()` method should return the character `'O'`

## Given code

```python
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
```

## Solution

```python
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
	def __init__(self, firstName, lastName, idNumber, scores):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
		self.scores = scores

	def calculate(Student):
		sum = 0

		for score in scores :
			sum += score

		ave = sum / len(scores)

		if ave < 40 :
			a = "T"
		elif 40 <= ave < 55:
			a = "D"
		elif 55 <= ave < 70:
			a = "P"
		elif 70 <= ave < 80:
			a = "A"
		elif 80 <= ave < 90:
			a = "E"
		elif 90 <= ave <= 100:
			a = "O"

		return a


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
```
