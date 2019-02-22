# 010 - Nested Lists
## Problem
Given the names and grades for each student in a Physics class of `N` students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

**Note**: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

#### Input Format

The first line contains an integer, `N`, the number of students.

The `2N` subsequent lines describe each student over `N` lines; the first line contains a student's name, and the second line contains their grade.


#### Constraints
2 <= N <= 5

There will always be one or more students having the second lowest grade.

#### Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

```
Sample Input :
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

```
Sample Output :
Berry
Harry
```

#### Explanation
There are 5 students in this class whose names and grades are assembled to build the following list:

`python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]`

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.


#### Given Code

```python
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
```

## Solution

```python
if __name__ == '__main__':
    students = list()
    for _ in range(int(input(""))):
        name = input()
        score = float(input())
        student = list()
        student.append(name)
        student.append(score)
        students.append(student)
    students.sort(key=lambda x: x[0], reverse=False)
    students.sort(key=lambda x: x[1], reverse=False)
    mn = min(students, key=lambda x: x[1])[1]
    second = None
    for x in range(len(students)):
        if students[x][1] == mn:
            continue
        if students[x][1] > mn and second == None:
            second = students[x][1]
            print(students[x][0])
        elif students[x][1] == second :
            print(students[x][0])
        else :
            continue
```
