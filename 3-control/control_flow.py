# Control statements are used to change how code is executed.

# if is used to run code when a statement is true
low_number = 9

high_number = 27

if low_number < high_number:
    print('if low_number is less than high_number, this will run.')
else:
    print('low_number is not less than high_number')


# if and elif can be used to check a sequence of statements
if high_number >= 100:
    print('High number is big! high_number = {}'.format(high_number))
elif low_number < high_number:
    print('if high_number is less than 100 and\nif low_number is less than high_number, this will run.')
else:
    print('low_number is not less than high_number')

# loops run the same code, multiple times.
# for is a great way loop. for will run once for every item in a sequence
number_list = [1, 2, 3]
for number in number_list:
    print('This print has run {} time'.format(number))

character_string = '123 Bad Route Rd'
for character in character_string:
    print(character)

# while will run one loop of code if a statement is true
number_of_loops = 0
while number_of_loops < 3:
    number_of_loops = number_of_loops + 1
    print('Number of times while statement has been true: {}'.format(number_of_loops))
