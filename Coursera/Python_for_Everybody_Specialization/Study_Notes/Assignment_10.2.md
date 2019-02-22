# Assignment 10.2
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

`From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008`

Once you have accumulated the counts for each hour, print out the counts,sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.


```Python
file = open("mbox-short.txt")
words = list()
hours = dict()
for line in file:
    if line.startswith("From "):
        word = line.split()
        hour = word[5].split(":")
        words.append(hour[0])

for hour in words:
    hours[hour] = hours.get(hour, 0) + 1

srt = list()
for k,v in hours.items():
    rev = (k,v)
    srt.append(rev)

big = sorted(srt)

for k,v in big:
    print(k,v)


# Output :
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
```
