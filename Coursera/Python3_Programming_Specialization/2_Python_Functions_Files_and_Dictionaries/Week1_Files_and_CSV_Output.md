# Python Functions, Files, and Dictionaries
*Coursera | Python 3 Programming Specialization | Course 2*

## Week 1 : Files and CSV Output

### Files
#### 1.1. Introduction: Working with Data Files

So far, the data we have used in this book have all been either coded right into the program, or have been entered by the user. In real life data reside in files. For example the images we worked with in the image processing unit ultimately live in files on your hard drive. Web pages, and word processing documents, and music are other examples of data that live in files. In this short chapter we will introduce the Python concepts necessary to use data from files in our programs.

For our purposes, we will assume that our data files are text files–that is, files filled with characters. The Python programs that you write are stored as text files. We can create these files in any of a number of ways. For example, we could use a text editor to type in and save the data. We could also download the data from a website and then save it in a file. Regardless of how the file is created, Python will allow us to manipulate the contents.

In Python, we must **open** files before we can use them and **close** them when we are done with them. As you might expect, once a file is opened it becomes a Python object just like all other data. Table 1 shows the functions and methods that can be used to open and close files.

| Method | Use | Expanation |
|--|--|--|
| `open` | `open(filename,'r')` | Open a file called filename and use it for reading. This will return a reference to a file object. |
| `open` | `open(filename,'w')` | Open a file called filename and use it for writing. This will also return a reference to a file object. |
| `close` | `filevariable.close()` | File use is complete. |


#### 1.2. Reading a File

As an example, suppose we have a text file called `olympics.txt` that contains the data representing about olympians across different years. The contents of the file are shown at the bottom of the page.

To open this file, we would call the `open` function. The variable, `fileref`, now holds a reference to the file object returned by `open`. When we are finished with the file, we can close it by using the `close` method. After the file is closed any further attempts to use `fileref` will result in an error.

```python
fileref = open("olympics.txt", "r")
fileref.close()
```


**Note** : A common mistake is to get confused about whether you are providing a variable name or a string literal as an input to the open function. In the code above, “olympics.txt” is a string literal that should correspond to the name of a file on your computer. If you put something without quotes, like `open(x, "r")`, it will be treated as a variable name. In this example, x should be a variable that’s already been bound to a string value like “olympics.txt”.


#### Alternative File Reading Methods

