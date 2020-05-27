from general_functions import return_formatted_name

# test setup

known_input = '     nathan      '
expected_output = 'Nathan'
#
# # test execution
print("Testing function return_formatted_name() with '            nathan          ' --->  'Nathan'")
print(return_formatted_name(known_input) == (expected_output))

# testing say_hello()

from general_functions import say_hello_name

known_input_say_hello = 'Nathan    '
expected_output_say_hello = 'hello Nathan'

print("Testing function say_hello_name() with 'Nathan    ' --> 'hello Nathan'")
print(say_hello_name(known_input_say_hello) == (expected_output_say_hello))

print(say_hello_name(known_input_say_hello))

from general_functions import surname

known_input_surname = '    forester     '
expected_output_surname = 'Forester'

print("Testing function surname() with '   forester     ' --> 'Forester'")
print(surname(known_input_surname) == (expected_output_surname))