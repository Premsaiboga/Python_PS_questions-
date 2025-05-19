# 1.Write a program to check if a number is even or odd. An even number is divisible by 2, while an odd number is not
z = int(input("enter a number: "))
if z%2 ==0:
    print("even")
else:
    print("odd")
print("------------------------------------------------------")

# 2.Check if a Year is a Leap Year

year = int(input("enter a year: "))
if year%400==0 and year%100==0:
     print("It is a leap year")
elif year%4==0 and year%100 != 0:
      print("It is a leap year")
else:
    print("it is not a leap year")
print("------------------------------------------------------")

# 3. Write a program that checks if a number is divisible by both 3 and 5. If it is, print "Divisible by 3 and 5", otherwise print "Not divisible by 3 and  5
a = int(input("Enter a number: "))
if a%3 ==0 and a%5==0:
     print(a,"is dvisible by 3 and 5")
else:
     print(a,"It is not divisible by 3 and 5")
print("------------------------------------------------------")


# 4.Write a program that checks if a person is eligible to vote. The eligibility condition is that the person's age should be 18 or older
b = int(input("enter your age: "))
if b>=18:
     print("You are eligibile for voteing")
else:
     print("you are not eligible for voteing")
print("------------------------------------------------------")

# 5.Write a program to check if a given number is a multiple of 10
c = int(input("enter a number: "))
if c%10==0:
     print(c,"is multiple of 10")
else:
     print(c,"is not a multiple of 10")
print("------------------------------------------------------")

# 6.Write a program to compare two numbers and print the smaller one
d=int(input("enter 1st value to compare: "))
e=int(input("enter 2nd value: "))
match d>e:
     case 0:
          print(d,"is the smallest number")
     case 1:
          print(e,"is the smallest number")
print("------------------------------------------------------")

# 7. Write a program that asks the user for a number and prints:
# "Even" if the number is divisible by 2,
# "Odd" if the number is not divisible by 2,
# "Divisible by 5" if the number is divisible by 5 (but not by 2),
# "Not divisible by 2 or 5" if the number is neither divisible by 2 nor 5.
# Example:
# Input: 10
# Output: Even
# Input: 7
# Output: Odd
# Input: 15
# Output: Divisible by 5
f=int(input("enter a numbr: "))
if f % 2 == 0:
    print("Even")
elif f % 5 == 0:
    print("Divisible by 5")
elif f % 2 != 0:
    print("Odd")
else:
    print("Not divisible by 2 or 5")
print("------------------------------------------------------")

# 8. Write a program that asks for the user’s age and classifies them into the following categories:
# "Child" if the age is less than 13,
# "Teenager" if the age is between 13 and 19,
# "Adult" if the age is between 20 and 59,
# "Senior" if the age is 60 or more.
# Example:
# Input: 25
# Output: Adult
# Input: 10
# Output: Child
g =int(input("Please enter your age: "))
if g<13:
     print("Child")
elif 13<=g<=19:
     print("Teenager")
elif 20<=g<=59:
     print("Adult")
else:
     print("Senior")
print("------------------------------------------------------")

# 9. Write a program that takes a number from the user and checks in which range it falls:
# "Below 0" if the number is less than 0,
# "Between 0 and 10" if the number is between 0 and 10 (exclusive),
# "Between 10 and 50" if the number is between 10 and 50 (exclusive),
# "Above 50" if the number is greater than 50.
# Example:
# Input: 3
# Output: Between 0 and 10
# Input: 30
# Output: Between 10 and 50
h = int(input("Please enter a number: "))
if h<0:
     print("Below 0")
elif 0<h<10:
     print("Between 0 and 10")
elif 10<h<50:
     print("Between 10 and 50")
else:
     print("Above 50")
print("------------------------------------------------------")


# 10. Write a program that converts temperature from Celsius to Fahrenheit. Ask the user to input the temperature in Celsius, and then:
# If the temperature is below 0°C, print "Below freezing point".
# If the temperature is between 0°C and 25°C, print "Cool".
# If the temperature is between 25°C and 40°C, print "Warm".
# If the temperature is above 40°C, print "Hot".
# Example:
# Input: 15
# Output: Cool
# Input: 45
# Output: Hot
i = float(input("enter the temperature in Celsius: "))
fah = (i * 1.8)+32
if i<0:
     print("Below freezing point")
elif 0<=i<25:
     print("Cool")
elif 25<=i<40:
     print("Warm")
else:
     print("Hot")
print("------------------------------------------------------")



