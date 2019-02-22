# Assignment 9.4
Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

**Desire Output** : `cwen@iupui.edu 5`

```Python
file = input("Enter file name:")
read = open(file)
words = list()
counts = dict()

for line in read:
    if line.startswith("From "):
        word = line.split()
        words.append(word[1])

for name in words :
    counts[name] = counts.get(name, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print(bigword, bigcount)

# Output : cwen@iupui.edu 5
```
