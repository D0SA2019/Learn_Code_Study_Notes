print("")
print("------ 12. File Input/Output ------")

print("")
print("------ 12.1. See It to Believe It ------")
my_list = [i ** 2 for i in range(1, 11)]

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()






print("")
print("------ 12.2. The open() Function ------")
my_file = open("output.txt", "r+")
print(my_file)
my_file.close()





print("")
print("------ 12.3. Writing ------")
my_list = [i ** 3 for i in range(1, 11)]

my_file = open("output1.txt", "w")

# Add your code below!
for i in my_list:
  my_file.write(str(i) + "\n")

my_file.close()






print("")
print("------ 12.4. Reading ------")
my_file = open("output.txt", "r")
print(my_file.read())
my_file.close()






print("")
print("------ 12.5. Reading Between the Lines ------")
my_file = open("text.txt", "r")
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.close()






print("")
print("------ 12.7. The 'with' and 'as' Keywords ------")
with open("text.txt", "w") as textfile:
  textfile.write("Success!")

fi = open("text.txt", "r+")
print(fi.read())






print("")
print("------ 12.8. Try It Yourself ------")
with open("text.txt", "r+") as my_file:
  my_file.write("New thing!")

fil = open("text.txt", "r+")
print(fil.read())






print("")
print("------ 12.9. Case Closed? ------")
f = open("text.txt")
print(f.closed)

f.close()
print(f.closed)

print("")

with open("text.txt", "r+") as my_file:
  my_file.write("New thing!")

  if not my_file.closed:
    my_file.close()
  print(my_file.closed)
