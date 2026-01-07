#List Manipulation. Remove the duplicated from the list.

input_list=list(map(int,input("Enter the values separated by space:").split()))
Enter the values separated by space:10 20 30 20 40

set1=set(input_list)
list2=list(set1)
print(f"remove the duplicate into list{list2}")
remove the duplicate into list[40, 10, 20, 30]

#  Sort the list in descending order.

input_list.sort(reverse=True)
print(f"descending order:",input_list)

# Calculate the sum of all the elements in the list

total=sum(input_list)
print(total)

#2 Tuple operations:
#Create a tuple containing the names of five countries. Write a Python program that performs the following operations:
my_tuple=("India","Canada","Africa","Paris","USA")

#print the length of tuple
print(len(my_tuple))

# Check if a given country is present in the tuple
if "Paris" in my_tuple:
     print("yes")
else:
     print("not available") 

#Create a new tuple by concatenating the original tuple with another tuple containing five more countries.
my_tuple2=("China","Iran","Dubai","UAE","Thailand")
print(my_tuple + my_tuple2)

# Extra: Try modifying the element at 2nd index. What is output and why. Discuss it
my_tuple[3]="Bali"

#TypeError: 'tuple' object does not support item assignment
#tuple is immutable so not changeable

#3 Dictionary Manipulation:

stoke={
    "Banana":10,
    "Apple":20,
    "Mango":30,
    }
print(stoke)

#add new item
stoke['Orange']=25
print(stoke)

#Update the quantity of an existing item.
stoke['Banana']=50
print(stoke)

#remove an item from the stoke
print(stoke.pop('Orange'))

# Print the items in stock alphabetically sorted along with their quantities
for item in sorted(stoke):
    print(item, ">", stoke[item])

#4 List Comprehensions:
# Write a Python program that generates a list of squares of even numbers between 1 and 20 using list comprehension

squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(squares)

#5 Dictionary Iteration
#Create a dictionary representing the population of five different cities. Write a Python program that prints the city with the highest population along with its populatio

population = {
  "Ahmedabad": 174,
  "Delhi": 400,
  "Pune": 120,
  "Banglore": 200,
  "Gurugram": 190
  }
city=max(population,key=population.get)

print(city, ">",population[city])

#6 Tuple Unpacking:
#Write a Python program that takes a tuple of three integers representing the sides of a triangle as input and determines if it forms a valid triangle. If it does, print its type (equilateral, isosceles, or scalene).

sides = tuple(map(int, input("Enter three sides of the triangle: ").split()))
a,b,c=sides

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
    
    if a==b==c:
        print("Triangle is equilateral")
    elif a==b or b==c or c==a:
        print("Triangle is scalene")
    else:
         print("Triangle is isosceles")
else:
    print(" It is Not Valid Triangle")

#7. List sorting
#Write a Python program that takes a list of tuples, where each tuple contains a student's name and their score in a test. Sort the list based on the scores in descending order and print the names of the top three students.
# List of tuples (student_name, score)
students = [
    ("Prit", 80),
    ("Smit", 95),
    ("Mit", 80),
    ("Devarsh", 78),
    ("Om", 65)
]

students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
print(students_sorted)

print("Top 3 Students:")
for student in students_sorted[:3]:
    print(student[0])

#8. Dictionary Filtering:
#Create a dictionary representing the prices of different items in a store. Write a Python program that filters out the items with prices less than a given threshold and prints them.
price = {
    "Milk": 50,
    "Almond": 120,
    "Sugar": 80,
    "Gud": 90,
    "Masala": 70
}

threshold = int(input("Enter the threshold value: "))

for item, price in prices.items():
    if price < threshold:
        print(item, ":", price)
#9. List Operations:
#Write a Python program that takes two lists of integers as input and performs the following operations:

list1=list(map(int,input("Enter the values separated by space:").split()))
list2=list(map(int,input("Enter the values separated by space:").split()))

set1=set(list1)
set2=set(list2)

# Find the intersection of the two lists (common elements)

common_element=list(set1 & set2)
print(common_element)

# Find the union of the two lists (all elements without duplicates)

union_element=list(set1 | set2)
print(union_element)

# Find the elements present in the first list but not in the second list

difference_element=list(set1 - set2)
print(difference_element)

#10. Dictionary Sorting:
#Write a Python program that takes a dictionary containing names as keys and their corresponding ages as values. Sort the dictionary based on ages in ascending order and print the names of the oldest and youngest person.

Dict = {'parth': 23, 'temp': 24, 'nikul': 18}

sorted_dict = dict(sorted(Dict.items(), key=lambda x: x[1]))

oldest=max(Dict,key=Dict.get)
youngest=min(Dict,key=Dict.get)


print("Sorted Dictionary:", sorted_dict)
print("Youngest Person:", youngest)
print("Oldest Person:", oldest)



