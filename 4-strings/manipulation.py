# Formatting
# {} are placeholders for the format() functions
print('Many types can be inserted into a string',
      'ints like {}\n'.format(5),
      'other strs like {}\n'.format('sassafras'),
      'floats {}\n'.format(3.14),
      'Even lists {}'.format(['thing one', 'thing two']))
# Varibles can be subsituted into a string.
fun_yet = 'fun yet?'
are_we = 'Are we having {}'.format(fun_yet)
print(are_we)
# Multiple placeholders can be used
fun_now = 'fun now!'
are = 'are'
we = 'we {} {}'.format(are, fun_now)
print(we)
# A string varible with placeholders can be formatted many times.
are_we = 'Are we having {}'
lunch_yet = 'lunch yet?'
print(are_we.format(lunch_yet))
print(are_we.format(fun_now))
# The string varible is unchanged because format() creates a new string
print(are_we)
# placeholders map to format arguments based on position.
# The position can also be specified with indices
one = 'thing 1'
two = 'thing 2'
print('If I ryhme will they sue, with {0} and {1}'.format(one, two))
print('With {1} and {0} it just isn\'t as fun.'.format(one, two))

# placeholders can also be mapped with keyword arguments.
print('{thing1} and {thing2}'.format(thing1=one, thing2=two))

# Types can be added to placeholders to do more advanced formatting.
print('float formatting can round. {0} becomes: {0:.3f}'.format(17.3468213457))
print('You can also specify padding. With ints: {0:0>7d} and strings: {1:*^11s}'.format(3, 'magic'))
# You can do much, much more with formating (https://docs.python.org/3.6/library/string.html#format-specification-mini-language)

# String slicing
# Positions in a string can be accessed with zero based indices
print('The fith character in sassafras is:', 'sassafras'[4])
# Slicing can give you a substring
print('We can get the middle 3 characters from sassafras:', 'sassafras'[3:6])
# We can also index from the end of the string starting with -1
print('The last character of sassafras is:', 'sassafras'[-1])
print('The last 3 characters of sassafras are:', 'sassafras'[-3:])

# There are also many methods that can be called on a string.
# You can alter the case of a string
print('Make a string lowercase:', 'THIS WAS IN CAPS'.lower())
print('Make it uppercase:', 'THIS WAS ALL LOWERCASE'.upper())

# Strings can be checked for what they contain
print('Check if a string ends with another string. Bad Route Rd ends with Rd?:', 'Bad Route Rd'.endswith('Rd'))
print('Find the index of one string in another string. In Bad Route Rd, Route starts at index:',
      'Bad Route Rd'.find('Route'))
print('Check if all characters are numeric.',
      "Is '123 Bad Route Rd' numeric?:",
      '123 Bad Route Rd'.isnumeric(),
      "Is '123' numeric?:",
      '123'.isnumeric())

# You can split a string up into a list.
print("'05-07-2018' separated by '-' becomes:", '05-07-2018'.split('-'))
print("split will use spaces by default. '123 Bad Route Rd' becomes:", '123 Bad Route Rd'.split())
