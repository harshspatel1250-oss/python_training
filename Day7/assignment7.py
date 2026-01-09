#1 write a program that opens a text file and reads the contents of the file.

file = open("text.txt", "r")

content = file.read()
print(content)

file.close()

#2 Write a program that opens a text file and writes some text to the file.

file = open("text.txt", "w")

file.write("I am python programmer.\n")

file.close()

#3 Write a program that opens a binary file and reads the first 10 bytes of the file.

file= open("text.txt", "rb")
data = file.read(10)
print(data)

#4 Write a program that creates a new text file, writes some text to the file, and then renames the file.
import os

file = open("second.txt", "w")
file.write("Technology is the application of scientific knowledge to create tools, techniques, and systems that solve problems, achieve goals, and improve human life.\n")


print("File created")

os.rename("second.txt", "first.txt")

print("File renamed")

#5 Write a program that deletes a text file.
import os

os.remove("first.txt")

print("delete successfully.")


