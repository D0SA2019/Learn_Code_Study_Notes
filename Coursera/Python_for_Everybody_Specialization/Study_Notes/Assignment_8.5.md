# Assignment 8.5

Open the file mbox-short.txt and read it line by line.
When you find a line that starts with 'From ' like the following line:

`From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008`

You will parse the From line using `split()` and print out the second word in the line
(i.e. the entire address of the person who sent the message). Then print out a count at the end.

Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

**Desire Output :**

```
Enter a file name: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu

[...some output removed...]

ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word
````



```python
ask = input("Enter a file name: ")
file = open(ask)
mail = list()
for l in file:
    if l.startswith("From "):
        l = l.split()
        mail.append(l)
        print(l[1])
print("There were", len(mail), "lines in the file with From as the first word")
```
