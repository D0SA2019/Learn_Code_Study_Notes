# 12. File Input/Output

### 12.1. See It to Believe It
Until now, the Python code you've been writing comes from one source and only goes to one place: you type it in at the keyboard and its results are displayed in the console. But what if you want to read information from a file on your computer, and/or write that information to another file?

This process is called *file I/O* (the "I/O" stands for "input/output"), and Python has a number of built-in functions that handle this for you.

Check out the code in the editor to the right.


##### Instructions
Click Run! You just wrote all the contents of `my_list` to a text file called `output.txt`.


```Python
# GIVEN
my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()


# on output.txt in the file
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
```


### 12.2. The open() Function
Let's walk through the process of writing to a file one step at a time.

The first code that you saw executed in the previous exercise was this:

```Python
f = open("output.txt", "w")
```

This told Python to open `output.txt` in `"w"` mode ("w" stands for "write"). We stored the result of this operation in a file object, `f`.

Doing this opens the file in write-mode and prepares Python to send data into the file.


##### Instructions
Create a variable, `my_file`, and set it equal to calling the `open()` function on `output.txt`. In this case, pass `"r+"` as a second argument to the function so the file will allow you to read *and* write to it!


You can open files in any of the following modes:

* write-only mode (`"w"`)
* read-only mode (`"r"`)
* read and write mode (`"r+"`)
* append mode (`"a"`), which adds any new data you write to the file to the end of the file.


```Python
# SOLUTION
my_file = open("output.txt", "r+")
print(my_file)


# OUTPUT
<_io.TextIOWrapper name='output.txt' mode='r+' encoding='UTF-8'>
```


### 12.3. Writing
Good work! Now it's time to write some data to a new `.txt` file.

We added the list comprehension from the first exercise to the code in the editor. Our goal in this exercise will be to write each element of that list to a file called `output.txt`. The `output.txt` file that you write to will be created in your current folder - for simplicity, the folder has been hidden. `output.txt` will list each number on its own line.

We can write to a Python file like so:

```Python
my_file.write("Data to be written")
```

The `.write()` method takes a string argument, so we'll need to do a few things here:

You must close the file. You do this simply by calling `my_file.close()` (we did this for you in the last exercise). If you don't close your file, Python won't write to it properly. From here on out, you gotta close your files!

##### Instructions

Iterate over `my_list` to get each value.

Use `my_file.write()` to write each value to a text file called, `output.txt`.

Make sure to call `str()` on the iterating data so `.write()` will accept it.

Make sure to add a newline `(+ "\n")` after each element to ensure each will appear on its own line.

Use `my_file.close()` to close the file when you're done.

Passing the exercise means that you successfully wrote `my_list` to `output.txt`!


```Python
# GIVEN
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")



# SOLUTION
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!
for i in my_list:
  my_file.write(str(i) + "\n")

my_file.close()


# on output.txt in the file
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
```


### 12.4. Reading
Excellent! You're a pro.

Finally, we want to know how to read from our `output.txt` file. As you might expect, we do this with the `read()` function, like so:

```Python
my_file = open("output.txt", "r")
print(my_file.read())


# OUTPUT
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
```

##### Instructions

Declare a variable, `my_file`, and set it equal to the file object returned by calling `open()` with both `"output.txt"` and `"r"`.

Next, `print` the result of using `.read()` on `my_file`, like the example above.

Make sure to `.close()` your file when you're done with it! All kinds of doom will happen if you don't.


```Python
# SOLUTION
my_file = open("output.txt", "r")

print(my_file.read())
my_file.close()



# OUTPUT
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
```

### 12.5. Reading Between the Lines
What if we want to read from a file line by line, rather than pulling the entire file in at once. Thankfully, Python includes a `.readline()` method that does exactly that.

If you open a file and call `.readline()` on the file object, you'll get the first line of the file; subsequent calls to `.readline()` will return successive lines.


##### Instructions
Declare a new variable `my_file` and store the result of calling `open()` on the `"text.txt"` file in `"r"`ead-only mode.

On three separate lines, `print` out the result of calling `my_file.readline()`. See how it gets the next line each time?

