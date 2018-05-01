"""Examples of operators in Python."""

# Operators act on operands.
# When both the operands are numbers, the operators work like they did in math class

# Addition and subtraction
print('Addition is + and subtraction is -. 11 - 6 =', 11 - 6)

# Multiplication
print('Multiplication with *. 3 * 4 =', 3 * 4)

# With +, - and * if at least one operand is a float(decimal number), the result will be a float
print('When all operands are ints, an int is produced. 4 * 3 - 2 =', 4 * 3 - 2)
print('When at least one operand is a float, a float is produced. 4 * 3 - 2.0 =', 4 * 3 - 2.0)

# Division is different
# Division with / will produce a float, even if both operands are ints.
print('Division with / and two ints. 5 / 2 =', 5 / 2)
print('Division with / and two ints. 5.0 / 2 =', 5.0 / 2)
print('Division with / and two ints. 5.0 / 2.0 =', 5.0 / 2.0)

# Division with // is floor division.
# It will truncate any fractional value. It will also produce and int if both operands are ints
print('Division with // and two ints. 5 // 2 =', 5 // 2)
print('Division with // and two ints. 5.0 // 2 =', 5.0 // 2)
print('Division with // and two ints. 5.0 // 2.0 =', 5.0 // 2.0)

# Division with %(modulo) will give you the remainder of a Division
print('Modulo with %. 5 % 2 =', 5 % 2)

# You can divide in many ways, with even more numbers. Just never by zero
# print('This print will not work because it contians an exception', 5 / 0)

# Operators can also work on types other than numbers.
# + and * operators can be used with string operands
print("+ can conactenate two strings together. 'First ' + 'Second':", 'First ' + 'Second')

print('* will duplicate a string any number of times:', 'over and ' * 3, 'over again')

# + and * can also be used with lists
print('+ can combine two lists into a new list. [1, 2] + [3, 4] creates a new list:', [1, 2] + [3, 4])

print('* will duplicate a list any number of times. [3, 3, 3] * 3:', [3, 3, 3] * 3)
se
# Comparison Operators
print("Equality can be checked with ==. 'hello' == 'hello': ", 'hello' == 'hello')
print("Lack of equality can be checked with !=. 'hello' != 'goodbye': ", 'hello' != 'goodbye')
print('Order can be determined with < and >.',
      '3 > 2:', 3 > 2,
      '5 >= 5', 5 >= 5)
print('Comparing the order of strings can be a little weird.',
      "'z' > 'a':", 'z' < 'a',
      "'Z' > 'a':", 'Z' < 'a')


# Built-in Functions
# Built-ins are like operators in that they are aviable every where in python.
# They are different because they are called () and a list of arguments.

# There are many built-in functions: https://docs.python.org/3/library/functions.html
print('print() is a useful one')

# type() can give information about data types
print('3 is an int. type(3):', type(3))
print("'6' is a str. type('6'):", type('6'))

# You can convert types with built-ins
print("'6' is a str, but let's make it an int. type(int('6'))", type(int('6')))

# There a few useful built-ins for lists.
print('len() will tell you the number of items in a list. len([1, 2, 3]):', len([1, 2, 3]))
print('min() and max() will return the smallest and largest items. min([1, 2, 3]):',
      min([1, 2, 3]),
      'max([1, 2, 3]):',
      max([1, 2, 3]))

# len() works with more than lists. It will give you the number of things in sequence (string) or collection (list).
print("one, two and six all have 3 character in the sequence of characters",
      "len('one'):", len('one'),
      "len('two'):", len('two'),
      "len('six'):", len('six'))

# Extra Credit
# Operators and built-ins can be used to pad a strings
print("Padding a string to 9 characters using Xs. 'X' * (9- len('hello')) + 'hello':", 'X' * (9 - len('hello')) + 'hello')
