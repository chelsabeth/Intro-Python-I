"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print('x is %d, y is %.2f, z is "%s"' % (x, y, z)) 

''' 
notes: 
%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)

link: https://www.learnpython.org/en/String_Formatting
'''

# Use the 'format' string method to print the same thing
txt = 'x is {ten}, y is {dec:.2f}, z is "{str}"'
print(txt.format(ten = x, dec = y, str = z))

# link: https://www.w3schools.com/python/ref_string_format.asp

# Finally, print the same thing using an f-string
print(f'x is {x}, y is {y:.2f}, z is "{z}""')