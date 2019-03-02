print("")
print("------ 9. Exam Statistics ------")

print("")
print("------ 9.1. Let's look at those grades! ------")
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print("Grades:", grades)




print("")
print("------ 9.2. Print those grades ------")
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
    for grade in grades_input:
        print(grade)


print_grades(grades)




print("")
print("------ 9.3. Review ------")

print("Let's compute some stats!")




print("")
print("------ 9.4. The sum of scores ------")
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    for grade in scores:
        total += grade
    return total


print(grades_sum(grades))




print("")
print("------ 9.5. Computing the Average ------")
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    for grade in scores:
        total += grade
    return total


print(grades_sum(grades))

def grades_average(grades_input):
    average = grades_sum(grades_input) / float(len(grades_input))
    return average

print(grades_average(grades))




print("")
print("------ 9.6. Review ------")
print("Time to conquer the variance!")




print("")
print("------ 9.7. The Variance ------")
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

print(grades_variance(grades))




print("")
print("------ 9.8. Standard Deviation ------")
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

print(grades_variance(grades))

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

print(grades_std_deviation(variance))






print("")
print("------ 9.9. Review ------")
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

print_grades(grades)
print(grades_sum(grades))
print(grades_average(grades))
print(grades_variance(grades))
print(grades_std_deviation(variance))
