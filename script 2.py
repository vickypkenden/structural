# Print a siple messsage to the console
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