# 11. Write a program that checks if a given grade (0-100) is valid or not. The grade is valid if it’s between 0 and 100 (inclusive). Otherwise, print "Invalid grade". Then, use elif to check:
# "Excellent" for a grade above or equal to 90,
# "Good" for a grade between 75 and 89,
# "Average" for a grade between 50 and 74,
# "Fail" for a grade below 50.
# Example:
# Input: 85
# Output: Good
# Input: 45
# Output: Fail
j = int(input("enter your grade: "))
if 0<=j<=100:
      if j>=90:
            print("Excellent")
      elif 75<=j<=89:
            print("Good")
      elif 50<=j<=74:
            print("Average")
      else:
            print("Fail")
else:
     print("Invalid Grade")
print("------------------------------------------------------")

# 12. 1.Write a program that checks if a given number is positive, negative, or zero and prints the result
k=int(input("enter a number: "))
if k<0:
     print("Negative number")
elif k>0:
     print("Positive number")
else: 
     print("zero")
print("------------------------------------------------------")

# 13. Write a program that accepts three numbers and determines the largest number among them.
l=int(input("enter a 1st number: "))
m=int(input("enter a 2nd number: "))
o=int(input("enter a 3rd number: "))
if l>=m and l>=o:
     print(l,"is the largest number" )
elif m>=l and m>=o:
      print(m,"is the largest number")
else:
     print(o,"is the largest number")
print("------------------------------------------------------")

# 14. Write a program to check if a given number is a prime number. A prime number is a number greater than 1 that is divisible only by 1 and itself.
p =int(input("Enter a number: "))

if p <= 1:
    print("Not a prime number")
else:
    for i in range(2, p):
        if p % i == 0:
            print("Not a prime number")
            break
    else:
          print("Prime number")
print("------------------------------------------------------")



# 15. Write a program that checks if a given character is a vowel or a consonant. The vowels are `a`, `e`, `i`, `o`, `u` (both uppercase and lowercase)
q = input("enter a Character: ")
if q.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")
print("------------------------------------------------------")

# 16. Print numbers from 1 to 10 using a for loop.
for i  in range(1,101):
     print(i)
print("------------------------------------------------------")

# 17. Print all even numbers from 2 to 20 using a for loop
for i in range(2,21,2):
     print(i)
print("------------------------------------------------------")

# 18. Print the square of each number from 1 to 10
for i in range(1,11):
     print(i*i)
print("------------------------------------------------------")

# 19. Print each letter of a given word (e.g., "Python") on a new line.
for i in "Python":
     print(i)
print("------------------------------------------------------")

# 20. Find the sum of numbers from 1 to 10 using a for loop.
r = 0
for i in range(1,11):
     r+=i
print(r)
print("------------------------------------------------------")

# 21. Print the multiplication table of a given number (e.g., 5).
for i in range(1,11):
     print("5 X",i, "=",5*i)
print("------------------------------------------------------")

# 22. Reverse a given word using a for loop.
for i in "Python"[::-1]:
     print(i)
print("------------------------------------------------------")

# 23. Find the factorial of a given number (e.g., 5!)
s = 5
fact = 1
for i in range(1, s+1):
    fact *= i
print(fact)
print("------------------------------------------------------")


# 24. Print a simple pattern like a right-angled triangle using "*"
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
print("------------------------------------------------------")

# 25. Count the number of vowels in a given word
for i in "education":
     if i=="a" or i=="e" or i =="i" or i == "o" or i=="u":
            print(i)
print("------------------------------------------------------")

# 26. Write a function called book_details that takes two positional arguments (title and author) and one keyword argument (year, defaulting to 2024).
# Call the function with different argument orders and observe the output.
# Function definition
def book_details(title, author, year=2024):
    print("Title:", title)
    print("Author:", author)
    print("Year:", year)

# Function calls with different argument orders

# 1. All positional arguments
book_details("Wings of Fire", "A.P.J. Abdul Kalam", 1999)

print("----------------------")

# 2. Positional + keyword argument
book_details("Wings of Fire", "A.P.J. Abdul Kalamo", year=1988)

print("----------------------")

# 3. Using default value for year
book_details("Wings of Fire", "A.P.J. Abdul Kalam")
print("------------------------------------------------------")


# 27. Write a function student_info that takes a student's name as a positional argument, multiple subjects as *args, and additional details (like age, grade) as **kwargs.
# Call the function with different numbers of subjects and extra details.
def student_info(name, *subjects, **details):
    print(f"Name: {name}")
    print("Subjects:", subjects)
    print("Additional details:")
    for key, value in details.items():
        print(f"  {key}: {value}")

# Example calls:

student_info("Alice", "Math", "Science", age=16, grade="10th")

