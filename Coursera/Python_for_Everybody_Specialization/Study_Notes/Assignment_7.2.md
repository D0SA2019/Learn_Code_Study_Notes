# Assignment 7.2

Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

`X-DSPAM-Confidence:    0.8475`

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.

`Average spam confidence: 0.750718518519`

You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.


```python
count = 0
sum = 0
file = input("Enter a file name: ")
data = open(file)
for line in data:
  if line.startswith("X-DSPAM-Confidence:"):
    count = count + 1
    line = line.strip()
    num = line[20:]
    sum = sum + float(num)
print("Average spam confidence: ", sum / count)

# Output : Average spam confidence:  0.7507185185185187
```
