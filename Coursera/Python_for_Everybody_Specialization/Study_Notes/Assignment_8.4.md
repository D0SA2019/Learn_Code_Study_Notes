# Assignment 8.4

Open the file `romeo.txt` and read it line by line. For each line, split the line into a list of words using the `split()` function. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.

You can download the sample data at http://www.pythonlearn.com/code/romeo.txt


```
Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']
````



```python
file = open("romeo.txt")
lines = " "
for l in file:
    l = l.rstrip()
    lines += l + " "
words = lines.split()
words.sort()
print(words)
```