print("----------------------")

student_info("Bob", "History", "English", "Physics", age=17)

print("----------------------")

student_info("Charlie", age=15, grade="9th")  # no subjects
print("------------------------------------------------------")

# 28. Create a function calculate_discounted_price that takes price and discount (default value 10%).
# Call the function with and without specifying the discount.
def calculate_discounted_price(price, discount=10):
    discounted_price = price - (price * discount / 100)
    return discounted_price

# Calling with default discount (10%)
print(calculate_discounted_price(1000))

# Calling with custom discount (e.g., 20%)
print(calculate_discounted_price(1000, 20))
print("------------------------------------------------------")


# 29. Write a function rectangle_properties that takes length and width and returns both area and perimeter
def rectangle_properties (length,Width):
     area = length*Width
     perimeter = 2(length*Width)
     return area, perimeter

print(rectangle_properties(100,200))
print("------------------------------------------------------")

# 30.Count Vowels in a String: Write a program that counts the number of vowels (a, e, i, o, u) in a given string
count = 0
for i in "education":
     if i in "aeiou":
            count+=1
print(count)
print("------------------------------------------------------")


# 31. Check if a String is a Palindrome: Write a Python program to check if a given string is a palindrome.
t = input("Enter a string to check Palindrome: ")
if t == t[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
print("------------------------------------------------------")

# 32.Reverse a String: Write a Python program that takes a string as input and prints the reverse of that string.
u =input("Enter a string: ")
print(u[::-1], end="")
print("------------------------------------------------------")

# 33. Count Occurrences of a Character: Write a Python program that counts how many times a specific character appears in a string.
string = "banana"
char = 'a'
count = string.count(char)
print(count)
print("------------------------------------------------------")

# 34. Remove Whitespace from a String: Write a Python program that removes all whitespaces from a given string.
v = input("Enter a string with spaces: ")
no_spaces = s.replace(" ", "")
print(no_spaces)
print("------------------------------------------------------")

# 35. Replace All Spaces with Underscores: Write a program that replaces all spaces in a string with underscores (_).
w = input("Enter a string with spaces: ")
no_spaces = w.replace(" ", "_" )
print(no_spaces)
print("------------------------------------------------------")

# 36. Check if a String Contains Only Digits: Write a Python program to check if a given string contains only digits.
x = input("enter a string: ")
dig = x.isdigit()
print(dig)
print("------------------------------------------------------")

# 37. Extract a Substring Using Indexing: Write a Python program that extracts a substring from a given string using string slicing. The program should take two indices as input (start and end) and return the substring.
y = input("Enter a string: ")
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
substring = s[start:end]
print("Substring:", substring)
print("------------------------------------------------------")

# 38. Without using replace method "replace" any string from the word
# Without using any method remove  each and every space
text = input("Enter a string with spaces: ")
result = ""
for char in text:
    if char != " ":
        result += char

print("Without spaces:", result)
print("------------------------------------------------------")

# 39. Testcases
#        I/p:  	cha_it_an_ya
# 	O/p: 	chaItAnYa    
aa = input("Enter string: ")  # e.g., cha_it_an_ya

result = ""
capitalize_next = False

for char in aa:
    if char == "_":
        capitalize_next = True
    else:
        if capitalize_next:
            result += char.upper()
            capitalize_next = False
        else:
            result += char

print(result)
print("------------------------------------------------------")


# 40.Print the given string
# Write a program that prints the string "Hello, World!".
print("Hello, World!")
print("------------------------------------------------------")

# 41.Print numbers from 1 to 10
for i in range(1,11):
     print(i,end="")
print("------------------------------------------------------")

# 42. Print the numbers from 1 to 10, each on a new line.
for i in range(1,11):
     print(i)
print("------------------------------------------------------")

# 43. Print even numbers between 1 and 20
for i in range(2,21,2):
     print(i)
print("------------------------------------------------------")

# 44. Write a program that prints all even numbers between 1 and 20.
for i in range(2,21,2):
     print(i)
print("------------------------------------------------------")

# 45. Print the length of a string
print(len("python"))
print("------------------------------------------------------")

# 46. Write a program that takes a string and prints its length.
ab = input("enter a string: ")
print(len(ab))
print("------------------------------------------------------")

# 47. Check if a string is empty
# Write a program that checks if a string is empty and prints "Empty" or "Not Empty" accordingly.
ac = input("enter a string: ")
if len(ac)==0:
     print("Empty")
else:
     print("Not Empty")
print("------------------------------------------------------")

# 48.Convert a string to uppercase
# Write a program that takes a string and converts it to uppercase.
ad = input("enter a string: ")
ad_upper = ad.upper()
print(ad_upper)
print("------------------------------------------------------")

# 49. Convert a string to lowercase
# Write a program that takes a string and converts it to lowercase.
ae = input("enter a string: ")
ad_low = ad.lower()
print(ad_low)
print("------------------------------------------------------")
# 50. Print the first character of a string
# Write a program that prints the first character of a given string.
af =  "Python"
print("the first character is",af[0])

# 51. Print the last character of a string
# Write a program that prints the last character of a given string.
print("the last character is",af[-1])

# 52. Count the number of vowels in a string
# Write a program that counts and prints the number of vowels (a, e, i, o, u) in a string
count = 0
for i in "education":
     if i in "aeiou":
            count+=1
print(count)
print("------------------------------------------------------")

# 53.Print Each Element:

# Given numbers = [1, 2, 3, 4, 5], use a for loop to print each number.
# Print List Elements with Text:
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print("The number is:", num)
print("------------------------------------------------------")

# 54.Given fruits = ["apple", "banana", "cherry"], use a for loop to print:
# I like apple  
# I like banana  
# I like cherry sum of list elements
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)
print("------------------------------------------------------")
# 55.Given nums = [10, 20, 30, 40], use a for loop to calculate and print the total sum.
# Count Even Numbers:
nums = [10, 20, 30, 40]
total_sum = 0
even_count = 0
for num in nums:
    total_sum += num
    if num % 2 == 0:
        even_count += 1

