#1 Write a program that takes a number as input from the user and displays whether the number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("This number is Even")
else:
    print("This number is Odd")

#2 Write a program that takes a list of numbers as input from the user and displays the sum of all the even numbers in the list.

numbers = list(map(int, input("Enter numbers: ").split()))

even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num

print("Sum of even numbers:", even_sum)

#3 Write a program that displays the numbers from 1 to 10 using a for loop. (try with single line)

print(*range(1, 11))

#4 Write a program that takes a number as input from the user and displays the multiplication table of the number using a while loop.

num = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

#5 Write a program that takes a list of numbers as input from the user and displays only the odd numbers in the list using a for loop.

numbers = list(map(int, input("Enter numbers: ").split()))

print("Odd numbers in the list:")
for num in numbers:
    if num % 2 != 0:
        print(num)

#6 Write a program that takes a number as input from the user and displays whether the number is prime or not using a try-except block.

try:
    n = int(input("Enter a number: "))

    if n < 2:
        print("Not a Prime Number")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("Not a Prime Number")
                break
        else:
            print("Prime Number")

except ValueError:
    print("Please enter a valid integer.")