Don't forget to `.close()` your file when you're done with it!


```Python
# SOLUTION
my_file = open("text.txt", "r")
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

my_file.close()



# OUTPUT
I'm the first line of the file!

I'm the second line.

Third line here, boss.
```

### 12.6. PSA: Buffering Data
We keep telling you that you always need to close your files after you're done writing to them. Here's why!

During the I/O process, data is *buffered*: this means that it is held in a temporary location before being written to the file.

Python doesn't *flush the buffer*—that is, write data to the file—until it's sure you're done writing. One way to do this is to close the file. If you write to a file without closing, the data won't make it to the target file.



##### Instructions

Check out our *extremely* bad code in the editor. Click Run—you'll note that our `read_file.read()` didn't read any data back!

* Add a `write_file.close()` call after writing to the file but before reading it.
* Add a `read_file.close()` call after the `print read_file.read()` line
* Run the code again.
* This time, you'll see the data come through!

```Python
# GIVEN
# Use a file handler to open a file for writing
write_file = open("text.txt", "w")

# Open the file for reading
read_file = open("text.txt", "r")

# Write to the file
write_file.write("Not closing files is VERY BAD.")

# Try to read from the file
print(read_file.read())



# SOLUTION
write_file = open("text.txt", "w")
write_file.close()

read_file = open("text.txt", "r")
read_file.close()

write_file.write("Not closing files is VERY BAD.")

print(read_file.read())



# OUTPUT
Traceback (most recent call last):
  File "12_File_Input_Output.py", line 79, in <module>
    write_file.write("Not closing files is VERY BAD.")
ValueError: I/O operation on closed file.
```

### 12.7. The 'with' and 'as' Keywords
Programming is all about getting the computer to do the work. Is there a way to get Python to automatically close our files for us?

Of course there is. This is Python.

You may not know this, but file objects contain a special pair of built-in methods:` __enter__()` and `__exit__()`. The details aren't important, but what is important is that when a file object's `__exit__()` method is invoked, it automatically closes the file. How do we invoke this method? With `with` and `as`.

The syntax looks like this:

```Python
with open("file", "mode") as variable:
  # Read or write to the file
```


##### Instructions
Check out the example in the editor. Note that we don't explicitly `close()` our file, and remember that if we don't close a file, our data will get stuck in the buffer. Click Run!

`Success!` is written to a file called `text.txt`.


```Python
# GIVEN
with open("text.txt", "w") as textfile:
  textfile.write("Success!")

fi = open("text.txt", "r+")
print(fi.read())


# OUTPUT
Success!
```

### 12.8. Try It Yourself
It worked! Our Python program successfully wrote to text.txt.


##### Instructions

Now you try: write any data you like to a file called `text.txt` using `with`...`as`. Give your file object the usual name: `my_file`.

```Python
# SOLUTION
with open("text.txt", "r+") as my_file:
  my_file.write("New thing!")

fil = open("text.txt", "r+")
print(fil.read())


# OUTPUT
New thing!
```

### 12.9. Case Closed?
Finally, we'll want a way to test whether a file we've opened is closed. Sometimes we'll have a lot of file objects open, and if we're not careful, they won't all be closed. How can we test this?

```Python
f = open("text.txt")
print(f.closed)

f.close()
print(f.closed)


# OUTPUT
False
True
```

Python file objects have a `closed` attribute which is `True` when the file is closed and `False` otherwise.

By checking `file_object.closed`, we'll know whether our file is closed and can call `close()` on it if it's still open.


##### Instructions

Below your `with`...`as` code, do two things:

* Check `if` the file is not `closed`.
* If that's the case, call `.close()` on it.
* (You don't need an `else` here, since your `if` statement should do nothing if `closed` is `True`.)
* After your `if` statement, `print` out the value of `my_file.closed` to make sure your file is really closed.


```Python
# GIVEN
with open("text.txt", "r+") as my_file:
  my_file.write("New thing!")


# SOLUTION
with open("text.txt", "r+") as my_file:
  my_file.write("New thing!")

  if not my_file.closed:
    my_file.close()
  print(my_file.closed)


# OUTPUT
True
```