print("Total Sum:", total_sum)
print("Count of Even Numbers:", even_count)
print("------------------------------------------------------")

# 56.Given numbers = [1, 2, 3, 4, 5, 6], use a for loop to count how many numbers are even.
# Find the Largest Number:
ag = [1, 2, 3, 4, 5, 6]
ev_count = 0
for i in ag:
     if i%2==0:
            ev_count +=1
print("Count of even numbers:",ev_count)
largest = max(ag)
print("The largest value is", largest)
print("------------------------------------------------------")

# 57.Given nums = [3, 7, 2, 8, 5], use a for loop to find and print the largest number.
# Copy a List:
ah = [3, 7, 2, 8, 5]
lar = ah[0]
for i in ah:
    if i > lar:
        lar = i
print("The largest number is", lar)
copy_list = ah[:] 
print("Copied list:", copy_list)
print("------------------------------------------------------")

# 58.Given original = [5, 10, 15, 20], use a for loop to copy all elements into a new list.
# Multiply Each Element by 2:
ai = [5, 10, 15, 20]
aj = []
for i in ai:
    aj.append(i*2)
print(aj)
print("------------------------------------------------------")

# 59.Given nums = [1, 2, 3, 4], use a for loop to create a new list where each number is doubled.
# Reverse a List (Using Loop):

ak = [1, 2, 3, 4]
al = []
for i in ak:
    al.append(i * 2)
print("Doubled list:", al)


reversed_list = []
for i in range(len(ak)-1, -1, -1):
    reversed_list.append(ak[i])
print("Reversed list:", reversed_list)
print("------------------------------------------------------")


# 60.Given words = ["hello", "world", "python"], use a for loop to print the elements in reverse order.
# Find Words Starting with 'A':
am = ["hello", "world", "python"]
an =  []
for i in range (len(am) -1,-1,-1):
     an.append(am[i])
print("Reveresed list: ",an)

ao=[]
for item in am:
    if item.lower().startswith('a'):
        ao.append(item)
print("item starts with A: ",ao)
print("------------------------------------------------------")   

# 61.Given words = ["apple", "banana", "avocado", "grape"], use a for loop to print only the words that start with "a".
ap=["apple", "banana", "avocado", "grape"]
aq = []
for item in ap:
    if item.lower().startswith('a'):
        aq.append(item)
print("item starts with A: ",aq)
print("------------------------------------------------------")   

# 62.Given numbers = [-5, 10, -3, 7, -2, 8], use a for loop to create a new list containing only the positive numbers.
ar = [-5, 10, -3, 7, -2, 8]
at=[]
for i in ar:
     if i>0:
         at.append(i)
print("Positive list: ",at)
print("------------------------------------------------------")   

# 63.Sum all elements in a list
# Given a list of numbers, find the sum of all the numbers in the list.
av = [4, 5, 6, 8, 2]
au = 0
for i in av:
     au += i
