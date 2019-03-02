# 9. Exam Statistics


### 9.1. Let's look at those grades!
Creating a program to compute statistics means that you won't have to whip out your calculator and manually crunch numbers. All you'll have to do is supply a new set of numbers and our program does all of the hard work.

This mini-project will give you some practice with functions, lists, and translating mathematical formulae into programming statements.

In order to use the scores in our program, we'll need them in a container, namely a list.

On the right, you'll see the grades listed (see what I did there). The data is anonymous to protect the privacy of the students.


##### Instructions

Hit Run to continue.

```Python
# GIVEN
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print("Grades:", grades)

# OUTPUT
Grades: [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
```

### 9.2. Print those grades

As a refresher, let's start off by writing a function to print out the list of grades, one element at a time.


##### Instructions
Define a function on line 3 called `print_grades` with one argument, a list called `grades_input`.

Inside the function, iterate through `grades_input` and print each item on its own line.

After your function, call `print_grades` with the `grades` list as the parameter.


```Python
# GIVEN
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


# SOLUTION
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
    for grade in grades_input:
        print(grade)


print_grades(grades)


# OUTPUT
100
100
90
40
80
100
85
70
90
65
90
85
50.5
```

### 9.3. Review
So far, you've created a helper function that will be used in the next sections.

You also have a solid handle on the concepts that we'll need to continue.

The next step in the creation of our grade statistics program involves computing the mean (average) of the grades.

Onwards.



##### Instructions
Hit Run to continue.


```Python
# GIVEN
print("Let's compute some stats!")


# OUTPUT
Let's compute some stats!
```


### 9.4. The sum of scores
Now that we have a function to print the grades, let's create another function to compute the sum of all of the test grades.

This will be super-helpful when we need to compute the average score.

I know what you're thinking, "let's just use the built-in `sum` function!" The built-in function would work beautifully, but it would be too easy.

Computing the sum manually involves computing a rolling sum. As you loop through the list, add the current grade to a variable that keeps track of the total, let's call that variable `total`.



##### Instructions

On line 3, define a function, `grades_sum`, that does the following:

* Takes in a list of scores, `scores`
* Computes the sum of the scores
* Returns the computed sum.

Call the newly created `grades_sum` function with the list of `grades` and `print` the result.


```Python
# GIVEN
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


# SOLUTION
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    for grade in scores:
        total += grade
    return total


print(grades_sum(grades))


# OUTPUT
1045.5
```


### 9.5. Computing the Average
The average test grade can be found by dividing the sum of the grades by the total number of grades.

Luckily, we just created an awesome function, `grades_sum` to compute the sum.



##### Instructions

Define a function, `grades_average`, below the `grades_sum` function that does the following:

* Has one argument, `grades_input`, a list
* Calls `grades_sum` with `grades_input`
* Computes the average of the grades by dividing that sum by `float(len(grades_input))`.
* Returns the average.

Call the newly created `grades_average` function with the list of `grades` and `print` the result.

```Python
# GIVEN
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    for grade in scores:
        total += grade
    return total


# SOLUTION by adding
def grades_average(grades_input):
    average = grades_sum(grades_input) / float(len(grades_input))
    return average

print(grades_average(grades))



# OUTPUT
80.42307692307692
```


### 9.6. Review
Great work creating the capability to compute the average of the test grades.

We're going to use the average for computing the variance. The variance allows us to see how widespread the grades were from the average.


##### Instructions

Hit Run to continue.

```Python
# GIVEN
print("Time to conquer the variance!")


# OUTPUT
Time to conquer the variance!
```


### 9.7. The Variance
Let's see how the grades varied against the average. This is called computing the variance.

A very large variance means that the students' grades were all over the place, while a small variance (relatively close to the average) means that the majority of the students had similar grades.



##### Instructions

On line 18, define a new function called `grades_variance` that accepts one argument, `scores`, a list.

First, create a variable `average` and store the result of calling `grades_average(scores)`.

Next, create another variable `variance` and set it to zero. We will use this as a rolling sum.

`for` each `score in scores:` Compute its squared difference: `(average - score) ** 2` and add that to `variance`.

Divide the total `variance` by the number of `scores`.

Then, return that result.

Finally, after your function code, `print grades_variance(grades)`.


```Python
# GIVEN
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores:
    total += score
  return total

def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average


# SOLUTION by adding
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    variance /= len(scores)
    return variance

print(grades_variance(grades))


# OUTPUT
334.0710059171598
```


### 9.8. Standard Deviation
Great job computing the variance! The last statistic will be much simpler: standard deviation.

The standard deviation is the square root of the variance. You can calculate the square root by raising the number to the one-half power.


##### Instructions
Define a function, `grades_std_deviation`, that takes one argument called `variance`.

`return` the result of `variance ** 0.5`

After the function, create a new variable called `variance` and store the result of calling `grades_variance(grades)`.

Finally `print` the result of calling `grades_std_deviation(variance)`.


```Python
# GIVEN
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores:
    total += score
  return total

def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    variance /= len(scores)
    return variance

print(grades_variance(grades))


# SOLUTION by adding
def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

print(grades_std_deviation(variance))



# OUTPUT
334.0710059171598
18.277609414722697
```


### 9.9. Review
You've done a great job completing this program.

We've created quite a few meaningful functions. Namely, we've created helper functions to print a list of grades, compute the sum, average, variance, and standard deviation about a set of grades.

Let's wrap up by printing out all of the statistics.

Who needs to pay for grade calculation software when you can write your own? :)



##### Instructions
Print out the following:

* all of the grades
* sum of grades
* average grade
* variance
* standard deviation


```Python
# GIVEN
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print(grade)

def grades_sum(scores):
  total = 0
  for score in scores:
    total += score
  return total

def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    variance /= len(scores)
    return variance

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)



# SOLUTION
print_grades(grades)
print(grades_sum(grades))
print(grades_average(grades))
print(grades_variance(grades))
print(grades_std_deviation(variance))



# OUTPUT
100
100
90
40
80
100
85
70
90
65
90
85
50.5
1045.5
80.42307692307692
334.0710059171598
18.277609414722697
```
