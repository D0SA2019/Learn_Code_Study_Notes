# Assignment 11.1 : Finding Numbers in a Haystack
In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

### Data Files
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

* Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt
* Actual data: http://python-data.dr-chuck.net/regex_sum_325328.txt

These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program.

***Note***: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

### Data Format
The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. Here is a sample of the output you might see:

*Why should you learn to write programs? 7746 12 1929 8827 Writing programs (or programming) is a very creative 7 and rewarding activity. You can write programs for many reasons, ranging from making your living to solving 8837 a difficult data analysis problem to having fun to helping 128 someone else solve a problem. This book assumes that everyone needs to know how to program ... The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none). Handling The Data The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.*

```Python
import re

file = open("regex_sum_42.txt")
numlist = list()
sum = 0
for line in file:
    number = re.findall("[0-9]+", line)
    for x in number:
        x = int(x)
        if x in numlist: continue
        else :
            numlist.append(x)
            sum += x
print("There are", len(numlist), "numbers in the text")
print("The sum of the numbers:",sum)
print("The numbers are in order:", sorted(numlist))


# Output :
# There are 89 numbers in the text
# The sum of the numbers: 445829
# The numbers are in order: [3, 4, 5, 42, 63, 171, 279, 517, 801, 829, 918, 956, 1004, 1052, 1079, 1117, 1218, 1704, 1720, 1792, 1865, 2054, 2312, 2564, 2572, 2727, 2834, 2923, 2981, 3036, 3062, 3342, 3482, 3538, 3665, 3816, 4034, 4183, 4497, 4509, 4676, 4806, 5047, 5349, 5415, 5460, 5561, 5616, 5801, 5858, 6015, 6096, 6373, 6482, 6662, 6702, 6872, 7073, 7084, 7100, 7114, 7123, 7209, 7221, 7449, 7655, 7777, 7936, 8001, 8003, 8062, 8135, 8402, 8454, 8533, 8567, 8687, 8752, 8805, 8824, 8877, 9258, 9548, 9552, 9634, 9663, 9703, 9772, 9795]
```