print("sum of all elemts is: ",au)
print("------------------------------------------------------")   
# 64.Find the smallest number in a list
# Given a list of numbers, find the smallest number in the list.
smallest = min(av)
print("the smallesst number is",smallest)
print("------------------------------------------------------")   
# 65.Count the number of elements in a list
# Write a function that takes a list and returns the number of elements in the list.
aw = list(map(int, input("Enter numbers separated by space: ").split()))
ax = 0
for item in aw:
     ax += item
print("the count is", ax)
print("------------------------------------------------------")   

# 66.Access the last element of a list
# Given a list, access and print the last element of the list.
print("the last element in the list is: ",aw[-1])
print("------------------------------------------------------")  

# 67.Append an element to a list
# Write a function to add an element to the end of a list.
aw.append(48)
print(aw)
print("------------------------------------------------------")   

# 68.Check if a list is empty
# Write a function that checks if a given list is empty. Return True if it is empty, otherwise return False.
def check_list(a):
     if len(a)==0:
          return True
     else:
          return False
print("------------------------------------------------------")   

# 69.Get the first N elements of a list
# Write a function that takes a list and a number N, and returns the first N elements from the list.
def elements(lt,number):
        return lt[:number]
print("------------------------------------------------------")   

# 70.Remove an element from the list
# Write a function that removes a specific element from a list if it exists.
def remove_element(a,b):
      a.remove(b)
      return a
print("------------------------------------------------------")   

# 71.Find the length of a list
# Given a list, write a function that returns the length (number of elements) of the list.
def length(a):
      return len(a)
print("------------------------------------------------------")   

# 72.Merge two lists
# Write a function that takes two lists and returns a new list that contains the elements of both lists.
def lt_add(a,b):
     return a+b
print("------------------------------------------------------")   

# 73.Create a list of integers from 1 to 10.
ay = []
for i in range(1,11):
     ay.append(i)
print(ay)
print("------------------------------------------------------")   

# 74.
# How can you access the first element of a list?
print(ay[0])
print("------------------------------------------------------")   

# 75.
# Write a Python code to append an element to the end of a list.
print(ay.append(67))
print("------------------------------------------------------")   

# 76.How do you remove the last element from a list?
ay.pop()
print(ay)
print("------------------------------------------------------")   

# 77.How can you find the length of a list?
print(len(ay))
print("------------------------------------------------------")   

# 78.
# Write a Python program to find the largest number in a list.
print(max(ay))
print("------------------------------------------------------")   

# 79.
# How can you sort a list in ascending order?
ay.sort()
print(ay)
print("------------------------------------------------------")   

# 80.
# Write a code to check if an element is present in a list or not.
elem = int(input("enter a number: "))
if elem in ay:
     print("the element is present")
else:
     print("the element is not present")
print("------------------------------------------------------")   

# 81.How do you find the index of an element in a list?
print(ay.index(elem))
print("------------------------------------------------------")   

# 82.How can you create a list of 5 elements, then remove all of them?
# Create a list with 5 elements
az = [1, 2, 3, 4, 5]
print("Original list:", az)

az.clear()
print("List after removing all elements:", az)
print("------------------------------------------------------")   


# 83.
# How can you slice a list to get elements from index 2 to 5?
print(ay[2:5])
print("------------------------------------------------------")   

# 84.
# How can you concatenate two lists in Python?
ba=[1, 2, 3, 4, 5]
bb=[5, 6, 7, 8, 9]
concatenated_list= ba+bb
print(concatenated_list)
print("------------------------------------------------------")   

# 85.How can you copy a list into another list?
bb=ba.copy()
print(bb)
print("------------------------------------------------------")   

# 86.Write a Python program to count the number of times an element appears in a list.
bc=[1, 1, 2, 3, 1, 5, 6, 1]
bd = 1
be= 0
for bd in bc:
     be+=1
print(be)
print("------------------------------------------------------")   

# 87.How can you check if a list is empty?
bf = []
if len(bf)==0:
     print("Empty")
else:
     print("not empty")
print("------------------------------------------------------")   

# 88.String Questions:
# Create a string variable that holds your name and print it.
bg= "Boga Premsai"
print(bg)
print("------------------------------------------------------")   
# 89.
# How do you convert a string to uppercase in Python?
print(bg.upper())
print("------------------------------------------------------")   

# 90.
# Write a code to check if a string contains a specific substring.
sub_str = "boga"
if bg.lower() in sub_str.lower():
     print(True)
else:
     print(False)
print("------------------------------------------------------") 

# 91.How can you find the length of a string in Python?
print(len(bg))
print("------------------------------------------------------") 

# 92.Write a Python program to reverse a string. 
bh=bg[::-1]
print(bh)
print("------------------------------------------------------") 



