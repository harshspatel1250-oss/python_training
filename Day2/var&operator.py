#1 Create a variable called "age" and assign it the value 25

age = 25

#2 Create a variable called "name" and assign it your name as a string
name = "Harsh"

#3 Create a variable called "temperature" and assign it a float value representing the current temperature in degrees Celsius
temperature = 17.2

#4 Calculate the area of a rectangle with length 5 and width 10, and assign the result to a variable called "area"
length = 5
width = 10
area = length*width
print(area)

#5 Increment the value of the "age" variable by 1 using a compound assignment operator
age = 21
age += 1
print(age)

#6 Create function in python which take integer as input and convert it to binary string. Input 5 → 101. 7 → 111

def int_to_binary(n):
    return bin(n)[2:]
print(int_to_binary(5)) 