Once you have a file “object”, the thing returned by the open function, Python provides three methods to read data from that object. The `read()` method returns the entire contents of the file as a single string (or just some characters if you provide a number as an input parameter. The `readlines` method returns the entire contents of the entire file as a list of strings, where each item in the list is one line of the file. The `readline` method reads one line from the file and returns it as a string. The strings returned by `readlines` or `readline` will contain the newline character at the end. Table 2 summarizes these methods and the following session shows them in action.


| Method Name | Use | Explanation |
|--|--|--|
| `write` | `filevar.write(astring)` | Add astring to the end of the file. filevar must refer to a file that has been opened for writing. |
| `read(n)` | `filevar.read()` | Reads and returns a string of n characters, or the entire file as a single string if `n` is not provided. |
| `readline(n)` | `filevar.readline()` | Returns the next line of the file with all text up to and including the newline character. If n is provided as a parameter than only n characters will be returned if the line is longer than `n`. |
| `readlines(n)` | `filevar.readlines()` | Returns a list of strings, each representing a single line of the file. If n is not provided then all lines of the file are returned. If n is provided then n characters are read but n is rounded up so that an entire line is returned. |

In this course, we will generally either iterate through the lines returned by `readlines()` with a for loop, or use `read()` to get all of the contents as a single string.

In other programming languages, where they don’t have the convenient for loop method of going through the lines of the file one by one, they use a different pattern which requires a different kind of loop, the `while` loop. Fortunately, you don’t need to learn this other pattern, and we will put off consideration of `while` loops until later in this course. We don’t need them for handling data from files.


**Note**: A common error that novice programmers make is not realizing that all these ways of reading the file contents, use up the file. After you call `readlines()`, if you call it again you’ll get an empty list.


**Reading all content**

```python
ol_file = open("olympics.txt", "r")
print(ol_file)

contents_full = ol_file.read()
print(contents_full)
```

**Output** :

```
<_io.TextIOWrapper name='olympics.txt' mode='r' encoding='UTF-8'>

Name,Sex,Age,Team,Event,Medal
A Dijiang,M,24,China,Basketball,NA
A Lamusi,M,23,China,Judo,NA
Gunnar Nielsen Aaby,M,24,Denmark,Football,NA
Edgar Lindenau Aabye,M,34,Denmark/Sweden,Tug-Of-War,Gold
Christine Jacoba Aaftink,F,21,Netherlands,Speed Skating,NA
Christine Jacoba Aaftink,F,21,Netherlands,Speed Skating,NA
Christine Jacoba Aaftink,F,25,Netherlands,Speed Skating,NA
Christine Jacoba Aaftink,F,25,Netherlands,Speed Skating,NA
Christine Jacoba Aaftink,F,27,Netherlands,Speed Skating,NA
Christine Jacoba Aaftink,F,27,Netherlands,Speed Skating,NA
Per Knut Aaland,M,31,United States,Cross Country Skiing,NA
Per Knut Aaland,M,31,United States,Cross Country Skiing,NA
Per Knut Aaland,M,31,United States,Cross Country Skiing,NA
Per Knut Aaland,M,31,United States,Cross Country Skiing,NA
Per Knut Aaland,M,33,United States,Cross Country Skiing,NA
Per Knut Aaland,M,33,United States,Cross Country Skiing,NA
Per Knut Aaland,M,33,United States,Cross Country Skiing,NA
Per Knut Aaland,M,33,United States,Cross Country Skiing,NA
John Aalberg,M,31,United States,Cross Country Skiing,NA
John Aalberg,M,31,United States,Cross Country Skiing,NA
John Aalberg,M,31,United States,Cross Country Skiing,NA
John Aalberg,M,31,United States,Cross Country Skiing,NA
John Aalberg,M,33,United States,Cross Country Skiing,NA
John Aalberg,M,33,United States,Cross Country Skiing,NA
John Aalberg,M,33,United States,Cross Country Skiing,NA
John Aalberg,M,33,United States,Cross Country Skiing,NA
"Cornelia ""Cor"" Aalten (-Strannood)",F,18,Netherlands,Athletics,NA
"Cornelia ""Cor"" Aalten (-Strannood)",F,18,Netherlands,Athletics,NA
Antti Sami Aalto,M,26,Finland,Ice Hockey,NA
"Einar Ferdinand ""Einari"" Aalto",M,26,Finland,Swimming,NA
Jorma Ilmari Aalto,M,22,Finland,Cross Country Skiing,NA
Jyri Tapani Aalto,M,31,Finland,Badminton,NA
Minna Maarit Aalto,F,30,Finland,Sailing,NA
Minna Maarit Aalto,F,34,Finland,Sailing,NA
Pirjo Hannele Aalto (Mattila-),F,32,Finland,Biathlon,NA
Arvo Ossian Aaltonen,M,22,Finland,Swimming,NA
Arvo Ossian Aaltonen,M,22,Finland,Swimming,NA
Arvo Ossian Aaltonen,M,30,Finland,Swimming,Bronze
Arvo Ossian Aaltonen,M,30,Finland,Swimming,Bronze
Arvo Ossian Aaltonen,M,34,Finland,Swimming,NA
Juhamatti Tapio Aaltonen,M,28,Finland,Ice Hockey,Bronze
Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,Bronze
Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,Gold
Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,NA
Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,Gold
Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,NA
Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,NA
Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,NA
Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,Gold
Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,NA
Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,Bronze
Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,NA
Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,NA
Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,NA
Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,NA
Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,NA
Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,NA
Timo Antero Aaltonen,M,31,Finland,Athletics,NA
Win Valdemar Aaltonen,M,54,Finland,Art Competitions,NA
```

**Reading first 100 character of the content**

```python
ol_file = open("olympics.txt", "r")
contents_100 = ol_file.read(100)
print(contents_100)
```

**Output** :

```
Name,Sex,Age,Team,Event,Medal
A Dijiang,M,24,China,Basketball,NA
A Lamusi,M,23,China,Judo,NA
Gunnar
```

**Reading first line of the content**

```python
ol_file = open("olympics.txt", "r")
contents_line = ol_file.readline()
print(contents_line)
```

**Output** :

```
Name,Sex,Age,Team,Event,Medal
```

**Reading first 5 character of the first line of the content**

```python
ol_file = open("olympics.txt", "r")
contents_line_5 = ol_file.readline(5)
print(contents_line_5)
```

**Output** :

```
Name,
```

**Reading content as lines**

```python
ol_file = open("olympics.txt", "r")
contents_lines = ol_file.readlines()
print(contents_lines)
```

**Output** :

```
['Name,Sex,Age,Team,Event,Medal\n', 'A Dijiang,M,24,China,Basketball,NA\n', 'A Lamusi,M,23,China,Judo,NA\n', 'Gunnar Nielsen Aaby,M,24,Denmark,Football,NA\n', 'Edgar Lindenau Aabye,M,34,Denmark/Sweden,Tug-Of-War,Gold\n', 'Christine Jacoba Aaftink,F,21,Netherlands,Speed Skating,NA\n', 'Christine Jacoba Aaftink,F,21,Netherlands,Speed Skating,NA\n', 'Christine Jacoba Aaftink,F,25,Netherlands,Speed Skating,NA\n', 'Christine Jacoba Aaftink,F,25,Netherlands,Speed Skating,NA\n', 'Christine Jacoba Aaftink,F,27,Netherlands,Speed Skating,NA\n', 'Christine Jacoba Aaftink,F,27,Netherlands,Speed Skating,NA\n', 'Per Knut Aaland,M,31,United States,Cross Country Skiing,NA\n', 'Per Knut Aaland,M,31,United States,Cross Country Skiing,NA\n', 'Per Knut Aaland,M,31,United States,Cross Country Skiing,NA\n', 'Per Knut Aaland,M,31,United States,Cross Country Skiing,NA\n', 'Per Knut Aaland,M,33,United States,Cross Country Skiing,NA\n', 'Per Knut Aaland,M,33,United States,Cross Country Skiing,NA\n', 'Per Knut Aaland,M,33,United States,Cross Country Skiing,NA\n', 'Per Knut Aaland,M,33,United States,Cross Country Skiing,NA\n', 'John Aalberg,M,31,United States,Cross Country Skiing,NA\n', 'John Aalberg,M,31,United States,Cross Country Skiing,NA\n', 'John Aalberg,M,31,United States,Cross Country Skiing,NA\n', 'John Aalberg,M,31,United States,Cross Country Skiing,NA\n', 'John Aalberg,M,33,United States,Cross Country Skiing,NA\n', 'John Aalberg,M,33,United States,Cross Country Skiing,NA\n', 'John Aalberg,M,33,United States,Cross Country Skiing,NA\n', 'John Aalberg,M,33,United States,Cross Country Skiing,NA\n', '"Cornelia ""Cor"" Aalten (-Strannood)",F,18,Netherlands,Athletics,NA\n', '"Cornelia ""Cor"" Aalten (-Strannood)",F,18,Netherlands,Athletics,NA\n', 'Antti Sami Aalto,M,26,Finland,Ice Hockey,NA\n', '"Einar Ferdinand ""Einari"" Aalto",M,26,Finland,Swimming,NA\n', 'Jorma Ilmari Aalto,M,22,Finland,Cross Country Skiing,NA\n', 'Jyri Tapani Aalto,M,31,Finland,Badminton,NA\n', 'Minna Maarit Aalto,F,30,Finland,Sailing,NA\n', 'Minna Maarit Aalto,F,34,Finland,Sailing,NA\n', 'Pirjo Hannele Aalto (Mattila-),F,32,Finland,Biathlon,NA\n', 'Arvo Ossian Aaltonen,M,22,Finland,Swimming,NA\n', 'Arvo Ossian Aaltonen,M,22,Finland,Swimming,NA\n', 'Arvo Ossian Aaltonen,M,30,Finland,Swimming,Bronze\n', 'Arvo Ossian Aaltonen,M,30,Finland,Swimming,Bronze\n', 'Arvo Ossian Aaltonen,M,34,Finland,Swimming,NA\n', 'Juhamatti Tapio Aaltonen,M,28,Finland,Ice Hockey,Bronze\n', 'Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,Bronze\n', 'Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,Gold\n', 'Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,NA\n', 'Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,Gold\n', 'Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,NA\n', 'Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,NA\n', 'Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,NA\n', 'Paavo Johannes Aaltonen,M,28,Finland,Gymnastics,Gold\n', 'Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,NA\n', 'Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,Bronze\n', 'Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,NA\n', 'Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,NA\n', 'Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,NA\n', 'Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,NA\n', 'Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,NA\n', 'Paavo Johannes Aaltonen,M,32,Finland,Gymnastics,NA\n', 'Timo Antero Aaltonen,M,31,Finland,Athletics,NA\n', 'Win Valdemar Aaltonen,M,54,Finland,Art Competitions,NA']
```

**Reading the lines consist of the first 100 character of the content**

```python
ol_file = open("olympics.txt", "r")
contents_lines_5 = ol_file.readlines(100)
print(contents_lines_5)
```

**Output** :

```
['Name,Sex,Age,Team,Event,Medal\n', 'A Dijiang,M,24,China,Basketball,NA\n', 'A Lamusi,M,23,China,Judo,NA\n', 'Gunnar Nielsen Aaby,M,24,Denmark,Football,NA\n']
```

#### Iterating over lines in a file

We will now use this file as input in a program that will do some data processing. In the program, we will examine each line of the file and print it with some additional text. Because `readlines()` returns a list of lines of text, we can use the for loop to iterate through each line of the file.

A line of a file is defined to be a sequence of characters up to and including a special character called the newline character. If you evaluate a string that contains a newline character you will see the character represented as `\n`. If you print a string that contains a newline you will not see the `\n`, you will just see its effects (a carriage return).

As the for loop iterates through each line of the file the loop variable will contain the current line of the file as a string of characters. The general pattern for processing each line of a text file is as follows:

```python
for line in myFile.readlines():
    statement1
    statement2
    ...
```

To process all of our olypmics data, we will use a for loop to iterate over the lines of the file. Using the `split` method, we can break each line into a list containing all the fields of interest about the athlete. We can then take the values corresponding to name, team and event to construct a simple sentence.


```python
olympicsfile = open("olympics.txt","r")
for aline in olympicsfile.readlines():
  values = aline.split(",")
  print(values[0], "is from", values[3], "and is on the roster for", values[4])
olympicsfile.close()
```

**Output** :

```
Name is from Team and is on the roster for Event
A Dijiang is from China and is on the roster for Basketball
A Lamusi is from China and is on the roster for Judo
Gunnar Nielsen Aaby is from Denmark and is on the roster for Football
Edgar Lindenau Aabye is from Denmark/Sweden and is on the roster for Tug-Of-War
Christine Jacoba Aaftink is from Netherlands and is on the roster for Speed Skating
Christine Jacoba Aaftink is from Netherlands and is on the roster for Speed Skating
Christine Jacoba Aaftink is from Netherlands and is on the roster for Speed Skating
Christine Jacoba Aaftink is from Netherlands and is on the roster for Speed Skating
Christine Jacoba Aaftink is from Netherlands and is on the roster for Speed Skating
Christine Jacoba Aaftink is from Netherlands and is on the roster for Speed Skating
Per Knut Aaland is from United States and is on the roster for Cross Country Skiing
Per Knut Aaland is from United States and is on the roster for Cross Country Skiing
Per Knut Aaland is from United States and is on the roster for Cross Country Skiing
Per Knut Aaland is from United States and is on the roster for Cross Country Skiing
Per Knut Aaland is from United States and is on the roster for Cross Country Skiing
Per Knut Aaland is from United States and is on the roster for Cross Country Skiing
Per Knut Aaland is from United States and is on the roster for Cross Country Skiing
Per Knut Aaland is from United States and is on the roster for Cross Country Skiing
John Aalberg is from United States and is on the roster for Cross Country Skiing
John Aalberg is from United States and is on the roster for Cross Country Skiing
John Aalberg is from United States and is on the roster for Cross Country Skiing
John Aalberg is from United States and is on the roster for Cross Country Skiing
John Aalberg is from United States and is on the roster for Cross Country Skiing
John Aalberg is from United States and is on the roster for Cross Country Skiing
John Aalberg is from United States and is on the roster for Cross Country Skiing
John Aalberg is from United States and is on the roster for Cross Country Skiing
"Cornelia ""Cor"" Aalten (-Strannood)" is from Netherlands and is on the roster for Athletics
"Cornelia ""Cor"" Aalten (-Strannood)" is from Netherlands and is on the roster for Athletics
Antti Sami Aalto is from Finland and is on the roster for Ice Hockey
"Einar Ferdinand ""Einari"" Aalto" is from Finland and is on the roster for Swimming
Jorma Ilmari Aalto is from Finland and is on the roster for Cross Country Skiing
Jyri Tapani Aalto is from Finland and is on the roster for Badminton
Minna Maarit Aalto is from Finland and is on the roster for Sailing
Minna Maarit Aalto is from Finland and is on the roster for Sailing
Pirjo Hannele Aalto (Mattila-) is from Finland and is on the roster for Biathlon
Arvo Ossian Aaltonen is from Finland and is on the roster for Swimming
Arvo Ossian Aaltonen is from Finland and is on the roster for Swimming
Arvo Ossian Aaltonen is from Finland and is on the roster for Swimming
Arvo Ossian Aaltonen is from Finland and is on the roster for Swimming
Arvo Ossian Aaltonen is from Finland and is on the roster for Swimming
Juhamatti Tapio Aaltonen is from Finland and is on the roster for Ice Hockey
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Paavo Johannes Aaltonen is from Finland and is on the roster for Gymnastics
Timo Antero Aaltonen is from Finland and is on the roster for Athletics
Win Valdemar Aaltonen is from Finland and is on the roster for Art Competitions
```

To make the code a little simpler, and to allow for more efficient processing, Python provides a built-in way to iterate through the contents of a file one line at a time, without first reading them all into a list. Some students find this confusing initially, so we don’t recommend doing it this way, until you get a little more comfortable with Python. But this idiom is preferred by Python programmers, so you should be prepared to read it. And when you start dealing with big files, you may notice the efficiency gains of using it.

```python
olympicsfile = open("olympics.txt","r")

for aline in olympicsfile:
  values = aline.split(",")
  print(values[0], "is from", values[3], "and is on the roster for", values[4])
olympicsfile.close()
```

**Output** :

```
Name is from Team and is on the roster for Event
A Dijiang is from China and is on the roster for Basketball
A Lamusi is from China and is on the roster for Judo
Gunnar Nielsen Aaby is from Denmark and is on the roster for Football
Edgar Lindenau Aabye is from Denmark/Sweden and is on the roster for Tug-Of-War
Christine Jacoba Aaftink is from Netherlands and is on the roster for Speed Skating
Christine Jacoba Aaftink is from Netherlands and is on the roster for Speed Skating
...
```


----
----

**Check Your Understanding**

**E1** : Using the file `school_prompt2.txt`, find the number of characters in the file and assign that value to the variable `num_char`.

```python
sc_file = open("school_prompt2.txt", "r")
num_char = len(sc_file.read())
print(num_char)
```

**Output** :

```
536
```

---
**E2** : Find the number of lines in the file, `travel_plans2.txt`, and assign it to the variable `num_lines`.

```python
tr_file = open("travel_plans2.txt", "r")
num_lines = len(tr_file.readlines())
print(num_lines)
```

**Output** :

```
11
```

---
**E3** : Create a string called `first_forty` that is comprised of the first 40 characters of `emotion_words2.txt`.

```python
em_file = open("emotion_words2.txt", "r")
first_forty = em_file.read(40)
print(first_forty)
```

**Output** :

```
Sad upset blue down melancholy somber bi
```

---

**E4** : Write code to find out how many lines are in the file `emotion_words.txt`. Save this value to the variable `num_lines`. Do not use the len method.

```python
em_file = open("emotion_words.txt", "r")
num_lines = 0

for line in em_file:
    num_lines +=1
print(num_lines)
```

**Output** :

```
7
```

---

#### 1.3. Finding a File in Your File System

In the examples we have provided, and in the simulated file system that we’ve built for this online textbook, all files sit in a single directory, and it’s the same directory where the python program is stored. Thus, we can just write `open('myfile.txt','r')`.

If you have installed python on your local computer and you are trying to get file reading and writing operations to work, there’s a little more that you may need to understand. Computer operating systems (like Windows and the Mac OS) organize files into a hierarchy of folders, with some folders containing other folders.

![](https://fopp.umsi.education/runestone/static/fopp/_images/ExampleFileHierarchy.png)

If your file and your Python program are in the same directory you can simply use the filename. For example, with the file hierarchy in the diagram, the file myPythonProgram.py could contain the code `open('data1.txt','r')`.

If your file and your Python program are in different directories, however, then you need to specify a path. You can think of the filename as the short name for a file, and the path as the full name. Typically, you will specify a relative file path, which says where to find the file to open, relative to the directory where the code is running from. For example, the file myPythonProgram.py could contain the code `open('../myData/data2.txt','r')`. The `../` means to go up one level in the directory structure, to the containing folder (allProjects); `myData/` says to descend into the myData subfolder.

There is also an option to use an absolute file path. For example, suppose the file structure in the figure is stored on a computer in the user’s home directory,``/Users/joebob01/myFiles``. Then code in any python program running from any file folder could open data2.txt via `open('/Users/joebob01/myFiles/allProjects/myData/data2.txt','r')`. You can tell an absolute file path because it begins with a /. If you will ever move your programs and data to another computer (e.g., to share them with someone else), it will be much more convenient if your use relative file paths rather than absolute. That way, if you preserve the folder structure when moving everything, you won’t need to change your code. If you use absolute paths, then the person you are sharing with probably not have the same home directory name, /Users/joebob01/. Note that python pathnames follow the UNIX conventions (Mac OS is a UNIX variant), rather than the Windows file pathnames that use : and ‘’. The python interpreter will translate to Windows pathnames when running on a Windows machine; you should be able to share your python program between a Windows machine and a MAC without having to rewrite the file open commands.



----
----

**Check Your Understanding**

**E1** : Say you are in a directory called Project. In it, you have a file with your python code. You would like to read in data from a file called “YearlyProjections.csv” which is in a folder called CompanyData, which is inside of Project. What is the best way to open the file in your python program?

A. open("YearlyProjections.csv", "r") <br>
B. open("../CompanyData/YearlyProjections.csv", "r") <br>
C. open("CompanyData/YearlyProjections.csv", "r") ✅ <br>
D. open("Project/CompanyData/YearlyProjections.csv", "r") <br>
E. open("../YearlyProjections.csv", "r") <br>

---

**E2** : Which of the following paths are relative file paths?

A. "Stacy/Applications/README.txt" ✅<br>
B. "/Users/Raquel/Documents/graduation_plans.doc" <br>
C. "/private/tmp/swtag.txt" <br>
D. "ScienceData/ProjectFive/experiment_data.csv" ✅<br>

---

#### 1.4. Writing to a File

One of the most commonly performed data processing tasks is to read data from a file, manipulate it in some way, and then write the resulting data out to a new data file to be used for other purposes later. To accomplish this, the `open` function discussed above can also be used to create a new file prepared for writing. Note in Table 1 that the only difference between opening a file for writing and opening a file for reading is the use of the `'w'` flag instead of the `'r'` flag as the second parameter. When we open a file for writing, a new, empty file with that name is created and made ready to accept our data. If an existing file has the same name, its contents are overwritten. As before, the function returns a reference to the new file object.

Table 2 shows one additional method on file objects that we have not used thus far. The `write` method allows us to add data to a text file. Recall that text files contain sequences of characters. We usually think of these character sequences as being the lines of the file where each line ends with the newline `\n` character. Be very careful to notice that the `write` method takes one parameter, a string. When invoked, the characters of the string will be added to the end of the file. This means that it is the programmer’s job to include the newline characters as part of the string if desired.

Assume that we have been asked to provide a file consisting of all the squared numbers from 1 to 12.

First, we will need to open the file. Afterwards, we will iterate through the numbers 1 through 12, and square each one of them. This new number will need to be converted to a string, and then it can be written into the file.

The program below solves part of the problem. We first want to make sure that we’ve written the correct code to calculate the square of each number.


```python
for number in range(13):
	square = number * number
	print(square)
```

**Output** :

```
0
1
4
9
16
25
36
49
64
81
100
121
144
```

When we run this program, we see the lines of output on the screen. Once we are satisfied that it is creating the appropriate output, the next step is to add the necessary pieces to produce an output file and write the data lines to it. To start, we need to open a new output file by calling the `open` function, `outfile = open("squared_numbers.txt",'w')`, using the `'w'` flag. We can choose any file name we like. If the file does not exist, it will be created. However, if the file does exist, it will be reinitialized as empty and you will lose any previous contents.

Once the file has been created, we just need to call the `write` method passing the string that we wish to add to the file. In this case, the string is already being printed so we will just change the `print` into a call to the `write` method. However, there is an additional step to take, since the write method can only accept a string as input. We’ll need to convert the number to a string. Then, we just need to add one extra character to the string. The newline character needs to be concatenated to the end of the line. The entire line now becomes `outfile.write(str(square)+ '\n')`. The print statement automatically outputs a newline character after whatever text it outputs, but the write method does not do that automatically. We also need to close the file when we are done.

The complete program is shown below.

```python
filename = "squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1, 13):
	square = number * number
	outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read())
```

**Output** :

```
1
4
9
16
25
36
49
64
81
100
121
144
```

----
----

#### 1.5. Using `with` to Open Files

Now that you have seen and practiced a bit with opening and closing files, there is another mechanism that Python provides for us that cleans up the often forgotten close. Forgetting to close a file does not necessarily cause a runtime error in the kinds of programs you typically write in an introductory programing course. However if you are writing a program that may run for days or weeks at a time that does a lot of file reading and writing you may run into trouble.

Python has the notion of a context manager that automates the process of doing common operations at the start of some task, as well as automating certain operations at the end of some task. For reading and writing a file, the normal operation is to open the file and assign it to a variable. At the end of working with a file the common operation is to make sure that file is closed.

The Python with statement makes using context managers easy. The general form of a with statement is:

```Python
with <create some object that understands context> as <some name>:
	do some stuff with the object
	...
```

When the program exits the with block, the context manager handles the common stuff that normally happens at the end, in our case closing a file. A simple example will clear up all of this abstract discussion of contexts. Here are the contents of a file called “mydata.txt”.


```python
with open("mydata.txt", "r") as md:
	for line in md:
		print(line)
```

**Output** :

```
1 2 3

4 5 6
```

The first line of the with statement opens the file and assigns it to the variable `md`. Then we can iterate over the file in any of the usual ways. When we are done we simply stop indenting and let Python take care of closing the file and cleaning up. The final line `print(md)`

This is equivalent to code that specifically closes the file at the end, but neatly marks the set of code that can make use of the open file as an indented block, and ensures that the programmer won’t forget to include the `.close()` invocation.

```python
md = open("mydata.txt", "r")
for line in md:
	print(line)
md.close()
```

**Output** :

```
1 2 3

4 5 6
```

#### Recipe for Reading and Processing a File

Here’s a foolproof recipe for processing the contents of a text file. If you’ve fully digested the previous sections, you’ll understand that there are other options as well. Some of those options are preferable for some situations, and some are preferred by python programmers for efficiency reasons. In this course, though, you can always succeed by following this recipe.

1. Open the file using `with` and `open`.

2. Use `.readlines()` to get a list of the lines of text in the file.

3. Use a `for` loop to iterate through the strings in the list, each being one line from the file. On each iteration, process that line of text

4. When you are done extracting data from the file, continue writing your code outside of the indentation. Using `with` will automatically close the file once the program exits the with block.


```python
fname = "yourfile.txt"

with open(fname, "r") as fileref:
	lines = fileref.readlines()
	for line in lines:
		#some code that references the variable line
		print(line)
#some other code not relying on fileref
```

However, this will not be good to use when you are working with large data. Imagine working with a datafile that has 1000 rows of data. It would take a long time to read in all the data and then if you had to iterate over it, even more time would be necessary. This would be a case where programmers prefer another option for efficiency reasons.

This option involves iterating over the file itself while still iterating over each line in the file:

```python
fname = "yourfile.txt"

with open(fname, "r") as fileref:
	for line in fileref:
		#some code that references the variable line
		print(line)
#some other code not relying on fileref
```

----
----

### CSV Output

#### 1.6. Reading a .csv File

CSV stands for Comma Separated Values. If you print out tabular data in CSV format, it can be easily imported into other programs like Excel, Google spreadsheets, or a statistics package (R, stata, SPSS, etc.).

For example, we can make a file with the following contents. If you save it as a file name grades.csv, then you could import it into one of those programs. The first line gives the column names and the later lines each give the data for one row.

```
Name,score,grade
Jamal,98,A+
Eloise,87,B+
Madeline,99,A+
Wei,94,A
```

We are able to read in CSV files the same way we have with other text files. Because of the standardized structure of the data, there is a common pattern for processing it. To practice this, we will be using data about olympic events.

Typically, CSV files will have a header as the first line, which contains column names. Then, each following row in the file will contain data that corresponds to the appropriate columns.

All file methods that we have mentioned - `read`, `readline`, and `readlines`, and simply iterating over the file object itself - will work on CSV files. In our examples, we will iterate over the lines. Because the values on each line are separated with commas, we can use the `.split()` method to parse each line into a collection of separate value.


```python
fileconnection = open("olympics.txt", "r")
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(",")
print(field_names)

for row in lines[1:]:
	vals = row.strip().split(",")
	if vals[5] != "NA":
		print("{}: {}; {}".format(
					vals[0],
					vals[4],
					vals[5]))
```

**Output** :

```
['Name', 'Sex', 'Age', 'Team', 'Event', 'Medal']
Edgar Lindenau Aabye: Tug-Of-War; Gold
Arvo Ossian Aaltonen: Swimming; Bronze
Arvo Ossian Aaltonen: Swimming; Bronze
Juhamatti Tapio Aaltonen: Ice Hockey; Bronze
Paavo Johannes Aaltonen: Gymnastics; Bronze
Paavo Johannes Aaltonen: Gymnastics; Gold
Paavo Johannes Aaltonen: Gymnastics; Gold
Paavo Johannes Aaltonen: Gymnastics; Gold
Paavo Johannes Aaltonen: Gymnastics; Bronze
```

In the above code, we open the file, olympics.txt, which contains data on some olympians. The contents are similar to our previous olympics file, but include an extra column with information about medals they won.

We split the first row to get the field names. We split other rows to get values. Note that we specify to split on commas by passing that as a parameter. Also note that we first pass the row through the `.strip()` method to get rid of the trailing n.

Once we have parsed the lines into their separate values, we can use those values in the program. For example, in the code above, we select only those rows where the olympian won a medal, and we print out only three of the fields, in a different format.

Note that the trick of splitting the text for each row based on the presence of commas only works because commas are not used in any of the field values. Suppose that some of our events were more specific, and used commas. For example, “Swimming, 100M Freestyle”. How will a program processing a .csv file know when a comma is separating columns, and when it is just part of the text string giving a value within a column?

The CSV format is actually a little more general than we have described and has a couple of solutions for that problem. One alternative format uses a different column separator, such as | or a tab (t). Sometimes, when a tab is used, the format is called tsv, for tab-separated values). If you get a file using a different separator, you can just call the `.split('|')` or `.split('\\t')`.

The other advanced CSV format uses commas to separate but encloses all values in double quotes.

For example, the data file might look like:

```
"Name","Sex","Age","Team","Event","Medal"
"A Dijiang","M","24","China","Basketball","NA"
"Edgar Lindenau Aabye","M","34","Denmark/Sweden","Tug-Of-War","Gold"
"Christine Jacoba Aaftink","F","21","Netherlands","Speed Skating, 1500M","NA"
```

If you are reading a .csv file that has enclosed all values in double quotes, it’s actually a pretty tricky programming problem to split the text for one row into a list of values. You won’t want to try to do it directly. Instead, you should use python’s built-in csv module. However, there’s a bit of a learning curve for that, and we find that students gain a better understanding of reading CSV format by first learning to read the simple, unquoted format and split lines on commas.

----
----

#### 1.7. Writing Data to a .csv File

The typical pattern for writing data to a CSV file will be to write a header row and loop through the items in a list, outputting one row for each. Here we a have a list of tuples, each representing one Olympian, a subset of the rows and columns from the file we have been reading from.



```python
olympians = [("John Aalberg", 31, "Cross Country Skiing"),
            ("Minna Maarit Aalto", 30, "Sailing"),
            ("Win Valdemar Aaltonen", 54, "Art Competitions"),
            ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
outfile.write("Name,Age,Sport")
outfile.write("\n")

for olympian in olympians:
	row_string = "{},{},{}".format(olympian[0], olympian[1], olympian[2])
	outfile.write(row_string)
	outfile.write("\n")

outfile.close()

# to test
oly_file = open("reduced_olympics.csv", "r")
print(oly_file.read())
oly_file.close()
```

**Output** :

```
Name,Age,Sport
John Aalberg,31,Cross Country Skiing
Minna Maarit Aalto,30,Sailing
Win Valdemar Aaltonen,54,Art Competitions
Wakako Abe,18,Cycling
```


There are a few things worth noting in the code above.

First, using `.format()` makes it really clear what we’re doing when we create the variable row_string. We are making a comma separated set of values; the `{}` curly braces indicated where to substitute in the actual values. The equivalent string concatenation would be very hard to read. An alternative, also clear way to do it would be with the `.join method: row_string = ','.join(olympian[0], olympian[1], olympian[2])`.

Second, unlike the print statement, remember that the .write() method on a file object does not automatically insert a newline. Instead, we have to explicitly add the character `\n` at the end of each line.

Third, we have to explicitly refer to each of the elements of olympian when building the string to write. Note that just putting `.format(olympian)` wouldn’t work because the interpreter would see only one value (a tuple) when it was expecting three values to try to substitute into the string template. Later in the book we will see that python provides an advanced technique for automatically unpacking the three values from the tuple, with `.format(*olympian)`.

As described previously, if one or more columns contain text, and that text could contain commas, we need to do something to distinguish a comma in the text from a comma that is separating different values (cells in the table). If we want to enclose each value in double quotes, it can start to get a little tricky, because we will need to have the double quote character inside the string output. But it is doable. Indeed, one reason Python allows strings to be delimited with either single quotes or double quotes is so that one can be used to delimit the string and the other can be a character in the string. If you get to the point where you need to quote all of the values, we recommend learning to use python’s csv module.


```python
olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
            ("Minna Maarit Aalto", 30, "Sailing"),
            ("Win Valdemar Aaltonen", 54, "Art Competitions"),
            ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics2.csv","w")
# output the header row
outfile.write('"Name","Age","Sport"')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()


# to test
oly_file2 = open("reduced_olympics2.csv", "r")
print(oly_file2.read())
oly_file2.close()
```

**Output** :

```
"Name","Age","Sport"
"John Aalberg", "31", "Cross Country Skiing, 15KM"
"Minna Maarit Aalto", "30", "Sailing"
"Win Valdemar Aaltonen", "54", "Art Competitions"
"Wakako Abe", "18", "Cycling"
```

----
----


#### 1.8. Tips on File Naming

When working with files, there are a few things to keep in mind. When naming files, it’s best to not include spaces. While most operating systems can handle files with spaces in their names, not all can.

Additionally, suffixes in files names, for example the .txt in `FileNameExample.txt`, are not magic. Instead, these suffixes are a convention. For some operating systems the suffixes have no special significance, and only have meaning when used in a program. Other operating systems infer information from the suffixes - for example, `.EXE` is a suffix that means a file is executable.

It’s a good idea to follow the conventions. If a file contains CSV formatted data, name it with the extension `.csv`, not `.txt`. A python program will be able to read it either way, but if you follow the convention you will help other people guess what’s in the file. And you will also help the computer’s operating system to guess what application program it should open when you double-click on the file.


----
----


#### 1.9. Chapter Assessments & Exercises

#### Assessments

**A1**. The textfile, `travel_plans.txt`, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable `num`.


```python
tr_file = open("travel_plans.txt", "r").read()
num = 0

for char in tr_file:
    num += 1

print(num)
```

**Output** :

```
315
```

-----

**A2**. We have provided a file called `emotion_words.txt` that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable `num_words`.


```python
emo_file = open("emotion_words.txt", "r").read()
num_words = len(emo_file.split())
print(num_words)
```

**Output** :

```
48
```

-----

**A3**. Assign to the variable `num_lines` the number of lines in the file `school_prompt.txt`.


```python
sc_file = open("school_prompt.txt", "r").readlines()
num_lines = 0

for line in sc_file:
    num_lines += 1

print(num_lines)
```

**Output** :

```
10
```

-----


**A4**. Assign the first 30 characters of `school_prompt.txt` as a string to the variable `beginning_chars`.


```python
beginning_chars = open("school_prompt.txt", "r").read(30)
print(beginning_chars)
```

**Output** :

```
30
```

-----

**A5**. Challenge: Using the file `school_prompt.txt`, assign the third word of every line to a list called `three`.


```python
sch_file = open("school_prompt.txt", "r").readlines()
three = []

for line in sch_file:
    line = line.strip().split()
    three.append(line[2])

print(three)
```

**Output** :

```
['for', 'find', 'to', 'many', 'they', 'solid', 'for', 'have', 'some', 'ups,']
```

-----

**A6**. Challenge: Create a list called `emotions` that contains the first word of every line in `emotion_words.txt`.


```python
emo_file = open("emotion_words.txt", "r").readlines()
emotions = []

for line in emo_file:
    line = line.strip().split()
    emotions.append(line[0])

print(emotions)
```

**Output** :

```
['Sad', 'Angry', 'Happy', 'Confused', 'Excited', 'Scared', 'Nervous']
```

-----

-----

**A7**. Assign the first 33 characters from the textfile, `travel_plans.txt` to the variable `first_chars`.


```python
first_chars = open("travel_plans.txt", "r").read(33)
print(first_chars)
```

**Output** :

```
This summer I will be travelling.
```

-----

**A8**. Challenge: Using the file `school_prompt.txt`, if the character ‘p’ is in a word, then add the word to a list called `p_words`.


```python
sc_file = open("school_prompt.txt", "r").read()

words = sc_file.split()
p_words = []

for word in words:
    if "p" in word:
        p_words.append(word)
print(p_words)
```

**Output** :

```
['topic', 'point', 'papers,', 'ups,', 'scripts.']
```

----
----

#### Exercises

**Q1**. The following sample file called `studentdata.txt` contains one line for each student in an imaginary class. The students name is the first thing on each line, followed by some exam scores. The number of scores might be different for each student.

```
joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10
john 14 32 25 16 89
```

Using the text file `studentdata.txt` write a program that prints out the names of students that have more than six quiz scores.


```python
stu_file = open("studentdata.txt", "r")

for student in stu_file.readlines():
    student = student.strip().split()
    if len(student) > 7:
        print(student[0])
```

**Output** :

```
sue
```

----

**Q2**. Create a list called `destination` using the data stored in `travel_plans.txt`. Each element of the list should contain a line from the file that lists a country and cities inside that country. Hint: each line that has this information also has a colon `:` in it.


```python
tr_file = open("travel_plans.txt", "r")
destination = []

for line in tr_file.readlines():
    if ":" in line:
        destination.append(line)
print(destination)
tr_file.close()
```

**Output** :

```
['Italy: Rome\n', 'Greece: Athens\n', 'England: London, Manchester\n', 'France: Paris, Nice, Lyon\n', 'Spain: Madrid, Barcelona, Granada\n', 'Austria: Vienna\n']
```

----

**Q3**. Create a list called `j_emotions` that contains every word in `emotion_words.txt` that begins with the letter `“j”`.


```python
emo_file = open("emotion_words.txt", "r")
emo_content = emo_file.read().split()
j_emotions = []

for emo in emo_content:
    if emo[0] == "j":
        j_emotions.append(emo)

print(j_emotions)
```

**Output** :

```
['joyous', 'jittery', 'jumpy']
```

----
