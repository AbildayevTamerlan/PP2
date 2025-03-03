# Task 1
import os

path = r"C:\KBTU\PP2"

print("Files:")
for entry in os.scandir(path):
   if entry.is_file():
      print(entry.name)

print("\nDirectories:")
for entry in os.scandir(path):
   if entry.is_dir():
      print(entry.name)

print("\nFiles and directories:")
for entry in os.scandir(path):
   print(entry.name)

print()


# Task 2
path = r"C:\KBTU\PP2\Lab01"

if os.path.exists(path):
   print(path)
    
   print(os.access(path, os.R_OK))
   print(os.access(path, os.W_OK))
   print(os.access(path, os.X_OK))

print()


# Task 3
path = r"C:\KBTU\PP2\Lab06"

for entry in os.scandir(path):
   if entry.is_file():
      file_path = entry.path
      directory, filename = os.path.split(file_path)

print(file_path)
print(directory)
print(filename)

print()


# Task 4
f = open("demofile1.txt")

n_lines = 0

for x in f:
   n_lines += 1

print(n_lines)

f.close()

print()


# Task 5
my_list = ["apple", "banana", "cherry"]

f = open("list.txt", "w")

for item in my_list:
   f.write(item + "\n")

f.close()

f = open("list.txt")

print(f.read())


# Task 6
import string

for letter in string.ascii_uppercase:
   f = open(f"{letter}.txt", "w")
   f.close()


# Task 7
f1 = open("demofile1.txt")

f2 = open("demofile2.txt", "w")

f2.write(f1.read())

f1.close()
f2.close()


# Task 8
for letter in string.ascii_uppercase:
   if os.path.exists(f"{letter}.txt"):
      os.remove(f"{letter}.txt")