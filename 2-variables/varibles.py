"""Example of python variables"""

# variables must begin with an underscore or letter
magic_number = 9
print('The magic number is: ', magic_number)

_secret_message = 'discombobulation'
print('The secret to learning python is to avoid variable name', _secret_message)

# variables can be any length
x = 3.14
print('The varible name "x" is not very descriptive, unless you are in math class. x is:', x)

the_longest_variable_name_could_be_very_descriptive_but_eventually_becomes_hard_to_type_and_read = True
print('Is varible name descriptiveness normally more important than length?:', the_longest_variable_name_could_be_very_descriptive_but_eventually_becomes_hard_to_type_and_read)

# Once variables have been assigned a value they can be used in many ways
rounded_pi = x
print('Variables can be assigned a value from other variables. Now pi is:', rounded_pi, 'and so is x:', x)

still_fun = 'fun'
still_fun = still_fun
print('Variables can even be assigned to themselves:', still_fun)
still_fun = still_fun + ' ' + still_fun + ' ' + still_fun
print('Or they can be assigned to statements that include themselves: ', still_fun)


# Here are some things you can NOT do with varible names
# 1st_rule_is = 'variables can not begin with numbers'
# print('The first rule we broke was: ', 1st_rule_is)
#
# case_matters = True
# print('Does case matter in varible names?:', Case_Matters)
#
# empty_nothing
# print(empty_nothing)

# Extra Credit
one, two = (1, 2)
print('Multiple variables can even be assigned on the same line.', 'one:', one, 'two:', two)
# SWAP!
two, one = one, two
print('And it can be used for an easy varible swap.', 'one:', one, 'two:', two)
