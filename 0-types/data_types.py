# Number types
# Intgers are whole numbers. They can be postive or negative
# The name of the integer type is int
print(7, 'is an int')
print(-55, 'is an int')

# Floats and decimal numbers. They can represent fractional values.
print(7.0, 'is a float')
print(-33.3333, 'is also a float')

# Strings are text. Surrounding text with qoutes will make it a stringself.
# The name of the string type is str
print('This is a string with single quotes')
print("This is a string with double quotes")
print("This is a string with double qoutes and it has it's 'own' singe qoute inside")
print("""Here is a string with triple quotes, and 'all' the other qoutes "inside" it.""")

# Lists are collections of other types.
print('You can fill a list with ints:', [1, 2, 3])
print('You can fill a list with strs:', ['a', 'b', 'c'])
print('You can fill a list with almost anything:', [1, 'a', [1, 2, 3]])
print("Access things in a list with more [] and indices. ['a', 'b', 'c'][0]:", ['a', 'b', 'c'][0])


# Dictionaries are collections of key, value pairs. Dictionaries are powerfull!
# The name of the dictionary type is dictionary
print('A key maps to a value:', {'key': 'value'})
print('Many types can be a key:',
      {'key': 5,
       9: 'value',
       1.5: True})
print('Anything can be a value:',
      {'lists': [1, 2, 3],
       'dictionaries': {'wow!': 'neat'},
       'objects?': object()})
print("Access things in a dictionary with [] and keys. {'key1': 'a', 'key2': 'b'}['key1']:", {'key1': 'a', 'key2': 'b'}['key1'])

# Extra Credit
# There are other interesting types.
print('Sets are like lists, but with no order and no duplicates. set([11, 33, 11, 22, 11])',
      set([11, 33, 11, 22, 11]))
print('Tuples are like lists, but they are immutable (can not be changed once created):', (1, 2, 3, 4))
