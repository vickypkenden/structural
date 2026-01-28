# Print a simple message to the console
print("Hello, World!")

#Working with textual data in Python
message = "Bobby's world! was a popular TV show."
print(message[0:5])  # concept of slicing

print(message.lower())  # converting to lowercase
print(message.upper())  # converting to uppercase
print(message.count('l'))  # counting occurrences of 'l'
print(message.find('world'))  # finding the index of 'world'
print(message.replace('Bobby', 'Tommy'))  # replacing 'Bobby' with 'Tommy'

greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name + '. Welcome!'   

message = '{}, {}. Welcome!'.format(greeting, name)  # using format method
print(message)
message = f'{greeting}, {name.upper()}. Welcome!'  # using f-strings
# print(dir(str)) # listing all string methods
# print(help(str))  # getting help on string methods

# Integers and floating-point numbers
num = 3
print(type(num))  # checking the type of num

num_float = 3.14
print(type(num_float))  # checking the type of num_float

#arithmetic operations
print( 3 // 2) #Floor division
print(3 ** 2)  # Exponentiation
print(3 % 2)   # Modulus

num = 1
num *= 10  # Augmented assignment
print(num)
print(round(3.14159, 2))  # Rounding to 2 decimal places
print(abs(-7))  # Absolute value

#Comparisons
num_1 = 5
num_2 = 10

print(num_1 == num_2)  # Equal to
print(num_1 != num_2)  # Not equal to
print(num_1 < num_2)   # Less than
print(num_1 <= num_2)  # Less than or equal to
print(num_1 > num_2)   # Greater than
print(num_1 >= num_2)  # Greater than or equal to

#Casting
num_1 = '100'
num_2 = '200'
print(int(num_1) + int(num_2))  # Converting strings to integers and adding

#Lists, tuples, and sets
courses = ['History', 'Math', 'Physics', 'CompSci']  # List
print(len(courses))
print(courses[0])  # Accessing first element
print(courses[-1])  # Accessing last element
print(courses[1:3])  # Slicing the list
courses.append('Art')  # Adding an element
courses.insert(0, 'Biology')  # Inserting at a specific position
courses_2 = ['Education', 'Economics']
courses.insert(0, courses_2)  # Inserting a list as an element
courses.extend(courses_2)  # Extending the list with another list
print(courses)
courses.pop()  # Removing the last element
courses.remove('Math')  # Removing a specific element
print(courses)
popped_course = courses.pop(0)  # Popping an element at index 0
print(popped_course)
courses.reverse()  # Reversing the list
courses.sort()  # Sorting the list
print(courses)
courses.sort(reverse=True)  # Sorting in descending order
print(courses)

sorted_courses = sorted(courses)  # Getting a sorted copy of the list
print(sorted_courses)

#minimum and maximum
nums = [3, 6, 2, 8, 4, 10]
print(min(nums))
print(max(nums))

print(courses.index('Physics'))  # Finding the index of an element
print('CompSci' in courses)  # Checking membership
for course in courses:  # Iterating through the list
    print(course)

for index, course in enumerate(courses):  # Enumerating with index
    print(index, course)

for index, course in enumerate(courses, start=1):  # Enumerating with custom start index
    print(index, course)

course_str = ', '.join(courses)  # Joining list elements into a string
print(course_str)

new_list = course_str.split(', ')  # Splitting string back into a list
print(new_list)

#Tuples
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')  # Tuple
print(tuple_1[0])  # Accessing first element
# tuple_1[0] = 'Art'  # This will raise an error since tuples are immutable 
tuple_2 = tuple_1  # Assigning tuple_1 to tuple_2
print(tuple_2)
#Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}  # Set
print('Math' in cs_courses)  # Checking membership

art_course = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_course))  # Intersection
print(cs_courses.union(art_course))  # Union
print(cs_courses.difference(art_course))  # Difference

#Empty lists, tuples, and sets
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = set()  # Note: {} creates an empty dictionary, not a set
empty_set = {}  # This creates an empty dictionary, not a set

#Dictionaries
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}  # Dictionary
print(student['name'])  # Accessing value by key
print(student.get('age'))  # Accessing value using get method
print(student.get('phone', 'Not Found'))  # Using get with a default value
student['age'] = 26  # Modifying a value
student['phone'] = '555-5555'  # Adding a new key-value pair
print(student)
student.update({'name': 'Jane', 'age': 27, 'address': '123 Main St'})  # Updating multiple key-value pairs
print(student)
del student['age']  # Deleting a key-value pair
age = student.pop('age', 'Not Found')  # Popping a key-value pair with default
print(age)

print(len(student))  # Getting the number of key-value pairs
print(student.keys())  # Getting all keys
print(student.values())  # Getting all values
print(student.items())  # Getting all key-value pairs

for key, value in student.items():  # Iterating through key-value pairs
    print(key, value)

# Conditionals and booleans - if, elif, else
language = 'Python'
if language == 'Python':
    print('Language is Python')

if True:
    print("It's true!")
if False:
    print("It's false!")  



#For while loops

nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)  

for i in range(1, 11):  # range from 0 to 9
    print(i)

x = 0
while x < 10:
    if x == 5:
        break
    print(x)    
    x += 1

#Functions
def hello_func(greeting, name='You'):
    return '{}, {} Function!'.format(greeting, name)
print(hello_func('Hi', name='Michael'))
    

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
course = ['Math', 'CompSci']
info = {'name': 'John', 'age': 22}

student_info(*course, **info)

#Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month < 1 or month > 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]
print(days_in_month(2020, 2))  # Leap year
print(days_in_month(2019, 2))  # Non-leap year
#DRY - Don't Repeat Yourself
